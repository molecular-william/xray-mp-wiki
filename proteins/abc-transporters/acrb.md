---
title: "AcrB Multidrug Efflux Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature05076, doi/10.1126##science.1131542, doi/10.1371##journal.pbio.0050007, doi/10.1038##nature13205, doi/10.1038##s41467-021-24151-3, doi/10.1038##nature01050, doi/10.1007##s10969-013-9154-x, doi/10.1016##j.jsb.2011.01.014, doi/10.1016##j.str.2007.09.023, doi/10.1038##ncomms13819, doi/10.7554##eLife.03145]
verified: false
---

# AcrB Multidrug Efflux Transporter

## Overview

AcrB is the inner membrane component of the [AcrA multidrug efflux pump periplasmic protein](/xray-mp-wiki/proteins/abc-transporters/acra/)/AcrB/TolC tripartite efflux pump from Escherichia coli, a member of the resistance-nodulation-cell division (RND) superfamily of transporters. Driven by the proton motive force, AcrB mediates the efflux of bile salts, detergents, organic solvents, and many structurally unrelated antibiotics. The protein forms a homotrimer, and its asymmetric crystal structure revealed three distinct monomer conformations (loose, tight, and open) representing consecutive states in a peristaltic transport cycle. The original 2.8 A structure (PDB 2DHH, 2DRD, 2DR6) from Murakami et al. (2006) captured the three protomers in distinct conformations corresponding to access, binding, and extrusion states, establishing the functionally rotating mechanism of drug export. A later pseudo-atomic model of the complete AcrAB-TolC assembly revealed the quaternary organization of the tripartite efflux pump and the role of the AcrZ modulatory partner.

## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature05076 (3 structures, 9 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2dhh">2DHH</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>Full-length AcrB (residues 1-1049)</td>
      <td>Unliganded</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2drd">2DRD</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>Full-length AcrB (residues 1-1049)</td>
      <td>Minocycline</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2dr6">2DR6</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>Full-length AcrB (residues 1-1049)</td>
      <td>Doxorubicin</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/organisms/e-coli/)
- **Expression construct**: Full-length AcrB
- **Tag info**: Untagged native protein

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
      <td>Cell growth and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified as described previously (Murakami et al. 2002, Nature 419:587-593).</td>
    </tr>
  </tbody>
</table>
**Final sample**: AcrB in 20 mM [sodium phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) (pH 6.0), 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% dodecanoyl sucrose

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AcrB in 20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">sodium phosphate</a> (pH 6.0), 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1% dodecanoyl sucrose; pre-incubated with substrate overnight at 4 C</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 4000</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">sodium phosphate</a> (pH 6.2), 50 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K (20 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> gradually increased to 30% (v/v)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal size 0.3 x 0.3 x 0.2 mm. Space group C2. <a href="/xray-mp-wiki/methods/miras/">MIRAS</a> phasing. Data collected at 100 K at SPring-8.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dhh">2DHH</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-inside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-inside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVV</span><span class="topo-outside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVP</span><span class="topo-inside">MAFFGGSTGAIYRQFSIT</span><span class="topo-membrane">IVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGWFNRMFEK</span><span class="topo-unknown">STHHYTDSV</span><span class="topo-outside">GGILRSTGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAY</span><span class="topo-inside">LFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-outside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALL</span><span class="topo-inside">AATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-outside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IE</span><span class="topo-unknown">ATLDAVR</span><span class="topo-outside">MRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-inside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-outside">PVFFVVVRRRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
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
      <td>341</td>
      <td>25</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>455</td>
      <td>441</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>489</td>
      <td>474</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>522</td>
      <td>513</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>531</td>
      <td>523</td>
      <td>531</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>532</td>
      <td>541</td>
      <td>532</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>554</td>
      <td>542</td>
      <td>554</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>555</td>
      <td>877</td>
      <td>555</td>
      <td>877</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>914</td>
      <td>896</td>
      <td>914</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>915</td>
      <td>930</td>
      <td>915</td>
      <td>930</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>962</td>
      <td>945</td>
      <td>962</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>963</td>
      <td>969</td>
      <td>963</td>
      <td>969</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>970</td>
      <td>974</td>
      <td>970</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1036</td>
      <td>1023</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dhh">2DHH</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MPNFFIDRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-inside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-outside">LILTPALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">F</span><span class="topo-unknown">GWFNRMFE</span><span class="topo-outside">K</span><span class="topo-unknown">STHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-inside">TFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLA</span><span class="topo-outside">IF</span></span>
<span class="topo-line"><span class="topo-outside">FV</span><span class="topo-unknown">PVFFVVV</span><span class="topo-outside">RRRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>342</td>
      <td>27</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>410</td>
      <td>397</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>485</td>
      <td>471</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>498</td>
      <td>486</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>521</td>
      <td>514</td>
      <td>521</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>536</td>
      <td>523</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>916</td>
      <td>899</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>929</td>
      <td>917</td>
      <td>929</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1018</td>
      <td>1005</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1022</td>
      <td>1019</td>
      <td>1022</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1029</td>
      <td>1023</td>
      <td>1029</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1036</td>
      <td>1030</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dhh">2DHH</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGL</span><span class="topo-inside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-inside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-outside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGWFN</span><span class="topo-unknown">RMFEKSTHHYTDSVGG</span><span class="topo-outside">ILRSTGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAA</span><span class="topo-outside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-inside">ATFRGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLV</span><span class="topo-inside">ISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-outside">F</span></span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">VPVFFVVVRRRF</span><span class="topo-outside">SRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>343</td>
      <td>26</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>442</td>
      <td>412</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>517</td>
      <td>513</td>
      <td>517</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>533</td>
      <td>518</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>541</td>
      <td>534</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>890</td>
      <td>875</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>928</td>
      <td>916</td>
      <td>928</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>943</td>
      <td>929</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>990</td>
      <td>976</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>1004</td>
      <td>991</td>
      <td>1004</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1021</td>
      <td>1020</td>
      <td>1021</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1033</td>
      <td>1022</td>
      <td>1033</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1036</td>
      <td>1034</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2drd">2DRD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-inside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-outside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGWFNRMFEK</span><span class="topo-unknown">STHHYTDSV</span><span class="topo-outside">GGILRSTGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-inside">RGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAKNAIL</span><span class="topo-outside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-outside">PVFFVVVRRRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>340</td>
      <td>27</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>441</td>
      <td>413</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>522</td>
      <td>513</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>531</td>
      <td>523</td>
      <td>531</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>532</td>
      <td>541</td>
      <td>532</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>928</td>
      <td>919</td>
      <td>928</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>944</td>
      <td>929</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1036</td>
      <td>1023</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2drd">2DRD</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MPNFFIDRPIFA</span><span class="topo-membrane">WVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRATL</span><span class="topo-membrane">IPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-outside">LILTPALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">F</span><span class="topo-unknown">GWFNRMFE</span><span class="topo-outside">K</span><span class="topo-unknown">STHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-outside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFV</span><span class="topo-inside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLA</span><span class="topo-outside">IF</span></span>
<span class="topo-line"><span class="topo-outside">FV</span><span class="topo-unknown">PVFFVVV</span><span class="topo-outside">RRRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>366</td>
      <td>358</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>386</td>
      <td>367</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>485</td>
      <td>471</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>498</td>
      <td>486</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>521</td>
      <td>514</td>
      <td>521</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>536</td>
      <td>523</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>542</td>
      <td>537</td>
      <td>542</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>557</td>
      <td>543</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>874</td>
      <td>558</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1018</td>
      <td>1004</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1022</td>
      <td>1019</td>
      <td>1022</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1029</td>
      <td>1023</td>
      <td>1029</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1036</td>
      <td>1030</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2drd">2DRD</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGWFNR</span><span class="topo-unknown">MFEKSTHHYTDSVGG</span><span class="topo-outside">ILRSTGR</span></span>
<span class="topo-line"><span class="topo-outside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFV</span><span class="topo-inside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-outside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">MLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-outside">F</span></span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-unknown">VPVFFVVVRRRF</span><span class="topo-outside">SRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>518</td>
      <td>513</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>533</td>
      <td>519</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>542</td>
      <td>534</td>
      <td>542</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>557</td>
      <td>543</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>873</td>
      <td>558</td>
      <td>873</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>919</td>
      <td>902</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1021</td>
      <td>1020</td>
      <td>1021</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1033</td>
      <td>1022</td>
      <td>1033</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1036</td>
      <td>1034</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dr6">2DR6</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFID</span><span class="topo-outside">RP</span><span class="topo-membrane">IFAWVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYLF</span><span class="topo-outside">LQ</span></span>
<span class="topo-line"><span class="topo-outside">NF</span><span class="topo-membrane">RATLIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIVVV</span><span class="topo-outside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTPAL</span><span class="topo-outside">CATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILRS</span><span class="topo-outside">TG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-outside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-inside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAILI</span><span class="topo-outside">VEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-outside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>27</td>
      <td>10</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>358</td>
      <td>341</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>362</td>
      <td>359</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>383</td>
      <td>363</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>413</td>
      <td>397</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>456</td>
      <td>440</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>492</td>
      <td>471</td>
      <td>492</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>493</td>
      <td>498</td>
      <td>493</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>515</td>
      <td>513</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>537</td>
      <td>516</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>539</td>
      <td>538</td>
      <td>539</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>556</td>
      <td>540</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>945</td>
      <td>928</td>
      <td>945</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>946</td>
      <td>974</td>
      <td>946</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dr6">2DR6</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAIL</span><span class="topo-inside">KLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIY</span><span class="topo-membrane">RQFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">F</span><span class="topo-unknown">GWFNRMFE</span><span class="topo-outside">KSTHHYTDSV</span><span class="topo-unknown">GGILRS</span><span class="topo-outside">TGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFV</span><span class="topo-inside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAALY</span><span class="topo-outside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-outside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-outside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>340</td>
      <td>29</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>467</td>
      <td>459</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>489</td>
      <td>468</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>521</td>
      <td>514</td>
      <td>521</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>522</td>
      <td>531</td>
      <td>522</td>
      <td>531</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>532</td>
      <td>537</td>
      <td>532</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>557</td>
      <td>542</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>873</td>
      <td>558</td>
      <td>873</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>892</td>
      <td>874</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2dr6">2DR6</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAIV</span><span class="topo-outside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPP</span><span class="topo-unknown">KEATRKSMG</span><span class="topo-outside">QIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-outside">FGWF</span><span class="topo-unknown">NRMFEKSTHHYTDS</span><span class="topo-outside">VGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFVR</span><span class="topo-inside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRR</span><span class="topo-outside">RFSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>411</td>
      <td>395</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>427</td>
      <td>412</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>436</td>
      <td>428</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>437</td>
      <td>441</td>
      <td>437</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>516</td>
      <td>513</td>
      <td>516</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>530</td>
      <td>517</td>
      <td>530</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>531</td>
      <td>540</td>
      <td>531</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>558</td>
      <td>541</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>891</td>
      <td>874</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1019</td>
      <td>1001</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1031</td>
      <td>1020</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1036</td>
      <td>1032</td>
      <td>1036</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1131542 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2gif">2GIF</a></td>
      <td>3.0</td>
      <td>P1</td>
      <td>Full-length AcrB</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/organisms/e-coli/)
