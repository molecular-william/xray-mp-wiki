---
title: "Bovine Mitochondrial F-ATPase c8-Ring (F1-c-ring Complex)"
created: 2026-06-21
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1011099107]
verified: agent
uniprot_id: ['P00829', 'P05630', 'P05631', 'P05632', 'P19483', 'P32876']
---

# Bovine Mitochondrial F-ATPase c8-Ring (F1-c-ring Complex)

<div class="expr-badges"><span class="expr-badge expr-mammalian">Mammalian</span> <span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P00829">UniProt: P00829</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P05630">UniProt: P05630</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P05631">UniProt: P05631</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P05632">UniProt: P05632</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P19483">UniProt: P19483</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P32876">UniProt: P32876</a>

<span class="expr-badge">Bos taurus</span>

## Overview

The bovine mitochondrial F-ATPase (ATP synthase) c8-ring is part of the membrane-embedded rotor of the enzyme that drives ATP synthesis using the transmembrane proton-motive force. The structure of the bovine F1-c-ring complex was determined at 3.5 A resolution, revealing that the c-ring contains 8 c-subunits (c8-ring). This is the first c-ring structure from a higher eukaryote, establishing that vertebrate F-ATPases contain c8-rings and require 2.7 protons per ATP synthesised (or 3.7 total including transport costs).

## Publications

### doi/10.1073##pnas.1011099107

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a></td>
      <td>3.5</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Bovine F1-c-ring subcomplex (F1 domain alpha3beta3gamma + c8-ring)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a>, Mg2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine heart mitochondria (native source)
- **Construct**: Native F1Fo-ATPase purified from bovine heart mitochondria; F1-c-ring subcomplex prepared by [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/)

**Purification:**

