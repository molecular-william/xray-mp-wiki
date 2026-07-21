---
title: "DeCLIC (Desulfofustis deltaproteobacterium Pentameric Ligand-Gated Ion Channel)"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1922701117]
verified: agent
uniprot_id: V4JF97
---

# DeCLIC (Desulfofustis deltaproteobacterium Pentameric Ligand-Gated Ion Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/V4JF97">UniProt: V4JF97</a>

<span class="expr-badge">Uncultured desulfofustis sp. PB-SRB1</span>

## Overview

DeCLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from a Desulfofustis deltaproteobacterium (closely related to Desulfofustis glycolicus), identified through a BLAST search on [Stelic](/xray-mp-wiki/proteins/cys-loop-receptors/stelic/). It is a multidomain pLGIC that incorporates a large periplasmic amino-terminal domain (NTD) accounting for approximately 50% of the total receptor mass. The NTD consists of two jelly-roll domains (NTD1, NTD2) that interact across each subunit interface. X-ray structures were determined in two conformational states: a Ca2+-bound closed-pore state at 3.55 A (PDB 6V45) and a Ca2+-free wide-open pore state at 3.83 A (PDB 6V4A). The NTD1 domain was also solved independently at 1.75 A (PDB 6V4B). DeCLIC is inhibited by extracellular Ca2+ (IC50 ~90 uM) and conducts currents upon Ca2+ depletion in Xenopus oocytes that are insensitive to quaternary ammonium blockers. The structures illustrate dramatic conformational state transitions and diverse regulatory mechanisms available to pLGICs, particularly involving Ca2+ modulation and periplasmic NTDs.


## Publications

### doi/10.1073##pnas.1922701117

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6v45">6V45</a></td>
      <td>3.55</td>
      <td>Not specified</td>
      <td>Full-length DeCLIC in Ca2+-bound closed-pore conformation</td>
      <td>Ca2+ (five symmetry-related Ca2+ ions at LBD subunit interfaces)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a></td>
      <td>3.83</td>
      <td>Not specified</td>
      <td>Full-length DeCLIC in Ca2+-free wide-open pore conformation</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6v4b">6V4B</a></td>
      <td>1.75</td>
      <td>Not specified</td>
      <td>DeCLIC NTD1 domain (residues 34-202), SeMet-labeled</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: Full-length DeCLIC expressed as fusion with [Maltose](/xray-mp-wiki/reagents/additives/maltose/) binding protein (MBP) in C43 E. coli, solubilized, cleaved, and purified in n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/))
- **Notes**: A soluble NTD fragment (residues 33-202) was also expressed for independent crystallization and structure determination using SeMet SAD phasing.


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
      <td>Protein expression</td>
      <td>Full-length DeCLIC expressed as MBP fusion in C43 E. coli. Soluble NTD fragment (residues 33-202) expressed separately.
</td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td>MBP fusion enabled solubilization and purification of full-length DeCLIC</td>
    </tr>
    <tr>
      <td>Solubilization and purification</td>
      <td>Standard <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization following protocols for other prokaryotic pLGICs</td>
      <td>Not specified</td>
      <td>Not specified + n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Full-length DeCLIC purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified DeCLIC in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>250 mM Ca2+ (for Ca2+-bound form); no Ca2+ (for Ca2+-free form)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified (extensive seeding and systematic screening required)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial hits with 250 mM Ca2+. Extensive seeding and systematic screening required for diffracting crystals. NTD1 fragment crystals grew from independent crystallization setup. Ba2+ anomalous datasets confirmed Ca2+ binding sites. Data collected at synchrotron sources.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHNLQQLLPTRSLIWIFSFLTSISIWCTVAHAETE</span><span class="topo-outside">GRVQHFTGYIEDGRGIFYSLPDMKQGDIIYASMQNTGGNLDPLVGIMAEEIDPAVSLGQVLEKALASENDLISELTAVADRIFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDDDGGKGYSASLEFTIPRDGTYHIFAGSTITNQRLDKFQPTYTTGSFQLILGLNAPQVISGEGEPEGEVFASLA</span><span class="topo-unknown">SLE</span><span class="topo-outside">IKPEAHVQELEIRLDKDTRYLTQHTRNLQPGDTFHALVEPIG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EAPLPRLRLTDSGGKPLAFGLIDQPGESVELNYTCDQDICELVVHVDGTDGQKDSGEAVYRLLVGINAPNL</span><span class="topo-unknown">RESGQTPVG</span><span class="topo-outside">SSVFLESDLVTVGLAVDQIVGVDQRSENFSVVGTLKLSWH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DPKLGFSPDQCGCTVKSFEDASIRAVAGEINLPLPSFSFYNQQGNRWSQNQVIFVTPDGRASYFERFTVTLQAPDFDFLAYPFDRQKFSIKVDLAVPTNMFIFNEIERFQQVVGDQLGEE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">EWVVTSYSQEITEVPFERGSTNSRFTTTLLVKRNLEYYI</span><span class="topo-membrane">LRIFVPLFLIISVSWVIF</span><span class="topo-inside">FLKDYGRQL</span><span class="topo-membrane">EVASGNLLVFVAFNFTI</span><span class="topo-outside">SGDLPRLGYLTV</span><span class="topo-membrane">LDRFMIVSFCLTAIVVLI</span><span class="topo-inside">SVCQKRL</span></span>
