---
title: "Campylobacter jejuni CmeB Multidrug Efflux Pump"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00217-z]
verified: agent
uniprot_id: Q0PBE4
---

# Campylobacter jejuni CmeB Multidrug Efflux Pump

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q0PBE4">UniProt: Q0PBE4</a>

<span class="expr-badge">Campylobacter jejuni</span>

## Overview

CmeB is the inner membrane Resistance-Nodulation-Division (RND) multidrug efflux pump component of the CmeABC tripartite efflux system from Campylobacter jejuni, a leading cause of human enterocolitis. CmeB assembles as a homotrimer and catalyzes the export of antimicrobials such as fluoroquinolones and macrolides, contributing significantly to both intrinsic and acquired antibiotic resistance. The CmeB trimer displays a unique asymmetric conformation where each protomer can function independently of one another, in contrast to the coordinated rotating mechanism proposed for the homologous [Acrb](/xray-mp-wiki/proteins/abc-transporters/acrb/) pump from E. coli. Single-molecule FRET imaging revealed four distinct conformational states (low, intermediate-1, intermediate-2, and high FRET) and demonstrated that individual protomers within the trimer undergo uncoordinated conformational transitions during drug export.

## Publications

### doi/10.1038##s41467-017-00217-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5t00">5T00</a></td>
      <td>3.15</td>
      <td>C2</td>
      <td>Full-length CmeB from Campylobacter jejuni (form I) — all three periplasmic clefts closed</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5lq3">5LQ3</a></td>
      <td>3.55</td>
      <td>P1</td>
      <td>Full-length CmeB from Campylobacter jejuni (form II) — one out of three periplasmic clefts open</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: CmeB from C. jejuni expressed as N-terminal 6xHis fusion in E. coli BL21(DE3) ΔacrB cells; cysteineless variant (C453S, C496S, C544S) for sm-FRET studies

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
      <td>Homogenization</td>
      <td>--</td>
      <td>not specified + --</td>
      <td>Cells disrupted for membrane protein extraction</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM Na-HEPES (pH 7.5) + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM Na-HEPES (pH 7.5), <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>N-terminal 6xHis tag purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Na-HEPES (pH 7.5) + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step; protein then concentrated to 20 µM for labeling</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CmeB in 20 mM Na-HEPES (pH 7.5), 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
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
      <td>Two crystal forms obtained: Form I (C2, resolution 3.15 Å) and Form II (P1, resolution 3.55 Å). X-ray data collected at 100 K at beamline 24ID-C (APS). Structures solved by molecular replacement using an AcrB-based (PDB 4DX5) model generated by FFAS03 server. Form I crystals belong to space group C2, form II to P1.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lq3">5LQ3</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">FSKFFIE</span><span class="topo-inside">RPVFA</span><span class="topo-membrane">SVVAIIISLAGAIGL</span><span class="topo-outside">TNLPIEQYPSLTPPTVKVSATYTGADAQTIASTVASPIEDAINGADNMIYMDSTSSSSGTMSLTVYFDIGTDPDQATIDVNNRISAATAKMP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DAVKKLGVTVRKTSSTTLAAISMYSSDGSMSAVDVYNYITLNVLDELKRVPGVGDANAIGNRNYSLRIWLKPDLLNKFGITATDVISAVNDQNAQYATGKIGEEPVTQKSPYVYSITMQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RLQNPSEFENIILRTNNDGSFLRLKDVADVEIGSQQYSSQGRLNGNDAVPIMINLQSGANALHTAELVQAKMQELSKNFPKGLTYKIPYDTTKFVIESIKEVVK</span><span class="topo-membrane">TFVEALILVIIVMYM</span><span class="topo-inside">F</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LKNFRAT</span><span class="topo-membrane">LIPMIAVPVSLLGTFAGL</span><span class="topo-outside">YVLGFSINLLTLF</span><span class="topo-membrane">ALILAIGIVVDDAI</span><span class="topo-inside">IVVENIDRILHENEQISVKDAAIQAMQEVSSPV</span><span class="topo-membrane">ISIVLVLCAVFVPVSF</span><span class="topo-outside">ISGFVGEIQRQF</span><span class="topo-membrane">ALTLAIS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VTISGFVA</span><span class="topo-inside">LTLTPSLCALFLRRNEGEPFK</span><span class="topo-unknown">FVKKFNDFFDWSTSVFSAGVAYILK</span><span class="topo-inside">RTIRF</span><span class="topo-membrane">VLIFCIMLGAIFYLY</span><span class="topo-outside">KAVPNSLVPEEDQGLMISIINLPSASALHRTISEVDHISQEVLKTN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">GVKDAMAMIGFDLFTSSLKENAAAMFIGLQDWKDRNVSADQIIAELNKKFAFDRNASSVFIGLPPIPGLSITGGFEMYVQNKSGKSYDEIQKDVNKLVAAANQRKELSRVRTTLDTTFPQ</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">YKLIIDRDKLKHYNLNMQDVFNTMNATIGTYYVNDFSMLGKNFQVNIRAKGDFRNTQDALKNIFVRSNDGKMIPLDSFLTLQRSSGPDDVKRFNLFPAAQVQGQPAPGYTSGQAIEAIAQ</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VAKETLGDDYSIAWSGSAYQEVSSKGTAS</span><span class="topo-membrane">YAFALGMIFVFLILAA</span><span class="topo-inside">QYERWLIP</span><span class="topo-membrane">LAVVTAVPFAVFGSFLLVYL</span><span class="topo-outside">RGFSNDIYFQ</span><span class="topo-membrane">TGLLLLIGLSAKNAI</span><span class="topo-inside">LIVEFAMEERFKKGKGVFEAAV</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030     </span>