- **Expression construct**: Native F1Fo-ATPase from bovine heart mitochondria
- **Tag info**: Purified via IF1(1-60) affinity column (residues 1-60 of F1-ATPase inhibitor protein IF1)

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
      <td>Purification of F1Fo-ATPase</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IF1(1-60) affinity column</td>
      <td>20 mM Tris-HCl pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM ADP, 2 mM MgSO4, 0.02% NaN3 + 20 mM N-dodecyl-N,N-(dimethylammonio)butyrate</td>
      <td>Purified from bovine heart mitochondria</td>
    </tr>
    <tr>
      <td>F1-c-ring subcomplex preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>HiTrap Q HP</td>
      <td>20 mM Tris-HCl pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM ADP, 2 mM MgSO4, 0.02% NaN3 + 0.95 mM n-tridecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/tridecylmaltoside/">TDM</a>)</td>
      <td>Eluted with 0-1 M NaCl gradient, complex eluted at 0.35-0.40 mM NaCl. Pooled fractions dialyzed against buffer with 0.95 mM <a href="/xray-mp-wiki/reagents/detergents/tridecylmaltoside/">TDM</a> and concentrated to 22 mg/mL on Vivaspin Q mini H spin column.</td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/mL in 20 mM Tris-HCl pH 8.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM ADP, 2 mM MgSO4, 0.02% NaN3, 5.7 mM [TDM](/xray-mp-wiki/reagents/detergents/tridecylmaltoside/), 1 mM [AMP-PNP](/xray-mp-wiki/reagents/ligands/amp-pnp/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Microbatch under oil</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bovine F1-c-ring complex at 10 mg/mL with 5.7 mM <a href="/xray-mp-wiki/reagents/detergents/tridecylmaltoside/">TDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14-16.5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4600, 100 mM Hepes pH 7.0, 50 mM K2HPO4 pH 7.0</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>2 uL protein + 2 uL reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>23 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>42 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>50 mM Hepes pH 7.0, 25 mM K2HPO4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested and analyzed by SDS-PAGE confirmed all subunits of F1-c-ring complex present and undegraded. Four crystals were harvested, washed three times in buffer, dissolved and analyzed.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>microbatch</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>23 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 14-16.5 % [precipitant] (PEG 4600)  
- Hepes: 100 mM [buffer]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSSGLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKARRRVGLKAPGIIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RISVREPMQTGIKAVDSLVPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYFR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETELFYKGIRPAINVGLSVSRVGSAA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKLEPSKITKFENAFLSHVISQHQALLGKIRTDGKISEESDAKLK</span></span>
<span class="topo-ruler">       490  </span>
<span class="topo-line"><span class="topo-inside">EIVTNFLAGFEA</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>492</td>
      <td>19</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSSGLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKARRRVGLKAPGIIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RISVREPMQTGIKAVDSLVPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYFR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETELFYKGIRPAINVGLSVSRVGSAA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKLEPSKITKFENAFLSHVISQHQALLGKIRTDGKISEESDAKLK</span></span>
<span class="topo-ruler">       490  </span>
<span class="topo-line"><span class="topo-inside">EIVTNFLAGFEA</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>492</td>
      <td>19</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADTSVDLEETGRVLSIGDGIARVHGLRNVQAEEMVEFSSGLKGMSLNLEPDNVGVVVFGNDKLIKEGDIVKRTGAIVDVPVGEELLGRVVDALGNAIDGKGPIGSKARRRVGLKAPGIIP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RISVREPMQTGIKAVDSLVPIGRGQRELIIGDRQTGKTSIAIDTIINQKRFNDGTDEKKKLYCIYVAIGQKRSTVAQLVKRLTDADAMKYTIVVSATASDAAPLQYLAPYSGCSMGEYFR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DNGKHALIIYDDLSKQAVAYRQMSLLLRRPPGREAYPGDVFYLHSRLLERAAKMNDAFGGGSLTALPVIETQAGDVSAYIPTNVISITDGQIFLETELFYKGIRPAINVGLSVSRVGSAA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QTRAMKQVAGTMKLELAQYREVAAFAQFGSDLDAATQQLLSRGVRLTELLKQGQYSPMAIEEQVAVIYAGVRGYLDKLEPSKITKFENAFLSHVISQHQALLGKIRTDGKISEESDAKLK</span></span>
<span class="topo-ruler">       490  </span>
<span class="topo-line"><span class="topo-inside">EIVTNFLAGFEA</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>492</td>
      <td>19</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">TTGRIVAVIGAVVDVQFDEGLPPILNALEVQGRETRLVLEVAQHLGESTVRTIAMDGTEGLVRGQKVLDSGAPIRIPVGPETLGRIMNVIGEPIDERGPIKTKQFAAIHAEAPEFVEMSV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EQEILVTGIKVVDLLAPYAKGGKIGLFGGAGVGKTVLIMELINNVAKAHGGYSVFAGVGERTREGNDLYHEMIESGVINLKDATSKVALVYGQMNEPPGARARVALTGLTVAEYFRDQEG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QDVLLFIDNIFRFTQAGSEVSALLGRIPSAVGYQPTLATDMGTMQERITTTKKGSITSVQAIYVPADDLTDPAPATTFAHLDATTVLSRAIAELGIYPAVDPLDSTSRIMDPNIVGSEHY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       </span>
<span class="topo-line"><span class="topo-inside">DVARGVQKILQDYKSLQDIIAILGMDELSEEDKLTVSRARKIQRFLSQPFQVAEVFTGHLGKLVPLKETIKGFQQILAGEYDHLPEQAFYMVGPIEEAVAKADKLAE</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>467</td>
      <td>9</td>
      <td>475</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">TTGRIVAVIGAVVDVQFDEGLPPILNALEVQGRETRLVLEVAQHLGESTVRTIAMDGTEGLVRGQKVLDSGAPIRIPVGPETLGRIMNVIGEPIDERGPIKTKQFAAIHAEAPEFVEMSV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EQEILVTGIKVVDLLAPYAKGGKIGLFGGAGVGKTVLIMELINNVAKAHGGYSVFAGVGERTREGNDLYHEMIESGVINLKDATSKVALVYGQMNEPPGARARVALTGLTVAEYFRDQEG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QDVLLFIDNIFRFTQAGSEVSALLGRIPSAVGYQPTLATDMGTMQERITTTKKGSITSVQAIYVPADDLTDPAPATTFAHLDATTVLSRAIAELGIYPAVDPLDSTSRIMDPNIVGSEHY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       </span>
<span class="topo-line"><span class="topo-inside">DVARGVQKILQDYKSLQDIIAILGMDELSEEDKLTVSRARKIQRFLSQPFQVAEVFTGHLGKLVPLKETIKGFQQILAGEYDHLPEQAFYMVGPIEEAVAKADKLA</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>466</td>
      <td>9</td>
      <td>474</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>467</td>
      <td>475</td>
      <td>475</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">TTGRIVAVIGAVVDVQFDEGLPPILNALEVQGRETRLVLEVAQHLGESTVRTIAMDGTEGLVRGQKVLDSGAPIRIPVGPETLGRIMNVIGEPIDERGPIKTKQFAAIHAEAPEFVEMSV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EQEILVTGIKVVDLLAPYAKGGKIGLFGGAGVGKTVLIMELINNVAKAHGGYSVFAGVGERTREGNDLYHEMIESGVINLKDATSKVALVYGQMNEPPGARARVALTGLTVAEYFRDQEG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QDVLLFIDNIFRFTQAGSEVSALLGRIPSAVGYQPTLATDMGTMQERITTTKKGSITSVQAIYVPADDLTDPAPATTFAHLDATTVLSRAIAELGIYPAVDPLDSTSRIMDPNIVGSEHY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       </span>
<span class="topo-line"><span class="topo-inside">DVARGVQKILQDYKSLQDIIAILGMDELSEEDKLTVSRARKIQRFLSQPFQVAEVFTGHLGKLVPLKETIKGFQQILAGEYDHLPEQAFYMVGPIEEAVAKADKLA</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>466</td>
      <td>9</td>
      <td>474</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>467</td>
      <td>475</td>
      <td>475</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ATLKDITRRLKSIKNIQKITKSMKMVAAAKYARAERELKPARVYGVGSLALYEKADIKTPE</span><span class="topo-unknown">DKKKH</span><span class="topo-inside">LIIGVSSDRGLCGAIHSSVAKQMKSEAANL</span><span class="topo-unknown">AAAG</span><span class="topo-inside">KEVKIIGVGDKIRSILHRTH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SDQFLVTFKEVGRRPPTFGDASVIALELLNSGYEFDEGSIIFNRFRSVISYKTEEKPIFSLDTISSAESMSIYDDIDADVLRNYQEYSLANIIYYSLKESTTSEQSARMTAMDNASKNAS</span></span>
<span class="topo-ruler">       250       260       270  </span>
<span class="topo-line"><span class="topo-inside">EMIDKLTLTFNRTRQAVITKELIEIISGAAAL</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>61</td>
      <td>1</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>66</td>
      <td>62</td>
      <td>66</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>96</td>
      <td>67</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>100</td>
      <td>97</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>272</td>
      <td>101</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">QMSFTFASPTQVFFNSANVRQVDVPTQTGAFGILAAHVPTLQVLRPGLVVVHAEDGTTSKYFVSSGSVTVNADSSVQLLAEEAVTLDMLDLGAAKANLEKAQSELLGAADEATRAEIQIR</span></span>
<span class="topo-ruler">       130 </span>
<span class="topo-line"><span class="topo-inside">IEANEALVKAL</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>131</td>
      <td>15</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain I (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40       </span>
<span class="topo-line"><span class="topo-inside">VAYWRQAGLSYIRYSQICAKAVRDALKTEFKANAMKTSGSTIKIVKV</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>47</td>
      <td>1</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain J (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAAT</span><span class="topo-membrane">VGVAGSGAGIGTV</span><span class="topo-inside">FGSLIIGYARNPSLKQQLFSYAI</span><span class="topo-membrane">LGFALSEAMGLFCL</span><span class="topo-outside">MVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>27</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>50</td>
      <td>29</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>64</td>
      <td>52</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>72</td>
      <td>66</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain K (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAAT</span><span class="topo-membrane">VGVAGSGAGIGTVF</span><span class="topo-inside">GSLIIGYARNPSLKQQLFSYA</span><span class="topo-membrane">ILGFALSEAMGLFCL</span><span class="topo-outside">MVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>28</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>49</td>
      <td>30</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>64</td>
      <td>51</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>72</td>
      <td>66</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAATV</span><span class="topo-membrane">GVAGSGAGIGTVF</span><span class="topo-inside">GSLIIGYARNPSLKQQLFSYA</span><span class="topo-membrane">ILGFALSEAMGLFC</span><span class="topo-outside">LMVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>17</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>49</td>
      <td>30</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>63</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>72</td>
      <td>65</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain M (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAATV</span><span class="topo-membrane">GVAGSGAGIGTVFG</span><span class="topo-inside">SLIIGYARNPSLKQQLFSY</span><span class="topo-membrane">AILGFALSEAMGLFC</span><span class="topo-outside">LMVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>48</td>
      <td>31</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>63</td>
      <td>50</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>72</td>
      <td>65</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain N (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAATV</span><span class="topo-membrane">GVAGSGAGIGTVFG</span><span class="topo-inside">SLIIGYARNPSLKQQLFSY</span><span class="topo-membrane">AILGFALSEAMGLF</span><span class="topo-outside">CLMVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>29</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>48</td>
      <td>31</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>62</td>
      <td>50</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>72</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain O (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAATV</span><span class="topo-membrane">GVAGSGAGIGTVF</span><span class="topo-inside">GSLIIGYARNPSLKQQLFSY</span><span class="topo-membrane">AILGFALSEAMGLF</span><span class="topo-outside">CLMVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>17</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>30</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>62</td>
      <td>50</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>72</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain P (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAAT</span><span class="topo-membrane">VGVAGSGAGIGTVF</span><span class="topo-inside">GSLIIGYARNPSLKQQLFSYA</span><span class="topo-membrane">ILGFALSEAMGLFCL</span><span class="topo-outside">MVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>28</td>
      <td>16</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>49</td>
      <td>30</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>64</td>
      <td>51</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>72</td>
      <td>66</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2xnd">2XND</a> — Chain Q (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70  </span>
<span class="topo-line"><span class="topo-outside">IDTAAKFIGAGAAT</span><span class="topo-membrane">VGVAGSGAGIGTV</span><span class="topo-inside">FGSLIIGYARNPSLKQQLFSYAI</span><span class="topo-membrane">LGFALSEAMGLFCL</span><span class="topo-outside">MVAFLILF</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>27</td>
      <td>16</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>50</td>
      <td>29</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>64</td>
      <td>52</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>72</td>
      <td>66</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### c8-ring stoichiometry in vertebrates

The bovine F-ATPase c-ring contains 8 c-subunits, establishing the first c-ring structure from a higher eukaryote. This contrasts with fungal (c10 in S. cerevisiae), eubacterial (c10-c15 in I. tartaricus), and plant chloroplast (c14 in S. oleracea) rings. The c-subunit sequences are nearly identical across vertebrates and highly conserved in invertebrates, suggesting c8-rings are universal in ~50,000 vertebrate species and many of the ~2 million invertebrate species.

### Bioenergetic cost of ATP synthesis

With a c8-ring, each 360 degree rotation of the central stalk (producing 3 ATP) requires 8 protons (one per c-subunit glutamate). Therefore 8/3 = 2.67 protons per ATP. Including the electrogenic exchange of ATP for ADP by the ADP/ATP translocase (one charge) and the electroneutral phosphate/proton symport (one proton) adds one more proton, giving a total of 3.7 protons per ATP exported to the cytoplasm. The P/O ratio is 10/3.7 = 2.7 for NADH and 6/3.7 = 1.6 for [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/), close to experimental values of 2.5 and 1.5.

### Cardiolipin binding and c8-ring stabilization

The c8-ring has eight trimethylated Lys43 residues that likely mark binding sites for [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/), an abundant inner mitochondrial membrane lipid with no head group. Unlike larger rings (c10+), the c8-ring outer ring has gaps between C-terminal alpha-helices that expose the inner ring to the lipid bilayer. Each bound [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) with two acyl side chains could help strengthen the c8-ring by cross-linking adjacent c-subunits. The Lys43 trimethylation is conserved across Animalia.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase</a> — Catalytic domain of the same ATP synthase complex
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Cardiolipin binds c8-ring external surface and stabilizes the ring structure
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/">F1-ATPase Rotary Catalytic Mechanism</a> — Rotary mechanism of ATP synthesis coupled to proton flow through c-ring
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/symmetry-mismatch-rotary-motor/">Symmetry Mismatch in Rotary Motors</a> — Mismatch between c8-ring (8-fold) and catalytic domain (3-fold) symmetry
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/rotary-atpase-mechanism/">Rotary ATPase Mechanism</a> — Broader rotary catalysis mechanism context
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/tridecylmaltoside/">TDM</a> — Detergent used in purification or crystallization
