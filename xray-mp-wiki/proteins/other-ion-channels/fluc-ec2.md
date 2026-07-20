---
title: "Fluc-Ec2 Fluoride Channel"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.31259, doi/10.7554##eLife.69482, doi/10.7554##eLife.18767]
verified: agent
uniprot_id: ['B7LI20', 'Q6J5N4']
---

# Fluc-Ec2 Fluoride Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B7LI20">UniProt: B7LI20</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q6J5N4">UniProt: Q6J5N4</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Ec2 is a fluoride ion channel from an E. coli virulence plasmid, belonging to the Fluc family. Fluc channels are small (~120 residues per subunit), dual-topology homodimeric membrane proteins that protect bacteria from environmental fluoride toxicity by allowing passive F- transit down its electrochemical gradient. Ec2 exhibits exceptionally high F-/Cl- selectivity and has two independent F- permeation pathways.

## Publications

### doi/10.7554/eLife.31259

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5a43">5A43</a></td>
      <td>2.65</td>
      <td>P4_1</td>
      <td>Ec2-S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a> complex</td>
      <td>F⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b24">6B24</a></td>
      <td>2.75</td>
      <td>P4_1</td>
      <td>F80Y <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> In complex with S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a></td>
      <td>F⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b2a">6B2A</a></td>
      <td>2.65</td>
      <td>P4_1</td>
      <td>F80M <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> In complex with S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a></td>
      <td>F⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b2b">6B2B</a></td>
      <td>2.60</td>
      <td>P4_1</td>
      <td>F83M <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> In complex with S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a></td>
      <td>F⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b2d">6B2D</a></td>
      <td>3.01</td>
      <td>P4_1</td>
      <td>T114S <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> In complex with S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a></td>
      <td>F⁻</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: C-terminal hexahistidine tag, R25K mutation (enhances expression without affecting function), pET21 vector

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: C-terminal hexahistidine tag, R25K mutation
- **Tag info**: C-terminal His6, not removed

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>Cells grown to OD 1.5 At 37°C, CpE-Induced Tight Junction Disassembly with <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> (Isopropyl-beta-D-thiogalactopyranoside) (Isopropyl-beta-D-thiogalactopyranoside) (Isopropyl-beta-D-thiogalactopyranoside)</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> (Tris-HCl Buffer) (Tris(hydroxymethyl)aminomethane) (Tris(hydroxymethyl)aminomethane) Ph 7.5, 100 mM NaCl</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/cobalt-hexamine/">Hexaamminecobalt(III) (Cobalt Hexamine)</a>(III) (Cobalt Hexamine)(III) (Cobalt Hexamine) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Cobalt Affinity Resin resin)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> (Tris-HCl Buffer) (Tris(hydroxymethyl)aminomethane) (Tris(hydroxymethyl)aminomethane) Ph 7.5, 100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Wash with 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200 Increase [SEC</a> Resin](/xray-mp-wiki/reagents/additives/superdex-200/) Increase</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> Ph 7.0, 100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>For functional assays; for <a href="/xray-mp-wiki/methods/structure-determination/lcp-serial-millisecond-crystallography/">LCP-SMX</a>, use 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> Ph 7.0, 100 mM NaF, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Monodisperse homodimers In 25 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) Ph 7.0, 100 mM NaCl, 5 mM Dm
**Yield**: Comparable to WT Sf9 Insect Cell Expression System levels
**Purity**: Monodisperse homodimers by gel filtration

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> (Hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Ec2-S9 <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s7/">Monobody S7</a> complex In 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> Ph 7.0, 100 mM NaF, 5 mM Dm</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>F⁻ ions located At 2F⁻ per Pore. Diffractive Imaging of Imperfect Crystals of F80Y, F80M, F83M, and T114S mutants obtained Microbatch Crystallization Under Oil similar conditions.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a43">5A43</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">I</span><span class="topo-membrane">KSLFAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTMLAY</span><span class="topo-outside">FLRQPHLDPF</span><span class="topo-membrane">WKLMITTGLCGGLSTFSTFSVEVF</span><span class="topo-inside">ALLQAGNYIW</span><span class="topo-membrane">ALTSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-membrane">ITIL</span><span class="topo-outside">F</span><span class="topo-unknown">A</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>27</td>
      <td>3</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>64</td>
      <td>55</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>88</td>
      <td>65</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>98</td>
      <td>89</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>124</td>
      <td>99</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>126</td>
      <td>126</td>
      <td>126</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b24">6B24</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">I</span><span class="topo-membrane">KSLFAVIIGGSVGCTLRWLLS</span><span class="topo-unknown">TKFNSL</span><span class="topo-inside">FPNLPP</span><span class="topo-membrane">GTLVVNLLAGLIIGTA</span><span class="topo-outside">LAYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTYSTFS</span><span class="topo-inside">VEVFALLQAGNYIWAL</span><span class="topo-membrane">TSVLVHVIGSLIMTALG</span><span class="topo-outside">FFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILF</span><span class="topo-unknown">A</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>3</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>29</td>
      <td>24</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>51</td>
      <td>36</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>67</td>
      <td>52</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>84</td>
      <td>68</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>101</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>125</td>
      <td>118</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b24">6B24</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-outside">SLFPN</span><span class="topo-membrane">LPPGTLVVNLLAGLII</span><span class="topo-inside">GTALAYFLRQPHLDPFWKLM</span><span class="topo-membrane">ITTGLCGGLSTYSTFSVEVF</span><span class="topo-outside">ALLQAGNY</span><span class="topo-membrane">IWALTSVLVHVIGSLIMT</span><span class="topo-inside">ALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-inside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>28</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>48</td>
      <td>33</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>68</td>
      <td>49</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>88</td>
      <td>69</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>96</td>
      <td>89</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>97</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>125</td>
      <td>115</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b2a">6B2A</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">I</span><span class="topo-membrane">KSLFAVIIGGSVGCTLRWLLS</span><span class="topo-unknown">TKFNSL</span><span class="topo-outside">FPNLPP</span><span class="topo-membrane">GTLVVNLLAGLIIGTA</span><span class="topo-inside">LAYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTMSTFS</span><span class="topo-outside">VEVFALLQAGNYIWA</span><span class="topo-membrane">LTSVLVHVIGSLIMTALG</span><span class="topo-inside">FFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-inside">ITILFA</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>3</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>29</td>
      <td>24</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>51</td>
      <td>36</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>67</td>
      <td>52</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>84</td>
      <td>68</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>99</td>
      <td>85</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>117</td>
      <td>100</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>126</td>
      <td>118</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b2a">6B2A</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLII</span><span class="topo-outside">GTALAYFLRQPHLDPFWKLM</span><span class="topo-membrane">ITTGLCGGLSTMSTFSVEVF</span><span class="topo-inside">ALLQAGNY</span><span class="topo-membrane">IWALTSVLVHVIGSLIMT</span><span class="topo-outside">ALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>48</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>68</td>
      <td>49</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>88</td>
      <td>69</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>96</td>
      <td>89</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>97</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>125</td>
      <td>115</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b2b">6B2B</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">IKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTA</span><span class="topo-outside">LAYFLRQPHLDPFWKLM</span><span class="topo-membrane">ITTGLCGGLSTFSTMSVEVF</span><span class="topo-inside">ALLQAGNYIW</span><span class="topo-membrane">ALTSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILFA</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>68</td>
      <td>52</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>88</td>
      <td>69</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>98</td>
      <td>89</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>120</td>
      <td>99</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>126</td>
      <td>121</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b2d">6B2D</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">I</span><span class="topo-membrane">KSLFAVIIGGSVGCTLRWLLS</span><span class="topo-unknown">TKFNSL</span><span class="topo-outside">FPN</span><span class="topo-membrane">LPPGTLVVNLLAGLIIGTA</span><span class="topo-inside">LAYFLRQPHLDPF</span><span class="topo-membrane">WKLMITTGLCGGLSTFSTFSVEVFALL</span><span class="topo-outside">QAGN</span><span class="topo-membrane">YIWALTSVLVHVIGSLIMSALG</span><span class="topo-inside">FFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-inside">ITILF</span><span class="topo-unknown">A</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>3</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>29</td>
      <td>24</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>32</td>
      <td>30</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>51</td>
      <td>33</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>64</td>
      <td>52</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>91</td>
      <td>65</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>95</td>
      <td>92</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>117</td>
      <td>96</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>125</td>
      <td>118</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b2d">6B2D</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGT</span><span class="topo-outside">ALAYFLRQPHLDPFWKLM</span><span class="topo-membrane">ITTGLCGGLSTFSTFSVEVF</span><span class="topo-inside">ALLQAGNYIW</span><span class="topo-membrane">ALTSVLVHVIGSLIMSALGF</span><span class="topo-outside">FI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>68</td>
      <td>51</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>88</td>
      <td>69</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>98</td>
      <td>89</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>118</td>
      <td>99</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>125</td>
      <td>119</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554/eLife.69482

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kkr">7KKR</a></td>
      <td>3.11</td>
      <td>P4_1</td>
      <td>Ec2 WT with Multi-Wavelength Anomalous Diffraction Br⁻</td>
      <td>Br⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kka">7KKA</a></td>
      <td>2.5</td>
      <td>P4_1</td>
      <td>Ec2 S81A <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> with Br⁻</td>
      <td>Br⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kkb">7KKB</a></td>
      <td>2.9</td>
      <td>P4_1</td>
      <td>Ec2 S81C <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> with Br⁻</td>
      <td>Br⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kk8">7KK8</a></td>
      <td>2.7</td>
      <td>P4_1</td>
      <td>Ec2 S81T <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> with Br⁻</td>
      <td>Br⁻</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kk9">7KK9</a></td>
      <td>3.1</td>
      <td>P4_1</td>
      <td>Ec2 S81A/T82A <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> with Br⁻</td>
      <td>Br⁻</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: C-terminal hexahistidine tag, R25K mutation (enhances expression without affecting function), pET21 vector

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: C-terminal His-tag, R25K mutation (or R28K for Fluc-Bpe), C74A background for [AGGC](/xray-mp-wiki/reagents/ligands/n-acetyl-s-geranylgeranyl-l-cysteine/) mutants
- **Tag info**: C-terminal His6

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
      <td>Rh Protein from Nitrosomonas europaea from Nitrosomonas europaea Sf9 Insect Cell Expression System</td>
      <td>E. coli Sf9 Insect Cell Expression System</td>
      <td>—</td>
      <td></td>
      <td>Histidine-tagged Fluc Family of Fluoride Ion Channels <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> expressed In E. coli and purified via <a href="/xray-mp-wiki/reagents/additives/cobalt-hexamine/">Hexaamminecobalt(III) (Cobalt Hexamine)</a>(III) (Cobalt Hexamine)(III) (Cobalt Hexamine) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> per published protocols</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/cobalt-hexamine/">Hexaamminecobalt(III) (Cobalt Hexamine)</a>(III) (Cobalt Hexamine)(III) (Cobalt Hexamine) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Standard published protocol</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a></td>
      <td>—</td>
      <td>100 mM NaBr, 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> Ph 7.0 (for crystallography); 100 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> Ph 7.0 (for functional assays)</td>
      <td>Final <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a> step for both <a href="/xray-mp-wiki/methods/structure-determination/lcp-serial-millisecond-crystallography/">LCP-SMX</a> and functional <a href="/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/">Proteoliposome Reconstitution</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Monodisperse homodimers In [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) (Tris-HCl Buffer) (Tris(hydroxymethyl)aminomethane) appropriate for [IMISX In-Situ Serial Crystallography](/xray-mp-wiki/methods/crystallization/imisx-in-situ-crystallization/) or functional studies
**Yield**: Comparable to WT Sf9 Insect Cell Expression System levels
**Purity**: Monodisperse by gel filtration

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> (Sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Fluc Family of Fluoride Ion Channels-Ec2 + <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s9/">Monobody S9</a> complex (1:1 molar ratio)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diffractive Imaging of Imperfect Crystals formed over 3-7 days. Multi-Wavelength Anomalous Diffraction Br⁻ data collected At 13.5 keV. <a href="/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/">Rhodopsin N2C/D282C Mutant</a> Ec2-S81C Diffractive Imaging of Imperfect Crystals obtained Microbatch Crystallization Under Oil similar conditions with 100 mM Br⁻.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kkr">7KKR</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTAL</span><span class="topo-outside">AYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTFSTFSVEVF</span><span class="topo-inside">ALLQAGNYIWAL</span><span class="topo-membrane">TSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-membrane">I</span><span class="topo-outside">TILF</span><span class="topo-unknown">A</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>53</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>88</td>
      <td>68</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>100</td>
      <td>89</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>121</td>
      <td>101</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>125</td>
      <td>122</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kkr">7KKR</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kka">7KKA</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-outside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTA</span><span class="topo-inside">LAYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTFATFSVEVF</span><span class="topo-outside">ALLQAGNYIWA</span><span class="topo-membrane">LTSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-inside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>67</td>
      <td>52</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>88</td>
      <td>68</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>99</td>
      <td>89</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>120</td>
      <td>100</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kka">7KKA</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kkb">7KKB</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLL</span><span class="topo-inside">STKFNSLFPNLPPGT</span><span class="topo-membrane">LVVNLLAGLIIGTA</span><span class="topo-outside">LAYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLAGGLSTFC</span><span class="topo-inside">TFSVEVFALLQAGNYIWALTSVL</span><span class="topo-membrane">VHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>51</td>
      <td>38</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>67</td>
      <td>52</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>81</td>
      <td>68</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>104</td>
      <td>82</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>120</td>
      <td>105</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kkb">7KKB</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kk8">7KK8</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTAL</span><span class="topo-outside">AYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTFTTFSVEVF</span><span class="topo-inside">ALLQAGNYIWA</span><span class="topo-membrane">LTSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-membrane">I</span><span class="topo-outside">TILF</span><span class="topo-unknown">A</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>53</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>88</td>
      <td>68</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>99</td>
      <td>89</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>121</td>
      <td>100</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>125</td>
      <td>122</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kk8">7KK8</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kk9">7KK9</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFNSL</span><span class="topo-inside">FPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTAL</span><span class="topo-outside">AYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTFAAFSVEV</span><span class="topo-inside">FALLQAGNYIWAL</span><span class="topo-membrane">TSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">ITILF</span><span class="topo-unknown">A</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>29</td>
      <td>6</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>33</td>
      <td>30</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>53</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>87</td>
      <td>68</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>100</td>
      <td>88</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>120</td>
      <td>101</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kk9">7KK9</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554/eLife.18767

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kbn">5KBN</a></td>
      <td>2.48</td>
      <td>P 41</td>
      <td>F80I mutant with <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s9/">Monobody S9</a></td>
      <td>F-</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kom">5KOM</a></td>
      <td>2.69</td>
      <td>P 41</td>
      <td>F83I mutant with <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s9/">Monobody S9</a></td>
      <td>F-</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: C-terminal hexahistidine tag, R25K mutation (enhances expression without affecting function), pET21 vector

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kbn">5KBN</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIKSL</span><span class="topo-membrane">FAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-inside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTAL</span><span class="topo-outside">AYFLRQPHLDPFWKL</span><span class="topo-membrane">MITTGLCGGLSTISTFSVEV</span><span class="topo-inside">FALLQAGNYIWAL</span><span class="topo-membrane">TSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">       130       140       </span>
<span class="topo-line"><span class="topo-outside">ITILFA</span><span class="topo-unknown">TRGKAASLVPRGSGGHHHHHH</span></span>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27</td>
      <td>6</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>53</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>87</td>
      <td>68</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>100</td>
      <td>88</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>120</td>
      <td>101</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>126</td>
      <td>121</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kbn">5KBN</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kom">5KOM</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">IKSLFAVIIGGSVGCTLRWLLSTKFN</span><span class="topo-outside">SLFPNL</span><span class="topo-membrane">PPGTLVVNLLAGLIIGTALAY</span><span class="topo-inside">FLRQPHLDPF</span><span class="topo-membrane">WKLMITTGLCGGLSTFSTISVEVF</span><span class="topo-outside">ALLQAGNYIWA</span><span class="topo-membrane">LTSVLVHVIGSLIMTALGFFI</span></span>
<span class="topo-ruler">       130       140       </span>
<span class="topo-line"><span class="topo-membrane">ITIL</span><span class="topo-inside">F</span><span class="topo-unknown">ATRGKAASLVPRGSGGHHHHHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>27</td>
      <td>2</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>28</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>54</td>
      <td>34</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>64</td>
      <td>55</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>88</td>
      <td>65</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>99</td>
      <td>89</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>124</td>
      <td>100</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kom">5KOM</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">SVSSVPTKLEVVAATPTSLLISWDAPAVTVVHYVITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYTMYYSYSDLYSYSSPISINYRT</span></span>
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
      <td>97</td>
      <td>1</td>
      <td>96</td>
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

### Polar track delineates F⁻ conduction pathway

A [Oxygen Ladder in Selectivity Filters](/xray-mp-wiki/concepts/transport-mechanisms/oxygen-ladder-selectivity-filter/) in Selectivity Filters in Selectivity Filters of H-bond donating residues (the 'Polar track') was proposed to demark the F⁻ Side-Entry Ion Conduction Pathway Axillary Malodour Production Pathway through the Fluc Family of Fluoride Ion Channels Pore. Mutagenesis showed that polarity is functionally dispensable At several positions (S84, S102, S110) but critical At N41 and H106.

### Central phenylalanines coordinate F⁻ via quadrupolar interaction

[TEVC](/xray-mp-wiki/methods/quality-assessment/two-electrode-voltage-clamp/) [Conserved Core Triad in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) in GPCR Activation in GPCR Activation phenylalanines (F80, F83) directly coordinate F⁻ through an electropositive edge-On (quadrupolar) [Cross-Protomer Interactions in Proteorhodopsin Oligomers](/xray-mp-wiki/concepts/structural-mechanisms/cross-protomer-interaction-proteorhodopsin/) in Proteorhodopsin Oligomers in Proteorhodopsin Oligomers. No other aromatic or canonical E. coli Polar Lipids group substitutes for these Phe residues, with the sole exception of Met (F80M), which coordinates F⁻ through its partially Positive γ-methylene.

### T114 uses beta-branched methyl rather than hydroxyl

The [Conserved Core Triad in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) in GPCR Activation in GPCR Activation Thr114 At one end of the E. coli Polar Lipids track requires its β-branched [BNG](/xray-mp-wiki/reagents/detergents/n-methyl-beta-d-glucoside/) group for function, not its Surface Hydroxyl Acidity. Val and Ile are active substitutes while Ser (retaining the hydroxyl but lacking the β-methyl) abolishes TREX1 RNase Activity and DNA/RNA Hybrid Processing, suggesting a structural integrity role rather than direct F⁻ [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-ion-coordination/).

### Channsporter permeation mechanism

The Fluc Family of Fluoride Ion Channels Pore is densely packed with Side chains rather than a [Water Networks in GPCR Ligand Binding](/xray-mp-wiki/concepts/signaling-receptors/water-network-in-ligand-binding/) in GPCR Ligand Binding in GPCR Ligand Binding-filled tunnel, suggesting an unconventional 'channsporter' Allosteric Mechanism of Aspartate Carbamoyltransferase where F⁻ passage is accomplished by concomitant movements of Side-[Apolar Side-Chain Packing in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/apolar-side-chain-packing/) in Membrane Proteins in Membrane Proteins rotamers On a submicrosecond timescale.

### Vestibule anion-binding site on the fluoride permeation pathway

An Multi-Wavelength Anomalous Diffraction Br⁻ soak identified a Non-specific [Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain](/xray-mp-wiki/proteins/slc-transporters/human-ae1-anion-exchanger/) (Band 3) - C-Terminal Membrane Domain (Band 3) - C-Terminal Membrane Domain-AChBP Site At the bottom of the electropositive aqueous vestibule, coordinated by the [Conserved Core Triad in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) in GPCR Activation in GPCR Activation Ser81 and Thr82 sidechains (Fluc-Ec2 numbering). This Site is adjacent to the E. coli Polar Lipids track Ec2 ions. Mutagenesis (S81A, S81T, S81C) and MTSES modification of an [Engineered Disulfide Bridge Conformational Trapping](/xray-mp-wiki/concepts/structural-mechanisms/engineered-disulfide-bridge-trapping/) [AGGC](/xray-mp-wiki/reagents/ligands/n-acetyl-s-geranylgeranyl-l-cysteine/) At the adjacent Ile48 demonstrated that this Site is On the Ec2 permeation Axillary Malodour Production Pathway. The S81C [Rhodopsin N2C/D282C Mutant](/xray-mp-wiki/proteins/gpcr/rhodopsin-n2c-d282c-mutant/) showed pH-Dependent Quinone Binding in Photosynthetic Reaction Centers in Photosynthetic Reaction Centers Ec2 currents, suggesting [Substrate-Protonation Coupling in MFS Symporters](/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/) in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) Symporters in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) Symporters of the [AGGC](/xray-mp-wiki/reagents/ligands/n-acetyl-s-geranylgeranyl-l-cysteine/) thiol controls Alternating Access Mechanism.

