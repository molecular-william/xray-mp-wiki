---
title: "Epithelial Calcium Channel TRPV6"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17975, doi/10.1038##s41598-017-10993-9]
verified: agent
uniprot_id: Q9R186
---

# Epithelial Calcium Channel TRPV6

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9R186">UniProt: Q9R186</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

TRPV6 is a Ca2+-selective transient receptor potential vanilloid channel uniquely expressed in epithelial tissues where it mediates active Ca2+ absorption across the intestinal and other epithelial barriers. TRPV6 forms homo- or heteromeric tetrameric assemblies of four subunits, each containing a central K+ channel-like transmembrane domain flanked by intracellular N- and C-terminal domains. The channel is essential for calcium homeostasis and its overexpression has been implicated in various cancers. Structural studies have revealed the architecture of TRPV6, its Ca2+ selectivity and permeation mechanism, and the molecular basis of inhibition by (4-phenylcyclohexyl)piperazine derivatives (PCHPDs) that act as inactivation-mimicking pore blockers.


## Publications

### doi/10.1038##nature17975

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iwk">5IWK</a></td>
      <td>3.25 A</td>
      <td>P4_12_12</td>
      <td>Rat TRPV6 crystallization construct (TRPV6_cryst), residues 1-668, mutations I62Y, L92N, M96Q, L495Q, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a> (bound at intersubunit interface during affinity purification)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iwp">5IWP</a></td>
      <td>3.85 A</td>
      <td>P4_12_12</td>
      <td>Rat TRPV6 crystallization construct with Ba2+</td>
      <td>Ba2+ (10 mM BaCl2)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iwr">5IWR</a></td>
      <td>3.65 A</td>
      <td>P4_12_12</td>
      <td>Rat TRPV6 crystallization construct with Ca2+</td>
      <td>Ca2+ (10 mM CaCl2)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iwt">5IWT</a></td>
      <td>3.80 A</td>
      <td>P4_12_12</td>
      <td>Rat TRPV6 crystallization construct with Gd3+</td>
      <td>Gd3+ (1 mM GdCl3)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK 293S cells (GnTI-), BacMam expression
- **Construct**: Rat TRPV6 (GenBank EDM15484.1), crystallization construct TRPV6_cryst comprising residues 1-668 with point mutations I62Y, L92N, M96Q, L495Q and C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/). C-terminal thrombin cleavage site (LVPRG) followed by eGFP and streptavidin affinity tag (WSHPQFEK). Expressed in [PEG](/xray-mp-wiki/reagents/additives/peg/) BacMam vector.
- **Notes**: For [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) studies, hTRPV6-FL (residues 1-725) and hTRPV6-CtD (residues 1-666, C-terminally truncated) constructs were used with C-terminal thrombin cleavage site followed by streptavidin affinity tag.

**Purification:**

