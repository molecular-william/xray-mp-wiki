---
title: "ECF-PanT (Energy-Coupling Factor Pantothenate Transporter)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.64389, doi/10.1073##pnas.1412246112]
verified: agent
uniprot_id: ['Q03PY5', 'Q03PY6', 'Q03PY7', 'Q03SM0', 'Q1GBG0', 'Q1GBI8', 'Q1GBI9', 'Q1GBJ0']
---

# ECF-PanT (Energy-Coupling Factor Pantothenate Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q03PY5">UniProt: Q03PY5</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q03PY6">UniProt: Q03PY6</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q03PY7">UniProt: Q03PY7</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q03SM0">UniProt: Q03SM0</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBG0">UniProt: Q1GBG0</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBI8">UniProt: Q1GBI8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBI9">UniProt: Q1GBI9</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1GBJ0">UniProt: Q1GBJ0</a>

<span class="expr-badge">Lactobacillus brevis</span>

## Overview

ECF-PanT is a group II energy-coupling factor (ECF) transporter that mediates the import of pantothenate (vitamin B5) across the bacterial membrane. The transporter consists of four subunits: the S-component PanT (substrate-binding integral membrane protein), the T-component EcfT (transmembrane coupling subunit), and two ATPase subunits EcfA and EcfA' (nucleotide-binding domains). Two structures have been determined from different Lactobacillus species: a 2.8 A crystal structure from L. delbrueckii subsp. bulgaricus (PDB 6ZG3), determined using a  crystallization chaperone, revealing an open, post-hydrolysis conformation with a largely occluded substrate-binding cavity; and a 3.25 A crystal structure of the LbECF-PanT complex from L. brevis, which together with the LbECF-FolT and LbECF-HmpT structures revealed the molecular basis for how different S-components share a common [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module in group II [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) transporters.

## Publications

### doi/10.7554##eLife.64389

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a></td>
      <td>2.8 A</td>
      <td>P1</td>
      <td>Full ECF-PanT complex (PanT, EcfT, EcfA, EcfA') from L. delbrueckii subsp. bulgaricus, co-purified with  Nb81 (CA14381)</td>
      <td> (from crystallization condition, occupying substrate-binding pocket)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (for ECF complex)
- **Construct**: ECF-PanT complex expressed from p2BAD plasmid in E. coli. PanT, EcfT, EcfA, EcfA' cloned under arabinose promoter.
- **Notes**: Expression in E. coli with 0.1 mg/mL L-arabinose induction at 25 C for 3 h. Solitary PanT expressed in Lactococcus lactis NZ9000 using pNZ8048 plasmid with nisin promoter. For functional studies, panT-ecfTAA' genes were cotransformed into E. coli DV1 (panF panD) strain.

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
      <td>Membrane preparation</td>
      <td>Cell disruption and ultracentrifugation</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 1 mM MgSO4, DNase + --</td>
      <td>Cells disrupted in Constant Cell Disruption System (E. coli: 25 kPSi, 1 passage; L. lactis: 39 kPSi, 2 passages). Membranes collected at 193,727 xg for 120 min, homogenized in 50 mM potassium phosphate pH 7.5.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 300 mM NaCl, 10% (v/v)  + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> ()</td>
      <td>Membranes incubated with 1%  for 1 h at 4 C. Non-solubilized material removed by centrifugation at 286,286 xg for 35 min.</td>
    </tr>
    <tr>
      <td> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td>Nickel-Sepharose</td>
      <td>50 mM potassium phosphate pH 7.5, 300 mM NaCl, 50 mM (wash); 500 mM  (elution) + 0.05% (w/v) </td>
      <td>Solubilized protein mixed with Ni-Sepharose resin for 1 h. Washed with 20 CV of wash buffer. Protein eluted in three-step gradient. Second fraction (highest protein content) supplemented with 1 mM Na-.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> (with )</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 (GE Healthcare)</td>
      <td>50 mM  Hcl]] pH 7.5, 150 mM NaCl + 0.05% (w/v) </td>
      <td>Purified  Nb81 mixed with ECF-PanT complex and applied to gel filtration column. Fractions containing -bound ECF-PanT pooled and concentrated.</td>
    </tr>
  </tbody>
