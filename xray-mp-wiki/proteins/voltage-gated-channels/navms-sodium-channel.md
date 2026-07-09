---
title: "NavMs Sodium Channel from Magnetococcus marinus"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NCOMMS3465]
verified: regex
uniprot_id: A0L5S6
---

# NavMs Sodium Channel from Magnetococcus marinus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0L5S6">UniProt: A0L5S6</a>

<span class="expr-badge">Magnetococcus marinus MC-1</span>

## Overview

[NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) is a prokaryotic voltage-gated sodium channel from Magnetococcus marinus that serves as a model system for understanding sodium channel structure, gating, and inactivation. The channel forms a homotetramer with each monomer consisting of a transmembrane domain containing the voltage sensor and pore functionalities, and a C-terminal domain (CTD) comprising a flexible linker region connected to a four-helix coiled-coil bundle. The 2.9 A crystal structure of the [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) pore with its full-length CTD reveals a fully open pore conformation. Combined electron paramagnetic resonance (EPR) spectroscopy, molecular dynamics simulations, and electrophysiology demonstrate that the coiled-coil domain couples inactivation with channel opening, enabled by negatively charged residues in the linker region.

## Publications

### doi/10.1038##NCOMMS3465

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3zjz">3ZJZ</a></td>
      <td>2.9</td>
      <td>C2221</td>
      <td>NavMs-pore + CTD (full-length C-terminal domain), residues 1-274 from Magnetococcus marinus</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli expression system (described in earlier NavMs-pore study, PDB 4F4L)
- **Construct**: NavMs-pore + CTD construct with full-length C-terminal domain

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
      <td>Purification</td>
      <td>HisTrap HP <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> followed by size-exclusion chromatography</td>
      <td>HisTrap HP column, size exclusion column</td>
      <td>Buffer A (composition not specified in raw paper) + Not specified</td>
      <td>Untagged wild-type NavMs-pore + CTD concentrated to 14 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NavMs-pore + CTD at 14 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M trisodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 34% v/v <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed in 2:1 ratio with reservoir solution for 150 nl sitting drops. Data collected at Diamond Light Source. Space group C2221, cell dimensions a=80.15, b=334.38, c=80.21 A. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using monomer A from NavMs-pore structure (PDB 4F4L).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zjz">3ZJZ</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMG</span><span class="topo-outside">V</span><span class="topo-membrane">GSVAALLTVVFYIAAVMATNL</span><span class="topo-inside">YGATFPEWFGDL</span><span class="topo-unknown">SKSLYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLFIGII</span><span class="topo-outside">VDAM</span><span class="topo-unknown">AITKEQEEEAKTGHHQEPISQTL</span></span>
<span class="topo-ruler">       130       140         </span>
<span class="topo-line"><span class="topo-unknown">LHLGDRLDRIEKQLAQNNELLQRQQPQKK</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>39</td>
      <td>28</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>40</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>97</td>
      <td>94</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>149</td>
      <td>98</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zjz">3ZJZ</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMG</span><span class="topo-outside">V</span><span class="topo-membrane">GSVAALLTVVFYIAAVMATNL</span><span class="topo-inside">YGATFPEWFGDL</span><span class="topo-unknown">SKSLYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLFIGII</span><span class="topo-outside">VDAM</span><span class="topo-unknown">AITKEQEEEAKTGHHQEPISQTL</span></span>
<span class="topo-ruler">       130       140         </span>
<span class="topo-line"><span class="topo-unknown">LHLGDRLDRIEKQLAQNNELLQRQQPQKK</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>39</td>
      <td>28</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>40</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>97</td>
      <td>94</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>149</td>
      <td>98</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zjz">3ZJZ</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMG</span><span class="topo-outside">V</span><span class="topo-membrane">GSVAALLTVVFYIAAVMATNL</span><span class="topo-inside">YGATFPEWFGDL</span><span class="topo-unknown">SKSLYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLFIGII</span><span class="topo-outside">VDAM</span><span class="topo-unknown">AITKEQEEEAKTGHHQEPISQTL</span></span>