### T-E-Y triad defines the opposite end of the pore

Sequence analysis of eukaryotic FEX [PE-PPE Fusion Proteins](/xray-mp-wiki/concepts/construct-design/pe-ppe-fusion-proteins/) identified three Pore-lining residues that follow eukaryotic Pore conservation patterns: Thr39 (TM2), Glu88 (TM3), and Tyr104 (TM4) In Fluc Family of Fluoride Ion Channels-Bpe. These form a [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)-bonded trio At the opposite end of the Pore from the vestibule [L-Serine](/xray-mp-wiki/reagents/substrates/l-serine/). Mutagenesis showed T39S, E88D, and Y104F retain function, while E88Q reduces currents to one-fifth of WT. T39S and Y104F increase Ec2 Molecular Dynamics Simulation (brief closures), suggesting the [Conserved Core Triad in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) in GPCR Activation in GPCR Activation stabilizes an open, Ec2-conducting GPCR Inactive Conformation.

### Anion recognition at the T-E-Y triad

Halides and pseudohalides inhibit Ec2 currents with a SLC6 Substrate Recognition by the GMG Motif series (OCN⁻ > SCN⁻ > NO₃⁻ > Cl⁻) correlated to pKa of the conjugate acid (Hydrogen bond acceptor strength). Oriented planar bilayer experiments showed the higher [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) [Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain](/xray-mp-wiki/proteins/slc-transporters/human-ae1-anion-exchanger/) (Band 3) - C-Terminal Membrane Domain (Band 3) - C-Terminal Membrane Domain-AChBP Site is On the [Conserved Core Triad in GPCR Activation](/xray-mp-wiki/concepts/signaling-receptors/conserved-core-triad/) in GPCR Activation in GPCR Activation Side of the Pore. The E88Q mutation nearly eliminates the ~60-fold difference In Cl⁻ vs OCN⁻ block (reducing it to ~4-fold), indicating Glu88 contributes to [Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain](/xray-mp-wiki/proteins/slc-transporters/human-ae1-anion-exchanger/) (Band 3) - C-Terminal Membrane Domain (Band 3) - C-Terminal Membrane Domain SLC6 Substrate Recognition by the GMG Motif. OCN⁻ blocks with Ki ~8 mM and is Competitive Antagonism in Cys-Loop Receptors in Cys-Loop Receptors with F⁻.

