---
title: "Thermus thermophilus SecDF Protein Translocation Motor"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09980, doi/10.1016##j.str.2018.01.002, doi/10.1016##j.celrep.2017.04.030]
verified: regex
uniprot_id: ['Q5SKE6', 'Q9RTE3']
---

# Thermus thermophilus SecDF Protein Translocation Motor

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SKE6">UniProt: Q5SKE6</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9RTE3">UniProt: Q9RTE3</a>

<span class="expr-badge">Deinococcus radiodurans str. R1</span>

## Overview

SecDF is a membrane protein belonging to the resistance-nodulation-division (RND) superfamily that enhances protein translocation at the extracytoplasmic side of the bacterial membrane using a proton gradient. It operates as part of the Sec translocon complex, working alongside SecA ATPase and the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) channel to drive protein export. The first X-ray crystal structure of full-length SecDF from Thermus thermophilus was determined at 3.3 A resolution (Tsukazaki et al., 2011, PDB 3AQP), revealing 12 transmembrane helices with flexible extracytoplasmic domains (P1-base, P1-head, and P4) and establishing that SecDF is the smallest known motor protein of the RND family. The protein undergoes dramatic conformational transitions between beta-sheet and beta-barrel architectures in its extracellular region, driven by remote coupling between the transmembrane proton transport pathway and the extracytoplasmic domains.


## Publications

### doi/10.1038##nature09980

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3aqp">3AQP</a></td>
      <td>3.3</td>
      <td>P43</td>
      <td>Full-length Thermus thermophilus SecDF (residues 2-515 and 522-726); expressed in E. coli</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecDF(1-735)-His10 from plasmid pTV118N; based on NCBI Reference sequence Gene ID 3168575

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
      <td>Cell lysis and membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a></td>
      <td>None</td>
      <td>Not specified + Not specified</td>
      <td><a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> cells expressing TtSecDF-<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6</a> were disrupted by passage through a <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a>ure cell</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Agarose</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a>ged SecDF purified from <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> membrane fraction in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final purification step for crystallization trials</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TtSecDF in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> at ~10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>28% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.5 M NaCl, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>PDB 3AQP; F form (original conformation); data collected at SPring-8 BL41XU and PF NW12; refined in space group P43 (pseudo-symmetry from P43212) with 2 molecules per ASU; 50-3.3 A resolution; Rwork/Rfree 0.298/0.319; zonal scaling procedure used to improve electron density; structure includes residues 2-515 and 522-726</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3aqp">3AQP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DRKNLTSL</span><span class="topo-membrane">FLLGVFLLALLFVWK</span><span class="topo-inside">PWAPEEPKVRLGLDLKGGLRIVLEADVENPTLDDLEKARTVLENRINALGVAEPLIQIQGQKRIVVELPGLSQADQDRALKLIGQRAVLEFRIVKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GATGTTVAQINQALRENPRLNREELEKDLIKPEDLGPPLLTGADLADARAVFDQFGRPQVSLTFTPEGAKKFEEVTRQNIGKRLAIVLDGRVYTAPVIRQAITGGQAVIEGLSSVEEASE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IALVLRSGSLPVPLKVAEIRAIGPTLGQDAIQA</span><span class="topo-membrane">GIRSALIGTLAIFLLI</span><span class="topo-outside">FAYYGPHLGLVA</span><span class="topo-membrane">SLGLLYTSALILGLLSGL</span><span class="topo-inside">GATLTLP</span><span class="topo-membrane">GIAGLVLTLGAAVDGN</span><span class="topo-outside">VLSFERIKEELRAGKKLR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">QAIPEGFRHSTLTI</span><span class="topo-membrane">MDVNIAHLLAAAALYQY</span><span class="topo-inside">ATGPVR</span><span class="topo-membrane">GFAVILAIGVVASVFSN</span><span class="topo-outside">LVFSRHLLERLADRGEIRPPMWLVDPRFNFMGPARYV</span><span class="topo-membrane">TAATLLLAALAAGVVFA</span><span class="topo-inside">KGFNYSIDFTGG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TAYTLRAEPNVEVETLRRFLEEKGFPGKEAVITQV</span><span class="topo-unknown">QAPTAA</span><span class="topo-inside">YREFLVKLPPLSDERRLELERLFASELKATVLASETVGPAIGEELRRNA</span><span class="topo-membrane">VMAVLVGLGLILLYVAF</span><span class="topo-outside">RFDWTFG</span><span class="topo-membrane">VASILA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">VAHDVAIVAGMYSLL</span><span class="topo-inside">GLEFSIP</span><span class="topo-membrane">TIAALLTIVGYSINDS</span><span class="topo-outside">IVVSDRIRENQKLLRHLPYAELVNRSINQTLSRTVM</span><span class="topo-membrane">TSLTTLLPILALLFLG</span><span class="topo-inside">GSVL</span><span class="topo-membrane">RDFALAIFVGIFVGTYSS</span><span class="topo-unknown">IYVVSALV</span></span>