- **Expression system**: HEK 293S (GnTI-)
- **Expression construct**: Rat TRPV6_cryst (residues 1-668, I62Y, L92N, M96Q, L495Q), C-terminal thrombin-eGFP-Strep tag
- **Tag info**: C-terminal streptavidin affinity tag (WSHPQFEK), removable by thrombin cleavage

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
      <td>Sonication</td>
      <td>--</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.8 uM aprotinin, 2 ug/ml leupeptin, 2 mM pepstatin A, 1 mM PMSF + --</td>
      <td>Misonix Sonicator, 12 x 15 <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/), power level 7</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Sorval centrifuge 7,500 rpm 15 min, then Beckman Ti45 rotor 40,000 RPM 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, protease inhibitors + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>2-4 hours incubation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Streptavidin-linked resin</td>
      <td>150 mM NaCl, 20 mM Tris pH 8.0, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Rotated 4-16 hours, eluted with 10 mM <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a></td>
    </tr>
    <tr>
      <td>Thrombin cleavage</td>
      <td>Protease cleavage</td>
      <td>--</td>
      <td>150 mM NaCl, 20 mM Tris pH 8.0, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Thrombin added at 1:50 ratio, 1.5 hours at 22C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superose 6 column</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM betaME + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Tetrameric channel fractions collected, 10 mM TCEP added</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified in 150 mM NaCl, 20 mM Tris pH 8.0, 1 mM betaME, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TRPV6_cryst at 2.5-3.0 mg/ml in 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM betaME, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-24% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 350 MME, 100 mM NaCl, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0-8.5</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>33-36% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 350 MME, 100 mM NaCl, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.2, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a>, flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew as thin plates (~400 um x ~120 um x ~20 um). 50 mM <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a> added to protein before crystallization to increase crystal size. For co-crystallization with cations, protein was incubated with 10 mM CaCl2, 10 mM BaCl2, or 1 mM GdCl3 for 1 hour at 4C prior to crystallization.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwk">5IWK</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWRV</span><span class="topo-unknown">AHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>444</td>
      <td>422</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>486</td>
      <td>480</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>584</td>
      <td>577</td>
      <td>584</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>606</td>
      <td>585</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwk">5IWK</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWRV</span><span class="topo-unknown">AHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>444</td>
      <td>422</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>486</td>
      <td>480</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>584</td>
      <td>577</td>
      <td>584</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>606</td>
      <td>585</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwk">5IWK</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWRV</span><span class="topo-unknown">AHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>444</td>
      <td>422</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>486</td>
      <td>480</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>584</td>
      <td>577</td>
      <td>584</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>606</td>
      <td>585</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwk">5IWK</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWRV</span><span class="topo-unknown">AHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>444</td>
      <td>422</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>486</td>
      <td>480</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>584</td>
      <td>577</td>
      <td>584</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>606</td>
      <td>585</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwp">5IWP</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">IQ</span><span class="topo-outside">KMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>486</td>
      <td>483</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwp">5IWP</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">IQ</span><span class="topo-outside">KMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>486</td>
      <td>483</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwp">5IWP</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">IQ</span><span class="topo-outside">KMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>486</td>
      <td>483</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwp">5IWP</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">IQ</span><span class="topo-outside">KMIF</span><span class="topo-membrane">GDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>486</td>
      <td>483</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>511</td>
      <td>487</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwr">5IWR</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-outside">FQ</span><span class="topo-unknown">MLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLER</span><span class="topo-outside">KLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>472</td>
      <td>471</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>605</td>
      <td>584</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>637</td>
      <td>606</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwr">5IWR</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-outside">FQ</span><span class="topo-unknown">MLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLER</span><span class="topo-outside">KLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>472</td>
      <td>471</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>605</td>
      <td>584</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>637</td>
      <td>606</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwr">5IWR</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-outside">FQ</span><span class="topo-unknown">MLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLER</span><span class="topo-outside">KLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>472</td>
      <td>471</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>605</td>
      <td>584</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>637</td>
      <td>606</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwr">5IWR</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-outside">FQ</span><span class="topo-unknown">MLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLER</span><span class="topo-outside">KLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>472</td>
      <td>471</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>605</td>
      <td>584</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>637</td>
      <td>606</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwt">5IWT</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwt">5IWT</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwt">5IWT</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iwt">5IWT</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRP</span><span class="topo-membrane">YFCVLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPKDD</span><span class="topo-membrane">LRLVGELVSIVGAVIILLVEIPDIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILG</span><span class="topo-membrane">GPFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFARG</span><span class="topo-unknown">FQMLGPFTI</span><span class="topo-outside">M</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMI</span><span class="topo-membrane">FGDLMRFCWQMAVVILGFASAFYIIF</span><span class="topo-inside">QTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLP</span><span class="topo-membrane">FMYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>326</td>
      <td>27</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>349</td>
      <td>327</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>382</td>
      <td>350</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>408</td>
      <td>383</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>443</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>449</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>485</td>
      <td>480</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>512</td>
      <td>524</td>
      <td>512</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>544</td>
      <td>525</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>551</td>
      <td>545</td>
      <td>551</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>576</td>
      <td>552</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>583</td>
      <td>577</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>606</td>
      <td>584</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41598-017-10993-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wo6">5WO6</a></td>
      <td>3.45 A</td>
      <td>P42_12</td>
      <td>TRPV6_cryst (same as 5IWK), mutations I62Y, L92N, M96Q, L495Q</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wo7">5WO7</a></td>
      <td>3.25 A</td>
      <td>P42_12</td>
      <td>TRPV6* (L495Q reverted to native L495), C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, I62Y, L92N, M96Q</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wo8">5WO8</a></td>
      <td>3.40 A</td>
      <td>P42_12</td>
      <td>TRPV6*-del1 (4 residues deleted in S4-S5 linker, 477-480)</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5wo9">5WO9</a></td>
      <td>3.6 A</td>
      <td>P42_12</td>
      <td>TRPV6_cryst with Ca2+, mutations I62Y, L92N, M96Q, L495Q</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5woa">5WOA</a></td>
      <td>3.85 A</td>
      <td>P42_12</td>
      <td>TRPV6_cryst with Gd3+, mutations I62Y, L92N, M96Q, L495Q</td>
      <td>Gd3+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK 293S cells (GnTI-), BacMam expression
