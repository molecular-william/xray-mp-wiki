---
title: "DsbA"
created: 2026-05-27
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2006.10.034, doi/10.1016##j.febslet.2008.07.063]
verified: agent
uniprot_id: ['P0A6M2', 'P0AEG4']
---

# DsbA

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0A6M2">UniProt: P0A6M2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AEG4">UniProt: P0AEG4</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

DsbA is a periplasmic dithiol oxidase from Escherichia coli belonging to the thioredoxin-like protein family. It is the primary enzyme responsible for introducing disulfide bonds into folding secretory and periplasmic proteins by disulfide exchange. DsbA contains a highly reactive, catalytically unstable disulfide bond between Cys27 and Cys29 (numbering of the E. coli protein) that rapidly oxidizes substrate proteins. Reduced DsbA is then reoxidized by the inner membrane quinone reductase [DSBB](/xray-mp-wiki/proteins/dsbB), completing the oxidative protein folding pathway in the E. coli periplasm.

## Publications

### doi/10.1016##j.cell.2006.10.034

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a></td>
      <td>3.7</td>
      <td>P4(2)2(1)2</td>
      <td>DsbB(Cys130Ser)-DsbA(Cys33Ala) complex, a stable reaction intermediate mimic held together by a Cys30(DsbA)-Cys104(DsbB) intermolecular disulfide bond</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/ubiquinone">UBIQUINONE</a> Q8 (bound to DsbB, not directly to DsbA)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: DsbA(Cys33Ala) variant expressed and purified from E. coli. Purified according to an improved protocol compared to the previously described procedure.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">AQYEDGKQYTTLEKPVAGAPQVLEFFSFFCPHAYQFEEVLHISDNVKKKLPEGVKMTKYHVNFMGGDLGKDLTQAWAVAMALGVEDKVTVPLFEGVQKTQTIRSASDIRDVFINAGIKGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180         </span>
<span class="topo-line"><span class="topo-inside">EYDAAWNSFVVKSLVAQQEKAAADVQLRGVPAMFVNGKYQLNPQGMDTSNMDVFVQQYADTVKYLSEK</span><span class="topo-unknown">K</span></span>
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
      <td>188</td>
      <td>1</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2hi7">2HI7</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLRFLNQASQGRG</span><span class="topo-outside">A</span><span class="topo-membrane">WLLMAFTALALELTALW</span><span class="topo-inside">FQHVMLLKPCVLCIYE</span><span class="topo-membrane">RVALFGVLGAALIGAIAP</span><span class="topo-outside">KTPL</span><span class="topo-membrane">RYVAMVIWLYSAFRGV</span><span class="topo-inside">QLTYEHTMLQLYPSPFATCDFMVRFPEWLPLDKWV</span></span>
<span class="topo-ruler">       130       140       150       160       170      </span>
<span class="topo-line"><span class="topo-inside">PQVFVA</span><span class="topo-unknown">SGDSAERQWDFLGLE</span><span class="topo-inside">MPQW</span><span class="topo-membrane">LLGIFIAYLIVAVLVVI</span><span class="topo-unknown">SQPFKAKKRDLFGR</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>48</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>69</td>
      <td>66</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>85</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>126</td>
      <td>86</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>141</td>
      <td>127</td>
      <td>141</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>145</td>
      <td>142</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>162</td>
      <td>146</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>163</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.febslet.2008.07.063

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3e9j">3E9J</a></td>
      <td>Not explicitly stated</td>
      <td>Not available</td>
      <td>DsbA(Cys33Ala) single-cysteine variant covalently bound to wtDsbB via intermolecular disulfide bond between Cys30 of DsbA and Cys104 of <a href="/xray-mp-wiki/proteins/dsbB">DSBB</a>. The Cys33Ala mutation was introduced to prevent formation of an incorrect disulfide bond during complex formation.</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/ubiquinone">UBIQUINONE</a> Q8 (bound to DsbB, not directly to DsbA)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: DsbA(Cys33Ala) variant expressed and purified from E. coli. Purified according to an improved protocol compared to the previously described procedure.

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
      <td>Expression and purification</td>
      <td>Expression and purification</td>
      <td>--</td>
      <td>-- + --</td>
      <td>DsbA(Cys33Ala) purified according to an improved protocol. Detailed protocol available in supplementary data.</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>In vitro complex formation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Purified DsbA(Cys33Ala) mixed with wtDsbB-Q8-enriched membrane suspension to form the mixed disulfide complex</td>
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
      <td>wtDsbB-DsbA(Cys33Ala)-Q8 complex in nonylmaltoside</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly stated</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not explicitly stated</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not explicitly stated</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None; crystals mounted in cryoloops and cryocooled by immersion into liquid nitrogen without additional cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown and cryocooled without cryoprotectant. Crystallographic data collection, structure solution and refinement described in supplementary data. Resolution same as the <a href="/xray-mp-wiki/proteins/dsbB">DSBB</a>(Cys130Ser)-DsbA(Cys33Ala)-Q8 complex structure.</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e9j">3E9J</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">AQYEDGKQYTTLEKPVAGAPQVLEFFSFFCPHAYQFEEVLHISDNVKKKLPEGVKMTKYHVNFMGGDLGKDLTQAWAVAMALGVEDKVTVPLFEGVQKTQTIRSASDIRDVFINAGIKGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180         </span>
