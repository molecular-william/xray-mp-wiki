---
title: "Transient Receptor Potential Vanilloid 2 (TRPV2)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0059-z]
verified: agent
uniprot_id: G1SNM3
---

# Transient Receptor Potential Vanilloid 2 (TRPV2)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G1SNM3">UniProt: G1SNM3</a>

<span class="expr-badge">Oryctolagus cuniculus</span>

## Overview

TRPV2 is a transient receptor potential vanilloid channel belonging to the TRPV subfamily of TRP channels. Unlike the highly Ca²⁺-selective [Epithelial Calcium Channel TRPV5](/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/)/TRPV6, TRPV2 is a non-selective cation channel that is activated by heat, cannabinoids, and 2-aminoethoxydiphenyl borate (2-APB). TRPV2 forms a domain-swapped homotetramer where each subunit comprises six transmembrane helices (S1-S6) with the voltage-sensor-like domain (S1-S4) interacting with the pore domain (S5-S6) of the neighboring protomer. The channel possesses two activation gates: one at the selectivity filter (SF gate) and another at the S6 helical bundle crossing (common gate). Crystal structures of rabbit TRPV2 reveal that [Resiniferatoxin (RTx)](/xray-mp-wiki/reagents/ligands/resiniferatoxin/) binding induces a two-fold symmetric opening of the selectivity filter gate wide enough for permeation of large organic cations.


## Publications

### doi/10.1038##s41594-018-0059-z

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bwj">6BWJ</a></td>
      <td>3.1 A</td>
      <td>P 2 2_1 2_1</td>
      <td>Rabbit miTRPV2_QM (minimal TRPV2 construct with quadruple mutations F470S, L505M, L508T, Q528E), residues 57-561 and 583-722, C-terminal FLAG affinity tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/resiniferatoxin/">Resiniferatoxin (RTx)</a> and Ca²⁺</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bwm">6BWM</a></td>
      <td>3.9 A</td>
      <td>P 2 2_1 2_1</td>
      <td>Rabbit miTRPV2 (minimal construct), residues 57-561 and 583-722, C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a></td>
      <td>Ca²⁺</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells, Bac-to-Bac baculovirus system
- **Construct**: Codon-optimized gene for full-length rabbit TRPV2. Minimal construct miTRPV2 (residues 57-561 and 583-722) cloned into pFastBac vector with C-terminal FLAG affinity tag. Quadruple mutant miTRPV2_QM (F470S, L505M, L508T, Q528E) used for RTx-sensitive crystallization. Selenomethionine-labeled protein expressed in ESF 921 Delta Series methionine-deficient Sf9 media.