</table>
**Final sample**: ECF-PanT-Nb81 complex in 50 mM  Hcl]] pH 7.5, 150 mM NaCl, 0.05% 
**Yield**: Sufficient for crystallization trials
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ECF-PanT-Nb81 complex at 6.3 mg/mL in 50 mM  Hcl]] pH 7.5, 150 mM NaCl, 0.05% (w/v) </td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>70 mM sodium  pH 4.5, 21-27% (v/v)  300</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>70 mM sodium  pH 4.5, 40% (v/v)  300</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in sitting drops.  Nb81 (CA14381) used as crystallization chaperone enabled crystal formation. Data collected at Diamond Light Source beamline I24 at 100 K. Crystal belonged to space group P1 (a=97.29 A, b=110.47 A, c=110.50 A, alpha=89.00 deg, beta=102.27 deg, gamma=102.24 deg). 2.8 A resolution.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHGENLYFQ</span><span class="topo-outside">GSDNIISFDHVTFTYPDSPRPALSDLSFAIERGSWTALIGHNGSGKSTVSKLINGLLAPDDLDKSSITVDGVKLGADTVWEVREKVGIVFQNPDNQFVGATV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SDDVAFGLENRAVPRPEMLKIVAQAVADVGMADYADSEPSNLSGGQKQRVAIAGILAVKPQVIILDESTSMLDPEGKEQILDLVRKIKEDNNLTVISITHDLEEAAGADQVLVLDDGQLL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300</span>
<span class="topo-line"><span class="topo-outside">DQGKPEEIFPKVEMLKRIGLDIPFVYRLKQLLKERGIVLPDEIDDDEKLVQSLWQLNS</span><span class="topo-unknown">KM</span></span>
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
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AIKFENVSYVYSPGSPLEAIGLDQLNFSLEEGKFIALVGHTGSGKSTLMQHFNALLKPTSGKIEIAGYTITPETGNKGLKDLRRKVSLAFQFSEAQLFENTVLKDVEYGPRNFGFSEDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AREAALKWLKKVGLKDDLIEHSPFDLSGGQMRRVALAGVLAYEPEIICLDEPAAGLDPMGRLEMMQLFKDYQAAGHTVILVTHNMDDVADYADDVLALEHGRLIKHASPKEVFKDSEWLQ</span></span>
<span class="topo-ruler">       250       260       270       280       </span>
<span class="topo-line"><span class="topo-outside">KHHLAEPRSARFAAKLEAAGLKLPGQPLTMPELADAIKQSLKG</span><span class="topo-unknown">GEHE</span></span>
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
      <td>2</td>
      <td>283</td>
      <td>2</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MYDSEARQKTLNLTVSAVFVAILLLEAFIPNVGYITILPGLPAITTIPLTVAVFASLRGPKAGAAFGLVWGLTSLLRAYVAPNGLVTILLFQNPLIALLPRLAAGWAAGLAGQLADKWEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210     </span>
<span class="topo-line"><span class="topo-outside">ESRKPLAYALSGLLASAVNTLIVILLSDLVYFIHPQKLALALGAKSGQSLLVILFTALAVNGILEAVFSGLITPLITAPLKKRLKRR</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>207</td>
      <td>1</td>
      <td>207</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKII</span><span class="topo-outside">IGRYLPGTTFVYRVDPRAKLLTTFYFIIMIFLANNWVSYLVISIFGLAYVFATGLKARVFWDGVKPMIWMIVFTSLLQTFFMAGGKVYWHWWIFTLSSEGLINGLYVFIRFAMII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LVSTVMTVTTKPLEIADAMEWMLTPLKLFKVNVGMISLVISIALRFVPTLFDQTVKIMNAQRSRGADFNDGGLVKRAKSVVPMLVPLFIDSLEVALDLSTAMESRGYKGSEGRTRYRILE</span></span>
