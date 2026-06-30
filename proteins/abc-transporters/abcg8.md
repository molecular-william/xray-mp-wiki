---
title: "ABCG8"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17666, doi/10.1016##j.jmb.2022.167795]
verified: false
---

# ABCG8

## Overview

ABCG8 is a member of the ATP-binding cassette (ABC) G subfamily of transporter proteins. It functions as an obligate heterodimer with ABCG5 to form the ABCG5/G8 complex, which mediates selective sterol excretion by preferentially effluxing dietary plant sterols over [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol). The ABCG5/G8 heterodimer is localized on canalicular membranes of the bile ducts in the liver and the brush border of enterocytes in the small intestines, where it plays a critical role in reverse cholesterol transport and prevents abnormal accumulation of plant sterols (sitosterolemia) in the human body.
The first X-ray crystal structure of human ABCG5/G8 was determined at 3.9 Å resolution (PDB 5DO7) using bicelle crystallization. In the ABCG5/G8 heterodimer, ABCG8 contributes key residues including T430 (which forms a hydrogen bond with cholesterol hydroxyl) and P415 (a landmark position at the end of the connecting helix). A conserved phenylalanine (F453) on transmembrane helix 2 is part of the phenylalanine highway motif. ABCG8 contains the catalytically active ATPase site (NBS2), with G8 Signature motif contributing to nucleotide binding and hydrolysis. 

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
      <td>3.9</td>
      <td>I 2 2 2</td>
      <td>Human ABCG5/G8 heterodimer, nucleotide-free inward-facing state (bicelle crystallization)</td>
      <td>Cholesterol (putative, in sterol vestibules)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag; coexpressed with ABCG5 (C-terminal His₁₂ tag). CBP tag and N-linked glycans cleaved by Endo H and HRV-3C protease. Protein treated by reductive methylation and cysteine alkylation before crystallization.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization">Bicelle crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">hanging drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>G5G8 heterodimers coexpressed in P. pastoris, purified by tandem <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> + CBP), treated by reductive methylation and cysteine alkylation, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a> <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s (10% <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> stock, lipids containing 5 mol% <a href="/xray-mp-wiki/reagents/lipids/cholesterol">cholesterol</a> and 95 mol% DMPC), <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> added at 10 mM before mixing, final protein concentration 5-10 mg ml⁻¹, protein/<a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> mixed 1:4 (v/v)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.7-2.0 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">ammonium sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5 (or <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0), 2-5% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a> (or <a href="/xray-mp-wiki/reagents/additives/peg-350-mme/">PEG 350 MME</a>), 1 mM TCEP</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20-22 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days to 2 weeks; maximum size 75-150 × 40-60 × 10-20 μm in 1-2 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/glycerol">glycerol</a>, 2 M (NH₄)₂SO₄, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 2-4% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals only diffracted to 3.9 Å when <a href="/xray-mp-wiki/reagents/lipids/cholesterol">cholesterol</a> was present in <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s. Two heterodimers in asymmetric unit. Tungsten <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD phasing</a> using sodium phosphotungstate derivative. Native data merged from 19 crystals to 3.9 Å resolution. Space group I 2 2 2. Structure refined to R/Rfree = 0.242/0.328.</td>
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
      <td>4.051</td>
      <td>I 2 2 2</td>
      <td>Human ABCG5/G8 heterodimer in complex with <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a></td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7jr7">7JR7</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>Human ABCG5/G8 heterodimer (cryo-EM structure used as <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> model)</td>
      <td>not specified</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: Human ABCG8 (UniProt Q9UNQ0) with C-terminal calmodulin-binding peptide (CBP) tag; coexpressed with ABCG5 (C-terminal His₁₂ tag). CBP tag and N-linked glycans cleaved by Endo H and HRV-3C protease. Protein treated by reductive methylation and cysteine alkylation before crystallization.

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
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM NaCl, protease inhibitors (<a href="/xray-mp-wiki/reagents/additives/leupeptin">Leupeptin</a>, pepstatin A, <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>) + --</td>
      <td>Insoluble membranes removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation">ultracentrifugation</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl, 0.1 mM TCEP + Not specified</td>
      <td>Solubilized supernatant treated with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
      <td>20-mL <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> column</td>
      <td>Not specified + Not specified</td>
      <td>Peak fractions from <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> elua<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> collected</td>
    </tr>
    <tr>
      <td>Calmodulin-binding peptide (CBP) chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> (CBP)</td>
      <td>5-mL CBP column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM NaCl, 0.1% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.1 mM TCEP, 1 mM CaCl2, 1 mM MgCl2 + beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> elua<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> mixed with CBP wash buffer and loaded onto CBP column</td>
    </tr>
    <tr>
      <td>Detergent exchange</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>CBP column</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/dmng">DMNG</a>-containing buffer + <a href="/xray-mp-wiki/reagents/detergents/dmng">DMNG</a></td>
      <td>CBP column washed sequentially to exchange detergents to decyl <a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>)</td>
    </tr>
    <tr>
      <td>Elution from CBP column</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>CBP column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM NaCl, 2 mM EGTA, 0.1% <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 mM TCEP + <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/proteins/abcg5">ABCG5/G8</a> proteins eluted from CBP column</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease digestion (<a href="/xray-mp-wiki/reagents/additives/endoh/">Endo H</a> and <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV-3C protease</a>)</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>N-linked glycans and CBP tag cleaved overnight at 4 C; <a href="/xray-mp-wiki/reagents/additives/endoh/">Endo H</a> (~0.2 mg per 10-15 mg protein) and <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV-3C protease</a> (~2 mg per 10-15 mg protein)</td>
    </tr>
    <tr>
      <td>Gel filtration chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> 30/100 GL column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, <a href="/xray-mp-wiki/reagents/detergents/cholate">Cholate</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>CBP tag-free proteins purified by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a>; peak fractions pooled</td>
    </tr>
    <tr>
      <td>Reductive methylation and cysteine alkylation</td>
      <td>Chemical modification</td>
      <td>2-mL <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> column</td>
      <td>Not specified + Not specified</td>
      <td>Methylated proteins relipidated with <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a>:<a href="/xray-mp-wiki/reagents/lipids/dope/">DOPE</a> (3:1, w/w), purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>, treated with <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">Iodoacetamide</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> incubation</td>
      <td>Ligand incubation</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>Proteins incubated with <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> (prepared in isopropanol) overnight at 4 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> with <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a>-treated ABCG5/G8 reconstituted into 10% DMPC/CHAPSO <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s (lipids:detergents 3:1 w/w, lipids containing 5 mol% cholesterol and 95 mol% DMPC), mixed 1:4 (v/v) with protein/<a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> stock, final protein concentration ~10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.8-2.0 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">Ammonium Sulfate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 2-5% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, 1 mM TCEP</td>
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
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">[sodium malonate</a>](/xray-mp-wiki/reagents/additives/sodium-malonate)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested by submersion in 0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-malonate">sodium malonate</a>. Space group I 2 2 2. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using PDB 7JR7.</td>
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

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7jr7">7JR7</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGDLSSLTPGGSMGLQVNRGSQSSLEGAPATAP</span><span class="topo-inside">EPHSLGILHASYSVS</span><span class="topo-unknown">HRVRPWWDITSCRQQW</span><span class="topo-inside">TRQILKDVSLYVESGQIMCILGSSGSGKTTLLDAMSGRLGRAGTFLGEVYVNGRAL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RREQFQDCFSYVLQSDTLLSSLTVRETLHYTALLAIRRGNPGSFQKKVEAVMAELSLSHVADRLIGNYSLGGISTGERRRVSIAAQLLQDPKVMLFDEPTTGLDCMTANQIVVLLVELAR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RNRIVVLTIHQPRSELFQLFDKIAILSFGELIFCGTPAEMLDFFNDCGYPCPEHSNPFDFYMDLTSVDTQSKEREIETSKRVQMIESAYKKSAICHKTLKNIERMKHLKTLPMVPFKTKD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SPG</span><span class="topo-unknown">VFSKLGVLLRRVTRNL</span><span class="topo-membrane">VRNKLAVITRLLQNLIMGLFLLFF</span><span class="topo-outside">VLRVRSNVLKGAIQDRVGLLY</span><span class="topo-membrane">QFVGATPYTGMLNAVNLF</span><span class="topo-inside">PVLRAVSDQESQDGLYQKWQMM</span><span class="topo-membrane">LAYALHVLPFSVVATM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">IFSSVC</span><span class="topo-outside">YWTLGLHPEVARFGYFS</span><span class="topo-membrane">AALLAPHLIGEFLTLVLL</span><span class="topo-inside">GIVQNPN</span><span class="topo-membrane">IVNSVVALLSIAGVLVGS</span><span class="topo-outside">GFLRNIQEMP</span><span class="topo-unknown">IPFKIISYFTFQKYC</span><span class="topo-outside">SEILVVNEFYGLNFTC</span><span class="topo-unknown">GSSNVSVTTNP</span><span class="topo-outside">MC</span></span>
<span class="topo-ruler">       610       620       630       640       650 </span>
<span class="topo-line"><span class="topo-outside">AFTQGIQFIEKTCPGATSRFTMNF</span><span class="topo-membrane">LILYSFIPALVILGIVV</span><span class="topo-inside">FKIRDHL</span><span class="topo-unknown">ISR</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>34</td>
      <td>48</td>
      <td>34</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>363</td>
      <td>65</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>379</td>
      <td>364</td>
      <td>379</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>380</td>
      <td>403</td>
      <td>380</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>424</td>
      <td>404</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>442</td>
      <td>425</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>464</td>
      <td>443</td>
      <td>464</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>465</td>
      <td>486</td>
      <td>465</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>503</td>
      <td>487</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>504</td>
      <td>521</td>
      <td>504</td>
      <td>521</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>522</td>
      <td>528</td>
      <td>522</td>
      <td>528</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>546</td>
      <td>529</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>547</td>
      <td>556</td>
      <td>547</td>
      <td>556</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>557</td>
      <td>571</td>
      <td>557</td>
      <td>571</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>572</td>
      <td>587</td>
      <td>572</td>
      <td>587</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>599</td>
      <td>624</td>
      <td>599</td>
      <td>624</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>625</td>
      <td>641</td>
      <td>625</td>
      <td>641</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>642</td>
      <td>648</td>
      <td>642</td>
      <td>648</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7jr7">7JR7</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAGKAAEERGLPKGATPQDTSGLQDRL</span><span class="topo-inside">FSSESDNSLYFTYSGQPNTLEVRDLNYQV</span><span class="topo-unknown">DLASQVPWFEQLAQFKMPWTSPSCQNSCEL</span><span class="topo-inside">GIQNLSFKVRSGQMLAIIGSSGCGRASLLDVITG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RGHGGKIKSGQIWINGQPSSPQLVRKCVAHVRQHNQLLPNLTVRETLAFIAQMRLPRTFSQAQRDKRVEDVIAELRLRQCADTRVGNMYVRGLSGGERRRVSIGVQLLWNPGILILDEPT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGLDSFTAHNLVKTLSRLAKGNRLVLISLHQPRSDIFRLFDLVLLMTSGTPIYLGAAQHMVQYFTAIGYPCPRYSNPADFYVDLTSIDRRSREQELATREKAQSLAALFLEKVRDLDDFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WK</span><span class="topo-unknown">AETKDLDEDTCVESSVTPLDTNCLPSP</span><span class="topo-inside">TKMPG</span><span class="topo-unknown">AVQQFTTLIRRQISND</span><span class="topo-inside">FRDLPTLL</span><span class="topo-membrane">IHGAEACLMSMTIGFLYF</span><span class="topo-outside">GHGSIQLSFMDTAAL</span><span class="topo-membrane">LFMIGALIPFNVILDVI</span><span class="topo-inside">SKCYSERAMLYY</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">ELEDGLYTTGPYFFAKILGE</span><span class="topo-membrane">LPEHCAYIIIYGMPTYWLA</span><span class="topo-outside">NLRPG</span><span class="topo-membrane">LQPFLLHFLLVWLVVFCCRIMALAAA</span><span class="topo-inside">ALLPTFH</span><span class="topo-membrane">MASFFSNALYNSFYLAG</span><span class="topo-outside">GFMINLSSLWTV</span><span class="topo-unknown">PAWISKVSFLRWCF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670   </span>