<span class="topo-ruler">       130       140         </span>
<span class="topo-line"><span class="topo-unknown">LHLGDRLDRIEKQLAQNNELLQRQQPQKK</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>39</td>
      <td>28</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>40</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>97</td>
      <td>94</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>149</td>
      <td>98</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3zjz">3ZJZ</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMG</span><span class="topo-outside">V</span><span class="topo-membrane">GSVAALLTVVFYIAAVMATNL</span><span class="topo-inside">YGATFPEWFGDL</span><span class="topo-unknown">SKSLYTLFQVMTLESWS</span><span class="topo-inside">MGIVRPVMNVHPN</span><span class="topo-membrane">AWVFFIPFIMLTTFTVLNLFIGII</span><span class="topo-outside">VDAM</span><span class="topo-unknown">AITKEQEEEAKTGHHQEPISQTL</span></span>
<span class="topo-ruler">       130       140         </span>
<span class="topo-line"><span class="topo-unknown">LHLGDRLDRIEKQLAQNNELLQRQQPQKK</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>39</td>
      <td>28</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>40</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>69</td>
      <td>57</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>97</td>
      <td>94</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>149</td>
      <td>98</td>
      <td>149</td>
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

### C-terminal domain structure and dynamics

The CTD of [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) consists of a flexible linker region (residues 222-239) connecting the transmembrane pore to a four-helix coiled-coil bundle (residues 240-270). EPR spectroscopy reveals the linker is flexible and dynamic but not fully disordered, while the coiled-coil region forms a stable tetrameric bundle. DEER distance measurements and molecular dynamics simulations show large motions in the CTD, explaining why this region is disordered in the crystal electron density map.

### Open pore conformation

The 2.9 A structure of NavMs-pore + CTD reveals a fully open pore conformation with all four monomers in their open state. The gating movement involves a change in the Psi angle of residue Thr84, producing an anticlockwise twisting motion of the lower end of the S6 helices (~4.5 A movement each). Both crystallographically distinct tetramers have true fourfold symmetry, with the distance between Met97 C-alpha atoms at the base of the pore being 21 A across both diagonals.

### Role of CTD in inactivation gating

Electrophysiology measurements show the CTD is necessary for inactivation gating and recovery, and for channel stability. The Delta223 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (removing the linker and coiled-coil) inactivates ~7 times slower than wild-type [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) and recovers from inactivation ~155 times slower. The Delta239 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (removing only the coiled-coil) has normal inactivation kinetics but uncoupled voltage dependence. Mutation of three negatively charged glutamate residues (E229, E230, E231) to glutamine slows inactivation ~5-fold.

### Gating mechanism model

A mechanism for gating is proposed whereby splaying of the bottom of the pore is possible without requiring unravelling of the coiled-coil. The CTD acts like an oscillator composed of a spring (the flexible linker) tethered to a mass (the coiled-coil) that enables opening of the gate without dissociating the tetramers. The linker and coiled-coil C-terminal region enables opening of the gate and fast inactivation at the appropriate membrane potential.

### Conservation across prokaryotic sodium channels

The CTDs of all identified prokaryotic sodium channels exhibit similar flexible linker/coiled-coil motifs. Evolutionary differences in linker length and flexibility may account for different inactivation kinetics. For example, [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) (with a considerably shorter linker region) inactivates 12-19 times slower than [NAVMS](/xray-mp-wiki/proteins/voltage-gated-channels/navms/).


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Related tetrameric ion channel serving as structural model
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting Drop Vapor Diffusion Crystallization</a> — Crystallization method used for NavMs
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-gating/">Sodium Channel Gating</a> — NavMs provides insights into sodium channel gating mechanisms
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/">NaChBac Bacterial Voltage-Gated Sodium Channel</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navms/">NAVMS</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