- **Expression construct**: Full-length AcrB
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
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a></td>
      <td>—</td>
      <td></td>
      <td>Membranes isolated</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2gif">2GIF</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">PNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLKPIAKGDHGEGKKGFF</span><span class="topo-unknown">GWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-outside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFVR</span><span class="topo-inside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-outside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVR</span><span class="topo-outside">RRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>513</td>
      <td>490</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>536</td>
      <td>514</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>558</td>
      <td>542</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1019</td>
      <td>1001</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1030</td>
      <td>1020</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1033</td>
      <td>1031</td>
      <td>1033</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1057</td>
      <td>1034</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2gif">2GIF</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">PNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-inside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAA</span><span class="topo-inside">FGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIVV</span><span class="topo-outside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPMA</span><span class="topo-inside">FFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLKPIAKGDHGEGKKGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGG</span><span class="topo-outside">ILRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-outside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-outside">RRFSRKNEDIEHSHT</span><span class="topo-unknown">VDHHLEHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>385</td>
      <td>366</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>396</td>
      <td>386</td>
      <td>396</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>412</td>
      <td>397</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>441</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>470</td>
      <td>458</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>515</td>
      <td>490</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>533</td>
      <td>516</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>540</td>
      <td>534</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1045</td>
      <td>1031</td>
      <td>1045</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1046</td>
      <td>1057</td>
      <td>1046</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2gif">2GIF</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">PNFFIDRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAIL</span><span class="topo-inside">KLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-inside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-outside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-inside">FGGSTGAIY</span><span class="topo-membrane">RQFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALIL</span><span class="topo-outside">TPALCATMLKPIAKGDHGEGKKGFFG</span><span class="topo-unknown">WFNRMFEKSTHHYTDSVGGIL</span><span class="topo-outside">RSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFVR</span><span class="topo-inside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-inside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-inside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVR</span><span class="topo-outside">RRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>11</td>
      <td>2</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>340</td>
      <td>29</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>467</td>
      <td>459</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>488</td>
      <td>468</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>489</td>
      <td>514</td>
      <td>489</td>
      <td>514</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>535</td>
      <td>515</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>540</td>
      <td>536</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>558</td>
      <td>541</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>891</td>
      <td>874</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1019</td>
      <td>1001</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1030</td>
      <td>1020</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1033</td>
      <td>1031</td>
      <td>1033</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1057</td>
      <td>1034</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1371##journal.pbio.0050007 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a></td>
      <td>2.54</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length AcrB with C-terminal 6xHis tag; in complex with DARPin 1108_19</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/organisms/e-coli/) BL21(DE3)
- **Expression construct**: Full-length AcrB with C-terminal 6xHis tag in pET28 vector
- **Tag info**: 6xHis tag; biotinylated

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>1 L culture; overnight induction at 30 C</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a></td>
      <td>—</td>
      <td></td>
      <td>Membranes collected and isolated</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Lipids/debris removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 100,000g for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 50 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a>; elute with 200 mM imidazole</td>
    </tr>
  </tbody>
</table>
**Final sample**: AcrB in 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/proteins/acrb/">AcrB</a>-<a href="/xray-mp-wiki/concepts/darpin/">DARPin</a> 1108_19 complex</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form P2(1)2(1)2(1). <a href="/xray-mp-wiki/concepts/darpin/">DARPin</a> provided additional crystal contacts. Diffracted to 2.5 A. Data collected at SLS beamline X06SA.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMA</span><span class="topo-outside">FFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLA</span><span class="topo-inside">ALYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNA</span><span class="topo-inside">ILIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLA</span><span class="topo-unknown">IF</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEHSH</span><span class="topo-unknown">TVDHHHHHHHH</span></span>
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
      <td>25</td>
      <td>11</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>342</td>
      <td>26</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>410</td>
      <td>397</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>457</td>
      <td>443</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>470</td>
      <td>458</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>512</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>542</td>
      <td>536</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>889</td>
      <td>875</td>
      <td>889</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>890</td>
      <td>901</td>
      <td>890</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>918</td>
      <td>902</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>942</td>
      <td>928</td>
      <td>942</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>943</td>
      <td>975</td>
      <td>943</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1018</td>
      <td>1004</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1044</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>1055</td>
      <td>1045</td>
      <td>1055</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSIT</span><span class="topo-membrane">IVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHHHHHHH</span></span>
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
      <td>341</td>
      <td>25</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>411</td>
      <td>399</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>455</td>
      <td>442</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>489</td>
      <td>474</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>540</td>
      <td>535</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>555</td>
      <td>541</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>915</td>
      <td>896</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1055</td>
      <td>1034</td>
      <td>1055</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPS</span><span class="topo-membrane">LYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRR</span><span class="topo-inside">RFSRKNEDI</span><span class="topo-unknown">EHSHTVDHHHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>26</td>
      <td>13</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>342</td>
      <td>27</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>410</td>
      <td>397</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>485</td>
      <td>471</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>875</td>
      <td>557</td>
      <td>875</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>876</td>
      <td>891</td>
      <td>876</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>916</td>
      <td>899</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>929</td>
      <td>917</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1031</td>
      <td>1020</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1040</td>
      <td>1032</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1041</td>
      <td>1055</td>
      <td>1041</td>
      <td>1055</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2j8s">2J8S</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSD</span><span class="topo-outside">LGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>166</td>
      <td>14</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature13205 (1 structure, 9 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a></td>
      <td>15-20 (pseudo-atomic model)</td>
      <td>N/A</td>
      <td>Complete AcrABZ-TolC complex assembled from fusion proteins</td>
      <td>Unliganded</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/organisms/e-coli/)