- **Construct**: Rat TRPV6 (GenBank EDM15484.1), crystallization construct TRPV6_cryst comprising residues 1-668 with point mutations I62Y, L92N, M96Q, L495Q and C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/). C-terminal thrombin cleavage site (LVPRG) followed by eGFP and streptavidin affinity tag (WSHPQFEK). Expressed in [PEG](/xray-mp-wiki/reagents/additives/peg/) BacMam vector.
- **Notes**: For [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) studies, hTRPV6-FL (residues 1-725) and hTRPV6-CtD (residues 1-666, C-terminally truncated) constructs were used with C-terminal thrombin cleavage site followed by streptavidin affinity tag.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TRPV6* or TRPV6*-del1 at 2.5-3.0 mg/ml in 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 1 mM betaME, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-24% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 350 MME, 50 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0-8.5</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>100 mM NaCl, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.2, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a>, 33-36% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 350 MME, flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein subjected to ultracentrifugation (Ti100 rotor, 40000 rpm, 40 min, 4C) prior to crystallization to remove aggregates. For cation-bound structures, protein was incubated with 10 mM CaCl2 or 1 mM GdCl3 for 1 h at 4C prior to crystallization.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wo6">5WO6</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRRE</span><span class="topo-outside">SWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRPYFCV</span><span class="topo-membrane">LGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVT</span><span class="topo-membrane">PKDDLRLVGELVSIVGAVIILLVEIP</span><span class="topo-outside">DIFR</span><span class="topo-unknown">LGVTRFFG</span><span class="topo-outside">QTILGG</span><span class="topo-membrane">PFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFA</span><span class="topo-outside">RGFQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKMIFGD</span><span class="topo-membrane">LMRFCWQMAVVILGFASAFYII</span><span class="topo-inside">FQTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDGP</span><span class="topo-inside">ANYDVDLPF</span><span class="topo-membrane">MYSITYAAFAIIATLLMLNLLIAMM</span><span class="topo-outside">GDTHWR</span><span class="topo-unknown">VAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660        </span>
<span class="topo-line"><span class="topo-unknown">VMLER</span><span class="topo-outside">KLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEK</span></span>
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
      <td>28</td>
      <td>330</td>
      <td>28</td>
      <td>330</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>349</td>
      <td>331</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>378</td>
      <td>350</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>404</td>
      <td>379</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>408</td>
      <td>405</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>422</td>
      <td>417</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>444</td>
      <td>423</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>468</td>
      <td>449</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>488</td>
      <td>469</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>510</td>
      <td>489</td>
      <td>510</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>524</td>
      <td>511</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>543</td>
      <td>525</td>
      <td>543</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>544</td>
      <td>552</td>
      <td>544</td>
      <td>552</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>553</td>
      <td>577</td>
      <td>553</td>
      <td>577</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>578</td>
      <td>583</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>605</td>
      <td>584</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>606</td>
      <td>637</td>
      <td>606</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wo7">5WO7</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRRES</span><span class="topo-outside">WAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRPYFC</span><span class="topo-membrane">VLGAIYVLYIICFTMCCVYRP</span><span class="topo-inside">LKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVT</span><span class="topo-membrane">PKDDLRLVGELVSIVGAVIILLVEIP</span><span class="topo-outside">D</span><span class="topo-unknown">IFRLGVTRFFGQTI</span><span class="topo-outside">LGG</span><span class="topo-membrane">PFHVIIVTYAFMVLVTMVMRLTNSD</span><span class="topo-inside">G</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFAR</span><span class="topo-outside">GFQMLGPF</span><span class="topo-membrane">TIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">IQKMIFGDLMRFCWLMAVVILGFASA</span><span class="topo-inside">FYIIFQTEDPDELGHFYDYP</span><span class="topo-unknown">MALFSTFELFLTIIDG</span><span class="topo-inside">PANYDVDLPFMYSI</span><span class="topo-membrane">TYAAFAIIATLLMLNLLIAMMG</span><span class="topo-outside">DTHWRVAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670      </span>