**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: miTRPV2, C-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

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
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">CaCl₂</a>, 1 µg/ml leupeptin, 1.5 µg/ml pepstatin, 0.84 µg/ml aprotinin, 0.3 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 14.3 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">β-Mercaptoethanol</a>, DNAseI + --</td>
      <td>3 × 30 pulses</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>Buffer A supplemented with 40 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and 4 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 40 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 4 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>1 hour at 4°C. Insoluble material removed by centrifugation (8,000g, 30 min).</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> resin</td>
      <td><a href="/xray-mp-wiki/reagents/antibodies/anti-flag/">Anti-FLAG</a> resin</td>
      <td>Buffer B (50 mM TRIS pH 8, 150 mM NaCl, 2 mM CaCl₂, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>) + 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Wash with Buffer B, elute with Buffer C containing 0.1 mg/ml <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> cleavage</td>
      <td>--</td>
      <td>50 mM TRIS pH 8, 150 mM NaCl, 2 mM CaCl₂, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 3 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Overnight incubation at 4°C with <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> and 3 mM TCEP</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superose-6/">Superose 6</a> column (GE Healthcare)</td>
      <td>-- + --</td>
      <td>Protein peak collected and concentrated to 8-10 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>miTRPV2 at 8-10 mg/ml in buffer supplemented with 5 mM TCEP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200-400 mM CaCl₂, 15-25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, pH 7-9</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Up to 2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained in many conditions. Best diffracting crystals grew in 200-400 mM CaCl₂, 15-25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> at pH 7-9. miTRPV2_QM+RTx protein was supplemented with 300 µM RTx and 5 mM TCEP before crystallization. Data from multiple crystals merged using BLEND.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>miTRPV2_QM at 8-10 mg/ml supplemented with 300 µM RTx and 5 mM TCEP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200-400 mM CaCl₂, 15-25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, pH 7-9</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Up to 2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>miTRPV2_QM extracted with 20 mM <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> and 2 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> in presence of 2 µM RTx. Purified in buffers containing 2 mM <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>, 0.2 mM <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/dmpc/">DMPC</a>, 2 µM RTx.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwj">6BWJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQPD</span><span class="topo-inside">LNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVAY</span><span class="topo-outside">HQ</span><span class="topo-unknown">PALEKQGFPPLKAT</span><span class="topo-outside">AGNSMLLL</span><span class="topo-membrane">GHILILLGGVYLLLGQLWYF</span><span class="topo-inside">WRRRLFIWISFMDSY</span><span class="topo-membrane">SEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVLC</span><span class="topo-outside">FLAIEW</span><span class="topo-membrane">YLPLLVSSLVMGWTNLLYYTR</span><span class="topo-inside">GFQHTGIYSVMIEKVILRD</span><span class="topo-membrane">LLRFLLVYLVFLFGFAVALVSL</span><span class="topo-outside">SR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEA</span><span class="topo-outside">PPYRS</span><span class="topo-unknown">ILDASLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGM</span><span class="topo-outside">G</span><span class="topo-unknown">ELAFQEQ</span><span class="topo-outside">LRFRG</span><span class="topo-membrane">VVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>68</td>
      <td>2</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>388</td>
      <td>70</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>409</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>411</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>425</td>
      <td>413</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>433</td>
      <td>427</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>453</td>
      <td>435</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>468</td>
      <td>455</td>
      <td>469</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>487</td>
      <td>470</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>493</td>
      <td>489</td>
      <td>494</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>514</td>
      <td>495</td>
      <td>515</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>533</td>
      <td>516</td>
      <td>534</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>534</td>
      <td>555</td>
      <td>535</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>557</td>
      <td>557</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>584</td>
      <td>559</td>
      <td>585</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>589</td>
      <td>586</td>
      <td>590</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>604</td>
      <td>591</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>605</td>
      <td>605</td>
      <td>606</td>
      <td>606</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>606</td>
      <td>612</td>
      <td>607</td>
      <td>613</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>613</td>
      <td>617</td>
      <td>614</td>
      <td>618</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>638</td>
      <td>619</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>726</td>
      <td>640</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwj">6BWJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQPDL</span><span class="topo-inside">NRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIPRFC</span><span class="topo-membrane">FNFLCYLVYMLIFTAVAYHQ</span><span class="topo-outside">PALE</span><span class="topo-unknown">KQGFPPLKAT</span><span class="topo-outside">AGNS</span><span class="topo-membrane">MLLLGHILILLGGVYLLLGQL</span><span class="topo-inside">WYFWRRRLFIWISFMDSY</span><span class="topo-membrane">SEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVLCFL</span><span class="topo-outside">AIEW</span><span class="topo-membrane">YLPLLVSSLVMGWTNLLYYT</span><span class="topo-inside">RGFQHTGIYSVMIEKV</span><span class="topo-membrane">ILRDLLRFLLVYLVFLFGFAVAL</span><span class="topo-outside">VSLSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEA</span><span class="topo-outside">PPYRSILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGMGE</span><span class="topo-outside">LAFQE</span><span class="topo-unknown">QLR</span><span class="topo-outside">FRGV</span><span class="topo-membrane">VLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>69</td>
      <td>2</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>391</td>
      <td>71</td>
      <td>392</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>411</td>
      <td>393</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>415</td>
      <td>413</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>425</td>
      <td>417</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>429</td>
      <td>427</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>450</td>
      <td>431</td>
      <td>451</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>451</td>
      <td>468</td>
      <td>452</td>
      <td>469</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>470</td>
      <td>490</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>493</td>
      <td>491</td>
      <td>494</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>513</td>
      <td>495</td>
      <td>514</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>514</td>
      <td>529</td>
      <td>515</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>552</td>
      <td>531</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>553</td>
      <td>557</td>
      <td>554</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>584</td>
      <td>559</td>
      <td>585</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>593</td>
      <td>586</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>606</td>
      <td>595</td>
      <td>607</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>607</td>
      <td>611</td>
      <td>608</td>
      <td>612</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>612</td>
      <td>614</td>
      <td>613</td>
      <td>615</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>615</td>
      <td>618</td>
      <td>616</td>
      <td>619</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>619</td>
      <td>638</td>
      <td>620</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>726</td>
      <td>640</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwj">6BWJ</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQPD</span><span class="topo-inside">LNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVA</span><span class="topo-outside">YHQ</span><span class="topo-unknown">PALEKQGFPPLKAT</span><span class="topo-outside">AGNSMLLLG</span><span class="topo-membrane">HILILLGGVYLLLGQLWYFWR</span><span class="topo-inside">RRLFIWISFMDS</span><span class="topo-membrane">YSEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQV</span><span class="topo-outside">LCFLAIEWYLP</span><span class="topo-membrane">LLVSSLVMGWTNLLYYTRG</span><span class="topo-inside">FQHTGIY</span><span class="topo-membrane">SVMIEKVILRDLLRFLLVYLVFLFGFAVAL</span><span class="topo-outside">VSLSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEA</span><span class="topo-outside">PPYRSILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGM</span><span class="topo-outside">G</span><span class="topo-unknown">ELAFQEQ</span><span class="topo-outside">LRFRGV</span><span class="topo-membrane">VLLLLLAYVLLTYVLLLNMLI</span><span class="topo-inside">ALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>68</td>
      <td>2</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>388</td>
      <td>70</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>408</td>
      <td>390</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>411</td>
      <td>410</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>425</td>
      <td>413</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>434</td>
      <td>427</td>
      <td>435</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>455</td>
      <td>436</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>467</td>
      <td>457</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>485</td>
      <td>469</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>496</td>
      <td>487</td>
      <td>497</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>515</td>
      <td>498</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>516</td>
      <td>522</td>
      <td>517</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>552</td>
      <td>524</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>553</td>
      <td>557</td>
      <td>554</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>584</td>
      <td>559</td>
      <td>585</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>593</td>
      <td>586</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>604</td>
      <td>595</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>605</td>
      <td>605</td>
      <td>606</td>
      <td>606</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>606</td>
      <td>612</td>
      <td>607</td>
      <td>613</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>613</td>
      <td>618</td>
      <td>614</td>
      <td>619</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>619</td>
      <td>639</td>
      <td>620</td>
      <td>640</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>640</td>
      <td>726</td>
      <td>641</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwj">6BWJ</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQPDL</span><span class="topo-inside">NRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVA</span><span class="topo-outside">YHQPALE</span><span class="topo-unknown">KQGFPPLKAT</span><span class="topo-outside">AGNSMLLL</span><span class="topo-membrane">GHILILLGGVYLLLGQLWYFW</span><span class="topo-inside">RRRLFIWISFMDS</span><span class="topo-membrane">YSEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVL</span><span class="topo-outside">CFLAIEWYLP</span><span class="topo-membrane">LLVSSLVMGWTNLLYYTRG</span><span class="topo-inside">FQHTGIY</span><span class="topo-membrane">SVMIEKVILRDLLRFLLVYLVFLFGFAVALV</span><span class="topo-outside">SLSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEA</span><span class="topo-outside">PPYRSILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGMGEL</span><span class="topo-outside">AFQE</span><span class="topo-unknown">QLR</span><span class="topo-outside">FRG</span><span class="topo-membrane">VVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>69</td>
      <td>2</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>388</td>
      <td>71</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>408</td>
      <td>390</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>410</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>425</td>
      <td>417</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>433</td>
      <td>427</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>454</td>
      <td>435</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>467</td>
      <td>456</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>486</td>
      <td>469</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>496</td>
      <td>488</td>
      <td>497</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>515</td>
      <td>498</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>516</td>
      <td>522</td>
      <td>517</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>553</td>
      <td>524</td>
      <td>554</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>557</td>
      <td>555</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>584</td>
      <td>559</td>
      <td>585</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>593</td>
      <td>586</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>607</td>
      <td>595</td>
      <td>608</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>608</td>
      <td>611</td>
      <td>609</td>
      <td>612</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>612</td>
      <td>614</td>
      <td>613</td>
      <td>615</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>615</td>
      <td>617</td>
      <td>616</td>
      <td>618</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>638</td>
      <td>619</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>726</td>
      <td>640</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwm">6BWM</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQP</span><span class="topo-inside">DLNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVAY</span><span class="topo-outside">HQ</span><span class="topo-unknown">PALEKQGFPPLKAT</span><span class="topo-outside">AGNSMLLL</span><span class="topo-membrane">GHILILLGGVYLLLGQLWYFWR</span><span class="topo-inside">RRLFIWISFMDS</span><span class="topo-membrane">YFEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQV</span><span class="topo-outside">LCFLAIEWYLP</span><span class="topo-membrane">LLVSSLVLGWLNLLYYTR</span><span class="topo-inside">GFQHTGIYSVMIQKV</span><span class="topo-membrane">ILRDLLRFLLVYLVFLFGFAVAL</span><span class="topo-outside">VSLSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEAPPYR</span><span class="topo-outside">SILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGM</span><span class="topo-outside">G</span><span class="topo-unknown">ELAFQEQ</span><span class="topo-outside">LRFRG</span><span class="topo-membrane">VVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>67</td>
      <td>2</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>388</td>
      <td>69</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>409</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>411</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>425</td>
      <td>413</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>433</td>
      <td>427</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>455</td>
      <td>435</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>467</td>
      <td>457</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>485</td>
      <td>469</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>496</td>
      <td>487</td>
      <td>497</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>514</td>
      <td>498</td>
      <td>515</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>529</td>
      <td>516</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>552</td>
      <td>531</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>553</td>
      <td>557</td>
      <td>554</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>588</td>
      <td>559</td>
      <td>589</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>589</td>
      <td>593</td>
      <td>590</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>604</td>
      <td>595</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>605</td>
      <td>605</td>
      <td>606</td>
      <td>606</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>606</td>
      <td>612</td>
      <td>607</td>
      <td>613</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>613</td>
      <td>617</td>
      <td>614</td>
      <td>618</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>638</td>
      <td>619</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>726</td>
      <td>640</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwm">6BWM</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQP</span><span class="topo-inside">DLNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVA</span><span class="topo-outside">YH</span><span class="topo-unknown">QPALEKQGFPPLKAT</span><span class="topo-outside">AGNSMLLL</span><span class="topo-membrane">GHILILLGGVYLLLGQLWYFW</span><span class="topo-inside">RRRLFIWISFMDS</span><span class="topo-membrane">YFEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVL</span><span class="topo-outside">CFLAIEWYLP</span><span class="topo-membrane">LLVSSLVLGWLNLLYYTR</span><span class="topo-inside">GFQHTGIYSVMIQKV</span><span class="topo-membrane">ILRDLLRFLLVYLVFLFGFAVALVS</span><span class="topo-outside">LSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEAPPYR</span><span class="topo-outside">SILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGMGELAFQEQLR</span><span class="topo-outside">F</span><span class="topo-membrane">RGVVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYW</span><span class="topo-unknown">WCR</span><span class="topo-inside">RKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>67</td>
      <td>2</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>388</td>
      <td>69</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>408</td>
      <td>390</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>410</td>
      <td>410</td>
      <td>411</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>425</td>
      <td>412</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>433</td>
      <td>427</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>454</td>
      <td>435</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>467</td>
      <td>456</td>
      <td>468</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>486</td>
      <td>469</td>
      <td>487</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>496</td>
      <td>488</td>
      <td>497</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>497</td>
      <td>514</td>
      <td>498</td>
      <td>515</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>515</td>
      <td>529</td>
      <td>516</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>554</td>
      <td>531</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>555</td>
      <td>557</td>
      <td>556</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>588</td>
      <td>559</td>
      <td>589</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>589</td>
      <td>593</td>
      <td>590</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>603</td>
      <td>595</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>604</td>
      <td>614</td>
      <td>605</td>
      <td>615</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>615</td>
      <td>615</td>
      <td>616</td>
      <td>616</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>616</td>
      <td>638</td>
      <td>617</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>673</td>
      <td>640</td>
      <td>674</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>676</td>
      <td>675</td>
      <td>677</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>677</td>
      <td>726</td>
      <td>678</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwm">6BWM</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQP</span><span class="topo-inside">DLNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIP</span><span class="topo-membrane">RFCFNFLCYLVYMLIFTAVAY</span><span class="topo-outside">HQ</span><span class="topo-unknown">PALEKQGFPPLKAT</span><span class="topo-outside">AGNSMLLL</span><span class="topo-membrane">GHILILLGGVYLLLGQLWYFW</span><span class="topo-inside">RRRLFIWISFMDSY</span><span class="topo-membrane">FEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVLC</span><span class="topo-outside">FLAIEW</span><span class="topo-membrane">YLPLLVSSLVLGWLNLLYYT</span><span class="topo-inside">RGFQHTGIYSVMIQKV</span><span class="topo-membrane">ILRDLLRFLLVYLVFLFGFAVALVSL</span><span class="topo-outside">SR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEAPPYR</span><span class="topo-outside">SI</span><span class="topo-unknown">LDASLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGMGELAFQEQ</span><span class="topo-outside">LR</span><span class="topo-membrane">FRGVVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYWWCRRKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>67</td>
      <td>2</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>388</td>
      <td>69</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>409</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>411</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>425</td>
      <td>413</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>433</td>
      <td>427</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>454</td>
      <td>435</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>468</td>
      <td>456</td>
      <td>469</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>487</td>
      <td>470</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>488</td>
      <td>493</td>
      <td>489</td>
      <td>494</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>513</td>
      <td>495</td>
      <td>514</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>514</td>
      <td>529</td>
      <td>515</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>555</td>
      <td>531</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>557</td>
      <td>557</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>588</td>
      <td>559</td>
      <td>589</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>589</td>
      <td>590</td>
      <td>590</td>
      <td>591</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>604</td>
      <td>592</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>605</td>
      <td>612</td>
      <td>606</td>
      <td>613</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>613</td>
      <td>614</td>
      <td>614</td>
      <td>615</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>615</td>
      <td>638</td>
      <td>616</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>726</td>
      <td>640</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bwm">6BWM</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TSPSSPPAFRLETSDGGQDGAEVDKAQLGYGAGPPPMESRFQDEDRNFPPQIKVNLNYRKGAGASQP</span><span class="topo-inside">DLNRFDRDRLFNVVARGNPEDLAGLLEYLRRTSKYLTDSEYTEGSTGKTCLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVLNLQDGVNACIQPLLEIDRDSGNPQPLVNAQCTDEYYRGHSALHIAIEKRSLQCVKLLVENGANVHAKACGHFFQKNQDTCFYFGELPLSLAACTKQWDVVNYLLENPHQPASLQAQD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLGNTVLHALVMIADDSAENSALVVRMYDGLLQAGARLCPNVQLEGIPNLEGLTPLKLAAKEGKIEIFKHILQREFSAPCQSLSRKFTEWCYGPVRVSLYDLASVDSWEENSVLEIIAFH</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">SRSPHRHRMVVLEPLNKLLQAKWDRLIPRFC</span><span class="topo-membrane">FNFLCYLVYMLIFTAVAYH</span><span class="topo-unknown">QPALEKQGFPPLKAT</span><span class="topo-outside">AGNS</span><span class="topo-membrane">MLLLGHILILLGGVYLLLGQLW</span><span class="topo-inside">YFWRRRLFIWISFMDSY</span><span class="topo-membrane">FEILFLLQALLT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">VLSQVLCFL</span><span class="topo-outside">AIEW</span><span class="topo-membrane">YLPLLVSSLVLGWLNLLYYT</span><span class="topo-inside">RGFQHTGIYSVMIQKV</span><span class="topo-membrane">ILRDLLRFLLVYLVFLFGFAVAL</span><span class="topo-outside">VSLSR</span><span class="topo-unknown">EAQNSRTPAGPNATEVGQPGAGQEDEAPPYR</span><span class="topo-outside">SILDA</span><span class="topo-unknown">SLELFKF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-unknown">TIGMGELAFQEQLR</span><span class="topo-outside">FRG</span><span class="topo-membrane">VVLLLLLAYVLLTYVLLLNML</span><span class="topo-inside">IALMSETVNSVATDSWSIWKLQKAISVLEMENGYW</span><span class="topo-unknown">WCR</span><span class="topo-inside">RKKQRAGVMLTVGTRPDGSPDERWCFRVGEMNWATWEQTLPRTL</span></span>