<span class="topo-ruler">       610       620       630       640  </span>
<span class="topo-line"><span class="topo-inside">GAVGKQAVAAQIDTWV</span><span class="topo-membrane">LVIYPLVYSLYIIWVYLR</span><span class="topo-outside">FF</span><span class="topo-unknown">TDHIGW</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>36</td>
      <td>195</td>
      <td>36</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>311</td>
      <td>199</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>519</td>
      <td>321</td>
      <td>519</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>537</td>
      <td>520</td>
      <td>537</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>538</td>
      <td>546</td>
      <td>538</td>
      <td>546</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>547</td>
      <td>563</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>575</td>
      <td>564</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>576</td>
      <td>593</td>
      <td>576</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>594</td>
      <td>616</td>
      <td>594</td>
      <td>616</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>617</td>
      <td>634</td>
      <td>617</td>
      <td>634</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>635</td>
      <td>636</td>
      <td>635</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHNLQQLLPTRSLIWIFSFLTSISIWCTVAHAETE</span><span class="topo-outside">GRVQHFTGYIEDGRGIFYSLPDMKQGDIIYASMQNTGGNLDPLVGIMAEEIDPAVSLGQVLEKALASENDLISELTAVADRIFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDDDGGKGYSASLEFTIPRDGTYHIFAGSTITNQRLDKFQPTYTTGSFQLILGLNAPQVISGEGEPEGEVFASLA</span><span class="topo-unknown">SLEI</span><span class="topo-outside">KPEAHVQELEIRLDKDTRYLTQHTRNLQPGDTFHALVEPIG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EAPLPRLRLTDSGGKPLAFGLIDQPGESVELNYTCDQDICELVVHVDGTDGQKDSGEAVYRLLVGINAPNLRESG</span><span class="topo-unknown">QTPVG</span><span class="topo-outside">SSVFLESDLVTVGLAVDQIVGVDQRSENFSVVGTLKLSWH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DPKLGFSPDQCGCTVKSFEDASIRAVAGEINLPLPSFSFYNQQGNRWSQNQVIFVTPDGRASYFERFTVTLQAPDFDFLAYPFDRQKFSIKVDLAVPTNMFIFNEIERFQQVVGDQLGEE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">EWVVTSYSQEITEVPFERGSTNSRFTTTLLVKRNLEYYI</span><span class="topo-membrane">LRIFVPLFLIISVSWVIF</span><span class="topo-inside">FLKDYGRQL</span><span class="topo-membrane">EVASGNLLVFVAFNFTI</span><span class="topo-outside">SGDLPRLGYLTV</span><span class="topo-membrane">LDRFMIVSFCLTAIVVLIS</span><span class="topo-inside">VCQKRL</span></span>