<span class="topo-line"><span class="topo-outside">EGLMKIQFSRRTYKM</span><span class="topo-unknown">PLGNLTI</span><span class="topo-outside">AVSGDKILSVMELDSYPLY</span><span class="topo-membrane">AIYLIVIGLSGGFMVLYYVS</span><span class="topo-inside">LRFIKQKPS</span><span class="topo-unknown">QDW</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>28</td>
      <td>56</td>
      <td>28</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>362</td>
      <td>87</td>
      <td>362</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>394</td>
      <td>390</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>395</td>
      <td>410</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>411</td>
      <td>418</td>
      <td>411</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>436</td>
      <td>419</td>
      <td>436</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>451</td>
      <td>437</td>
      <td>451</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>468</td>
      <td>452</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>500</td>
      <td>469</td>
      <td>500</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>501</td>
      <td>519</td>
      <td>501</td>
      <td>519</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>520</td>
      <td>524</td>
      <td>520</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>550</td>
      <td>525</td>
      <td>550</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>551</td>
      <td>557</td>
      <td>551</td>
      <td>557</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>574</td>
      <td>558</td>
      <td>574</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>575</td>
      <td>586</td>
      <td>575</td>
      <td>586</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>600</td>
      <td>587</td>
      <td>600</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>601</td>
      <td>615</td>
      <td>601</td>
      <td>615</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>623</td>
      <td>641</td>
      <td>623</td>
      <td>641</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>642</td>
      <td>661</td>
      <td>642</td>
      <td>661</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>662</td>
      <td>670</td>
      <td>662</td>
      <td>670</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### ABCG8 contributes the catalytically active NBS2