<span class="topo-ruler">       730       740       750       760       770      </span>
<span class="topo-line"><span class="topo-inside">CEEPSG</span><span class="topo-unknown">AAAPGVMKNPTPASQRGEDSASEEDHLPLQLLQSRDYKDDDDKAHHHHHH</span></span>
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
      <td>67</td>
      <td>2</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>391</td>
      <td>69</td>
      <td>392</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>410</td>
      <td>393</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>425</td>
      <td>412</td>
      <td>426</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>426</td>
      <td>429</td>
      <td>427</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>451</td>
      <td>431</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>468</td>
      <td>453</td>
      <td>469</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>489</td>
      <td>470</td>
      <td>490</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>493</td>
      <td>491</td>
      <td>494</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>494</td>
      <td>513</td>
      <td>495</td>
      <td>514</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>514</td>
      <td>529</td>
      <td>515</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>552</td>
      <td>531</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>553</td>
      <td>557</td>
      <td>554</td>
      <td>558</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>588</td>
      <td>559</td>
      <td>589</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>589</td>
      <td>593</td>
      <td>590</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>594</td>
      <td>603</td>
      <td>595</td>
      <td>604</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>604</td>
      <td>614</td>
      <td>605</td>
      <td>615</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>615</td>
      <td>617</td>
      <td>616</td>
      <td>618</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>638</td>
      <td>619</td>
      <td>639</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>673</td>
      <td>640</td>
      <td>674</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>676</td>
      <td>675</td>
      <td>677</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>677</td>
      <td>726</td>
      <td>678</td>
      <td>727</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>727</td>
      <td>776</td>
      <td>728</td>
      <td>777</td>
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