<span class="topo-ruler">       610       620       630       640  </span>
<span class="topo-line"><span class="topo-inside">GAVGKQAVAAQIDTWV</span><span class="topo-membrane">LVIYPLVYSLYIIWVYLR</span><span class="topo-outside">FF</span><span class="topo-unknown">TDHIGW</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>36</td>
      <td>195</td>
      <td>36</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>315</td>
      <td>200</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>519</td>
      <td>321</td>
      <td>519</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>537</td>
      <td>520</td>
      <td>537</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>538</td>
      <td>546</td>
      <td>538</td>
      <td>546</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>547</td>
      <td>563</td>
      <td>547</td>
      <td>563</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>575</td>
      <td>564</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>576</td>
      <td>594</td>
      <td>576</td>
      <td>594</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>595</td>
      <td>616</td>
      <td>595</td>
      <td>616</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>617</td>
      <td>634</td>
      <td>617</td>
      <td>634</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>635</td>
      <td>636</td>
      <td>635</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHNLQQLLPTRSLIWIFSFLTSISIWCTVAHAETE</span><span class="topo-outside">GRVQHFTGYIEDGRGIFYSLPDMKQGDIIYASMQNTGGNLDPLVGIMAEEIDPAVSLGQVLEKALASENDLISELTAVADRIFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDDDGGKGYSASLEFTIPRDGTYHIFAGSTITNQRLDKFQPTYTTGSFQLILGLNAPQVISGEGEPEGEVFASLA</span><span class="topo-unknown">SLEI</span><span class="topo-outside">KPEAHVQELEIRLDKDTRYLTQHTRNLQPGDTFHALVEPIG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EAPLPRLRLTDSGGKPLAFGLIDQPGESVELNYTCDQDICELVVHVDGTDGQKDSGEAVYRLLVGINAPNLRESG</span><span class="topo-unknown">QTPVG</span><span class="topo-outside">SSVFLESDLVTVGLAVDQIVGVDQRSENFSVVGTLKLSWH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DPKLGFSPDQCGCTVKSFEDASIRAVAGEINLPLPSFSFYNQQGNRWSQNQVIFVTPDGRASYFERFTVTLQAPDFDFLAYPFDRQKFSIKVDLAVPTNMFIFNEIERFQQVVGDQLGEE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">EWVVTSYSQEITEVPFERGSTNSRFTTTLLVKRNLEYYI</span><span class="topo-membrane">LRIFVPLFLIISVSWVIFF</span><span class="topo-inside">LKDYGRQ</span><span class="topo-membrane">LEVASGNLLVFVAFNFTI</span><span class="topo-outside">SGDLPRLGYLTVLD</span><span class="topo-membrane">RFMIVSFCLTAIVVLISV</span><span class="topo-inside">CQKRL</span></span>
<span class="topo-ruler">       610       620       630       640  </span>
<span class="topo-line"><span class="topo-inside">GAVGKQAVAAQI</span><span class="topo-membrane">DTWVLVIYPLVYSLYIIWV</span><span class="topo-outside">YLRFF</span><span class="topo-unknown">TDHIGW</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>36</td>
      <td>195</td>
      <td>36</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>315</td>
      <td>200</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>519</td>
      <td>321</td>
      <td>519</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>538</td>
      <td>520</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>539</td>
      <td>545</td>
      <td>539</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>563</td>
      <td>546</td>
      <td>563</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>564</td>
      <td>577</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>578</td>
      <td>595</td>
      <td>578</td>
      <td>595</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>596</td>
      <td>612</td>
      <td>596</td>
      <td>612</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>613</td>
      <td>631</td>
      <td>613</td>
      <td>631</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>632</td>
      <td>636</td>
      <td>632</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHNLQQLLPTRSLIWIFSFLTSISIWCTVAHAETE</span><span class="topo-outside">GRVQHFTGYIEDGRGIFYSLPDMKQGDIIYASMQNTGGNLDPLVGIMAEEIDPAVSLGQVLEKALASENDLISELTAVADRIFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDDDGGKGYSASLEFTIPRDGTYHIFAGSTITNQRLDKFQPTYTTGSFQLILGLNAPQVISGEGEPEGEVFASLA</span><span class="topo-unknown">SLE</span><span class="topo-outside">IKPEAHVQELEIRLDKDTRYLTQHTRNLQPGDTFHALVEPIG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EAPLPRLRLTDSGGKPLAFGLIDQPGESVELNYTCDQDICELVVHVDGTDGQKDSGEAVYRLLVGINAPNLRESG</span><span class="topo-unknown">QTPVG</span><span class="topo-outside">SSVFLESDLVTVGLAVDQIVGVDQRSENFSVVGTLKLSWH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DPKLGFSPDQCGCTVKSFEDASIRAVAGEINLPLPSFSFYNQQGNRWSQNQVIFVTPDGRASYFERFTVTLQAPDFDFLAYPFDRQKFSIKVDLAVPTNMFIFNEIERFQQVVGDQLGEE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">EWVVTSYSQEITEVPFERGSTNSRFTTTLLVKRNLEYYILR</span><span class="topo-membrane">IFVPLFLIISVSWVIFFL</span><span class="topo-inside">KDYGRQ</span><span class="topo-membrane">LEVASGNLLVFVAFNFTI</span><span class="topo-outside">SGDLPRLGYLTVLDR</span><span class="topo-membrane">FMIVSFCLTAIVVLISVC</span><span class="topo-inside">QKRL</span></span>