<span class="topo-line"><span class="topo-inside">AAAKLRFRPI</span><span class="topo-membrane">IMTSLAFTFGVLPMIF</span><span class="topo-outside">ATGAGSASRHSL</span><span class="topo-membrane">GTGLIGGMIAASTLAI</span><span class="topo-unknown">FFVPLFFYLLENFNEWL</span><span class="topo-inside">DK</span><span class="topo-unknown">KR</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>13</td>
      <td>9</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>28</td>
      <td>14</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>344</td>
      <td>29</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>359</td>
      <td>345</td>
      <td>359</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>367</td>
      <td>360</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>385</td>
      <td>368</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>398</td>
      <td>386</td>
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
      <td>445</td>
      <td>413</td>
      <td>445</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>446</td>
      <td>461</td>
      <td>446</td>
      <td>461</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>462</td>
      <td>473</td>
      <td>462</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>488</td>
      <td>474</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>489</td>
      <td>509</td>
      <td>489</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>534</td>
      <td>510</td>
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
      <td>869</td>
      <td>555</td>
      <td>869</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>870</td>
      <td>885</td>
      <td>870</td>
      <td>885</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>886</td>
      <td>893</td>
      <td>886</td>
      <td>893</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>894</td>
      <td>913</td>
      <td>894</td>
      <td>913</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>914</td>
      <td>923</td>
      <td>914</td>
      <td>923</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>924</td>
      <td>938</td>
      <td>924</td>
      <td>938</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>939</td>
      <td>970</td>
      <td>939</td>
      <td>970</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>971</td>
      <td>986</td>
      <td>971</td>
      <td>986</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>987</td>
      <td>998</td>
      <td>987</td>
      <td>998</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1014</td>
      <td>999</td>
      <td>1014</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1015</td>
      <td>1031</td>
      <td>1015</td>
      <td>1031</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1032</td>
      <td>1033</td>
      <td>1032</td>
      <td>1033</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lq3">5LQ3</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MFSKFFIERPV</span><span class="topo-membrane">FASVVAIIISLAGAI</span><span class="topo-outside">GLTNLPIEQYPSLTPPTVKVSATYTGADAQTIASTVASPIEDAINGADNMIYMDSTSSSSGTMSLTVYFDIGTDPDQATIDVNNRISAATAKMP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DAVKKLGVTVRKTSSTTLAAISMYSSDGSMSAVDVYNYITLNVLDELKRVPGVGDANAIGNRNYSLRIWLKPDLLNKFGITATDVISAVNDQNAQYATGKIGEEPVTQKSPYVYSITMQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RLQNPSEFENIILRTNNDGSFLRLKDVADVEIGSQQYSSQGRLNGNDAVPIMINLQSGANALHTAELVQAKMQELSKNFPKGLTYKIPYDTTKFVIESIKEVV</span><span class="topo-membrane">KTFVEALILVIIVMY</span><span class="topo-inside">MF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LKNFRAT</span><span class="topo-membrane">LIPMIAVPVSLLGTFAG</span><span class="topo-outside">LYVLGFSINLLTLFAL</span><span class="topo-membrane">ILAIGIVVDDAII</span><span class="topo-inside">VVENIDRILHENEQISVKDAAIQAMQEVSSP</span><span class="topo-membrane">VISIVLVLCAVFVP</span><span class="topo-outside">VSFISGFVGEIQRQFA</span><span class="topo-membrane">LTLAIS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VTISGFVALTLT</span><span class="topo-inside">PSLCALFLRRNEGEPF</span><span class="topo-unknown">KFVKKFNDFFDWSTSVFSAGVAYILK</span><span class="topo-inside">RTIRF</span><span class="topo-membrane">VLIFCIMLGAIFYLY</span><span class="topo-outside">KAVPNSLVPEEDQGLMISIINLPSASALHRTISEVDHISQEVLKTN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">GVKDAMAMIGFDLFTSSLKENAAAMFIGLQDWKDRNVSADQIIAELNKKFAFDRNASSVFIGLPPIPGLSITGGFEMYVQNKSGKSYDEIQKDVNKLVAAANQRKELSRVRTTLDTTFPQ</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">YKLIIDRDKLKHYNLNMQDVFNTMNATIGTYYVNDFSMLGKNFQVNIRAKGDFRNTQDALKNIFVRSNDGKMIPLDSFLTLQRSSGPDDVKRFNLFPAAQVQGQPAPGYTSGQAIEAIAQ</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VAKETLGDDYSIAWSGSAYQEVSSKGTASY</span><span class="topo-membrane">AFALGMIFVFLILAA</span><span class="topo-inside">QYERWLIP</span><span class="topo-membrane">LAVVTAVPFAVFGSFLLV</span><span class="topo-outside">YLRGFSNDIYFQTG</span><span class="topo-membrane">LLLLIGLSAKNAI</span><span class="topo-inside">LIVEFAMEERFKKGKGVFEAAV</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030     </span>