### Two-fold symmetric selectivity filter gate opening

The TRPV2 channel can adopt a two-fold (C2) symmetric arrangement of subunits,
in contrast to the canonical four-fold (C4) symmetric arrangement observed in
most TRP channel structures. In the RTx- and Ca²⁺-bound state (6BWJ), two
diagonally positioned subunits (A and C) are widened while the other two (B and D)
are contracted, producing a two-fold symmetric pore conformation. The distance
between Ile603 carbonyls across the selectivity filter increases to 12.3 Å in
the widened subunits, compared to 5.2 Å in the closed state, creating an
opening large enough for permeation of large organic cations such as YO-PRO-1
(376 Da). This represents the first structural capture of a fully open SF gate
in a TRPV channel.

### Role of π-helix in S4-S5 linker mediated gating

A π-helix between the S4-S5 linker and S5 (termed π-hinge_S4-S5) determines
the quaternary structural arrangement of TRPV2 subunits. In the Ca²⁺-bound
structure (6BWM), two distinct π-helix positions (beginning at Asp534 vs
Ile531) produce different angles between the S4-S5 linker and S5, resulting
in different degrees of subunit rotation and the two-fold symmetric
rearrangement. RTx binding pushes down on the base of S5 via the π-hinge,
forcing the S4-S5 linker into a different conformation, leading to subunit
rotation and SF gate widening.

