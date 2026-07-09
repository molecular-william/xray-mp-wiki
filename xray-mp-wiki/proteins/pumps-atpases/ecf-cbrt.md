---
title: "ECF-CbrT (ECF-type ABC Transporter for Vitamin B12 from Lactobacillus delbrueckii)"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.35828]
verified: regex
uniprot_id: ['Q1G7W0', 'Q1GBI8', 'Q1GBI9', 'Q1GBJ0']
---

# ECF-CbrT (ECF-type ABC Transporter for Vitamin B12 from Lactobacillus delbrueckii)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1G7W0">UniProt: Q1G7W0</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBI8">UniProt: Q1GBI8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBI9">UniProt: Q1GBI9</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBJ0">UniProt: Q1GBJ0</a>

<span class="expr-badge">Lactobacillus delbrueckii</span>

## Overview

ECF-CbrT is an Energy Coupling Factor (ECF)-type ABC transporter from Lactobacillus delbrueckii subsp. bulgaricus that mediates the specific, -dependent uptake of vitamin B12 () and its precursor cobinamide (Cbi). The complex consists of the S-component CbrT (substrate-binding protein), the transmembrane protein EcfT, and two ATPase subunits EcfA and EcfA'. It is unrelated to the well-characterized B12 transporter BtuCDF, but shares similar biochemical features, indicating functional convergence.


## Publications