<span class="topo-ruler">       610       620       630       640  </span>
<span class="topo-line"><span class="topo-inside">GAVGKQAVAAQI</span><span class="topo-membrane">DTWVLVIYPLVYSLYIIW</span><span class="topo-outside">VYLRFF</span><span class="topo-unknown">TDHIGW</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>36</td>
      <td>195</td>
      <td>36</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>315</td>
      <td>199</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>521</td>
      <td>321</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>522</td>
      <td>539</td>
      <td>522</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>540</td>
      <td>545</td>
      <td>540</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>563</td>
      <td>546</td>
      <td>563</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>578</td>
      <td>564</td>
      <td>578</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>579</td>
      <td>596</td>
      <td>579</td>
      <td>596</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>597</td>
      <td>612</td>
      <td>597</td>
      <td>612</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>613</td>
      <td>630</td>
      <td>613</td>
      <td>630</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>631</td>
      <td>636</td>
      <td>631</td>
      <td>636</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v4a">6V4A</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHNLQQLLPTRSLIWIFSFLTSISIWCTVAHAETE</span><span class="topo-outside">GRVQHFTGYIEDGRGIFYSLPDMKQGDIIYASMQNTGGNLDPLVGIMAEEIDPAVSLGQVLEKALASENDLISELTAVADRIFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDDDGGKGYSASLEFTIPRDGTYHIFAGSTITNQRLDKFQPTYTTGSFQLILGLNAPQVISGEGEPEGEVFASLA</span><span class="topo-unknown">SLE</span><span class="topo-outside">IKPEAHVQELEIRLDKDTRYLTQHTRNLQPGDTFHALVEPIG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EAPLPRLRLTDSGGKPLAFGLIDQPGESVELNYTCDQDICELVVHVDGTDGQKDSGEAVYRLLVGINAPNL</span><span class="topo-unknown">RESGQTPVG</span><span class="topo-outside">SSVFLESDLVTVGLAVDQIVGVDQRSENFSVVGTLKLSWH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DPKLGFSPDQCGCTVKSFEDASIRAVAGEINLPLPSFSFYNQQGNRWSQNQVIFVTPDGRASYFERFTVTLQAPDFDFLAYPFDRQKFSIKVDLAVPTNMFIFNEIERFQQVVGDQLGEE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">EWVVTSYSQEITEVPFERGSTNSRFTTTLLVKRNLEYYIL</span><span class="topo-membrane">RIFVPLFLIISVSWVIFFL</span><span class="topo-inside">KDYGRQ</span><span class="topo-membrane">LEVASGNLLVFVAFNFTI</span><span class="topo-outside">SGDLPRLGYLTVL</span><span class="topo-membrane">DRFMIVSFCLTAIVVLIS</span><span class="topo-inside">VCQKRL</span></span>