- **Expression construct**: AcrB with C-terminal His5 tag; AcrZ with C-terminal His5 tag; AcrA-polyGlySer-AcrZ-His5 fusion and TolC for complete assembly
- **Tag info**: His5 tag on AcrB; His5 tag on AcrZ

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>—</td>
      <td></td>
      <td>AcrBZ complex enriched by IMAC before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">size-exclusion chromatography</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Gel filtration</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step for AcrBZ complex</td>
    </tr>
    <tr>
      <td>GraFix gradient</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>-glutaraldehyde gradient <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>—</td>
      <td></td>
      <td>Crosslinking and gradient fixation for <a href="/xray-mp-wiki/methods/cryo-em/">cryo-EM</a> specimen preparation</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified AcrABZ-TolC complex in 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 400 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AcrBZ-<a href="/xray-mp-wiki/concepts/darpin/">DARPin</a> complex</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystals of AcrBZ with <a href="/xray-mp-wiki/concepts/darpin/">DARPin</a>. Data at Diamond Light Source.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AcrBZ complex (without <a href="/xray-mp-wiki/concepts/darpin/">DARPin</a>)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>AcrBZ complex crystallized by <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a>.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-inside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-outside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTAT</span><span class="topo-inside">GFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-inside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRR</span><span class="topo-outside">RFSRKN</span><span class="topo-unknown">EDIEHSHTVD</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>341</td>
      <td>27</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>678</td>
      <td>674</td>
      <td>678</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>679</td>
      <td>874</td>
      <td>679</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1031</td>
      <td>1023</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1037</td>
      <td>1032</td>
      <td>1037</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1047</td>
      <td>1038</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-inside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-inside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-inside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">LELLKSLVFAVIMVPVVMAIILGLI</span><span class="topo-unknown">YGLGEVFNI</span><span class="topo-outside">FSGVGKKDQPG</span><span class="topo-unknown">QNH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>26</td>
      <td>2</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>35</td>
      <td>27</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>49</td>
      <td>47</td>
      <td>49</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain D (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-inside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-outside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTAT</span><span class="topo-inside">GFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-inside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRR</span><span class="topo-outside">RFSRKN</span><span class="topo-unknown">EDIEHSHTVD</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>341</td>
      <td>27</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>678</td>
      <td>674</td>
      <td>678</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>679</td>
      <td>874</td>
      <td>679</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1031</td>
      <td>1023</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1037</td>
      <td>1032</td>
      <td>1037</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1047</td>
      <td>1038</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-inside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-inside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-inside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">LELLKSLVFAVIMVPVVMAIILGLI</span><span class="topo-unknown">YGLGEVFNI</span><span class="topo-outside">FSGVGKKDQPG</span><span class="topo-unknown">QNH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>26</td>
      <td>2</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>35</td>
      <td>27</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>49</td>
      <td>47</td>
      <td>49</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain G (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-outside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-inside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-inside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-inside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-inside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-inside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-inside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-outside">FLQ</span></span>
<span class="topo-line"><span class="topo-outside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-inside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-outside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-outside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-inside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-outside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-outside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-inside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-inside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-inside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTAT</span><span class="topo-inside">GFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-inside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-inside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-inside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-outside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-inside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-outside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-outside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-inside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRR</span><span class="topo-outside">RFSRKN</span><span class="topo-unknown">EDIEHSHTVD</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>341</td>
      <td>27</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>678</td>
      <td>674</td>
      <td>678</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>679</td>
      <td>874</td>
      <td>679</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1031</td>
      <td>1023</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1037</td>
      <td>1032</td>
      <td>1037</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1038</td>
      <td>1047</td>
      <td>1038</td>
      <td>1047</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-inside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-inside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-inside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c48">4C48</a> — Chain I (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">LELLKSLVFAVIMVPVVMAIILGLI</span><span class="topo-unknown">YGLGEVFNI</span><span class="topo-outside">FSGVGKKDQPG</span><span class="topo-unknown">QNH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>26</td>
      <td>2</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>35</td>
      <td>27</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>46</td>
      <td>36</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>49</td>
      <td>47</td>
      <td>49</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41467-021-24151-3 (10 structures, 51 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>AcrB Gly619Pro variant co-crystallized with rifabutin</td>
      <td>Rifabutin</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>AcrB Gly621Pro variant co-crystallized with rifabutin</td>
      <td>Rifabutin (2 molecules)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>AcrB wild-type co-crystallized with beta-lactam mixture</td>
      <td>Fusidic acid (partial occupancy)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>AcrB Gly621Pro co-crystallized with 3-formylrifamycin SV</td>
      <td>3-Formylrifamycin SV</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>AcrB Gly619Pro co-crystallized with erythromycin</td>
      <td>Erythromycin</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>AcrB wild-type co-crystallized with antibiotic cocktail (erythromycin, linezolid, oxacillin, fusidic acid)</td>
      <td>Fusidic acid (TMD-BP)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>AcrB Phe380Ala variant</td>
      <td>Unliganded</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>AcrB Phe563Ala variant in complex with DARPin</td>
      <td>Unliganded</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>AcrB Phe380Ala variant soaked with fusidic acid</td>
      <td>Fusidic acid</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>AcrB Gly619Pro_Gly621Pro double variant co-crystallized with fusidic acid</td>
      <td>Fusidic acid</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKGF</span><span class="topo-unknown">FGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRRF</span><span class="topo-inside">SRKNEDIEH</span><span class="topo-unknown">SHTVDHHLEHHHHHH</span></span>
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
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>442</td>
      <td>412</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>512</td>
      <td>490</td>
      <td>512</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>537</td>
      <td>513</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>890</td>
      <td>875</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>916</td>
      <td>899</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>927</td>
      <td>917</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1033</td>
      <td>1020</td>
      <td>1033</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1042</td>
      <td>1034</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">PNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSIT</span><span class="topo-membrane">IVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGV</span><span class="topo-unknown">MPLVISTGAG</span><span class="topo-outside">SGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>341</td>
      <td>25</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>439</td>
      <td>413</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>489</td>
      <td>474</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>986</td>
      <td>975</td>
      <td>986</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>997</td>
      <td>1004</td>
      <td>997</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>343</td>
      <td>27</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>441</td>
      <td>411</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>455</td>
      <td>442</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>470</td>
      <td>456</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>540</td>
      <td>535</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>915</td>
      <td>896</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>975</td>
      <td>945</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEIL</span><span class="topo-unknown">QKLN</span></span>
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
      <td>165</td>
      <td>13</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo7">6ZO7</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLP</span><span class="topo-unknown">PKEATRKSMGQI</span><span class="topo-inside">QGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEH</span><span class="topo-unknown">SHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
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
      <td>342</td>
      <td>26</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>396</td>
      <td>383</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>426</td>
      <td>412</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>438</td>
      <td>427</td>
      <td>438</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>439</td>
      <td>442</td>
      <td>439</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1042</td>
      <td>1033</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">PNFFIDRP</span><span class="topo-membrane">IFAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRA</span><span class="topo-membrane">TLIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVVV</span><span class="topo-inside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSIT</span><span class="topo-membrane">IVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTP</span><span class="topo-inside">ALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAILI</span><span class="topo-inside">VEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>9</td>
      <td>2</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>364</td>
      <td>358</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>382</td>
      <td>365</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>413</td>
      <td>399</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>490</td>
      <td>474</td>
      <td>490</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>510</td>
      <td>491</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>536</td>
      <td>511</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>539</td>
      <td>537</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>945</td>
      <td>931</td>
      <td>945</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>946</td>
      <td>974</td>
      <td>946</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAALY</span><span class="topo-inside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSR</span><span class="topo-unknown">KNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>343</td>
      <td>27</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>410</td>
      <td>397</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>441</td>
      <td>411</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>535</td>
      <td>511</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>540</td>
      <td>536</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>892</td>
      <td>877</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>916</td>
      <td>896</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>929</td>
      <td>917</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>975</td>
      <td>945</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1035</td>
      <td>1033</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zo9">6ZO9</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLA</span><span class="topo-unknown">IF</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEH</span><span class="topo-unknown">SHTVDHHLEHHHHHH</span></span>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>890</td>
      <td>877</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>915</td>
      <td>902</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1018</td>
      <td>1005</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1042</td>
      <td>1033</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVM</span><span class="topo-inside">YLFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FAVLAAFGFSINTLTMFGMV</span><span class="topo-membrane">LAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKGF</span><span class="topo-unknown">FGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LV</span><span class="topo-unknown">ISTGAGSGA</span><span class="topo-outside">QNAVGT</span><span class="topo-membrane">GVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>355</td>
      <td>343</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>365</td>
      <td>356</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>399</td>
      <td>380</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>411</td>
      <td>400</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>454</td>
      <td>442</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>512</td>
      <td>490</td>
      <td>512</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>534</td>
      <td>513</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>540</td>
      <td>535</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>553</td>
      <td>541</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>915</td>
      <td>896</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>990</td>
      <td>989</td>
      <td>990</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>1005</td>
      <td>1000</td>
      <td>1005</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1006</td>
      <td>1022</td>
      <td>1006</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKTL</span><span class="topo-membrane">VEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSR</span><span class="topo-unknown">KNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>344</td>
      <td>26</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>472</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1035</td>
      <td>1033</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoa">6ZOA</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLA</span><span class="topo-unknown">IF</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSR</span><span class="topo-unknown">KNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>890</td>
      <td>877</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>915</td>
      <td>902</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1018</td>
      <td>1005</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1035</td>
      <td>1033</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FAVLAAFGFSINTLTMFGMV</span><span class="topo-membrane">LAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVGTGV</span><span class="topo-membrane">MGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>399</td>
      <td>380</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>412</td>
      <td>400</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>441</td>
      <td>413</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>454</td>
      <td>442</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>540</td>
      <td>535</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>553</td>
      <td>541</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>915</td>
      <td>896</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1007</td>
      <td>989</td>
      <td>1007</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1008</td>
      <td>1022</td>
      <td>1008</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKTL</span><span class="topo-membrane">VEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>344</td>
      <td>26</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>472</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zob">6ZOB</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFPFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLV</span><span class="topo-outside">ISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>442</td>
      <td>412</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>928</td>
      <td>916</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>943</td>
      <td>929</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>990</td>
      <td>975</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>1004</td>
      <td>991</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFID</span><span class="topo-inside">RP</span><span class="topo-membrane">IFAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRA</span><span class="topo-membrane">TLIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVVV</span><span class="topo-inside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTPAL</span><span class="topo-inside">CATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFPFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAILI</span><span class="topo-inside">VEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVGTG</span><span class="topo-membrane">VMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>364</td>
      <td>358</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>382</td>
      <td>365</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>413</td>
      <td>399</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>474</td>
      <td>456</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>492</td>
      <td>475</td>
      <td>492</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>493</td>
      <td>511</td>
      <td>493</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>539</td>
      <td>537</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>945</td>
      <td>931</td>
      <td>945</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>946</td>
      <td>974</td>
      <td>946</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1006</td>
      <td>989</td>
      <td>1006</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1007</td>
      <td>1022</td>
      <td>1007</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFPFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>343</td>
      <td>27</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>470</td>
      <td>456</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>555</td>
      <td>541</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>915</td>
      <td>896</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>975</td>
      <td>945</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEIL</span><span class="topo-unknown">QKLN</span></span>
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
      <td>11</td>
      <td>165</td>
      <td>11</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoc">6ZOC</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFVR</span><span class="topo-outside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQN</span><span class="topo-membrane">AVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVR</span><span class="topo-inside">RRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>411</td>
      <td>395</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>512</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>541</td>
      <td>536</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>558</td>
      <td>542</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>891</td>
      <td>874</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1001</td>
      <td>993</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1002</td>
      <td>1019</td>
      <td>1002</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1030</td>
      <td>1020</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1033</td>
      <td>1031</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">PNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHE</span><span class="topo-membrane">VVKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLV</span><span class="topo-unknown">ISTGAGSGAQNAV</span><span class="topo-outside">G</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>339</td>
      <td>27</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>357</td>
      <td>340</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>439</td>
      <td>413</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>456</td>
      <td>440</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>556</td>
      <td>540</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>990</td>
      <td>975</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1004</td>
      <td>1004</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRR</span><span class="topo-inside">R</span><span class="topo-unknown">FSRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>341</td>
      <td>28</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>441</td>
      <td>411</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>512</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>540</td>
      <td>536</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>557</td>
      <td>541</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>874</td>
      <td>558</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>975</td>
      <td>945</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1031</td>
      <td>1023</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1032</td>
      <td>1032</td>
      <td>1032</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zod">6ZOD</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSD</span><span class="topo-outside">LGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEIL</span><span class="topo-unknown">QKLN</span></span>
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
      <td>14</td>
      <td>165</td>
      <td>14</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSALPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSRKNEDI</span><span class="topo-unknown">EHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>365</td>
      <td>357</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>537</td>
      <td>511</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>540</td>
      <td>538</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1040</td>
      <td>1033</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSALPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSRKNEDI</span><span class="topo-unknown">EHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>365</td>
      <td>357</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>537</td>
      <td>511</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>540</td>
      <td>538</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1040</td>
      <td>1033</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain E (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSALPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSRKNEDI</span><span class="topo-unknown">EHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>365</td>
      <td>357</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>537</td>
      <td>511</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>540</td>
      <td>538</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1040</td>
      <td>1033</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoe">6ZOE</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTAAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLP</span><span class="topo-unknown">PKEATRKSMGQI</span><span class="topo-inside">QGAL</span><span class="topo-membrane">VGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEH</span><span class="topo-unknown">SHTVDHHLEHHHHHH</span></span>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>426</td>
      <td>412</td>
      <td>426</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>438</td>
      <td>427</td>
      <td>438</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>439</td>
      <td>442</td>
      <td>439</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>456</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>890</td>
      <td>875</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>916</td>
      <td>899</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>928</td>
      <td>917</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>943</td>
      <td>929</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1042</td>
      <td>1033</td>
      <td>1042</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">PNFFIDRP</span><span class="topo-membrane">IFAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTAAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTP</span><span class="topo-inside">ALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRRF</span><span class="topo-inside">S</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>9</td>
      <td>2</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>439</td>
      <td>413</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>454</td>
      <td>440</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>490</td>
      <td>475</td>
      <td>490</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>510</td>
      <td>491</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1033</td>
      <td>1023</td>
      <td>1033</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1034</td>
      <td>1034</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTAAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YESWSI</span><span class="topo-membrane">PFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSR</span><span class="topo-unknown">KNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>343</td>
      <td>27</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>470</td>
      <td>456</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>897</td>
      <td>892</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>915</td>
      <td>898</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1004</td>
      <td>992</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1035</td>
      <td>1033</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHG</span><span class="topo-outside">SDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>12</td>
      <td>166</td>
      <td>12</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zof">6ZOF</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTFAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPATVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLA</span><span class="topo-unknown">IF</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>890</td>
      <td>877</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>915</td>
      <td>902</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1018</td>
      <td>1005</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTFAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FAVLAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPATVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLYA</span><span class="topo-membrane">ISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGA</span><span class="topo-outside">LLAATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVGTGV</span><span class="topo-membrane">MGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>398</td>
      <td>380</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>441</td>
      <td>413</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>454</td>
      <td>442</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>878</td>
      <td>554</td>
      <td>878</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>879</td>
      <td>891</td>
      <td>879</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>912</td>
      <td>896</td>
      <td>912</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1007</td>
      <td>989</td>
      <td>1007</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1008</td>
      <td>1022</td>
      <td>1008</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTFAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKTL</span><span class="topo-membrane">VEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPATVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>344</td>
      <td>26</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>472</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQK</span><span class="topo-unknown">LN</span></span>
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
      <td>11</td>
      <td>167</td>
      <td>11</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zog">6ZOG</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLA</span><span class="topo-unknown">IF</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>876</td>
      <td>557</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>890</td>
      <td>877</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>915</td>
      <td>902</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>943</td>
      <td>930</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1018</td>
      <td>1005</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1032</td>
      <td>1019</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FAVLAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGA</span><span class="topo-outside">LLAATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVM</span><span class="topo-outside">PLVISTGAGSGAQNAVGTGV</span><span class="topo-membrane">MGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FS</span><span class="topo-unknown">RKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>398</td>
      <td>380</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>441</td>
      <td>413</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>454</td>
      <td>442</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>912</td>
      <td>896</td>
      <td>912</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>944</td>
      <td>931</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>987</td>
      <td>975</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>1007</td>
      <td>988</td>
      <td>1007</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1008</td>
      <td>1022</td>
      <td>1008</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1034</td>
      <td>1033</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPIFA</span><span class="topo-membrane">WVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKT</span><span class="topo-membrane">LVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAPRPQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>343</td>
      <td>26</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>472</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zoh">6ZOH</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSD</span><span class="topo-outside">LGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>14</td>
      <td>166</td>
      <td>14</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature01050 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1iwg">1IWG</a></td>
      <td>3.5</td>
      <td>R32</td>
      <td>Wild-type AcrB from E. coli with C-terminal polyhistidine tag, expressed in E. coli JM109</td>
      <td>None (apo form)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1iwg">1IWG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRATL</span><span class="topo-membrane">IPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDW</span><span class="topo-unknown">TGMSYQERL</span><span class="topo-outside">SGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIST</span><span class="topo-outside">GAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLA</span><span class="topo-inside">IF</span></span>
<span class="topo-line"><span class="topo-inside">FVPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>11</td>
      <td>7</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>366</td>
      <td>357</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>386</td>
      <td>367</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>542</td>
      <td>537</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>557</td>
      <td>543</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>859</td>
      <td>712</td>
      <td>859</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>860</td>
      <td>868</td>
      <td>860</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>873</td>
      <td>869</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>993</td>
      <td>976</td>
      <td>993</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>994</td>
      <td>1000</td>
      <td>994</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1018</td>
      <td>1001</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1025</td>
      <td>1019</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1iwg">1IWG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRATL</span><span class="topo-membrane">IPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDW</span><span class="topo-unknown">TGMSYQERL</span><span class="topo-outside">SGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIST</span><span class="topo-outside">GAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLA</span><span class="topo-inside">IF</span></span>
<span class="topo-line"><span class="topo-inside">FVPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>11</td>
      <td>7</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>366</td>
      <td>357</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>386</td>
      <td>367</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>542</td>
      <td>537</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>557</td>
      <td>543</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>859</td>
      <td>712</td>
      <td>859</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>860</td>
      <td>868</td>
      <td>860</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>873</td>
      <td>869</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>993</td>
      <td>976</td>
      <td>993</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>994</td>
      <td>1000</td>
      <td>994</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1018</td>
      <td>1001</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1025</td>
      <td>1019</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1iwg">1IWG</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMY</span><span class="topo-inside">LFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRATL</span><span class="topo-membrane">IPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDW</span><span class="topo-unknown">TGMSYQERL</span><span class="topo-outside">SGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIST</span><span class="topo-outside">GAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLA</span><span class="topo-inside">IF</span></span>
<span class="topo-line"><span class="topo-inside">FVPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>11</td>
      <td>7</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>366</td>
      <td>357</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>386</td>
      <td>367</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>542</td>
      <td>537</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>557</td>
      <td>543</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>859</td>
      <td>712</td>
      <td>859</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>860</td>
      <td>868</td>
      <td>860</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>873</td>
      <td>869</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>993</td>
      <td>976</td>
      <td>993</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>994</td>
      <td>1000</td>
      <td>994</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1018</td>
      <td>1001</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1025</td>
      <td>1019</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1007##s10969-013-9154-x (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4k7q">4K7Q</a></td>
      <td>3.5</td>
      <td>R32</td>
      <td>Wild-type AcrB with C-terminal polyhistidine tag</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/linezolid">Linezolid</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4k7q">4K7Q</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLTM</span><span class="topo-membrane">FGMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSY</span><span class="topo-unknown">QERL</span><span class="topo-outside">SGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-inside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IE</span><span class="topo-unknown">ATLDAV</span><span class="topo-inside">RMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-inside">VPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>7</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>395</td>
      <td>387</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>411</td>
      <td>396</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>557</td>
      <td>541</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>864</td>
      <td>712</td>
      <td>864</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>865</td>
      <td>868</td>
      <td>865</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>874</td>
      <td>869</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>962</td>
      <td>945</td>
      <td>962</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>963</td>
      <td>968</td>
      <td>963</td>
      <td>968</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>969</td>
      <td>974</td>
      <td>969</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1021</td>
      <td>1004</td>
      <td>1021</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1025</td>
      <td>1022</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4k7q">4K7Q</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLTM</span><span class="topo-membrane">FGMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSY</span><span class="topo-unknown">QERL</span><span class="topo-outside">SGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-inside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IE</span><span class="topo-unknown">ATLDAV</span><span class="topo-inside">RMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-inside">VPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>7</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>395</td>
      <td>387</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>411</td>
      <td>396</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>557</td>
      <td>541</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>864</td>
      <td>712</td>
      <td>864</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>865</td>
      <td>868</td>
      <td>865</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>874</td>
      <td>869</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>962</td>
      <td>945</td>
      <td>962</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>963</td>
      <td>968</td>
      <td>963</td>
      <td>968</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>969</td>
      <td>974</td>
      <td>969</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1021</td>
      <td>1004</td>
      <td>1021</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1025</td>
      <td>1022</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4k7q">4K7Q</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MPNFFI</span><span class="topo-inside">DRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLTM</span><span class="topo-membrane">FGMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLK</span><span class="topo-unknown">PIAKGDHGEGKKGF</span><span class="topo-inside">F</span><span class="topo-unknown">GWFNRMFEKST</span><span class="topo-inside">H</span><span class="topo-unknown">HYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHP</span><span class="topo-unknown">D</span><span class="topo-outside">MLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSY</span><span class="topo-unknown">QERL</span><span class="topo-outside">SGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-inside">ESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IE</span><span class="topo-unknown">ATLDAV</span><span class="topo-inside">RMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-inside">VPVF</span><span class="topo-unknown">FVVVRRR</span><span class="topo-inside">FSRK</span><span class="topo-unknown">NEDIEHSHTVDHHHHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>7</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>395</td>
      <td>387</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>411</td>
      <td>396</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>458</td>
      <td>442</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>498</td>
      <td>490</td>
      <td>498</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>499</td>
      <td>512</td>
      <td>499</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>524</td>
      <td>514</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>536</td>
      <td>526</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>540</td>
      <td>537</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>557</td>
      <td>541</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>710</td>
      <td>558</td>
      <td>710</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>711</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>712</td>
      <td>864</td>
      <td>712</td>
      <td>864</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>865</td>
      <td>868</td>
      <td>865</td>
      <td>868</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>869</td>
      <td>874</td>
      <td>869</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>895</td>
      <td>893</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>962</td>
      <td>945</td>
      <td>962</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>963</td>
      <td>968</td>
      <td>963</td>
      <td>968</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>969</td>
      <td>974</td>
      <td>969</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>975</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1021</td>
      <td>1004</td>
      <td>1021</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1025</td>
      <td>1022</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1032</td>
      <td>1026</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1036</td>
      <td>1033</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1053</td>
      <td>1037</td>
      <td>1053</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.jsb.2011.01.014 (3 structures, 10 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2jbs">2JBS</a></td>
      <td>2.54</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB in complex with <a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#1 crystallization chaperone</td>
      <td><a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#1</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a></td>
      <td>2.70</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB in complex with <a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#2 crystallization chaperone</td>
      <td><a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#2</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a></td>
      <td>3.34</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB in complex with <a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#3 crystallization chaperone</td>
      <td><a href="/xray-mp-wiki/concepts/darpin">DARPin</a>#3</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKGFFGWFNRMFEKSTHHYTDSVGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFVRL</span><span class="topo-outside">PSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAI</span><span class="topo-unknown">VELGTAT</span><span class="topo-outside">GFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQ</span><span class="topo-unknown">ERLSGN</span><span class="topo-outside">QA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLA</span><span class="topo-inside">IF</span></span>
<span class="topo-line"><span class="topo-inside">FVPVFFVVVRRRFSR</span><span class="topo-unknown">KNE</span><span class="topo-inside">DIEHSH</span><span class="topo-unknown">TVDHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>469</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>542</td>
      <td>490</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>559</td>
      <td>543</td>
      <td>559</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>560</td>
      <td>671</td>
      <td>560</td>
      <td>671</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>672</td>
      <td>678</td>
      <td>672</td>
      <td>678</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>679</td>
      <td>865</td>
      <td>679</td>
      <td>865</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>866</td>
      <td>871</td>
      <td>866</td>
      <td>871</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>872</td>
      <td>873</td>
      <td>872</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>919</td>
      <td>902</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1018</td>
      <td>1001</td>
      <td>1018</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1019</td>
      <td>1035</td>
      <td>1019</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1036</td>
      <td>1038</td>
      <td>1036</td>
      <td>1038</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1039</td>
      <td>1044</td>
      <td>1039</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>1049</td>
      <td>1045</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKGFFGWFNRMFEKSTHHYTDSVGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIV</span><span class="topo-unknown">ELG</span><span class="topo-outside">TATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQE</span><span class="topo-unknown">RLSG</span><span class="topo-outside">NQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-inside">PVFFVVVRRRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>470</td>
      <td>457</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>540</td>
      <td>490</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>556</td>
      <td>541</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>672</td>
      <td>557</td>
      <td>672</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>673</td>
      <td>675</td>
      <td>673</td>
      <td>675</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>676</td>
      <td>866</td>
      <td>676</td>
      <td>866</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>867</td>
      <td>870</td>
      <td>867</td>
      <td>870</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>871</td>
      <td>874</td>
      <td>871</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>918</td>
      <td>896</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1033</td>
      <td>1023</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1049</td>
      <td>1034</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPIFA</span><span class="topo-membrane">WVIAIIIMLAGGLAIL</span><span class="topo-outside">KLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYR</span><span class="topo-membrane">QFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVA</span><span class="topo-inside">LILTPALCATMLKPIAKGDHGEGKKGFFGWFNRMFEKSTHHYTDSVGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-inside">F</span></span>
<span class="topo-line"><span class="topo-inside">FVPVFFVVVRRRFS</span><span class="topo-unknown">RKNEDIEHSHTVDHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>340</td>
      <td>29</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>468</td>
      <td>459</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>485</td>
      <td>469</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>541</td>
      <td>486</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>557</td>
      <td>542</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>874</td>
      <td>558</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1034</td>
      <td>1020</td>
      <td>1034</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1035</td>
      <td>1049</td>
      <td>1035</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGQDDEVRILMANGADVNARDFTGWTPLHLAAHFGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAKDSLGVTPLHLAARRGHLEIVEVLLKNGADVNASDSHGFTPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">AKRGHLEIVEVLLKNGADVNAQDKFGKTAFDISIDNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3noc">3NOC</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSD</span><span class="topo-outside">LGKKLLEAARAGQDDEVRILMANGADVNARDFTGWTPLHLAAHFGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAKDSLGVTPLHLAARRGHLEIVEVLLKNGADVNASDSHGFTPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">AKRGHLEIVEVLLKNGADVNAQDKFGKTAFDISIDNGNEDLAEIL</span><span class="topo-unknown">QKLN</span></span>
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
      <td>1</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>165</td>
      <td>14</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>169</td>
      <td>166</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHG</span><span class="topo-unknown">EGKKGF</span><span class="topo-inside">FGWFNRMFEKSTHHYTDSVGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">YL</span><span class="topo-membrane">VLYLIIVVGMAYLFVR</span><span class="topo-outside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIV</span><span class="topo-unknown">ELGTA</span><span class="topo-outside">TGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTG</span><span class="topo-unknown">MSYQERLSGN</span><span class="topo-outside">QAP</span><span class="topo-membrane">SLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIPFS</span></span>
<span class="topo-line"><span class="topo-inside">V</span><span class="topo-membrane">MLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQN</span><span class="topo-membrane">AVGTGVMGGMVTATVLAI</span><span class="topo-inside">F</span></span>
<span class="topo-line"><span class="topo-inside">FVPVFFVVVRRRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>340</td>
      <td>27</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>506</td>
      <td>490</td>
      <td>506</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>512</td>
      <td>507</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>542</td>
      <td>513</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>558</td>
      <td>543</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>672</td>
      <td>559</td>
      <td>672</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>673</td>
      <td>677</td>
      <td>673</td>
      <td>677</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>678</td>
      <td>861</td>
      <td>678</td>
      <td>861</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>862</td>
      <td>871</td>
      <td>862</td>
      <td>871</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>872</td>
      <td>874</td>
      <td>872</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>890</td>
      <td>875</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>901</td>
      <td>891</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>919</td>
      <td>902</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1001</td>
      <td>992</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1002</td>
      <td>1019</td>
      <td>1002</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1033</td>
      <td>1020</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1049</td>
      <td>1034</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">PNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYLF</span><span class="topo-inside">LQ</span></span>
<span class="topo-line"><span class="topo-inside">NF</span><span class="topo-membrane">RATLIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVVV</span><span class="topo-inside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTP</span><span class="topo-inside">ALCATMLKPIAKGDHGEGKKGFFGWFNRMFEKSTHHYTDSVGGILRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPT</span><span class="topo-unknown">GVG</span><span class="topo-outside">YDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAILIV</span><span class="topo-inside">EFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRL</span><span class="topo-membrane">RPILMTSLAFILGVMPLV</span><span class="topo-outside">IST</span><span class="topo-unknown">GA</span><span class="topo-outside">GSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-inside">PVFFVVVRRRF</span><span class="topo-unknown">SRKNEDIEHSHTVDHH</span></span>
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
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>341</td>
      <td>27</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>358</td>
      <td>342</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>362</td>
      <td>359</td>
      <td>362</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>383</td>
      <td>363</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>413</td>
      <td>398</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>490</td>
      <td>472</td>
      <td>490</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>539</td>
      <td>491</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>555</td>
      <td>540</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>853</td>
      <td>556</td>
      <td>853</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>854</td>
      <td>856</td>
      <td>854</td>
      <td>856</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>857</td>
      <td>876</td>
      <td>857</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>892</td>
      <td>877</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>929</td>
      <td>916</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>946</td>
      <td>930</td>
      <td>946</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>947</td>
      <td>972</td>
      <td>947</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>990</td>
      <td>973</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>993</td>
      <td>991</td>
      <td>993</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>994</td>
      <td>995</td>
      <td>994</td>
      <td>995</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>996</td>
      <td>1004</td>
      <td>996</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1033</td>
      <td>1023</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1049</td>
      <td>1034</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPIFA</span><span class="topo-membrane">WVIAIIIMLAGGLAIL</span><span class="topo-outside">KLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALIL</span><span class="topo-inside">TPALCATMLKPIAKGDHGEGKKGFFGWFNRMFEKSTHHYTDSVGGILRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-inside">PVFFVVVRRRFSRKNEDI</span><span class="topo-unknown">EHSHTVDHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>341</td>
      <td>29</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>488</td>
      <td>471</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>489</td>
      <td>541</td>
      <td>489</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1040</td>
      <td>1023</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1041</td>
      <td>1049</td>
      <td>1041</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGQDDEVRILMANGADVNASDHVGWTPLHLAAYFGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNADDSLGVTPLHLAADRGHLEVVEVLLKNGADVNANDHNGFTPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANIGHLEIVEVLLKHGADVNAQDKFGKTAFDISIDNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>13</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3nog">3NOG</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGS</span><span class="topo-outside">DLGKKLLEAARAGQDDEVRILMANGADVNASDHVGWTPLHLAAYFGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNADDSLGVTPLHLAADRGHLEVVEVLLKNGADVNANDHNGFTPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANIGHLEIVEVLLKHGADVNAQDKFGK</span><span class="topo-unknown">TAF</span><span class="topo-outside">DISIDNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>147</td>
      <td>13</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>150</td>
      <td>148</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.str.2007.09.023 (1 structure, 6 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a></td>
      <td>3.5</td>
      <td>P3221</td>
      <td>AcrB in complex with endogenous <a href="/xray-mp-wiki/proteins/yajc">YajC</a> transmembrane subunit</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ampicillin">Ampicillin</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain E (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##ncomms13819 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a></td>
      <td>2.5</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>Wild-type AcrB in complex with <a href="/xray-mp-wiki/concepts/darpin">DARPin</a> crystallization chaperone</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/fusidic-acid">Fusidic Acid</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFVR</span><span class="topo-outside">LPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQN</span><span class="topo-membrane">AVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEHSH</span><span class="topo-unknown">TVDHHLEHHHHHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>411</td>
      <td>395</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>442</td>
      <td>412</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>558</td>
      <td>542</td>
      <td>558</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>559</td>
      <td>873</td>
      <td>559</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>891</td>
      <td>874</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1001</td>
      <td>992</td>
      <td>1001</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1002</td>
      <td>1019</td>
      <td>1002</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1044</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>1057</td>
      <td>1045</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVVV</span><span class="topo-inside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>340</td>
      <td>27</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>413</td>
      <td>398</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>456</td>
      <td>440</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>535</td>
      <td>511</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>539</td>
      <td>536</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>556</td>
      <td>540</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>892</td>
      <td>875</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>916</td>
      <td>895</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>928</td>
      <td>917</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>944</td>
      <td>929</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1057</td>
      <td>1034</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPIF</span><span class="topo-membrane">AWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVV</span><span class="topo-membrane">KTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSI</span><span class="topo-membrane">PFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>341</td>
      <td>28</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>470</td>
      <td>459</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>512</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>541</td>
      <td>536</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>557</td>
      <td>542</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>874</td>
      <td>558</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>897</td>
      <td>892</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>919</td>
      <td>898</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1003</td>
      <td>993</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1057</td>
      <td>1034</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dx5">4DX5</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-outside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>169</td>
      <td>167</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.7554##eLife.03145 (4 structures, 17 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u8v">4U8V</a></td>
      <td>2.0</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB(D407N) mutant in complex with DARPin crystallization chaperone</td>
      <td>Minocycline</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u8y">4U8Y</a></td>
      <td>2.3</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB(D408N) mutant in complex with DARPin crystallization chaperone</td>
      <td>Minocycline</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u95">4U95</a></td>
      <td>2.3</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB(K940A) mutant in complex with DARPin crystallization chaperone</td>
      <td>Minocycline</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a></td>
      <td>2.0</td>
      <td>P2$_{1}$2$_{1}$2$_{1}$</td>
      <td>AcrB(R971A) mutant in complex with DARPin crystallization chaperone</td>
      <td>None (no minocycline added)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) transformed with pET28 vector; overnight induction at 30 C
- **Construct**: Full-length AcrB with C-terminal hexahistidine tag
- **Notes**: DARPin 1108_19 expressed from pQIA vector under IPTG-inducible T5 promoter in E. coli XL1-blue

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8v">4U8V</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLT</span><span class="topo-membrane">MFGMVLAIGLLVNDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMAF</span><span class="topo-outside">FGGSTGAIY</span><span class="topo-membrane">RQFSITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNR</span><span class="topo-inside">MFEKST</span><span class="topo-unknown">HHYTDSVGGILR</span><span class="topo-inside">STGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQA</span><span class="topo-membrane">PSLYAISLIVVFLCLAA</span><span class="topo-inside">LYESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVY</span><span class="topo-membrane">FQVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVIS</span><span class="topo-outside">TGAGSGAQ</span><span class="topo-membrane">NAVGTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVR</span><span class="topo-inside">RRFSRKNEDIEHSH</span><span class="topo-unknown">TVDHHLEHHHHHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>340</td>
      <td>28</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>458</td>
      <td>443</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>467</td>
      <td>459</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>489</td>
      <td>468</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>518</td>
      <td>511</td>
      <td>518</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>519</td>
      <td>524</td>
      <td>519</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>536</td>
      <td>525</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>557</td>
      <td>542</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>873</td>
      <td>558</td>
      <td>873</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>874</td>
      <td>890</td>
      <td>874</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>898</td>
      <td>891</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>919</td>
      <td>899</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>926</td>
      <td>920</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>943</td>
      <td>927</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>992</td>
      <td>976</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1000</td>
      <td>993</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1019</td>
      <td>1001</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1030</td>
      <td>1020</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1044</td>
      <td>1031</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8v">4U8V</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLAI</span><span class="topo-outside">LKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHE</span><span class="topo-membrane">VVKTLVEAIILVFLVM</span><span class="topo-inside">YLFLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVLAAF</span><span class="topo-outside">GFSINTLTM</span><span class="topo-membrane">FGMVLAIGLLVNDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPMA</span><span class="topo-outside">FFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAYLFV</span><span class="topo-outside">RLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATFR</span><span class="topo-outside">GLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>27</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>339</td>
      <td>28</td>
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
      <td>365</td>
      <td>356</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>386</td>
      <td>366</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>395</td>
      <td>387</td>
      <td>395</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>411</td>
      <td>396</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>457</td>
      <td>442</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>470</td>
      <td>458</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>540</td>
      <td>535</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>557</td>
      <td>541</td>
      <td>557</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>558</td>
      <td>874</td>
      <td>558</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>895</td>
      <td>892</td>
      <td>895</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>896</td>
      <td>919</td>
      <td>896</td>
      <td>919</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>920</td>
      <td>927</td>
      <td>920</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>944</td>
      <td>928</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>975</td>
      <td>945</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8v">4U8V</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8v">4U8V</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-outside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8y">4U8Y</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMF</span><span class="topo-membrane">GMVLAIGLLVDNAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVPMA</span><span class="topo-outside">FFGGSTGAIYRQF</span><span class="topo-membrane">SITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYF</span><span class="topo-membrane">QVGLLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRPI</span><span class="topo-membrane">LMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEHSH</span><span class="topo-unknown">TVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
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
      <td>342</td>
      <td>26</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>384</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>411</td>
      <td>397</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>442</td>
      <td>412</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>457</td>
      <td>443</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>470</td>
      <td>458</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>537</td>
      <td>512</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>918</td>
      <td>899</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>927</td>
      <td>919</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>943</td>
      <td>928</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>991</td>
      <td>976</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1044</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8y">4U8Y</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRP</span><span class="topo-membrane">IFAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDNAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSIT</span><span class="topo-membrane">IVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAY</span><span class="topo-outside">LFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAILI</span><span class="topo-inside">VEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>412</td>
      <td>399</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>439</td>
      <td>413</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>473</td>
      <td>456</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>489</td>
      <td>474</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>534</td>
      <td>511</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>535</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>554</td>
      <td>540</td>
      <td>554</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>555</td>
      <td>877</td>
      <td>555</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>892</td>
      <td>878</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>945</td>
      <td>931</td>
      <td>945</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>946</td>
      <td>974</td>
      <td>946</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>988</td>
      <td>975</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8y">4U8Y</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u8y">4U8Y</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-outside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u95">4U95</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIV</span><span class="topo-inside">VVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGA</span><span class="topo-membrane">LVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKGF</span><span class="topo-unknown">FGWFNRMFEKSTHHYTDSVGGILRS</span><span class="topo-inside">TGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAP</span><span class="topo-membrane">SLYAISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLAA</span><span class="topo-outside">TFRGLTNDVYFQ</span><span class="topo-membrane">VGLLTTIGLSAANAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEHSH</span><span class="topo-unknown">TVDHHLEHHHHHH</span></span>
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
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>441</td>
      <td>412</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>456</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>512</td>
      <td>490</td>
      <td>512</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>537</td>
      <td>513</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>541</td>
      <td>538</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>874</td>
      <td>557</td>
      <td>874</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>875</td>
      <td>891</td>
      <td>875</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>916</td>
      <td>899</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>928</td>
      <td>917</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>943</td>
      <td>929</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>974</td>
      <td>944</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1019</td>
      <td>1004</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1044</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u95">4U95</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRP</span><span class="topo-membrane">IFAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRA</span><span class="topo-membrane">TLIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFGM</span><span class="topo-membrane">VLAIGLLVDDAIVVV</span><span class="topo-inside">ENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILTPAL</span><span class="topo-inside">CATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTG</span><span class="topo-membrane">R</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAY</span><span class="topo-outside">LFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAALYE</span><span class="topo-inside">S</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAANAILIV</span><span class="topo-inside">EFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMRLR</span><span class="topo-membrane">PILMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>24</td>
      <td>10</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>364</td>
      <td>358</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>382</td>
      <td>365</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>398</td>
      <td>383</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>413</td>
      <td>399</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>439</td>
      <td>414</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>440</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>474</td>
      <td>456</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>492</td>
      <td>475</td>
      <td>492</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>493</td>
      <td>510</td>
      <td>493</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>535</td>
      <td>511</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>539</td>
      <td>536</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>554</td>
      <td>540</td>
      <td>554</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>555</td>
      <td>877</td>
      <td>555</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>893</td>
      <td>878</td>
      <td>893</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>894</td>
      <td>894</td>
      <td>894</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>947</td>
      <td>973</td>
      <td>947</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>988</td>
      <td>974</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1022</td>
      <td>1005</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u95">4U95</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u95">4U95</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-outside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKTL</span><span class="topo-membrane">VEAIILVFLVMYLF</span><span class="topo-inside">LQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGG</span><span class="topo-inside">ILRSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMAY</span><span class="topo-outside">LFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">ALRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVGTG</span><span class="topo-membrane">VMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">FSRKNEDIEHSH</span><span class="topo-unknown">TVDHHLEHHHHHH</span></span>
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
      <td>344</td>
      <td>25</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>358</td>
      <td>345</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>533</td>
      <td>512</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>534</td>
      <td>540</td>
      <td>534</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>554</td>
      <td>541</td>
      <td>554</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>555</td>
      <td>877</td>
      <td>555</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>959</td>
      <td>944</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>975</td>
      <td>971</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1006</td>
      <td>989</td>
      <td>1006</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1007</td>
      <td>1022</td>
      <td>1007</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1044</td>
      <td>1033</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGG</span><span class="topo-outside">LAILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVK</span><span class="topo-membrane">TLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FAVLAAFGFSINTLTMFGMV</span><span class="topo-membrane">LAIGLLVDDAIVV</span><span class="topo-inside">VENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQ</span><span class="topo-membrane">GALVGIAMVLSAVFV</span><span class="topo-outside">PMAFFGGSTGAIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKK</span><span class="topo-unknown">GFFGWFNRMFEKSTHHYTDSVGGIL</span><span class="topo-inside">RSTGR</span></span>
<span class="topo-line"><span class="topo-membrane">YLVLYLIIVVGMA</span><span class="topo-outside">YLFVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLYA</span><span class="topo-membrane">ISLIVVFLCLAALY</span><span class="topo-inside">ES</span><span class="topo-membrane">WSIPFS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVGL</span><span class="topo-membrane">LTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMALRP</span><span class="topo-membrane">ILMTSLAFILGVM</span><span class="topo-outside">PLVISTGAGSGAQNAVGTG</span><span class="topo-membrane">VMGGMVTATVLAIF</span></span>
<span class="topo-line"><span class="topo-membrane">FV</span><span class="topo-unknown">PVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>342</td>
      <td>25</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>399</td>
      <td>380</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>412</td>
      <td>400</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>439</td>
      <td>413</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>440</td>
      <td>454</td>
      <td>440</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>535</td>
      <td>511</td>
      <td>535</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>540</td>
      <td>536</td>
      <td>540</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>553</td>
      <td>541</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>878</td>
      <td>554</td>
      <td>878</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>879</td>
      <td>892</td>
      <td>879</td>
      <td>892</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>893</td>
      <td>894</td>
      <td>893</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>915</td>
      <td>895</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>931</td>
      <td>916</td>
      <td>931</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>932</td>
      <td>944</td>
      <td>932</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>974</td>
      <td>945</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>987</td>
      <td>975</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>1006</td>
      <td>988</td>
      <td>1006</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1007</td>
      <td>1022</td>
      <td>1007</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1032</td>
      <td>1023</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">PNFFID</span><span class="topo-inside">RPI</span><span class="topo-membrane">FAWVIAIIIMLAGGL</span><span class="topo-outside">AILKLPVAQYPTIAPPAVTISASYPGADAKTVQDT</span></span>
<span class="topo-line"><span class="topo-outside">VTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGS</span></span>
<span class="topo-line"><span class="topo-outside">QYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLATGANAL</span></span>
<span class="topo-line"><span class="topo-outside">DTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEVVKTL</span><span class="topo-membrane">VEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAI</span><span class="topo-inside">VVVENVERVM</span></span>
<span class="topo-line"><span class="topo-inside">AEEGLPPKEATRKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFVP</span><span class="topo-outside">MAFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAKGDHGEGKKG</span><span class="topo-unknown">FFGWFNRMFEKSTHHYTDSVGGI</span><span class="topo-inside">LRSTGR</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-membrane">LVLYLIIVVGMAYL</span><span class="topo-outside">FVRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKD</span></span>
<span class="topo-line"><span class="topo-outside">AMVFAFNLPAIVELGTATGFDFELIDQAGLGHEKLTQARNQLLAEAAKHPDMLTSVRPNG</span></span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYR</span></span>
<span class="topo-line"><span class="topo-outside">MLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSLY</span><span class="topo-membrane">AISLIVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">VMLVVPLGVIGALLA</span><span class="topo-outside">ATFRGLTNDVYFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKDLMDKEGKGL</span></span>
<span class="topo-line"><span class="topo-inside">IEATLDAVRMALRPI</span><span class="topo-membrane">LMTSLAFILGVMP</span><span class="topo-outside">LVISTGAGSGAQNAVG</span><span class="topo-membrane">TGVMGGMVTATVLAI</span><span class="topo-unknown">F</span></span>
<span class="topo-line"><span class="topo-unknown">FVPVFFVVVRRR</span><span class="topo-inside">F</span><span class="topo-unknown">SRKNEDIEHSHTVDHHLEHHHHHH</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Inside</td>
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
      <td>344</td>
      <td>26</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>442</td>
      <td>411</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>511</td>
      <td>490</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>512</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>535</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>877</td>
      <td>556</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>891</td>
      <td>878</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>898</td>
      <td>892</td>
      <td>898</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>899</td>
      <td>915</td>
      <td>899</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>930</td>
      <td>916</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>975</td>
      <td>944</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>976</td>
      <td>988</td>
      <td>976</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1004</td>
      <td>989</td>
      <td>1004</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1005</td>
      <td>1019</td>
      <td>1005</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1032</td>
      <td>1020</td>
      <td>1032</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHH</span><span class="topo-outside">GSDLGKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>11</td>
      <td>166</td>
      <td>11</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u96">4U96</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGSDL</span><span class="topo-outside">GKKLLEAARAGRDDEVRILMANGADVNAADVVGWTPLHLAAYWGHL</span></span>
<span class="topo-line"><span class="topo-outside">EIVEVLLKNGADVNAYDTLGSTPLHLAAHFGHLEIVEVLLKNGADVNAKDDNGITPLHLA</span></span>
<span class="topo-line"><span class="topo-outside">ANRGHLEIVEVLLKYGADVNAQDKFGKTAFDISINNGNEDLAEILQ</span><span class="topo-unknown">KLN</span></span>
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
      <td>15</td>
      <td>166</td>
      <td>15</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
</details>


## Biological / Functional Insights

### Three protomer conformations establish a functionally rotating mechanism

The 2.8 A C2 crystal structure revealed three distinct protomer conformations in the asymmetric unit: access (green), binding (blue), and extrusion (red). Each represents a different functional state of the transport cycle.

### Multi-site drug binding in a voluminous aromatic pocket

The substrate binding pocket is rich in aromatic residues. Different sets of residues are used for different substrates (minocycline vs doxorubicin).

### Asymmetric trimer with L/T/O conformations

The AcrB trimer exhibits three distinct monomer conformations: loose (L), tight (T), and open (O), representing consecutive states of the transport cycle.

### DARPin selection and inhibition of AcrB

DARPin 1108_19 (KD=28 nM) was co-crystallized with AcrB. The structure revealed that only two of three AcrB subunits bind DARPins, confirming asymmetric conformation.

### Pseudo-atomic model of AcrAB-TolC assembly

The cryo-EM model of the complete pump reveals that TolC does not directly interact with AcrB in the assembly. Instead, the two proteins are bridged entirely through AcrA. Stoichiometry: AcrB trimer, AcrA hexamer, TolC trimer.

### AcrZ binding and allosteric modulation

AcrZ is a 49-residue, predominantly hydrophobic alpha-helix that fits into a wide groove in the transmembrane domain of AcrB. Its helical axis is inclined at nearly 45 degrees relative to the membrane normal. The N-terminus is in the periplasm and the C-terminus in the cytoplasm.

### Dedicated drug transport channels CH1-CH4 with substrate specificity

13 X-ray structures of AcrB in intermediate transport states revealed four entry channels (CH1-CH4) with distinct substrate specificities. CH1 via TM7/TM8 groove is the main pathway for low molecular weight (LMW) drugs, DDM, and fusidic acid. CH2 prefers high molecular weight (HMW) drugs like macrolides and ansamycins. CH3 transports planar aromatic cations. CH4 transports carboxylated drugs. Transport occurs through a peristaltic pump mechanism rather than passive diffusion.

### Transmembrane domain allosteric binding pocket (TMD-BP)

Co-crystallization of AcrB with an antibiotic cocktail (erythromycin, linezolid, oxacillin, fusidic acid) revealed fusidic acid bound to a deep ~1700 A^3 cavity in the T protomer transmembrane domain, surrounded by TM2, TM4, TM10-12 and near the Asp407/Asp408/Lys940 proton relay residues. TM11 and TM12 undergo substantial displacement (13.6 degrees and 36.7 degrees tilting). Thiol cross-link protection assays showed the TMD-BP can accommodate oxacillin and novobiocin but not erythromycin or linezolid. This allosteric site may cause hyperactivation of the pump in the presence of multiple drugs.

### Peristaltic drug movement through CH1 captured in intermediate states

A DDM molecule trapped in a transient L-to-T state of the CH1 tunnel (TM8/PC2 tunnel) shows the peristaltic movement of substrates toward the deep binding pocket. The c-loop undergoes large conformational changes from TM8-proximal to TM8-distal orientation. Comparison with earlier snapshots reveals stepwise peristaltic transport of DDM.

### Switch-loop rigidification reveals HMW drug binding in T protomer

Gly619Pro and Gly621Pro switch-loop variants allow binding of ansamycin drugs (3-formylrifamycin SV, rifabutin) to the access pocket of the T protomer in addition to the L protomer, demonstrating that HMW drugs can bypass the deep binding pocket during transport.

### TolC opening mechanism

In isolation, TolC assumes a closed resting state. In the assembled pump, interactions with the alpha-helical hairpins of AcrA switch TolC to an open state. The dilation from closed to open is driven by chelate cooperativity from hexameric AcrA and allosteric cooperativity breaking interprotomer interactions.


## Cross-References

- <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">Designed Ankyrin Repeat Protein (DARPin)</a> — DARPin 1108_19 used as crystallization chaperone and inhibitor
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-beta-D-maltoside)</a> — Primary detergent for AcrB solubilization and purification
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/reagents/ligands/minocycline/">Minocycline</a> — Substrate used in drug complex structure determination
- <a href="/xray-mp-wiki/reagents/ligands/doxorubicin/">Doxorubicin</a> — Substrate used in drug complex structure determination
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/">RND Efflux Pumps</a> — AcrB is the prototypical RND transporter
- <a href="/xray-mp-wiki/proteins/abc-transporters/acra/">AcrA multidrug efflux pump periplasmic protein</a> — AcrA is the periplasmic adaptor in the AcrAB-TolC complex
- <a href="/xray-mp-wiki/proteins/abc-transporters/emre/">EmrE (E. coli Small Multidrug Resistance Transporter)</a> — Related membrane protein for comparison
- <a href="/xray-mp-wiki/proteins/abc-transporters/yajc/">E. coli YajC Transmembrane Protein</a> — Forms a stable complex with AcrB; crystal structure determined together (PDB 2RDD)
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexB/">MexB Efflux Pump</a> — Close homologue (RND family efflux pump); similar multidrug-binding cavity mechanism
- <a href="/xray-mp-wiki/concepts/multidrug-resistance/">Multidrug Resistance</a> — AcrB is a major contributor to multidrug resistance in Gram-negative bacteria
- <a href="/xray-mp-wiki/reagents/ligands/abi-pp/">ABI-PP</a> — First inhibitor-bound structure of AcrB solved; ABI-PP binds to hydrophobic trap in distal pocket
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/helix-shift-mechanism/">Helix Shift Mechanism for Carboxylate Drug Transport</a> — Mechanism proposed for active transport of carboxylate drugs from the membrane via TM2 helix upward shift
- <a href="/xray-mp-wiki/proteins/abc-transporters/tolc/">TolC Outer Membrane Channel</a> — Outer membrane partner in the AcrAB-TolC tripartite efflux system