<span class="topo-ruler">       730       740 </span>
<span class="topo-line"><span class="topo-unknown">VAWKN</span><span class="topo-outside">R</span><span class="topo-unknown">RKAQEASKAHHHHHH</span></span>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>9</td>
      <td>2</td>
      <td>9</td>
      <td>Outside</td>
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
      <td>273</td>
      <td>25</td>
      <td>273</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>289</td>
      <td>274</td>
      <td>289</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>301</td>
      <td>290</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>319</td>
      <td>302</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>326</td>
      <td>320</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>342</td>
      <td>327</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>374</td>
      <td>343</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>391</td>
      <td>375</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>397</td>
      <td>392</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>414</td>
      <td>398</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>451</td>
      <td>415</td>
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
      <td>515</td>
      <td>469</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>521</td>
      <td>516</td>
      <td>521</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>522</td>
      <td>570</td>
      <td>522</td>
      <td>570</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>571</td>
      <td>587</td>
      <td>571</td>
      <td>587</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>588</td>
      <td>594</td>
      <td>588</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>595</td>
      <td>615</td>
      <td>595</td>
      <td>615</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>616</td>
      <td>622</td>
      <td>616</td>
      <td>622</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>623</td>
      <td>638</td>
      <td>623</td>
      <td>638</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>674</td>
      <td>639</td>
      <td>674</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>675</td>
      <td>690</td>
      <td>675</td>
      <td>690</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>691</td>
      <td>694</td>
      <td>691</td>
      <td>694</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>712</td>
      <td>695</td>
      <td>712</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>713</td>
      <td>725</td>
      <td>713</td>
      <td>725</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>726</td>
      <td>726</td>
      <td>726</td>
      <td>726</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>741</td>
      <td>727</td>
      <td>741</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2018.01.002

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5yhf">5YHF</a></td>
      <td>2.8</td>
      <td>P1</td>
      <td>Thermus thermophilus SecDF residues 1-735 with C-terminal His10 tag; expressed in E. coli BL21(DE3)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecDF(1-735)-His10 from plasmid pTV118N; based on NCBI Reference sequence Gene ID 3168575

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
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Agarose</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His10-tagged SecDF purified from <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> membrane fraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Not specified</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> buffer + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final sample in 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified SecDF mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> at 1:1 ratio (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>5YHF; Super F form; helical data collection at SPring-8 BL32XU; 1.0 A wavelength; space group P1; 44.1-2.8 A resolution (shell 2.9-2.8 A); Rwork/Rfree 0.202/0.236; 734 protein residues; 5790 non-hydrogen atoms; 132 ligand atoms; 27 solvent molecules</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5yhf">5YHF</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DRKN</span><span class="topo-membrane">LTSLFLLGVFLLALLFV</span><span class="topo-inside">WKPWAPEEPKVRLGLDLKGGLRIVLEADVENPTLDDLEKARTVLENRINALGVAEPLIQIQGQKRIVVELPGLSQADQDRALKLIGQRAVLEFRIVKE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GATGTTVAQINQALRENPRLNREELEKDLIKPEDLGPPLLTGADLADARAVFDQFGRPQVSLTFTPEGAKKFEEVTRQNIGKRLAIVLDGRVYTAPVIRQAITGGQAVIEGLSSVEEASE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IALVLRSGSLPVPLKVAEIRAIGPTLGQDAIQAGIR</span><span class="topo-membrane">SALIGTLAIFLLIFA</span><span class="topo-outside">YYGPHLG</span><span class="topo-membrane">LVASLGLLYTSALILGLLSGL</span><span class="topo-inside">GATLTLP</span><span class="topo-membrane">GIAGLVLTLGAAVDGN</span><span class="topo-outside">VLSFERIKEELRAGKKLR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">QAIPEGFRHSTLTI</span><span class="topo-membrane">MDVNIAHLLAAAALYQYA</span><span class="topo-inside">TGPV</span><span class="topo-membrane">RGFAVILAIGVVASVFSNLVFS</span><span class="topo-outside">RHLLERLADRGEIRPPMWLVDPRFNFMGPARYVTAA</span><span class="topo-membrane">TLLLAALAAGVVFAKG</span><span class="topo-inside">FNYSIDFTGG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TAYTLRAEPNVEVETLRRFLEEKGFPGKEAVITQVQAPTAAYREFLVKLPPLSDERRLELERLFASELKATVLASETVGPAIGEELRRN</span><span class="topo-membrane">AVMAVLVGLGLILLYV</span><span class="topo-outside">AFRFDWTFGVAS</span><span class="topo-membrane">ILA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">VAHDVAIVAGMYSLLGL</span><span class="topo-inside">EFSIP</span><span class="topo-membrane">TIAALLTIVGYSINDS</span><span class="topo-outside">IVVSDRIRENQKLLRHLPYAELVNRSINQTLSRTV</span><span class="topo-membrane">MTSLTTLLPILALLFLG</span><span class="topo-inside">GSVLR</span><span class="topo-membrane">DFALAIFVGIFVGTYS</span><span class="topo-outside">SIYVVSALV</span></span>
<span class="topo-ruler">       730       740 </span>
<span class="topo-line"><span class="topo-outside">VAWKNRRKAQEASKA</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>22</td>
      <td>6</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>276</td>
      <td>23</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>298</td>
      <td>292</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>319</td>
      <td>299</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>326</td>
      <td>320</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>342</td>
      <td>327</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>374</td>
      <td>343</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>375</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>396</td>
      <td>393</td>
      <td>396</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>418</td>
      <td>397</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>454</td>
      <td>419</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>470</td>
      <td>455</td>
      <td>470</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>569</td>
      <td>471</td>
      <td>569</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>570</td>
      <td>585</td>
      <td>570</td>
      <td>585</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>586</td>
      <td>597</td>
      <td>586</td>
      <td>597</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>617</td>
      <td>598</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>618</td>
      <td>622</td>
      <td>618</td>
      <td>622</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>623</td>
      <td>638</td>
      <td>623</td>
      <td>638</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>673</td>
      <td>639</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>690</td>
      <td>674</td>
      <td>690</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>691</td>
      <td>695</td>
      <td>691</td>
      <td>695</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>696</td>
      <td>711</td>
      <td>696</td>
      <td>711</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>712</td>
      <td>735</td>
      <td>712</td>
      <td>735</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>736</td>
      <td>741</td>
      <td>736</td>
      <td>741</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.celrep.2017.04.030

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xam">5XAM</a></td>
      <td>2.6</td>
      <td>P2_12_12_1</td>
      <td>Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolA molecule</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xan">5XAN</a></td>
      <td>2.8</td>
      <td>P2_12_12_1</td>
      <td>Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolB molecule</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> fragment (O-(CCO)4) modeled in P1-head cavity</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xap">5XAP</a></td>
      <td>2.6</td>
      <td>C2</td>
      <td>Thermus thermophilus SecDF(Met-28-768)-His6 with I143C/L268C mutations; expressed in E. coli BL21(DE3); MolC molecule</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecDF(1-735)-His10 from plasmid pTV118N; based on NCBI Reference sequence Gene ID 3168575

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
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Agarose</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>DrSecDF(Met-28-768)-<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6</a> purified from <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> membrane fraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Not specified</td>
      <td>100 mM NH4NO3, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5 + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final sample in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for crystallization trials</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified SecDF with I143C/L268C mutations at ~10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>28% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 0.5 M NaCl (for P2_12_12_1 crystals) or 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 200, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 6.6, 0.1 M Li2SO4 (for C2 crystals)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K for X-ray data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>PDB 5XAM, 5XAN, 5XAP; I form crystals; data collected at SPring-8 BL32XU; 1.0 A wavelength; 5XAM (MolA, P2_12_12_1, 2.6 A, Rwork/Rfree 0.188/0.228); 5XAN (MolB, P2_12_12_1, 2.8 A, tunnel-containing conformation); 5XAP (MolC, C2, 2.6 A, Rwork/Rfree 0.189/0.224)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xam">5XAM</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-outside">RPNPWT</span><span class="topo-membrane">ALLLLLTLLGSLLYIWRP</span><span class="topo-inside">WEHKNDPWSLWNDQYQFMTLGLDLKGGLRIELAPESGTATRDELDRVKTVIENRINALGVAEPTVTVSGGKRVVVEIPGATPAVQDRARSIIQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TARLEFRIVNSDAKPDPAVREKNPRSSGYTLAQLGPVVATGETIADATSGTDQRSGQWVVNFKTTDAGAKTFGDFTGKNV</span><span class="topo-unknown">NR</span><span class="topo-inside">LMAVVLDDQIQSVATINQRLFRDIQISGNFTPEEASQL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ALVLKSGALPIKIVTAAERSIGPSLGADAIRSG</span><span class="topo-membrane">AIAALVGIGLVFVMLFAY</span><span class="topo-outside">YGLWFG</span><span class="topo-membrane">LVGALGLLFSSIIILGILGGF</span><span class="topo-inside">GATLTLP</span><span class="topo-membrane">GIAGLVLTIGAAVDGNV</span><span class="topo-outside">ISFERIKEELARGKGIKN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIGAGYEHSTAAI</span><span class="topo-membrane">LDVNASHLLSALALYNY</span><span class="topo-inside">STGAV</span><span class="topo-membrane">KGFAVTLIIGVIASTFSNLVFA</span><span class="topo-outside">KWFMQWLAQRRPNMSAPQWIKHTHFDFMKPAKV</span><span class="topo-membrane">ITTLSVLLALAGAALVATR</span><span class="topo-inside">GLNYGVDFAPG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TTLTARVDRQVTTEQLRNSVIGAGVSKVTGQSATI</span><span class="topo-unknown">Q</span><span class="topo-inside">RDTTPGQQGQNFTVKVPELNDAEVKQIGAAIGKLPQGQVLASETVGPAVGKELTQKT</span><span class="topo-membrane">IYAVLLGLGLILVYVGFR</span><span class="topo-outside">FDFIMG</span><span class="topo-membrane">LGS</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">IIAAIHDVAIAMGLFSLL</span><span class="topo-inside">GLEFTVAS</span><span class="topo-membrane">VAALLTLIGYSLNDSII</span><span class="topo-outside">VSDRIRENMKTMRGHSYREIVNAAINQTLSRT</span><span class="topo-membrane">VMTSVSTMLPLISLLIF</span><span class="topo-inside">GGPVL</span><span class="topo-membrane">RDFSLILLVGILVGTYSSIYI</span><span class="topo-outside">VA</span></span>
<span class="topo-ruler">       730       740       750</span>
<span class="topo-line"><span class="topo-outside">PLVVYFEEWRDK</span><span class="topo-unknown">NRAAKPVTNSHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>3</td>
      <td>8</td>
      <td>29</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>35</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>200</td>
      <td>53</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>273</td>
      <td>229</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>291</td>
      <td>300</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>297</td>
      <td>318</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>324</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>345</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>342</td>
      <td>352</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>373</td>
      <td>369</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>390</td>
      <td>400</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>395</td>
      <td>417</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>417</td>
      <td>422</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>450</td>
      <td>444</td>
      <td>476</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>469</td>
      <td>477</td>
      <td>495</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>470</td>
      <td>515</td>
      <td>496</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>573</td>
      <td>543</td>
      <td>599</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>574</td>
      <td>591</td>
      <td>600</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>597</td>
      <td>618</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>618</td>
      <td>624</td>
      <td>644</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>619</td>
      <td>626</td>
      <td>645</td>
      <td>652</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>643</td>
      <td>653</td>
      <td>669</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>644</td>
      <td>675</td>
      <td>670</td>
      <td>701</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>676</td>
      <td>692</td>
      <td>702</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>693</td>
      <td>697</td>
      <td>719</td>
      <td>723</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>698</td>
      <td>718</td>
      <td>724</td>
      <td>744</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>719</td>
      <td>732</td>
      <td>745</td>
      <td>758</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xan">5XAN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSR</span><span class="topo-outside">PNPW</span><span class="topo-membrane">TALLLLLTLLGSLLYIW</span><span class="topo-inside">RPWEHKNDPWSLWNDQYQFMTLGLDLKGGLRIELAPESGTATRDELDRVKTVIENRINALGVAEPTVTVSGGKRVVVEIPGATPAVQDRARSCIQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TARLEFRIVNSDAKPDPAVREKNPRSSGYTLAQLGPVVATGETIADATSGTDQRSGQWVVNFKTTDAGAKTFGDFTGKNVNRLMAVVLDDQIQSVATINQRLFRDIQISGNFTPEEASQL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ACVLKSGALPIKIVTAAERSIGPSLGADAIRSGAI</span><span class="topo-membrane">AALVGIGLVFVMLFA</span><span class="topo-outside">YYGLWFG</span><span class="topo-membrane">LVGALGLLFSSIIILGIL</span><span class="topo-inside">GGFGATLTLPGIA</span><span class="topo-membrane">GLVLTIGAAVDGN</span><span class="topo-outside">VISFERIKEELARGKGIKN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIGAGYEHSTAAI</span><span class="topo-membrane">LDVNASHLLSALALY</span><span class="topo-inside">NYSTGAVKGF</span><span class="topo-membrane">AVTLIIGVIASTFSNLVFA</span><span class="topo-outside">KWFMQWLAQRRPNMSAPQWIKHTHFDFMKPAKV</span><span class="topo-membrane">ITTLSVLLALAGAALV</span><span class="topo-inside">ATRGLNYGVDFAPG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TTLTARVDRQVTTEQLRNSVIGAGVSKVTGQSATIQRDTTPGQQGQNFTVKVPELNDAEVKQIGAAIGKLPQGQVLASETVGPAVGKELTQKTIYA</span><span class="topo-membrane">VLLGLGLILVYVGFR</span><span class="topo-outside">FDFIMG</span><span class="topo-membrane">LGS</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">IIAAIHDVAIAMGLF</span><span class="topo-inside">SLLGLEFTVASV</span><span class="topo-membrane">AALLTLIGYSLNDS</span><span class="topo-outside">IIVSDRIRENMKTMRGHSYREIVNAAINQTLSRT</span><span class="topo-membrane">VMTSVSTMLPLISLLIF</span><span class="topo-inside">GGPVLRDF</span><span class="topo-membrane">SLILLVGILVGTYSS</span><span class="topo-outside">IYI</span><span class="topo-unknown">VA</span></span>
<span class="topo-ruler">       730       740       750</span>
<span class="topo-line"><span class="topo-unknown">PLVVYFEEWR</span><span class="topo-outside">D</span><span class="topo-unknown">KNRAAKPVTNSHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>4</td>
      <td>7</td>
      <td>30</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>275</td>
      <td>51</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>290</td>
      <td>302</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>297</td>
      <td>317</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>315</td>
      <td>324</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>328</td>
      <td>342</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>341</td>
      <td>355</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>373</td>
      <td>368</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>388</td>
      <td>400</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>398</td>
      <td>415</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>417</td>
      <td>425</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>450</td>
      <td>444</td>
      <td>476</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>466</td>
      <td>477</td>
      <td>492</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>576</td>
      <td>493</td>
      <td>602</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>577</td>
      <td>591</td>
      <td>603</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>597</td>
      <td>618</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>615</td>
      <td>624</td>
      <td>641</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>616</td>
      <td>627</td>
      <td>642</td>
      <td>653</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>641</td>
      <td>654</td>
      <td>667</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>642</td>
      <td>675</td>
      <td>668</td>
      <td>701</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>676</td>
      <td>692</td>
      <td>702</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>693</td>
      <td>700</td>
      <td>719</td>
      <td>726</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>701</td>
      <td>715</td>
      <td>727</td>
      <td>741</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>716</td>
      <td>718</td>
      <td>742</td>
      <td>744</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>719</td>
      <td>730</td>
      <td>745</td>
      <td>756</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>731</td>
      <td>731</td>
      <td>757</td>
      <td>757</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xan">5XAN</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">SRPNPW</span><span class="topo-membrane">TALLLLLTLLGSLLYI</span><span class="topo-inside">WRPWEHKNDPWSLWNDQYQFMTLGLDLKGGLRIELAPESGTATRDELDRVKTVIENRINALGVAEPTVTVSGGKRVVVEIPGATPAVQDRARSCIQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TARLEFRIVNSDAKPDPAVREKNPRSSGYTLAQLGPVVATGETIADATSGTDQRSGQWVVNFKTTDAGAKTFGDFTGKNVNRLMAVVLDDQIQSVATINQRLFRDIQISGNFTPEEASQL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ACVLKSGALPIKIVTAAERSIGPSLGADAIRSGAI</span><span class="topo-membrane">AALVGIGLVFVMLF</span><span class="topo-outside">AYYGLWFG</span><span class="topo-membrane">LVGALGLLFSSIIILGIL</span><span class="topo-inside">GGFGATLTLPGIA</span><span class="topo-membrane">GLVLTIGAAVDGN</span><span class="topo-outside">VISFERIKEELARGKGIKN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AIGAGYEHSTAAI</span><span class="topo-membrane">LDVNASHLLSALAL</span><span class="topo-inside">YNYSTGAVKGF</span><span class="topo-membrane">AVTLIIGVIASTFSNLVFA</span><span class="topo-outside">KWFMQWLAQRRPNMSAPQWIKHTHFDFMKPAKVI</span><span class="topo-membrane">TTLSVLLALAGAALVA</span><span class="topo-inside">TRGLNYGVDFAPG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">TTLTARVDRQVTTEQLRNSVIGAGVSKVTGQSATIQRDTTPGQQGQNFTVKVPELNDAEVKQIGAAIGKLPQGQVLASETVGPAVGKELTQKTIYA</span><span class="topo-membrane">VLLGLGLILVYVGFR</span><span class="topo-outside">FDFIMG</span><span class="topo-membrane">LGS</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">IIAAIHDVAIAMGLF</span><span class="topo-inside">SLLGLEFTVASV</span><span class="topo-membrane">AALLTLIGYSLNDSI</span><span class="topo-outside">IVSDRIRENMKTMRGHSYREIVNAAINQTLSRTV</span><span class="topo-membrane">MTSVSTMLPLISLLIF</span><span class="topo-inside">GGPVLRDF</span><span class="topo-membrane">SLILLVGILVGTYSS</span><span class="topo-outside">IYIVA</span></span>
<span class="topo-ruler">       730       740       750</span>
<span class="topo-line"><span class="topo-outside">PLVVYFEEWRDKNR</span><span class="topo-unknown">AAKPVTNSHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>7</td>
      <td>28</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>23</td>
      <td>34</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>275</td>
      <td>50</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>302</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>297</td>
      <td>316</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>315</td>
      <td>324</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>328</td>
      <td>342</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>341</td>
      <td>355</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>373</td>
      <td>368</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>400</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>398</td>
      <td>414</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>417</td>
      <td>425</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>451</td>
      <td>444</td>
      <td>477</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>467</td>
      <td>478</td>
      <td>493</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>468</td>
      <td>576</td>
      <td>494</td>
      <td>602</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>577</td>
      <td>591</td>
      <td>603</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>597</td>
      <td>618</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>615</td>
      <td>624</td>
      <td>641</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>616</td>
      <td>627</td>
      <td>642</td>
      <td>653</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>642</td>
      <td>654</td>
      <td>668</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>643</td>
      <td>676</td>
      <td>669</td>
      <td>702</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>677</td>
      <td>692</td>
      <td>703</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>693</td>
      <td>700</td>
      <td>719</td>
      <td>726</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>701</td>
      <td>715</td>
      <td>727</td>
      <td>741</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>716</td>
      <td>734</td>
      <td>742</td>
      <td>760</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xap">5XAP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-inside">RPNPWT</span><span class="topo-membrane">ALLLLLTLLGSLLYIW</span><span class="topo-outside">RPWEHKNDPWSLWNDQYQFMTLGLDLKGGLRIELAPESGTATRDELDRVKTVIENRINALGVAEPTVTVSGGKRVVVEIPGATPAVQDRARSCIQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TARLEFRIVNSDAKPDPAVREKNPRSSGYTLAQLGPVVATGETIADATSGTDQRSGQWVVNFKTTDAGAKTFGDFTGKNVNRLMAVVLDDQIQSVATINQRLFRDIQISGNFTPEEASQL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ACVLKSGALPIKIVTAAERSIGPSLGADAIRSG</span><span class="topo-membrane">AIAALVGIGLVFVMLF</span><span class="topo-inside">AYYGLWFGL</span><span class="topo-membrane">VGALGLLFSSIIILGILGG</span><span class="topo-outside">FGATLTLPG</span><span class="topo-membrane">IAGLVLTIGAAVDGN</span><span class="topo-inside">VISFERIKEELARGKGIKN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">AIGAGYEHSTAAI</span><span class="topo-membrane">LDVNASHLLSALALYN</span><span class="topo-outside">YSTGAVKGF</span><span class="topo-membrane">AVTLIIGVIASTFSNLVFA</span><span class="topo-inside">KWFMQWLAQRRPNMSAPQWIKHTHFDFMKPAKVI</span><span class="topo-membrane">TTLSVLLALAGAALVA</span><span class="topo-outside">TRGLNYGVDFAPG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">TTLTARVDRQVTTEQLRNSVIGAGVSKVTGQSATIQRDTTPGQQGQNFTVKVPELNDAEVKQIGAAIGKLPQGQVLASETVGPAVGKELTQKTIYA</span><span class="topo-membrane">VLLGLGLILVYVGFR</span><span class="topo-inside">FDFIMG</span><span class="topo-membrane">LGS</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">IIAAIHDVAIAMGLFSLL</span><span class="topo-outside">GLEFTVASV</span><span class="topo-membrane">AALLTLIGYSLNDSI</span><span class="topo-inside">IVSDRIRENMKTMRGHSYREIVNAAINQTLSRTV</span><span class="topo-membrane">MTSVSTMLPLISLLIF</span><span class="topo-outside">GGPVLR</span><span class="topo-membrane">DFSLILLVGILVGTYSS</span><span class="topo-inside">IYIVA</span></span>
<span class="topo-ruler">       730       740       750</span>
<span class="topo-line"><span class="topo-inside">PLVVYFEEWRDKNR</span><span class="topo-unknown">AAKPVTNSHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>3</td>
      <td>8</td>
      <td>29</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>24</td>
      <td>35</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>273</td>
      <td>51</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>289</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>298</td>
      <td>316</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>317</td>
      <td>325</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>326</td>
      <td>344</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>341</td>
      <td>353</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>373</td>
      <td>368</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>389</td>
      <td>400</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>398</td>
      <td>416</td>
      <td>424</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>417</td>
      <td>425</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>451</td>
      <td>444</td>
      <td>477</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>467</td>
      <td>478</td>
      <td>493</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>468</td>
      <td>576</td>
      <td>494</td>
      <td>602</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>577</td>
      <td>591</td>
      <td>603</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>597</td>
      <td>618</td>
      <td>623</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>618</td>
      <td>624</td>
      <td>644</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>619</td>
      <td>627</td>
      <td>645</td>
      <td>653</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>642</td>
      <td>654</td>
      <td>668</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>643</td>
      <td>676</td>
      <td>669</td>
      <td>702</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>677</td>
      <td>692</td>
      <td>703</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>693</td>
      <td>698</td>
      <td>719</td>
      <td>724</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>699</td>
      <td>715</td>
      <td>725</td>
      <td>741</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>716</td>
      <td>734</td>
      <td>742</td>
      <td>760</td>
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

### First crystal structure of full-length SecDF reveals F-form architecture

The first X-ray crystal structure of full-length SecDF from T. thermophilus was determined at 3.3 A resolution (Tsukazaki et al., 2011, PDB 3AQP), revealing 12 transmembrane helices arranged in a pseudo-symmetrical RND transporter fold. The structure showed two large periplasmic domains (P1, comprising head and base subdomains; P4) connected by flexible linkers. The P1 domain was also solved separately at 2.6 A by X-ray crystallography and the P4 domain by NMR, enabling accurate model building of the full-length structure. The structure established SecDF as the smallest known motor protein of the RND family and provided the first structural framework for understanding how SecDF uses proton motive force to drive protein translocation.

### I-form structures reveal tunnel formation in the transmembrane region

The crystal structures of SecDF in the I form (PDB 5XAM, 5XAN, 5XAP) at 2.6-2.8 A resolution revealed a novel penetrating tunnel through the transmembrane region in the MolB conformation (5XAN). This tunnel is formed by an approximately 4 A shift of TM5 relative to other I-form molecules (MolA, MolC) and the F form. The tunnel center exhibits a negative electrostatic potential arising from the conserved essential Asp365 residue. MD simulations showed that deprotonation of Asp365 attracts water molecules from the cytoplasmic bulk phase, leading to outward TM5 shift and tunnel formation. The conserved Tyr662 residue, whose side chain fluctuates between orientations observed in MolA vs MolB/MolC, is essential for providing sufficient space for tunnel formation. These findings demonstrate that the I-form tunnel functions as a proton pathway, with water molecules forming single-file hydrogen-bonded chains through the tunnel when Asp365 is deprotonated.

### P1-head cavity captures substrate peptides during translocation

The I-form structures revealed a cavity in the P1-head domain that interacts with a polyethylene glycol molecule (modeled as O-(CCO)4 in the 5XAN structure), potentially mimicking a substrate peptide. The P1-head cavity in the I form is larger than in the F form, suggesting that the I form holds substrates more stably. Site-directed photo-crosslinking experiments with pBPA confirmed that the P1-head cavity interacts with translocating polypeptides, supporting a model where the P1-head captures the emerging polypeptide from the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon during protein translocation.

### Super-membrane-facing (Super F) form reveals beta-barrel architecture

The crystal structure of SecDF (PDB 5YHF) reveals a novel conformation termed the Super-membrane-facing (Super F) form, in which the extracytoplasmic P1-base and P4 domains adopt a beta-barrel architecture instead of the beta-sheet structure seen in the previously reported F form (PDB 3AQP) and I form structures. This drastic structural transition represents the most extreme conformational change observed in SecDF to date.

### Remote coupling mechanism links proton transport to conformational transitions

The Super F form structure reveals a conserved salt bridge between Asp340 in transmembrane helix 4 (TM4) and Arg671 in transmembrane helix 10 (TM10), with their C-alpha-C-alpha distance reduced from 12.9 A in the F form to 2.6 A in the Super F form.

### Conserved transmembrane regions D1, D5, F1, and F2 transmit structural changes

Comparison of the F form and Super F form structures reveals that highly conserved regions D1, D5, F1, and F2 play an important role in transmitting structural changes from the transmembrane region to the extracytoplasmic side.

### SecDF functions as a proton-activated protein translocation motor

The original 2011 study demonstrated that SecDF conducts protons through its transmembrane region, with conserved charged residues Asp340 and Arg671 being essential for proton transport. Patch-clamp analysis of TtSecDF-containing spheroplasts showed a slope conductance of approximately 102 pS at -60 mV, corresponding to a flow of 4.2 x 10^7 protons per second. The P1 domain was shown to bind unfolded proteins (casein) in a dose-dependent manner, confirming its role in capturing emerging preproteins from the [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) translocon.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — SecDF operates at the extracytoplasmic side of the SecYEG channel to pull precursor proteins during translocation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/">RND Efflux Pumps</a> — SecDF belongs to the RND superfamily; structural insights into remote coupling mechanism
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid used for LCP crystallization of SecDF (PDB 5YHF)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for SecDF Super F form structure determination
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