<span class="topo-ruler">       610       620       630       640  </span>
<span class="topo-line"><span class="topo-inside">GAVGKQAVAAQID</span><span class="topo-membrane">TWVLVIYPLVYSLYIIWVY</span><span class="topo-outside">LRFF</span><span class="topo-unknown">TDHIGW</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>36</td>
      <td>195</td>
      <td>36</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>311</td>
      <td>199</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>520</td>
      <td>321</td>
      <td>520</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>539</td>
      <td>521</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>540</td>
      <td>545</td>
      <td>540</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>563</td>
      <td>546</td>
      <td>563</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>564</td>
      <td>576</td>
      <td>564</td>
      <td>576</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>577</td>
      <td>594</td>
      <td>577</td>
      <td>594</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>595</td>
      <td>613</td>
      <td>595</td>
      <td>613</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>614</td>
      <td>632</td>
      <td>614</td>
      <td>632</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>633</td>
      <td>636</td>
      <td>633</td>
      <td>636</td>
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

### Ca2+-dependent gating mechanism

DeCLIC is inhibited by extracellular Ca2+ with IC50 ~90 uM. Ca2+ binds at the LBD subunit interface coordinated by E347 (beta1-beta2 loop), D437 and backbone carbonyls P434, P436 (Pro-loop), and E479 (complementary loop F). Upon Ca2+ depletion, loop F swings inward 8 A toward the channel axis, disrupting the Ca2+-mediated intersubunit contacts. A conserved electrostatic network between the F, beta1-beta2, and Pro-loops, homologous to the pH-sensing network in [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/), reorganizes to form intrasubunit contacts (Q344/E481), liberating arginines (R345, R569) that orient toward expanded TMD subunit interfaces to facilitate intercalation of lipid head groups.

### Multidomain allosteric transitions

DeCLIC exhibits state-dependent conformational changes across all three domains. The NTD undergoes radial contraction upon Ca2+ depletion, bringing NTD2 beta''1-beta''2 loops into proximity with LBD loop C (near the orthosteric agonist-binding site). The LBD exhibits domain contraction with decreased center-of-mass distance between adjacent subunits, and the amphipathic alpha1 helix translates and rotates ~40 degrees counter-clockwise toward the channel axis. The TMD exhibits outward twist and blooming with increased intersubunit distances, relieving all three hydrophobic constriction gates to create a wide-open pore.

### Reclassification of ELIC as 'locally closed' conformation

Based on the DeCLIC structures, the authors reclassify the previous structure of bacterial [Elic](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) (the first high-resolution pLGIC structure) as a 'locally closed' conformation rather than a fully closed state. ELIC's pore aligns closely with Ca2+-bound DeCLIC, including hydrophobic constrictions at 16' and 9' positions. [Elic](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) has been crystallized under numerous conditions but always in a nonconducting state, consistent with reclassification as a locally closed conformation that does not fully represent the resting state.

### Normal mode analysis of allosteric coupling

Torsional normal mode analysis predicted atomic fluctuations correlating well with B-factors (correlation factors 0.94 and 0.88 for closed and open states). A limited set of normal modes described 80% of the torsional component of both gating transitions. The analysis revealed that the vestibular site shows the largest couplings among all functional sites (orthosteric, vestibular, and pore), consistent with a role in allosteric modulation. Directionality and coordination couplings decreased in the open state while deformation coupling increased, consistent with the closed-to-open transition.


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related prokaryotic pLGIC; reclassified as 'locally closed' conformation based on DeCLIC structures
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/stelic/">sTeLIC (Tevnia jerichonana Endosymbiont Pentameric Ligand-Gated Ion Channel)</a> — Related prokaryotic pLGIC; DeCLIC identified via BLAST search on sTeLIC
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC (Gloeobacter violaceus Pentameric Ligand-Gated Ion Channel)</a> — Related prokaryotic pLGIC; gating mechanism compared in functional analysis
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/">Cys-Loop Receptor Family</a> — pLGIC family classification; DeCLIC is a prokaryotic Cys-loop receptor homolog
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/hydrophobic-gating/">Hydrophobic Gating</a> — Pore constriction gates at F16' and L9' positions controlled by hydrophobic residues
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Referenced in context related to Maltose
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in context related to DDM