<span class="topo-ruler">       250       260     </span>
<span class="topo-line"><span class="topo-outside">WS</span><span class="topo-unknown">KVDLIPVAYCLLLTILMITTR</span><span class="topo-outside">KH</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>242</td>
      <td>6</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>263</td>
      <td>243</td>
      <td>263</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>265</td>
      <td>264</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHGENLYFQG</span><span class="topo-outside">SDNIISFDHVTFTYPDSPRPALSDLSFAIERGSWTALIGHNGSGKSTVSKLINGLLAPDDLDKSSITVDGVKLGADTVWEVREKVGIVFQNPDNQFVGATV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SDDVAFGLENRAVPRPEMLKIVAQAVADVGMADYADSEPSNLSGGQKQRVAIAGILAVKPQVIILDESTSMLDPEGKEQILDLVRKIKEDNNLTVISITHDLEEAAGADQVLVLDDGQLL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300</span>
<span class="topo-line"><span class="topo-outside">DQGKPEEIFPKVEMLKRIGLDIPFVYRLKQLLKERGIVLPDEIDDDEKLVQSLWQLNS</span><span class="topo-unknown">KM</span></span>
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
      <td>20</td>
      <td>298</td>
      <td>2</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MAIKFENVSYVYSPGSPLEAIGLDQLNFSLEEGKFIALVGHTGSGKSTLMQHFNALLKPTSGKIEIAGYTITPETGNKGLKDLRRKVSLAFQFSEAQLFENTVLKDVEYGPRNFGFSEDE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AREAALKWLKKVGLKDDLIEHSPFDLSGGQMRRVALAGVLAYEPEIICLDEPAAGLDPMGRLEMMQLFKDYQAAGHTVILVTHNMDDVADYADDVLALEHGRLIKHASPKEVFKDSEWLQ</span></span>