ABCG8 contains the catalytically active Signature motif that contributes to NBS2, which binds and hydrolyses ATP. In contrast, ABCG5 contains an inactive Signature motif (NBS1) that binds but does not hydrolyse ATP. The three-helix bundle (CnH/CpH/E-helix) of G8 exhibits greater flexibility and transitions between different conformations, linking ATP hydrolysis to sterol transport via allosteric communication.

### Cholesterol hydrogen bonding with ABCG8_T430

In the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol)-bound ABCG5/G8 structure (PDB 8CUB), the cholesterol hydroxyl group forms a hydrogen bond with ABCG8_T430. The cholesterol extends across the interfacial space with its hydrocarbon tail remaining straight and in contact with hydrophobic residues on ABCG5 such as L516, L537, I562, F565, and F567. The sterol fits into an indented planar cleft within the upper region of the vestibule formed by the re-entry and transmembrane helices.

### Phenylalanine highway in ABCG8

ABCG8 contains a conserved phenylalanine F453 at position F1 of the phenylalanine highway (PH) on transmembrane helix 2. In ABCG8, F453 stacks underneath F576 (along with M577), which comprise the hydrophobic valve. The PH creates a highway-shaped open space at the TMD dimer interface, with aromatic side chains pointing inward, potentially serving as a molecular clamp for sterol transport.