<span class="topo-line"><span class="topo-outside">VMLERKLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPRLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>329</td>
      <td>29</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>330</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>378</td>
      <td>351</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>404</td>
      <td>379</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>405</td>
      <td>405</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>419</td>
      <td>406</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>447</td>
      <td>423</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>448</td>
      <td>448</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>469</td>
      <td>449</td>
      <td>469</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>477</td>
      <td>470</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>506</td>
      <td>478</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>507</td>
      <td>526</td>
      <td>507</td>
      <td>526</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>527</td>
      <td>542</td>
      <td>527</td>
      <td>542</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>556</td>
      <td>543</td>
      <td>556</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>557</td>
      <td>578</td>
      <td>557</td>
      <td>578</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>579</td>
      <td>637</td>
      <td>579</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>638</td>
      <td>676</td>
      <td>638</td>
      <td>676</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wo8">5WO8</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRR</span><span class="topo-outside">ESWAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRPYFCVLG</span><span class="topo-membrane">AIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPK</span><span class="topo-membrane">DDLRLVGELVSIVGAVIILLVEI</span><span class="topo-outside">PDIF</span><span class="topo-unknown">RLGVTRFFG</span><span class="topo-outside">QTILGG</span><span class="topo-membrane">PFHVIIVTYAFMVLVTMVMRLT</span><span class="topo-inside">NSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFA</span><span class="topo-outside">RG</span><span class="topo-unknown">FQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">IQKMI</span><span class="topo-outside">FGDL</span><span class="topo-membrane">MRFCWLMAVVILGFASAFYII</span><span class="topo-inside">FQTEDPDELGHFYD</span><span class="topo-unknown">YPMALFSTFELFLTIIDG</span><span class="topo-inside">PANYDVDLPF</span><span class="topo-membrane">MYSITYAAFAIIATLLMLNLLIAM</span><span class="topo-outside">MGDTHWRVAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-outside">VMLERKLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>27</td>
      <td>332</td>
      <td>27</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>349</td>
      <td>333</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>380</td>
      <td>350</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>403</td>
      <td>381</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>407</td>
      <td>404</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>422</td>
      <td>417</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>444</td>
      <td>423</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>468</td>
      <td>449</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>470</td>
      <td>469</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>486</td>
      <td>489</td>
      <td>486</td>
      <td>489</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>524</td>
      <td>511</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>525</td>
      <td>542</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>543</td>
      <td>552</td>
      <td>543</td>
      <td>552</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>553</td>
      <td>576</td>
      <td>553</td>
      <td>576</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>577</td>
      <td>637</td>
      <td>577</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5wo9">5WO9</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRRES</span><span class="topo-outside">WAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRPYFC</span><span class="topo-membrane">VLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPK</span><span class="topo-membrane">DDLRLVGELVSIVGAVIILLVEI</span><span class="topo-outside">PD</span><span class="topo-unknown">IFRLGVTRFFGQTI</span><span class="topo-outside">LGG</span><span class="topo-membrane">PFHVIIVTYAFMVLVTMVMRLTNS</span><span class="topo-inside">DG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFA</span><span class="topo-outside">RGF</span><span class="topo-unknown">QMLGPF</span><span class="topo-membrane">TIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">IQKMIFGDLMRFCWLMAVVILGFAS</span><span class="topo-inside">AFYIIFQTEDPDELGHFYDYPMAL</span><span class="topo-unknown">FSTFELFLTII</span><span class="topo-inside">DGPANYDVDLPFMYSITYA</span><span class="topo-membrane">AFAIIATLLMLNLLIAMMG</span><span class="topo-outside">DTH</span><span class="topo-unknown">WRVAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-unknown">VMLERK</span><span class="topo-outside">LPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>29</td>
      <td>329</td>
      <td>29</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>349</td>
      <td>330</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>380</td>
      <td>350</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>403</td>
      <td>381</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>405</td>
      <td>404</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>446</td>
      <td>423</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>447</td>
      <td>448</td>
      <td>447</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>468</td>
      <td>449</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>471</td>
      <td>469</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>477</td>
      <td>472</td>
      <td>477</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>478</td>
      <td>505</td>
      <td>478</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>529</td>
      <td>506</td>
      <td>529</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>540</td>
      <td>530</td>
      <td>540</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>541</td>
      <td>559</td>
      <td>541</td>
      <td>559</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>560</td>
      <td>578</td>
      <td>560</td>
      <td>578</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>579</td>
      <td>581</td>
      <td>579</td>
      <td>581</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>582</td>
      <td>606</td>
      <td>582</td>
      <td>606</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>637</td>
      <td>607</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5woa">5WOA</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGWSLPKEKGLILCLWNKFCRWFHRRES</span><span class="topo-outside">WAQSRDEQNLLQQKRIWESPLLLAAKENNVQALYKLLKFEGCEVHQKGAMGETALHIAALYDNNEAAQVLMEAAPELVFEPMTSELYEGQTA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LHIAVINQNVNLVRALLARGASVSARATGSVFHYRPHNLIYYGEHPLSFAACVGSEEIVRLLIEHGADIRAQDSLGNTVLHILILQPNKTFACQMYNLLLSYDGGDHLKSLELVPNNQGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TPFKLAGVEGNIVMFQHLMQKRKHIQWTYGPLTSTLYDLTEIDSSGDDQSLLELIVTTKKREARQILDQTPVKELVSLKWKRYGRPYFC</span><span class="topo-membrane">VLGAIYVLYIICFTMCCVYR</span><span class="topo-inside">PLKPRITNRTN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PRDNTLLQQKLLQEAYVTPK</span><span class="topo-membrane">DDLRLVGELVSIVGAVIILLVEIPD</span><span class="topo-unknown">IFRLGVTRFFGQTI</span><span class="topo-outside">LGG</span><span class="topo-membrane">PFHVIIVTYAFMVLVTMVMRL</span><span class="topo-inside">TNSDG</span><span class="topo-membrane">EVVPMSFALVLGWCNVMYFA</span><span class="topo-outside">RGFQMLGPFTIM</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">IQKM</span><span class="topo-membrane">IFGDLMRFCWLMAVVILGFASAFYII</span><span class="topo-inside">FQTEDPDELGHFYDY</span><span class="topo-unknown">PMALFSTFELFLTIIDGPA</span><span class="topo-inside">NYDVDLPF</span><span class="topo-membrane">MYSITYAAFAIIATLLMLNLLI</span><span class="topo-outside">AMMGDTHWRVAHERDELWRAQVVATT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670  </span>