### doi/10.7554##eLife.35828

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a></td>
      <td>3.4</td>
      <td>—</td>
      <td>Full ECF-CbrT complex (CbrT, EcfT, EcfA, EcfA')</td>
      <td>apo (inward-facing)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: CbrT inserted into p2BAD_ECF with XbaI/XhoI; [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module expressed from same plasmid
- **Notes**: Expression induced with L-arabinose at 37°C
- **Induction**: 0.00001% L-arabinose

**Purification:**

- **Expression system**: Escherichia coli MC1061
- **Expression construct**: Full ECF-CbrT complex
- **Tag info**: C-terminal octa-His-tag on CbrT (solitary) or untagged in complex

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
      <td>Cell harvest and membrane preparation</td>
      <td>Centrifugation and membrane vesicle preparation</td>
      <td>—</td>
      <td>50 mM KPi, pH 7.5</td>
      <td>Cells harvested 3 hr post-induction</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM KPi, pH 7.5, 300 mM NaCl, 10%  + 1% </td>
      <td>45 min at 4°C with constant agitation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>BioRad PolyPrep column, 0.5 mL Ni2+ resin</td>
      <td>50 mM KPi, pH 7.5, 300 mM NaCl, 10%  + 0.05% </td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td>—</td>
      <td>50 mM KPi, pH 7.5, 150 mM NaCl + 0.05% </td>
      <td></td>
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
      <td>Purified ECF-CbrT in 50 mM KPi pH 7.5, 150 mM NaCl, 0.05% </td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>OH-Cbl was added in excess to crystallization condition but not bound in structure</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQTKER</span><span class="topo-inside">YQLQRLTLLALLTAMCVVLRIFKIIDIPNVQPVTDIIMLTTLELGAGTGILLAILVMVISNIFLGFGIWTLPQIFAYAACALTVALFAR</span><span class="topo-unknown">LLPLKSRKFF</span><span class="topo-inside">WLQELLAGFLGLEYG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180  </span>
<span class="topo-line"><span class="topo-inside">FFVSLGMAGWGGWAAFIAYWVSGLTFDLYHAAGNLAFYPIFYLPLVLGLDRFKKKA</span><span class="topo-unknown">GWKQNA</span></span>
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
      <td>7</td>
      <td>95</td>
      <td>7</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>176</td>
      <td>106</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHGENLYFQ</span><span class="topo-inside">GSDNIISFDHVTFTYPDSPRPALSDLSFAIERGSWTALIGHNGSGKSTVSKLINGLLAPDDLDKSSITVDGVKLGADTVWEVREKVGIVFQNPDNQFVGATV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SDDVAFGLENRAVPRPEMLKIVAQAVADVGMADYADSEPSNLSGGQKQRVAIAGILAVKPQVIILDESTSMLDPEGKEQILDLVRKIKEDNNLTVISITHDLEEAAGADQVLVLDDGQLL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300</span>
<span class="topo-line"><span class="topo-inside">DQGKPEEIFPKVEMLKRIGLDIPFVYRLKQLLKERGIVLPDEIDDDEKLVQSLWQLNS</span><span class="topo-unknown">KM</span></span>
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
      <td>19</td>
      <td>298</td>
      <td>1</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MAIKFENVSYVYSPGSPLEAIGLDQLNFSLEEGKFIALVGHTGSGKSTLMQHFNALLKPTSGKIEIAGYTITPETGNKGLKDLRRKVSLAFQFSEAQLFENTVLKDVEYGPRNFGFSEDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AREAALKWLKKVGLKDDLIEHSPFDLSGGQMRRVALAGVLAYEPEIICLDEPAAGLDPMGRLEMMQLFKDYQAAGHTVILVTHNMDDVADYADDVLALEHGRLIKHASPKEVFKDSEWLQ</span></span>
<span class="topo-ruler">       250       260       270       280       </span>
<span class="topo-line"><span class="topo-inside">KHHLAEPRSARFAAKLEAAGLKLPGQPLTMPELADAIKQSLK</span><span class="topo-unknown">GGEHE</span></span>
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
      <td>282</td>
      <td>1</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKII</span><span class="topo-inside">IGRYLPGTTFVYRVDPRAKLL</span><span class="topo-membrane">TTFYFIIMIFLANNW</span><span class="topo-outside">V</span><span class="topo-membrane">SYLVISIFGLAYVF</span><span class="topo-inside">ATGLKARVFWDGVKPMI</span><span class="topo-membrane">WMIVFTSLLQTFF</span><span class="topo-outside">MAGGKVYWHWWIFTLSSEG</span><span class="topo-membrane">LINGLYVFIRFAMII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">STVMTVTTKPLEIADAMEWMLTPLKLFKVNVGMISLVISIALRFVPTLFDQTVKIMNAQRSRGADFNDGGLVKRAKSVVPMLVPLFIDSLEVALDLSTAMESRGYKGSEGRTRYRILE</span></span>
<span class="topo-ruler">       250       260     </span>
<span class="topo-line"><span class="topo-inside">WSKVDL</span><span class="topo-membrane">IPVAYCLLLTILMIT</span><span class="topo-outside">TRK</span><span class="topo-unknown">H</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>41</td>
      <td>27</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>43</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>73</td>
      <td>57</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>86</td>
      <td>74</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>87</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>122</td>
      <td>106</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>246</td>
      <td>123</td>
      <td>246</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>261</td>
      <td>247</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>264</td>
      <td>262</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fnp">6FNP</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MAIKFENVSYVYSPGSPLEAIGLDQLNFSLEEGKFIALVGHTGSGKSTLMQHFNALLKPTSGKIEIAGYTITPETGNKGLKDLRRKVSLAFQFSEAQLFENTVLKDVEYGPRNFGFSEDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AREAALKWLKKVGLKDDLIEHSPFDLSGGQMRRVALAGVLAYEPEIICLDEPAAGLDPMGRLEMMQLFKDYQAAGHTVILVTHNMDDVADYADDVLALEHGRLIKHASPKEVFKDSEWLQ</span></span>
<span class="topo-ruler">       250       260       270       280       </span>
<span class="topo-line"><span class="topo-inside">KHHLAEPRSARFAAKLEAAGLKLPGQPLTMPELADAIKQSLK</span><span class="topo-unknown">GGEHE</span></span>
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
      <td>282</td>
      <td>1</td>
      <td>282</td>
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

### ECF-CbrT is a vitamin B12 transporter

ECF-CbrT supports -dependent growth of an E. coli knockout strain
lacking the endogenous B12 transporter BtuCDF. The full complex (CbrT + ECF
module) is required for transport; solitary CbrT cannot sustain growth.

### Substrate specificity and promiscuity

ECF-CbrT transports both  (Cbl) and cobinamide (Cbi). Competition
assays show promiscuity toward the beta-axial ligand: CN-Cbl, OH-Cbl,
Met-Cbl inhibit uptake strongly, while Ado-Cbl (bulkier) inhibits partially.
Hemin does not compete, confirming specificity for B12-related compounds.

### High-affinity binding

CbrT binds CN-Cbl with Kd of 9.2  and Cbi with Kd of 36  by [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/).
Binding is 1:1 stoichiometry. The apo protein is unstable, indicating
substrate binding has a stabilizing effect.

### Structural comparison with ECF-FolT2

The crystal structure at 3.4 Å reveals the S-component CbrT in a toppled,
inward-facing apo conformation. The identical [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module (EcfA, EcfA',
EcfT) adjusts to interact with different S-components (CbrT vs FolT2)
via conformational changes in the EcfT membrane domain, hinging around
Pro71. Loop 3 of CbrT occludes the empty binding cavity, unlike FolT2.

### Functional convergence with BtuCDF

Despite being structurally and mechanistically unrelated to BtuCDF,
ECF-CbrT shows similar kinetic parameters (Km 2.1  for Cbl,
Vmax 0.06 nmol/mg/s), suggesting convergent evolution of B12 transport.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/">ECF Transporter Family</a> — ECF-CbrT is a group II ECF transporter
- <a href="/xray-mp-wiki/reagents/ligands/cobalamin/">Cobalamin</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in ecf-cbrt text
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Referenced in ecf-cbrt text
