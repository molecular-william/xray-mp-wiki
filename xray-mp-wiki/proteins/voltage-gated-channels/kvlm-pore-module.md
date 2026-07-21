---
title: "KvLm Pore Module (Voltage-Gated K+ Channel Pore from Listeria monocytogenes)"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, potassium-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.m112.415091]
verified: agent
uniprot_id: Q8Y5K1
---

# KvLm Pore Module (Voltage-Gated K+ Channel Pore from Listeria monocytogenes)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8Y5K1">UniProt: Q8Y5K1</a>

<span class="expr-badge">Listeria monocytogenes</span>

## Overview

The KvLm pore module (PM) is a sensorless pore module dissected from the KvLm voltage-gated potassium channel from Listeria monocytogenes. The A98C mutant was crystallized in lipidic cubic phase (LCP) using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) membranes, yielding structures at 3.1 A ([Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) condition) and 3.35 A (sodium nitrate condition) resolution. This represents the first crystal structure of a Kv channel pore module in a closed state, with the activation gate closed but the selectivity filter in a conductive, ready-to-conduct conformation. Functional reconstitution in droplet interface bilayers (DIBs) demonstrated that the PM is functional, with single-channel conductance of 68 pS in 0.5 M KCl, and gates open at 0 mV long enough for open-channel blockers ([TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/), 4-AP) to enter.


## Publications

### doi/10.1074/jbc.M112.415091

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a></td>
      <td>3.1</td>
      <td>P42_12</td>
      <td>KvLm PM A98C mutant, residues 1-137 (tetramer), crystallized in LCP with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
      <td>K+ ions (S2-S4 positions in selectivity filter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a></td>
      <td>3.35</td>
      <td>P2_12_2</td>
      <td>KvLm PM A98C mutant, 2 subunits in asymmetric unit</td>
      <td>K+ ions (fully occupied selectivity filter)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: KvLm PM A98C mutant (single amino acid mutation), expressed as previously described (Santos et al., 2008, JGP)

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
      <td>Microfluidizer</td>
      <td>—</td>
      <td>50 mM Hepes pH 7.5, 50 mM KCl, 5 mM MnCl2, 0.1 mM CaCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% NaN3 with BSA, lysozyme, DNase, and protease inhibitors</td>
      <td>Membranes pelleted at 125,000 x g</td>
    </tr>
    <tr>
      <td>Membrane washing</td>
      <td>Sequential low-salt and high-salt washes</td>
      <td>—</td>
      <td>Low-salt: 50 mM Hepes pH 7.5, 50 mM KCl plus additives. High-salt: same with 0.5 M KCl</td>
      <td>Membranes washed twice by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Hepes pH 7.5, 50 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 20 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td>Solubilized for 3-3.5 h at 4 C, then adjusted to 400 mM KCl and ultracentrifuged at 125,000 x g</td>
    </tr>
    <tr>
      <td>IMAC <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt IMAC (Co2+) resin</td>
      <td>Cobalt IMAC (Clontech)</td>
      <td>50 mM Hepes pH 7.5, 200-400 mM KCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1-10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5-15 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 5-15 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Rigorous three-step wash: 20 CV high salt, 20 CV medium salt, 20 CV low salt. Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>.</td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>PD-10 desalting column (GE Healthcare)</td>
      <td>—</td>
      <td>50 mM Hepes pH 7.5, 200 mM KCl, 3 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.1 mM TCEP (crystallization buffer) + 3 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion</td>
      <td>Overnight trypsin-TPCK digestion</td>
      <td>—</td>
      <td></td>
      <td>Protein digestion at ~20 C overnight to remove flexible regions for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Trypsin-digested KvLm PM in crystallization buffer (50 mM Hepes pH 7.5, 200 mM KCl, 3 mM DM, 0.1 mM TCEP)</td>
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
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP formed using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (1-oleoyl-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>). Also crystallized in alternative condition with sodium nitrate instead of <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>. Data collected at GM/CA-CAT beamline (23-ID) at APS using minibeam.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Ammonium Sulfate: 0.5-0.6 M [salt]  
- Hepes: 50 mM [buffer]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h33">4H33</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRYIVPIYSFF</span><span class="topo-inside">RSN</span><span class="topo-membrane">GLNRFLMIFVLLVIIIPVPM</span><span class="topo-outside">VFIEPEINNY</span><span class="topo-unknown">PDALWWAIVTATTVGYG</span><span class="topo-outside">DIVPVTP</span><span class="topo-membrane">IGRILASIMMLFGIAFIGMITSTIT</span><span class="topo-inside">NFFRCKKPT</span><span class="topo-unknown">NSSTQRANKITQLISETP</span></span>
<span class="topo-ruler">       130       </span>
<span class="topo-line"><span class="topo-unknown">DLTKEEIAVVEQFLTLR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>34</td>
      <td>15</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>44</td>
      <td>35</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>45</td>
      <td>61</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>62</td>
      <td>68</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>93</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>102</td>
      <td>94</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>137</td>
      <td>103</td>
      <td>137</td>
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

### First Kv channel pore structure with closed activation gate

The KvLm PM represents the first structure of a Kv channel pore trapped with the activation gate closed. The inner helices (TM S6) cross near the intracellular side, occluding the pore. The closed gate is positively charged, generated by residues R97CKK that cap the inner helix. This is distinct from [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), which has a stable closed conformation; the KvLm PM is in an unstable closed state that can gate open.

### Conductive selectivity filter in a closed channel

Despite the closed activation gate, the selectivity filter adopts a ready-to-conduct conformation with backbone carbonyls of Thr57, Val58, Gly59, and Tyr60 facing the permeation path. Three equidistant (3.1 A) K+ ions occupy positions S2-S4. The Val58 carbonyl spontaneously reverts to the conductive conformation during refinement, confirming this is the preferred state independent of ion occupancy.

### Modular architecture of Kv channels

Comparison with the Kv1.2-Kv2.1 chimera (which includes the voltage sensor) shows that the selectivity filter conformation and lipid immobilization surfaces are conserved in the sensorless PM, while the activation gate is sensor-dependent. The S4-S5 linker was present in the construct but not visible in electron density, suggesting it is mobile in the absence of the voltage sensor.

### LCP crystallization in native-like membrane environment

This was among the first structures of a membrane protein crystallized in LCP (lipidic cubic phase) using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/), providing a native-like lipid bilayer environment. The structure demonstrates that LCP can yield near-atomic resolution (3.1 A) for potassium channels.

### Functional reconstitution in droplet interface bilayers

The KvLm PM was functionally reconstituted in [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) lipid bilayers using droplet interface bilayers (DIBs). Single-channel recordings showed conductance of 68 +/- 9 pS in 0.5 M KCl and 4 +/- 2 pS in 27 mM KCl. The channel opens primarily at positive potentials and is blocked by [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) and 4-AP at 0 mV, confirming the pore is accessible even when the crystal structure shows a closed gate.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Another family of prokaryotic potassium channels used for structural comparison of channel gating mechanisms
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Primary crystallization method used to obtain the KvLm PM structure in a lipid membrane environment
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating via Plug Domain Displacement</a> — Comparison of gating mechanisms; KvLm PM shows closed activation gate with conductive filter
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KCSA</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Detergent used in purification or crystallization