<span class="topo-line"><span class="topo-outside">VMLERKLPRCLWPRSGICGREYGLGDRWFLRVEDRQD</span><span class="topo-unknown">LNRQRIRRYAQAFQQQDDLYSEDLEKDSGEKLVPR</span></span>
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
      <td>1</td>
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>329</td>
      <td>29</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>349</td>
      <td>330</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>380</td>
      <td>350</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>405</td>
      <td>381</td>
      <td>405</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>419</td>
      <td>406</td>
      <td>419</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>443</td>
      <td>423</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>448</td>
      <td>444</td>
      <td>448</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>468</td>
      <td>449</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>484</td>
      <td>469</td>
      <td>484</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>485</td>
      <td>510</td>
      <td>485</td>
      <td>510</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>525</td>
      <td>511</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>544</td>
      <td>526</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>545</td>
      <td>552</td>
      <td>545</td>
      <td>552</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>553</td>
      <td>574</td>
      <td>553</td>
      <td>574</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>575</td>
      <td>637</td>
      <td>575</td>
      <td>637</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>638</td>
      <td>672</td>
      <td>638</td>
      <td>672</td>
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

### TRPV6 architecture and domain organization

TRPV6 forms a four-fold symmetrical tetramer with a central ion channel pore and a ~70 A tall intracellular skirt. Each subunit contains an ankyrin repeat domain (ARD) with six ankyrin repeats, a linker domain with beta-hairpin and helix-turn-helix motif, pre-S1 helix, and a K+ channel-like transmembrane domain (S1-S6 with P-loop). A unique non-swapped TM domain arrangement was observed where S1-S4 and pore domains of the same protomer pack against each other.