<span class="topo-ruler">       250       260       270       280       </span>
<span class="topo-line"><span class="topo-outside">KHHLAEPRSARFAAKLEAAGLKLPGQPLTMPELADAIKQSLKG</span><span class="topo-unknown">GEHE</span></span>
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
      <td>283</td>
      <td>1</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain H (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MYDSEARQKTLNLTVSAVFVAILLLEAFIPNVGY</span><span class="topo-unknown">ITILPGLPAIT</span><span class="topo-outside">TIPLTVAVFASLRG</span><span class="topo-unknown">PKAGAAFGLVWGLTSLLRAYV</span><span class="topo-outside">A</span><span class="topo-unknown">PNGLVTILLFQNPLIALLPRLAAGWAA</span><span class="topo-outside">GLAGQLADKWEK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210     </span>
<span class="topo-line"><span class="topo-outside">ESRKPLAYALSGL</span><span class="topo-membrane">LASAVNTLIVILLSDLVYFIHP</span><span class="topo-inside">QKLALALGAKSG</span><span class="topo-membrane">QSLLVILFTALAVNGILEAVF</span><span class="topo-outside">SGLITPLITAPLKKRLKRR</span><span class="topo-unknown">WSHPQFEK</span></span>
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
      <td>34</td>
      <td>1</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>45</td>
      <td>35</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>59</td>
      <td>46</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>67</td>
      <td>60</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>68</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>108</td>
      <td>82</td>
      <td>108</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>155</td>
      <td>134</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>167</td>
      <td>156</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>188</td>
      <td>168</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>207</td>
      <td>189</td>
      <td>207</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg3">6ZG3</a> — Chain I (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSKII</span><span class="topo-outside">IGRYLPGTT</span><span class="topo-membrane">FVYRVDPRAKLLTTFYFIIMIFLAN</span><span class="topo-inside">NWVS</span><span class="topo-membrane">YLVISIFGLAYVFATGL</span><span class="topo-outside">K</span><span class="topo-membrane">ARVFWDGVKPMIWMIVFTSLLQTFFM</span><span class="topo-inside">AGGKVYWHWWIFTLSSEGL</span><span class="topo-membrane">INGLYVFIRFAMII</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LVSTVMTVTT</span><span class="topo-outside">KPLEIADAMEWMLTPLKLFKVNVGMISLVISIALRFVPTLFDQTVKIMNAQRSRGADFNDGGLVKRAKSVVPMLVPLFIDSLEVALDLSTAMESRGYKGSEGRTRYRILE</span></span>
<span class="topo-ruler">       250       260     </span>
<span class="topo-line"><span class="topo-outside">W</span><span class="topo-membrane">SKVDLIPVAYCLLLTILMI</span><span class="topo-inside">TTRKH</span></span>
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
      <td>14</td>
      <td>6</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>15</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>43</td>
      <td>40</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>61</td>
      <td>61</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>87</td>
      <td>62</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>130</td>
      <td>107</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>241</td>
      <td>131</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>260</td>
      <td>242</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>265</td>
      <td>261</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1412246112

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rfs">4RFS</a></td>
      <td>3.25 A</td>
      <td></td>
      <td>Full LbECF-PanT complex (PanT, EcfT, EcfA, EcfA') from L. brevis</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (for ECF complex)
- **Construct**: ECF-PanT complex expressed from p2BAD plasmid in E. coli. PanT, EcfT, EcfA, EcfA' cloned under arabinose promoter.
- **Notes**: Expression in E. coli with 0.1 mg/mL L-arabinose induction at 25 C for 3 h. Solitary PanT expressed in Lactococcus lactis NZ9000 using pNZ8048 plasmid with nisin promoter. For functional studies, panT-ecfTAA' genes were cotransformed into E. coli DV1 (panF panD) strain.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rfs">4RFS</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AIAFEHVTYTYQAGTPMAHTALTDVSLTVPDRGYLAIIGHTGSGKSTLIQQLNALLKPTSGTIKIDEFTITPETTNAALKPLRQHVGMVFQFPENQLFEETVRQDIAFGPKNFGMADAD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ALALADEMLTTVGLDQSYAERSPFELSGGQMRRVAIAGVLAMQPKVLVLDEPTAGLDPQGRQEMMRLFARLHQEQGLTIVLVTHQMEDVAQYAEQVAVMHEGRLMKFGTPADVFSNREWL</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">QDHQLDVPQAAQFARRLRDRGLTFPKQPLTADQLADYLAQQWAQR</span><span class="topo-unknown">GADHV</span></span>
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
      <td>2</td>
      <td>285</td>
      <td>2</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rfs">4RFS</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MT</span><span class="topo-inside">ENIISVDHLTYQYDENQAPALTDVSFTVHAGEWLAIVGHNGSGKSTLAKSLDGLLPFTQGSVTVGGITLTPETVWQVREQIGMIFQNPDNQFVGATVEDDVAFGLENRQISRDEMVPR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VQAALAQVGMTSFAQREPSSLSGGQKQRVALAGIVAIAPKILILDEATSMLDPQGRIEMLAIVRQLRQQQNLTVISITHDIDEAASADRVLVIDDGRLVDEAVPSQIFERGTQLVEMGLD</span></span>
<span class="topo-ruler">       250       260       270         </span>
<span class="topo-line"><span class="topo-inside">LPFTEKLKAALRQRGITPPTTYQTAAEMEEWLWQSLS</span><span class="topo-unknown">NT</span></span>
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
      <td>3</td>
      <td>277</td>
      <td>3</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rfs">4RFS</a> — Chain S (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MT</span><span class="topo-inside">RHKTFRLVVDALLMAIVLLQNLVPFLGYIPFGPFSMTLIGLTVIVAGSALGPRDGLLIGGFWGLITFVRAFTWPSSPVAPLIFTNPLISILPRLLMGLVAGSLYLWGRHRQWSMRQAM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200   </span>
<span class="topo-line"><span class="topo-inside">QVAAGCAAL</span><span class="topo-membrane">TNTVLVLGLVFLFYQTP</span><span class="topo-outside">AV</span><span class="topo-unknown">ATAFGATGNQT</span><span class="topo-outside">L</span><span class="topo-membrane">GYVLMISLFTNGIPEL</span><span class="topo-inside">ILDVLVAPLIAMPLRRQWERLKPQ</span><span class="topo-unknown">TTK</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>129</td>
      <td>3</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>146</td>
      <td>130</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>148</td>
      <td>147</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>160</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>200</td>
      <td>177</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rfs">4RFS</a> — Chain T (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSQDPMSNFIFGRYLPLDSVV</span><span class="topo-inside">HRLDPRAKLM</span><span class="topo-membrane">LSFCYIIVVFLANNI</span><span class="topo-outside">W</span><span class="topo-membrane">SYAILIAFTVGAILS</span><span class="topo-inside">SKISLG</span><span class="topo-unknown">FFLKGI</span><span class="topo-membrane">RPLLWLIVFTVVLQLLFSPA</span><span class="topo-outside">GGHTYFHW</span><span class="topo-unknown">AFINV</span><span class="topo-outside">T</span><span class="topo-membrane">QDG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LINAGYIFVRFLLIIMMS</span><span class="topo-inside">TLLTLSTQPLDIATGLASLMKPLRWVKVPVDTLAMMLSIALRFVPTLMDEATKIMNAQRARGVDFGEGGLFKQAKSLIPLMVPLFMSAFNRAEDLSTAMEAR</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-inside">GYQDSEHRSQYR</span><span class="topo-unknown">ILTWQR</span><span class="topo-inside">RDT</span><span class="topo-membrane">VTWLLFLLGFVAILIF</span><span class="topo-unknown">RHW</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>31</td>
      <td>40</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>55</td>
      <td>27</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>56</td>
      <td>42</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>77</td>
      <td>58</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>64</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>84</td>
      <td>103</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>90</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>117</td>
      <td>103</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>138</td>
      <td>104</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>252</td>
      <td>125</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>261</td>
      <td>245</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>248</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dynamic S-component exchange in Group II ECF transporters

Co-reconstitution experiments with ECF-PanT and ECF-FoIT2 in proteoliposomes demonstrated that the S-components PanT and FoIT2 dynamically associate with and dissociate from the shared [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module. Folate transport was observed when FoIT2 was co-reconstituted with ECF-PanT, and pantothenate transport was observed when PanT was co-reconstituted with ECF-FoIT2, indicating S-component exchange occurs as part of the transport mechanism.

### Substrate-loaded S-components compete more effectively for the ECF module

Competition experiments showed that the rate of pantothenate transport was inhibited by unlabelled folate, and vice versa, in a dose-dependent manner. This suggests that substrate-bound S-components compete more efficiently for association with the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) module than apo-proteins, recapitulating previous in vivo observations.

### Structural basis for differential substrate binding kinetics

The ECF-PanT structure reveals an occluded binding pocket (880 A^3) with loops L1 and L3 in a closed conformation. Comparison with ECF-FoIT2 suggests smaller conformational changes are needed for pantothenate binding to PanT than folate binding to FoIT2, explaining the faster apparent substrate association kinetics of PanT. In ECF-PanT, key binding residues (R101, N139, W69) all point towards the binding pocket center, while in ECF-FoIT2 the binding site is more accessible from the cytoplasmic side.

### Molecular basis for ECF module sharing in Group II ECF transporters

Structural comparison of LbECF-PanT, LbECF-FolT, and LbECF-HmpT from L. brevis revealed that different EcfS proteins use a common surface area composed of transmembrane helices SM1, SM2, and SM6 to interact with the coupling helices CH2 and CH3 of the same EcfT. CH2 interacts mainly with SM1 via hydrophobic interactions, modulating sliding movement of EcfS. CH3 binds to a hydrophobic surface groove formed by SM1, SM2, and SM6, transmitting conformational changes from EcfA/A' to EcfS. The AxxxA motif (Ala13 and Ala17) in SM1 is involved in EcfT interaction. The conformational flexibility of EcfT allows it to accommodate different EcfS proteins, enabling module sharing in group II [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter-family/) transporters.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter/">ECF Transporter (Energy-Coupling Factor Transporter)</a> — ECF-PanT is a group II ECF transporter that shares a common ECF module
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ribu/">RibU (ECF-Type Riboflavin Transporter S Component)</a> — Another characterized ECF transporter S-component for comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator-Type Transport Mechanism</a> — ECF transporters use an elevator-type toppling mechanism for substrate translocation
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Detergent used for membrane solubilization and purification
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Crystallization method used for ECF-PanT-Nb81 structure determination
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Referenced in ecf-pant text
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> — Referenced in ecf-pant text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in ecf-pant text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in ecf-pant text
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel Nta</a> — Referenced in ecf-pant text