### P415 landmark on ABCG8 connecting helix

Proline 415 (P415) in ABCG8 marks the end of the connecting helix that bridges the transmembrane domain to the nucleotide-binding domain. In wild-type ABCG5/G8, the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) binding cloud stretches from P415 (ABCG8) to A540 (ABCG5), forming a continuous binding pattern. The A540F mutation introduces a break in this docking prediction, separating the two clusters.

### Asymmetric sterol binding on ABCG5/G8

Sterol docking poses on ABCG5/G8 are distributed asymmetrically at the opposing membrane-transporter interfaces. On the ABCG8-dominant side, sterol molecules orient in various but seemingly unspecific directions. [Stigmasterol](/xray-mp-wiki/reagents/lipids/stigmasterol) binds in two clusters partitioned between each monomer, while cholesterol binds in two separate pockets. The highest clusters of stigmasterol and cholesterol are located on opposite sides of the transporter-membrane interface.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg5/">ABCG5</a> — Obligate heterodimer partner; [ABCG5/G8](/xray-mp-wiki/proteins/abcg5) heterodimer crystallized together in PDB 5DO7 (first ABC sterol transporter structure) and PDB 8CUB
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg1/">ABCG1</a> — Homodimeric ABCG sterol transporter; extensively compared for sterol binding patterns
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg2/">ABCG2</a> — Multidrug transporter ABCG member; shares hydrophobic valve and PH motif for comparison
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Central ligand; hydrogen bonds with ABCG8_T430; used in crystallization and incubation
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) derivative used in purification and crystallization buffers (0.01% w/v)
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">Decyl Maltose Neopentyl Glycol (DMNG)</a> — Primary detergent used in final purification and crystallization sample buffer
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — Crystallization buffer (100 mM, pH 6.5)
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Crystallization precipitant (1.8-2.0 M)
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — G5G8 was crystallized using bicelle crystallization with DMPC/cholesterol bicelles
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — G5G8 is an ABCG subfamily member; the 2016 structure defined the ABC2 exporter superfamily fold