### Multi-ion alternating occupancy permeation mechanism

A Multi-Wavelength Anomalous Diffraction-Ion permeation Allosteric Mechanism of Aspartate Carbamoyltransferase is proposed for Fluc Family of Fluoride Ion Channels [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) involving [Alternating Ion-Bound Configurations in K+ Channel Selectivity Filters](/xray-mp-wiki/concepts/transport-mechanisms/alternating-ion-bound-configurations/) in K+ Channel Selectivity Filters in K+ Channel Selectivity Filters occupancy of [Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain](/xray-mp-wiki/proteins/slc-transporters/human-ae1-anion-exchanger/) (Band 3) - C-Terminal Membrane Domain (Band 3) - C-Terminal Membrane Domain-AChBP sites. Ec2 enters the electropositive vestibule (F0 Site At Ser81/Thr82), is electrostatically repelled into the narrow E. coli Polar Lipids track (F1 Site requiring serine rotamerization), then moves to F2 near Glu88. Electrostatic conflict with the E88 [Carboxylate Dyad in Oligosaccharyltransferase](/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/) in Oligosaccharyltransferase in Oligosaccharyltransferase causes it to swing out into solution, allowing Ec2 to exit. Sidechain rotamerization accompanies Ion movement, with AChBP sites assembled only as the TatA Substrate of E. coli [Rhomboid Protease Family](/xray-mp-wiki/concepts/protein-families/rhomboid-protease/) GlpG approaches.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-beta-D-maltoside (DM)</a> — Primary detergent for purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Used in initial purification steps
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)</a> — Buffer used in SEC and functional assays
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in cell lysis and affinity chromatography
- <a href="/xray-mp-wiki/reagents/protein-tags/monobody-s9/">Monobody S9</a> — Crystallization chaperone used for Ec2-Br⁻ complex structures
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/fluc-family/">Fluc Family of Fluoride Ion Channels</a> — Fluc-Ec2 is a member of the Fluc family
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/dual-topology-architecture/">Dual-Topology Architecture</a> — Fluc channels exhibit dual-topology homodimeric architecture
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Referenced in fluc-ec2 description
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/">Carboxylate Dyad in Oligosaccharyltransferase</a> — Referenced in fluc-ec2 description
- <a href="/xray-mp-wiki/concepts/signaling-receptors/polar-network-gpcr-activation/">Polar Network in GPCR Activation</a> — Referenced in fluc-ec2 description
- <a href="/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/">Fluoride Channel from B. pertussis (Bpe)</a> — Bpe is the closest Fluc homologue; identical fold with 33% sequence identity; both share dual-topology architecture
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — NaF used in Ec2 purification buffer (100 mM) for fluoride channel activity
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/dual-topology-channels/">Dual-Topology Channels</a> — Ec2 is a dual-topology homodimer; Ec2-S9 structure confirms conserved dual-topology architecture
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — SAD phasing with selenomethionine-labelled Ec2 used to solve the structure and avoid model bias
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — Referenced in ec2-fluoride-channel text
- <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> — Referenced in ec2-fluoride-channel text
