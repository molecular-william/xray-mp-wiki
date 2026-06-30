---
title: "Human ABCG5/ABCG8 Sterol Transporter Heterodimer"
created: 2026-06-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, abc-transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17666, doi/10.1016##j.jmb.2022.167795]
verified: false
---

# Human ABCG5/ABCG8 Sterol Transporter Heterodimer

## Overview

ABCG5 and ABCG8 form an obligate heterodimer that functions as a sterol efflux transporter in the liver and intestines. The complex exports dietary sterols including plant sterols and [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) into bile, preventing toxic accumulation of sterols in the body. Mutations in either subunit cause sitosterolemia, a rare genetic disorder characterized by elevated plant sterol levels. The first X-ray crystal structure of the human ABCG5/G8 heterodimer was determined at 3.9 Angstrom resolution using [bicelle crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/).

## Publications

### doi/10.1038##nature17666

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5do7">5DO7</a></td>
      <td>3.9 A</td>
      <td>I 2 2 2</td>
      <td>Human ABCG5/G8 heterodimer, nucleotide-free inward-facing state</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> (in sterol vestibules)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG5 (UniProt P45844) with C-terminal His12 tag; human ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag. CBP tag and N-linked glycans cleaved by Endo H and [HRV-3C protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/). Protein treated by reductive methylation and cysteine alkylation before crystallization.

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
      <td>Cell lysis</td>
      <td>Membrane preparation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, protease inhibitors (<a href="/xray-mp-wiki/reagents/additives/leupeptin">Leupeptin</a>, pepstatin A, <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>) + --</td>
      <td>Insoluble membranes removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + Not specified</td>
      <td>Solubilized supernatant treated with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
      <td>20-mL <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> column</td>
      <td>Not specified + Not specified</td>
      <td>Peak fractions from <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> elua<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> collected</td>
    </tr>
    <tr>
      <td>Calmodulin-binding peptide (CBP) chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a> (CBP)</td>
      <td>5-mL CBP column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholate/">Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 1 mM CaCl2, 1 mM MgCl2</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> elua<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> mixed with CBP wash buffer and loaded onto CBP column</td>
    </tr>
    <tr>
      <td>Detergent exchange and concentration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.0005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
      <td>Exchanged to <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a> for final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ABCG5/G8 heterodimer reconstituted into <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s (10% <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> stock, lipids containing 5 mol% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> and 95 mol% DMPC), <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> added at 10 mM, final protein concentration 5-10 mg/mL, protein/<a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> mixed 1:4 (v/v)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.7-2.0 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 2-5% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20-22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days to 2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 2 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 2-4% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals only diffracted to 3.9 Angstrom when <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> was present in bicelles. Two heterodimers in asymmetric unit. Tungsten <a href="/xray-mp-wiki/methods/phasing/single-wavelength-anomalous-diffraction/">SAD</a> phasing using sodium phosphotungstate derivative. Native data merged from 19 crystals. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using cryo-EM model PDB 7JR7.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5do7">5DO7</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLSSLTPGGSMGLQVNRGSQSSLEGAPATAP</span><span class="topo-inside">EPHSLGILHASYS</span><span class="topo-unknown">VSHRVRPWWDITSCRQQWT</span><span class="topo-inside">RQILKDVSLYVESGQIMCILGSSGSGKTTLLDAMSGRLGRAGTFLGEVYVNGRAL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RREQFQDCFSYVLQSDTLLSSLTVRETLHYTALLAIRRGNPGSFQKKVEAVMAELSLSHVADRLIGNYSLGGISTGERRRVSIAAQLLQDPKVMLFDEPTTGLDCMTANQIVVLLVELAR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RNRIVVLTIHQPRSELFQLFDKIAILSFGELIFCGTPAEMLDFFNDCGYPCPEHSNPFDFYMDLTSVDTQSKEREIETSKRVQMIESAYKKSAICHKTLKNIERMKHLKTLPMVPFKTKD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SPGVFSKLGVLLRRVTRNLVRNKLAVIT</span><span class="topo-membrane">RLLQNLIMGLFLLFFVLR</span><span class="topo-outside">VRSNVLKGAIQDRVG</span><span class="topo-membrane">LLYQFVGATPYTGMLN</span><span class="topo-inside">AVNLFPVLRAVSDQESQDGLYQKWQMMLAYALHV</span><span class="topo-membrane">LPFSVVATM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">IFSSVCYWTLG</span><span class="topo-outside">LHPEV</span><span class="topo-membrane">ARFGYFSAALLAPHLIGEFLTLVL</span><span class="topo-inside">LGIVQNPNIV</span><span class="topo-membrane">NSVVALLSIAGVLVGS</span><span class="topo-outside">GFLRNIQEMPIPFKI</span><span class="topo-unknown">ISYFTFQKYCS</span><span class="topo-outside">EILVVNEFYGLNFTC</span><span class="topo-unknown">GSSNVSVTTNPMC</span></span>