<span class="topo-line"><span class="topo-inside">AAAKLRFRP</span><span class="topo-membrane">IIMTSLAFTFGVLP</span><span class="topo-outside">MIFATGAGSASRHSLG</span><span class="topo-membrane">TGLIGGMIAASTLAIFFV</span><span class="topo-unknown">PLFFYLLENFNEW</span><span class="topo-inside">LDK</span><span class="topo-unknown">KR</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>358</td>
      <td>344</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>367</td>
      <td>359</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>384</td>
      <td>368</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>400</td>
      <td>385</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>413</td>
      <td>401</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>444</td>
      <td>414</td>
      <td>444</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>458</td>
      <td>445</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>474</td>
      <td>459</td>
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
      <td>508</td>
      <td>493</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>534</td>
      <td>509</td>
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
      <td>870</td>
      <td>555</td>
      <td>870</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>871</td>
      <td>885</td>
      <td>871</td>
      <td>885</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>886</td>
      <td>893</td>
      <td>886</td>
      <td>893</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>894</td>
      <td>911</td>
      <td>894</td>
      <td>911</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>912</td>
      <td>925</td>
      <td>912</td>
      <td>925</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>926</td>
      <td>938</td>
      <td>926</td>
      <td>938</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>939</td>
      <td>969</td>
      <td>939</td>
      <td>969</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>970</td>
      <td>983</td>
      <td>970</td>
      <td>983</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>984</td>
      <td>999</td>
      <td>984</td>
      <td>999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>1017</td>
      <td>1000</td>
      <td>1017</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1030</td>
      <td>1018</td>
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
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lq3">5LQ3</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">FSKFFI</span><span class="topo-inside">ERPVFA</span><span class="topo-membrane">SVVAIIISLAGAIG</span><span class="topo-outside">LTNLPIEQYPSLTPPTVKVSATYTGADAQTIASTVASPIEDAINGADNMIYMDSTSSSSGTMSLTVYFDIGTDPDQATIDVNNRISAATAKMP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DAVKKLGVTVRKTSSTTLAAISMYSSDGSMSAVDVYNYITLNVLDELKRVPGVGDANAIGNRNYSLRIWLKPDLLNKFGITATDVISAVNDQNAQYATGKIGEEPVTQKSPYVYSITMQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RLQNPSEFENIILRTNNDGSFLRLKDVADVEIGSQQYSSQGRLNGNDAVPIMINLQSGANALHTAELVQAKMQELSKNFPKGLTYKIPYDTTKFVIESIKEVVKT</span><span class="topo-membrane">FVEALILVIIVMYM</span><span class="topo-inside">F</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LKNFRAT</span><span class="topo-membrane">LIPMIAVPVSLLGTFAG</span><span class="topo-outside">LYVLGFSINLLTLFA</span><span class="topo-membrane">LILAIGIVVDDAI</span><span class="topo-inside">IVVENIDRILHENEQISVKDAAIQAMQEVSSP</span><span class="topo-membrane">VISIVLVLCAVFVPV</span><span class="topo-outside">SFISGFVGEIQRQF</span><span class="topo-membrane">ALTLAIS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VTISGFVAL</span><span class="topo-inside">TLTPSLCALFLRRNEGEPF</span><span class="topo-unknown">KFVKKFNDFFDWSTSVFSAGVAYILK</span><span class="topo-inside">RTIR</span><span class="topo-membrane">FVLIFCIMLGAIFYL</span><span class="topo-outside">YKAVPNSLVPEEDQGLMISIINLPSASALHRTISEVDHISQEVLKTN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">GVKDAMAMIGFDLFTSSLKENAAAMFIGLQDWKDRNVSADQIIAELNKKFAFDRNASSVFIGLPPIPGLSITGGFEMYVQNKSGKSYDEIQKDVNKLVAAANQRKELSRVRTTLDTTFPQ</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">YKLIIDRDKLKHYNLNMQDVFNTMNATIGTYYVNDFSMLGKNFQVNIRAKGDFRNTQDALKNIFVRSNDGKMIPLDSFLTLQRSSGPDDVKRFNLFPAAQVQGQPAPGYTSGQAIEAIAQ</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">VAKETLGDDYSIAWSGSAYQEVSSKGTASYA</span><span class="topo-membrane">FALGMIFVFLILAAQ</span><span class="topo-inside">YERWLI</span><span class="topo-membrane">PLAVVTAVPFAVFGSFLL</span><span class="topo-outside">VYLRGFSNDIYFQTG</span><span class="topo-membrane">LLLLIGLSAKNAI</span><span class="topo-inside">LIVEFAMEERFKKGKGVFEAAV</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030     </span>
<span class="topo-line"><span class="topo-inside">AAAKLRFRPI</span><span class="topo-membrane">IMTSLAFTFGVLPMIF</span><span class="topo-outside">ATGAGSASRHSLG</span><span class="topo-membrane">TGLIGGMIAASTLAIFFV</span><span class="topo-unknown">PLFFYLLENFNEWLDK</span><span class="topo-inside">KR</span></span>
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
      <td>13</td>
      <td>8</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>27</td>
      <td>14</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>345</td>
      <td>28</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>346</td>
      <td>359</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>367</td>
      <td>360</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>384</td>
      <td>368</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>399</td>
      <td>385</td>
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
      <td>444</td>
      <td>413</td>
      <td>444</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>459</td>
      <td>445</td>
      <td>459</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>460</td>
      <td>473</td>
      <td>460</td>
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
      <td>508</td>
      <td>490</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>534</td>
      <td>509</td>
      <td>534</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>538</td>
      <td>535</td>
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
      <td>871</td>
      <td>554</td>
      <td>871</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>872</td>
      <td>886</td>
      <td>872</td>
      <td>886</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>887</td>
      <td>892</td>
      <td>887</td>
      <td>892</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>893</td>
      <td>910</td>
      <td>893</td>
      <td>910</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>911</td>
      <td>925</td>
      <td>911</td>
      <td>925</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>926</td>
      <td>938</td>
      <td>926</td>
      <td>938</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>939</td>
      <td>970</td>
      <td>939</td>
      <td>970</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>971</td>
      <td>986</td>
      <td>971</td>
      <td>986</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>987</td>
      <td>999</td>
      <td>987</td>
      <td>999</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>1017</td>
      <td>1000</td>
      <td>1017</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1018</td>
      <td>1033</td>
      <td>1018</td>
      <td>1033</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1034</td>
      <td>1035</td>
      <td>1034</td>
      <td>1035</td>
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