<span class="topo-line"><span class="topo-inside">EYDAAWNSFVVKSLVAQQEKAAADVQLRGVPAMFVNGKYQLNPQGMDTSNMDVFVQQYADTVKYLSEK</span><span class="topo-unknown">K</span></span>
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
      <td>188</td>
      <td>1</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e9j">3E9J</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MLRFLNQASQGRG</span><span class="topo-outside">A</span><span class="topo-membrane">WLLMAFTALALELTALW</span><span class="topo-inside">FQHVMLLKPCVLCIYE</span><span class="topo-membrane">RVALFGVLGAALIGAIAP</span><span class="topo-outside">KTPLR</span><span class="topo-membrane">YVAMVIWLYSAFRGVQ</span><span class="topo-inside">LTYEHTMLQLYPSPFATCDFMVRFPEWLPLDKWV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180  </span>
<span class="topo-line"><span class="topo-inside">PQVFVA</span><span class="topo-unknown">SGDCAERQWDFLGLE</span><span class="topo-inside">MPQW</span><span class="topo-membrane">LLGIFIAYLIVAVLVVI</span><span class="topo-unknown">SQPFKAKKRDLFGRHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>48</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>70</td>
      <td>66</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>71</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>126</td>
      <td>87</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>141</td>
      <td>127</td>
      <td>141</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>145</td>
      <td>142</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>162</td>
      <td>146</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>163</td>
      <td>182</td>
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

### Disulfide exchange mechanism with DsbB

DsbA forms an intermolecular disulfide bond with [DSBB](/xray-mp-wiki/proteins/dsbB) during the reoxidation cycle. In the mixed disulfide complex, DsbA(Cys30) forms a disulfide bond with DsbB(Cys104). When wild-type DsbA reacts with wtDsbB, Cys33 of DsbA attacks the intermolecular DsbA(Cys30)-(Cys104)DsbB disulfide bond, regenerating oxidized DsbA and producing semi-reduced DsbB. This semi-reduced state has an inter-loop disulfide exchange that creates the reduced Cys41/Cys44 pair and the Cys104-Cys130 disulfide bond.

### Cys33Ala variant for trapping the charge-transfer intermediate

The DsbA(Cys33Ala) single-cysteine variant was used to trap the charge-transfer intermediate between [DSBB](/xray-mp-wiki/proteins/dsbB) and Q8. The Cys33Ala mutation prevents formation of an incorrect disulfide bond, allowing the formation of a stable ternary complex between wtDsbB, Q8, and DsbA covalently bound via a single intermolecular disulfide bond. This variant enabled crystallization of the charge-transfer complex.

### Oxidative protein folding pathway

DsbA is the central oxidant in the E. coli periplasmic oxidative protein folding pathway. It introduces disulfide bonds into folding polypeptides by disulfide exchange, becoming reduced in the process. The reduced DsbA is then reoxidized by DsbB, which transfers electrons to [UBIQUINONE](/xray-mp-wiki/reagents/cofactors/ubiquinone) Q8 in the inner membrane. This pathway is essential for proper folding of many secretory proteins in Gram-negative bacteria.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/dsbB/">DsbB</a> — DsbB is the inner membrane quinone reductase that reoxidizes reduced DsbA, completing the oxidative protein folding cycle
- <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone/">Ubiquinone</a> — Terminal electron acceptor in the DsbA-DsbB oxidative folding pathway
- <a href="/xray-mp-wiki/reagents/detergents/nonylmaltoside/">Nonylmaltoside</a> — Detergent used for solubilization of the DsbB-DsbA complex
- <a href="/xray-mp-wiki/reagents/cofactors/ubiquinone">UBIQUINONE</a> — Reagent used in this study