<span class="topo-ruler">       610       620       630       640       650       660      </span>
<span class="topo-line"><span class="topo-outside">AFTQGIQFIEKTCPGATSRFTMN</span><span class="topo-membrane">FLILYSFIPALVILGIVV</span><span class="topo-inside">FKIRDHLIS</span><span class="topo-unknown">RGSHHHHHHGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>33</td>
      <td>1</td>
      <td>33</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>46</td>
      <td>34</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>65</td>
      <td>47</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>388</td>
      <td>66</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>406</td>
      <td>389</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>421</td>
      <td>407</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>437</td>
      <td>422</td>
      <td>437</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>438</td>
      <td>471</td>
      <td>438</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>491</td>
      <td>472</td>
      <td>491</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>492</td>
      <td>496</td>
      <td>492</td>
      <td>496</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>520</td>
      <td>497</td>
      <td>520</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>521</td>
      <td>530</td>
      <td>521</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>531</td>
      <td>546</td>
      <td>531</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>547</td>
      <td>561</td>
      <td>547</td>
      <td>561</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>572</td>
      <td>562</td>
      <td>572</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>573</td>
      <td>587</td>
      <td>573</td>
      <td>587</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>600</td>
      <td>588</td>
      <td>600</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>601</td>
      <td>623</td>
      <td>601</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>624</td>
      <td>641</td>
      <td>624</td>
      <td>641</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>642</td>
      <td>650</td>
      <td>642</td>
      <td>650</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>651</td>
      <td>666</td>
      <td>651</td>
      <td>666</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5do7">5DO7</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSAGKAAEERGLPKGATPQDTSG</span><span class="topo-inside">LQDRLFSSESDNSLYFTYSGQP</span><span class="topo-unknown">NTLEVRDLNYQVDLASQVPWFEQLAQFKMPWTSPSCQNSCEL</span><span class="topo-inside">GIQNLSFKVRSGQMLAIIGSSGCGRASLLDVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGRGHGGKIKSGQIWINGQPSSPQLVRKCVAHVRQHNQLLPNLTVRETLAFIAQMRLPRTFSQAQRDKRVEDVIAELRLRQCADTRVGNMYVRGLSGGERRRVSIGVQLLWNPGILILDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PTSGLDSFTAHNLVKTLSRLAKGNRLVLISLHQPRSDIFRLFDLVLLMTSGTPIYLGAAQHMVQYFTAIGYPCPRYSNPADFY</span><span class="topo-unknown">VDLTSIDRRSREQELATREK</span><span class="topo-inside">AQSLAALFLEKVRDLDD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">FLWKAETK</span><span class="topo-unknown">DLDEDTCVESSVTPLDTNCLPSPTKMP</span><span class="topo-inside">GAVQQFTTLIRRQISNDFRDLPTL</span><span class="topo-membrane">LIHGAEACLMSMTIGFL</span><span class="topo-outside">YFGHGSIQLSFMDTAAL</span><span class="topo-membrane">LFMIGALIPFNVILDV</span><span class="topo-inside">ISKCYSERAML</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YYELEDGLYTTGPYFFAKILGE</span><span class="topo-membrane">LPEHCAYIIIYGMPTY</span><span class="topo-outside">WLANLRPGLQPFL</span><span class="topo-membrane">LHFLLVWLVVFCCRIMA</span><span class="topo-inside">LAAAALLPTFHMASF</span><span class="topo-membrane">FSNALYNSFYLAGGFMI</span><span class="topo-outside">NLSSL</span><span class="topo-unknown">WTVPAWISKVSFLRW</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680     </span>