### Independent protomer function within the CmeB trimer

Single-molecule FRET imaging of CmeB trimers embedded in liposomes revealed that individual protomers undergo conformational transitions independently of one another. Four distinct FRET states (low ~0.20, intermediate-1 ~0.35, intermediate-2 ~0.45, and high ~0.60) were observed. The transition density plots were symmetrical, arguing against the rotating mechanism proposed for [Acrb](/xray-mp-wiki/proteins/abc-transporters/acrb/) where protomers cycle sequentially through access, binding, and extrusion states. Instead, each CmeB protomer can autonomously go through conformational changes leading to substrate extrusion.

### Proton relay network and energy coupling

The conserved charged residues D409, D410, and K935 form a salt-bridge triad in the transmembrane domain, establishing the proton-relay network for energy coupling. The D409A mutant completely abolished proton transport activity and severely reduced conformational dynamics, confirming that the proton-motive force drives the uncoordinated conformational transitions observed in each protomer.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">Dodecylmaltoside (DDM)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — 20 mM Na-HEPES (pH 7.5) used in purification and crystallization buffers
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB Multidrug Efflux Transporter</a> — Homologous RND efflux pump used as molecular replacement search model; comparison of transport mechanisms
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final polishing step in CmeB purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Phasing method for CmeB structure determination using AcrB model
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">Isothermal Titration Calorimetry</a> — Used to measure binding of taurodeoxycholate to CmeB
- <a href="/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/">Proteoliposome Reconstitution</a> — CmeB reconstituted into liposomes for sm-FRET studies
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">Acrb</a> — Referenced in the context of Acrb
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in the context of DDM
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in the context of Imidazole