### Ca2+ selectivity and permeation mechanism

Ca2+ selectivity is determined by direct coordination of Ca2+ by a ring of aspartate side chains in the selectivity filter (sequence 538TIID541). D541 side chains protrude toward the pore central axis. A Ca2+ knock-off mechanism of permeation is proposed where Site 1 is constitutively occupied by Ca2+ due to charge repulsion between D541 side chains.

### Domain swapping governed by residue 495

TRPV6 can adopt either a domain-swapped or non-swapped transmembrane architecture depending on residue 495 in the S5 helix. The native leucine (L495) drives a domain-swapped fold. Mutation to glutamine (L495Q) converts to non-swapped. The S4-S5 linker length is also a critical determinant.

### Inactivation-mimicking pore block by PCHPDs

(4-Phenylcyclohexyl)piperazine derivatives (PCHPDs) are potent and selective TRPV6 inhibitors that act via two binding sites: (i) modulatory sites at lipid-binding site 2 (LBS-2) between S1-S4 and pore domains, and (ii) the main site in the ion channel pore at the intracellular entrance. At the pore site, PCHPDs plug the open pore, physically obstructing ion conductance, mimicking the action of calmodulin (CaM) which causes Ca2+-induced inactivation. The inhibitor binding at the pore mimics the tryptophan cage mechanism where K115 of CaM interacts with W583. This represents a unique inactivation-mimicking inhibition strategy unprecedented among TRP channels.

### Tryptophan cage mechanism for pore block

Four W583 residues from each TRPV6 subunit form a tight cubic cage (4.2 A between indole rings) that provides a unique environment for cation-pi interaction with the epsilon-amino group of CaM K115. PCHPDs exploit this same site, mimicking the inactivation mechanism. The W583F mutation dramatically reduces [cis-22a (PCHPD TRPV6 Inhibitor)](/xray-mp-wiki/reagents/ligands/cis-22a/) affinity (75-fold increase in IC50 from 0.083 to 6.19 uM), confirming the importance of this tryptophan cage for inhibition.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/">Epithelial Calcium Channel TRPV5</a> — Closely related Ca2+ channel (~75% sequence identity); CaM-dependent inactivation mechanism conserved
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/trpv2/">TRPV2</a> — TRP channel family member; structural comparison of lipid-binding sites
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — PCHPD inhibition mimics Ca2+-induced inactivation mechanism; tryptophan cage at pore intracellular entrance
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization detergent (20 mM) for TRPV6 extraction from membranes
- <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a> — Elution agent for Strep affinity purification (10 mM); bound at intersubunit interface in crystal structure
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a> — Additive used in purification or crystallization buffers