<span class="topo-line"><span class="topo-unknown">CFEGL</span><span class="topo-outside">MKIQFSRRTYKMPLGNLTIAVSGDKILSVMELDSYPLY</span><span class="topo-membrane">AIYLIVIGLSGGFMV</span><span class="topo-inside">LYYVSLRFIKQKPSQDW</span><span class="topo-unknown">ASNSLEVLFQ</span></span>
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
      <td>24</td>
      <td>-1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>46</td>
      <td>23</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>88</td>
      <td>45</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>323</td>
      <td>87</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>343</td>
      <td>322</td>
      <td>341</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>344</td>
      <td>368</td>
      <td>342</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>395</td>
      <td>367</td>
      <td>393</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>396</td>
      <td>419</td>
      <td>394</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>436</td>
      <td>418</td>
      <td>434</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>453</td>
      <td>435</td>
      <td>451</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>469</td>
      <td>452</td>
      <td>467</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>502</td>
      <td>468</td>
      <td>500</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>518</td>
      <td>501</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>531</td>
      <td>517</td>
      <td>529</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>532</td>
      <td>548</td>
      <td>530</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>549</td>
      <td>563</td>
      <td>547</td>
      <td>561</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>580</td>
      <td>562</td>
      <td>578</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>581</td>
      <td>585</td>
      <td>579</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>605</td>
      <td>584</td>
      <td>603</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>643</td>
      <td>604</td>
      <td>641</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>644</td>
      <td>658</td>
      <td>642</td>
      <td>656</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>659</td>
      <td>675</td>
      <td>657</td>
      <td>673</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>676</td>
      <td>685</td>
      <td>674</td>
      <td>683</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.jmb.2022.167795

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8cub">8CUB</a></td>
      <td>4.05 A</td>
      <td>I 2 2 2</td>
      <td>Human ABCG5/G8 heterodimer in complex with cholesterol</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG5 (UniProt P45844) with C-terminal His12 tag; human ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag. CBP tag and N-linked glycans cleaved by Endo H and [HRV-3C protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/). Protein treated by reductive methylation and cysteine alkylation before crystallization.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> with <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a>-treated ABCG5/G8 reconstituted into 10% DMPC/CHAPSO <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s (lipids:detergents 3:1 w/w, lipids containing 5 mol% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a>), mixed 1:4 (v/v) with protein/<a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> stock, final protein concentration ~10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.8-2.0 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 2-5% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">sodium malonate</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group I 2 2 2. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using PDB 7JR7.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cub">8CUB</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DLSSLTPGGSMGLQVNRGSQSSLEGAPATAP</span><span class="topo-outside">EPHSLGILHASYSVS</span><span class="topo-unknown">HRVRPWWDITSCRQQW</span><span class="topo-outside">TRQILKDVSLYVESGQIMCILGSSGSGKTTLLDAMSGRLGRAGTFLGEVYVNGRALRR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EQFQDCFSYVLQSDTLLSSLTVRETLHYTALLAIRRGNPGSFQKKVEAVMAELSLSHVADRLIGNYSLGGISTGERRRVSIAAQLLQDPKVMLFDEPTTGLDCMTANQIVVLLVELARRN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RIVVLTIHQPRSELFQLFDKIAILSFGELIFCGTPAEMLDFFNDCGYPCPEHSNPFDFYMDLTSVDTQSKEREIETSKRVQMIESAYKKSAICHKTLKNIERMKHLKTLPMVPFKTKDSP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GVFSKLGVLLRRVTRNLVRNKLAV</span><span class="topo-membrane">ITRLLQNLIMGLFLLFFVLR</span><span class="topo-inside">VRSNVLKGAIQDRVG</span><span class="topo-membrane">LLYQFVGATPYTGMLNAVN</span><span class="topo-outside">LFPVLRAVSDQESQDGLYQKWQMMLAY</span><span class="topo-membrane">ALHVLPFSVVATMIF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SSVCYWTLG</span><span class="topo-inside">LHPEV</span><span class="topo-membrane">ARFGYFSAALLAPHLIGEFLTLVLLGIV</span><span class="topo-outside">QNP</span><span class="topo-membrane">NIVNSVVALLSIAGVLVGS</span><span class="topo-inside">GFLRNIQEMPIP</span><span class="topo-unknown">FKIISYFTFQKYCSEIL</span><span class="topo-inside">VVNEFYGLNFTC</span><span class="topo-unknown">GSSNVSVTTNP</span><span class="topo-inside">MCAF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660    </span>