### Ca²⁺ coordination in the selectivity filter

In the contracted subunits of the RTx-bound structure, Ca²⁺ ions are
coordinated in the selectivity filter through a novel mechanism involving
helical dipole utilization. Two pore helices align so that carbonyls of
Phe601, Thr602, and Ile603 at the C-termini of the pore helices make
water-mediated coordination of Ca²⁺. In the Ca²⁺-bound structure (6BWM),
a putative Ca²⁺ ion is coordinated in the SF gate, with Ile603 carbonyls
coordinating via water molecules.

### Hydrogen bond triad in pore helix gating

A hydrogen bond triad consisting of Tyr542 (S5), Thr602 (pore helix), and
Tyr627 (S6) stabilizes the contracted subunit conformation. This triad is
broken in the widened subunits, allowing the pore helix to adopt a different
angle. Mutagenesis of Thr602Ala or Tyr542Ala significantly reduces YO-PRO-1
uptake while preserving Na⁺ conductance, demonstrating that the hydrogen bond
network is critical for large organic cation permeation through the SF gate.
The equivalent Thr641Ala mutation in TRPV1 produces a similar phenotype.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/trpv6/">Epithelial Calcium Channel TRPV6</a> — TRPV family member, structural comparison of selectivity filter gating
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/trpv5/">Epithelial Calcium Channel TRPV5</a> — TRPV family member, structural comparison
- <a href="/xray-mp-wiki/reagents/ligands/resiniferatoxin/">Resiniferatoxin (RTx)</a> — Vanilloid toxin that binds TRPV2 and induces SF gate opening
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization detergent (40 mM) for miTRPV2 extraction
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">Decyl Maltoside Neopentyl Glycol (DMNG)</a> — Detergent (0.1 mM) used in buffers during purification
- <a href="/xray-mp-wiki/reagents/detergents/og/">Octyl Glucose Neopentyl Glycol (OGNG)</a> — Detergent (20 mM) used for miTRPV2_QM extraction with RTx
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Lipid additive (4 mM/0.1-0.2 mM) used in detergent extraction and purification buffers
- <a href="/xray-mp-wiki/reagents/lipids/dmpc/">1,2-Dimyristoyl-sn-glycero-3-phosphocholine (DMPC)</a> — Lipid (0.1 mg/ml) added to purification buffers
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