<span class="topo-line"><span class="topo-inside">TQGIQFIEKTCPGATSRFT</span><span class="topo-membrane">MNFLILYSFIPALVILGIVV</span><span class="topo-outside">FKIRDHL</span><span class="topo-unknown">ISRGSHHHHHHGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>31</td>
      <td>3</td>
      <td>33</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>46</td>
      <td>34</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>62</td>
      <td>49</td>
      <td>64</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>384</td>
      <td>65</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>404</td>
      <td>387</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>419</td>
      <td>407</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>438</td>
      <td>422</td>
      <td>440</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>465</td>
      <td>441</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>489</td>
      <td>468</td>
      <td>491</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>494</td>
      <td>492</td>
      <td>496</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>495</td>
      <td>522</td>
      <td>497</td>
      <td>524</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>523</td>
      <td>525</td>
      <td>525</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>544</td>
      <td>528</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>545</td>
      <td>556</td>
      <td>547</td>
      <td>558</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>557</td>
      <td>573</td>
      <td>559</td>
      <td>575</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>574</td>
      <td>585</td>
      <td>576</td>
      <td>587</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>596</td>
      <td>588</td>
      <td>598</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>597</td>
      <td>619</td>
      <td>599</td>
      <td>621</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>620</td>
      <td>639</td>
      <td>622</td>
      <td>641</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>640</td>
      <td>646</td>
      <td>642</td>
      <td>648</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>647</td>
      <td>664</td>
      <td>649</td>
      <td>666</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8cub">8CUB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSAGKAAEERGLPKGATPQDTSGLQDRL</span><span class="topo-outside">FSSESDNSLYFTYSGQPNTLEVRDLNYQV</span><span class="topo-unknown">DLASQVPWFEQLAQFKMPWTSPSCQNSCEL</span><span class="topo-outside">GIQNLSFKVRSGQMLAIIGSSGCGRASLLDVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TGRGHGGKIKSGQIWINGQPSSPQLVRKCVAHVRQHNQLLPNLTVRETLAFIAQMRLPRTFSQAQRDKRVEDVIAELRLRQCADTRVGNMYVRGLSGGERRRVSIGVQLLWNPGILILDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">PTSGLDSFTAHNLVKTLSRLAKGNRLVLISLHQPRSDIFRLFDLVLLMTSGTPIYLGAAQHMVQYFTAIGYPCPRYSNPADFYVDLTSIDRRSREQELATREKAQSLAALFLEKVRDLDD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">FLWK</span><span class="topo-unknown">AETKDLDEDTCVESSVTPLDTNCLPSP</span><span class="topo-outside">TKMPGAVQQFTTLIRRQISNDFRD</span><span class="topo-membrane">LPTLLIHGAEACLMSMTIGFL</span><span class="topo-inside">YFGHGSIQLSFMDTAAL</span><span class="topo-membrane">LFMIGALIPFNVILDVISK</span><span class="topo-outside">CYSERAML</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YYELEDGLYTTGPYF</span><span class="topo-membrane">FAKILGELPEHCAYIIIYGMPTY</span><span class="topo-inside">WLANLRPGLQPFL</span><span class="topo-membrane">LHFLLVWLVVFCCRIMALAAAALL</span><span class="topo-outside">PTFH</span><span class="topo-membrane">MASFFSNALYNSFYLAGGFMI</span><span class="topo-inside">NLSSL</span><span class="topo-unknown">WTVPAWISKVSFLRW</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       </span>
<span class="topo-line"><span class="topo-unknown">CF</span><span class="topo-inside">EGLMKIQFSRRTYKM</span><span class="topo-unknown">PLGNLTI</span><span class="topo-inside">AVSGDKILSVMELDSYPLYA</span><span class="topo-membrane">IYLIVIGLSGGFMVLYYVS</span><span class="topo-outside">LRFIKQKPS</span><span class="topo-unknown">QDWASNSLEVLFQME</span></span>
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
      <td>29</td>
      <td>-1</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>58</td>
      <td>28</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>88</td>
      <td>57</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>364</td>
      <td>87</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>391</td>
      <td>363</td>
      <td>389</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>392</td>
      <td>415</td>
      <td>390</td>
      <td>413</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>436</td>
      <td>414</td>
      <td>434</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>453</td>
      <td>435</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>454</td>
      <td>472</td>
      <td>452</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>495</td>
      <td>471</td>
      <td>493</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>496</td>
      <td>518</td>
      <td>494</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>531</td>
      <td>517</td>
      <td>529</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>532</td>
      <td>555</td>
      <td>530</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>559</td>
      <td>554</td>
      <td>557</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>560</td>
      <td>580</td>
      <td>558</td>
      <td>578</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>581</td>
      <td>585</td>
      <td>579</td>
      <td>583</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>602</td>
      <td>584</td>
      <td>600</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>603</td>
      <td>617</td>
      <td>601</td>
      <td>615</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>624</td>
      <td>616</td>
      <td>622</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>625</td>
      <td>644</td>
      <td>623</td>
      <td>642</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>645</td>
      <td>663</td>
      <td>643</td>
      <td>661</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>664</td>
      <td>672</td>
      <td>662</td>
      <td>670</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>673</td>
      <td>687</td>
      <td>671</td>
      <td>685</td>
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

### Sterol transport by ABCG5/G8 heterodimer

The ABCG5/G8 heterodimer uses a conserved phenylalanine highway on transmembrane helix 2 for sterol transport. The complex exhibits asymmetric sterol binding at the transporter-membrane interface.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Method used for structure determination
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg5/">ABCG5</a> — ABCG5 subunit of the heterodimer
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg8/">ABCG8</a> — ABCG8 subunit of the heterodimer
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Crystallization precipitant
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a> — Detergent used in final purification buffer
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Central ligand; used in crystallization and incubation
