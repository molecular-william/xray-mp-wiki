---
title: "NaK Channel from Bacillus cereus"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04508, doi/10.1038##nsmb.1531, doi/10.1073##pnas.1013636108, doi/10.1073##pnas.1013643108, doi/10.1073##pnas.1111688108, doi/10.1107##s205225252100213x, doi/10.1073##pnas.0707324104]
verified: agent
uniprot_id: ['C2R3K4', 'Q81HW2']
---

# NaK Channel from Bacillus cereus


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/C2R3K4">UniProt: C2R3K4</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q81HW2">UniProt: Q81HW2</a>

<span class="expr-badge">Bacillus cereus</span>

## Overview

NaK is a non-selective tetrameric cation channel from Bacillus cereus that conducts both Na+ and K+ ions. It shares high sequence homology and overall architecture with the bacterial [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel, but its selectivity filter adopts a different architecture that results in loss of ion selectivity. Engineering of NaK mutants has enabled systematic analysis of ion selectivity mechanisms, including the NaK2K mutant which recapitulates a K+-selective filter with four contiguous ion binding sites. This paper demonstrates that a bridging hydrogen bond between an aromatic residue on the pore helix (Tyr55) and an acidic residue following the TVGYG signature sequence (Asp68) is essential for maintaining the four-sited K+ selective filter configuration.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature04508 (2 structures)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a></td>
      <td>2.4</td>
      <td>C2221</td>
      <td>NaK channel residues 1-103</td>
      <td>Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a></td>
      <td>2.8</td>
      <td>C2221</td>
      <td>NaK channel residues 1-104</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK channel in pQE60 vector

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>NaCl or KCl + <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a></td>
      <td>Protein purified as a tetramer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NaK channel at 30-35 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>36-42% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 200 mM CaCl2, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5-8.5, 4% t-butanol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of space group C2221</td>
    </tr>
  </tbody>
</table>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nsmb.1531 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a></td>
      <td>1.6</td>
      <td>I4</td>
      <td>NaKN delta 19 open conformation</td>
      <td>Various monovalent cations</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NaKN delta 19 (truncated construct)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>55-70% (v/v) <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD</a>, 1 mM CaCl2, 100 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.5</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals frozen in liquid propane; crystallization solution served as cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Open conformation, space group I4</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">LSFLLTLKRMLRACLRA</span><span class="topo-inside">WKDKEFQV</span><span class="topo-membrane">LFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGF</span><span class="topo-inside">IHKLAVNVQL</span><span class="topo-unknown">PSILSN</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>18</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>26</td>
      <td>19</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>45</td>
      <td>27</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>94</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>104</td>
      <td>95</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">LSFLLTLKRMLRACL</span><span class="topo-inside">RAWKDKEFQV</span><span class="topo-membrane">LFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGF</span><span class="topo-inside">IHKLAVNVQ</span><span class="topo-unknown">LPSILSN</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>16</td>
      <td>2</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>45</td>
      <td>27</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>94</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>103</td>
      <td>95</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">LSFLLTLKRMLRACLRA</span><span class="topo-inside">WKDKEFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGF</span><span class="topo-inside">IHKLAVNVQL</span><span class="topo-unknown">PSILSN</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>18</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>25</td>
      <td>19</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>45</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>94</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>104</td>
      <td>95</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ahy">2AHY</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">LSFLLTLKRMLRACL</span><span class="topo-inside">RAWKDKEFQV</span><span class="topo-membrane">LFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGF</span><span class="topo-inside">IHKLAVNVQ</span><span class="topo-unknown">LPSILSN</span></span>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>16</td>
      <td>2</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>45</td>
      <td>27</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>50</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>74</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>94</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>103</td>
      <td>95</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1013636108 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a></td>
      <td>1.62</td>
      <td>I4</td>
      <td>NaK2CNG-D mutant on NaKN delta 19 background</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>NaK2K (D66Y/N68D) on NaKN delta 19 background</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK mutants on NaKN delta 19 background

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
      <td>Expression</td>
      <td>E. coli culture</td>
      <td></td>
      <td></td>
      <td>Cloned into pQE60, expressed in E. coli XL1-Blue cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Detergent solubilization and purification</td>
      <td></td>
      <td>Monovalent salt + n-Decyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Same procedures as NaKN delta 19</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NaK2CNG-D and NaK2K mutants at 30-35 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, CaCl2, <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group I4, same conditions as NaKN delta 19</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1013643108 (3 structures, 12 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a></td>
      <td>1.62</td>
      <td>not specified</td>
      <td>NaK2CNG-D on NaKN delta 19 background</td>
      <td>K+, Na+, Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a></td>
      <td>1.58-1.95</td>
      <td>not specified</td>
      <td>NaK2CNG-E chimera on NaKN delta 19 background</td>
      <td>K+, Na+, Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a></td>
      <td>1.58-1.95</td>
      <td>not specified</td>
      <td>NaK2CNG-N chimera on NaKN delta 19 background</td>
      <td>K+, Na+, Ca2+</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK2CNG chimeras on NaKN delta 19 background with F92A mutation

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
      <td>Expression</td>
      <td>E. coli culture</td>
      <td></td>
      <td></td>
      <td>Cloned into pQE60, expressed in E. coli XL1-Blue cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Detergent solubilization and purification</td>
      <td></td>
      <td>Monovalent salt (NaCl, KCl) + n-Decyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Purified as tetramers</td>
    </tr>
    <tr>
      <td>Reconstitution</td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/">Proteoliposome Reconstitution</a></td>
      <td></td>
      <td>HEPES pH 7.4</td>
      <td>Reconstituted into 3:1 <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> lipid vesicles at 0.1 ug/mg protein/lipid ratio for functional studies</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NaK2CNG chimeras at 30-35 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, CaCl2, <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures between 1.58 and 1.95 A resolution</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3k0d">3K0D</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">MAKDK</span><span class="topo-outside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGETPPP</span><span class="topo-inside">QTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>8</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>51</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>71</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>74</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>113</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1111688108 (4 structures, 16 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3e8h">3E8H</a></td>
      <td>1.80</td>
      <td>not specified</td>
      <td>NaK_D66Y mutant</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a></td>
      <td>1.95</td>
      <td>not specified</td>
      <td>NaK_N68D mutant</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a></td>
      <td>1.55</td>
      <td>not specified</td>
      <td>NaK2K (D66Y/N68D) double mutant</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>NaK2K mutants (Y66F, Y55F, Y55W, D68E) and Kir-mimicking NaK (V59E/D66Y/F69R, Y55L/V59E/D66Y/F69R)</td>
      <td>not specified</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK mutants on NaKN delta 19 background with F92A mutation

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
      <td>Expression</td>
      <td>E. coli culture</td>
      <td></td>
      <td></td>
      <td>All NaK mutants cloned into pQE60</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Detergent solubilization and purification</td>
      <td></td>
      <td>Monovalent salt + n-Decyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Protein purification followed NaKN delta 19 protocol</td>
    </tr>
    <tr>
      <td>Reconstitution</td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/">Proteoliposome Reconstitution</a></td>
      <td></td>
      <td>Not specified</td>
      <td>Reconstituted into 3:1 <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> lipid vesicles at 0.2 ug/mg protein/lipid ratio for giant liposome patch clamp</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NaK mutants at 30-35 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Similar to NaKN delta 19 conditions</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>All mutant structures determined in open conformation between 1.70 to 1.95 A resolution</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e8h">3E8H</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WKDK</span><span class="topo-inside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-inside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-inside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>4</td>
      <td>19</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7</td>
      <td>23</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>112</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e8h">3E8H</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WKDK</span><span class="topo-inside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-inside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-inside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>4</td>
      <td>19</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7</td>
      <td>23</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>112</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e8h">3E8H</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WKDK</span><span class="topo-inside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-inside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-inside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>4</td>
      <td>19</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7</td>
      <td>23</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>112</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3e8h">3E8H</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WKDK</span><span class="topo-inside">EFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFYSTV</span><span class="topo-outside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-outside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-inside">KLAVNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-inside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>4</td>
      <td>19</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7</td>
      <td>23</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>68</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>93</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>95</td>
      <td>112</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>96</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ouf">3OUF</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">DFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILS</span><span class="topo-outside">NLVP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>103</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>110</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3t1c">3T1C</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-unknown">MAK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGYG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-outside">VNV</span><span class="topo-unknown">QLPSILSNL</span><span class="topo-outside">VP</span><span class="topo-unknown">R</span></span>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>25</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>82</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>100</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>94</td>
      <td>103</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>96</td>
      <td>112</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>97</td>
      <td>114</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1107##s205225252100213x (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6v8y">6V8Y</a></td>
      <td>1.53</td>
      <td>C2221</td>
      <td>NaKΔ19 (truncated NaK, residues 20-103) crystallized with both K+ and Na+ present</td>
      <td>K+, Na+</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v8y">6V8Y</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WK</span><span class="topo-outside">DKEFQVL</span><span class="topo-membrane">FVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTDF</span><span class="topo-membrane">GKIFTILYIFIGIGLVFGFIH</span><span class="topo-unknown">KLAVNVQLPSILS</span><span class="topo-outside">N</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>9</td>
      <td>21</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>27</td>
      <td>28</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>57</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>78</td>
      <td>76</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>97</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>92</td>
      <td>110</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v8y">6V8Y</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WK</span><span class="topo-outside">DKEFQVL</span><span class="topo-membrane">FVLTILTLISGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">IDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSN</span><span class="topo-outside">LVPR</span></span>
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
      <td>3</td>
      <td>9</td>
      <td>21</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>27</td>
      <td>28</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>32</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>103</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>111</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v8y">6V8Y</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WK</span><span class="topo-outside">DKEF</span><span class="topo-membrane">QVLFVLTILTLISGTIFY</span><span class="topo-inside">STVEGLRPIDA</span><span class="topo-unknown">LYFSVVTLTTVGD</span><span class="topo-inside">GNFSPQTDF</span><span class="topo-membrane">GKIFTILYIFIGIGLVFGFIHKLA</span><span class="topo-unknown">VNVQLPSILS</span><span class="topo-outside">N</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>6</td>
      <td>21</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>25</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>35</td>
      <td>43</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>48</td>
      <td>54</td>
      <td>66</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>67</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>81</td>
      <td>76</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>91</td>
      <td>100</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>92</td>
      <td>110</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v8y">6V8Y</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WK</span><span class="topo-outside">DKEFQ</span><span class="topo-membrane">VLFVLTILTLISGTIFY</span><span class="topo-inside">STVEGLRPIDA</span><span class="topo-unknown">LYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTDFG</span><span class="topo-membrane">KIFTILYIFIGIGLVFGFIH</span><span class="topo-outside">KLAVNV</span><span class="topo-unknown">QLPSILSN</span><span class="topo-outside">LVPR</span></span>
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
      <td>3</td>
      <td>7</td>
      <td>21</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>26</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>35</td>
      <td>43</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>49</td>
      <td>54</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>58</td>
      <td>68</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>78</td>
      <td>77</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>97</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>103</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>111</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.0707324104 (0 structures)</strong></summary>

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: NaK channel mutants in pQE60 vector

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
      <td>Expression</td>
      <td>E. coli culture</td>
      <td></td>
      <td></td>
      <td>Cloned into pQE60, expressed in E. coli XL1-Blue cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Detergent solubilization and purification</td>
      <td></td>
      <td>Monovalent salt (NaCl, RbCl, or LiCl) + n-Decyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Purified as tetramers in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> with monovalent salt for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Wild-type and mutant NaK channels at 30-35 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM CaCl2, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 37-42% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 4% <a href="/xray-mp-wiki/reagents/additives/tert-butanol/">tert-Butanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group C2221</td>
    </tr>
  </tbody>
</table>
</details>


## Biological / Functional Insights

### Ion conduction properties of NaK

Functional analysis using 86Rb flux assays shows that NaK can conduct both Na+ and K+ ions. A truncated form (NaKN delta 19) lacking the N-terminal M0 helix showed higher flux rates than full-length NaK. The channel conducts K+ ions better than Na+ ions and is unable to conduct Li+ or [NMG](/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/)+. Na+ and K+ ions bind at sites 3, 4 and the central cavity without preference, consistent with the non-selective nature of the channel.

### Cyclic nucleotide-gated channel pore architecture

The NaK selectivity filter sequence (TVGDG) resembles that of cyclic nucleotide-gated (CNG) channels, which also lack the tyrosine and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues from the conserved TVGYG sequence. The external Ca2+-binding site in NaK reveals the structural basis of external divalent cation blockage observed in CNG channels, relevant for visual transduction.

### Ion binding sites and divalent cation block

Electron density maps show ions binding at the extracellular entrance, along the selectivity filter, and in the central cavity. Monovalent cations bind at sites 3, 4 and the central cavity, while divalent cations (Ca2+) bind only at the extracellular entrance to the filter, formed by four carbonyl oxygen atoms from Gly67 residues. The NaK selectivity filter retains its proper conformation in both Na+ and K+ environments, unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) which requires K+ to stabilize the filter.

### Open conformation and inner helix bending at Gly87 gating hinge

The NaKN delta 19 structure reveals the intracellular gate in an open state. Inner helices develop a 34 degree bend at Gly87 (the conserved gating hinge) that splays the gate wide open. Inner helices also undergo a 45 degree clockwise twist. Outer helices tilt tangentially by about 11 degrees without twisting. The open NaK structure superimposes with [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) (PDB 1LNQ) with an r.m.s.d. of 0.74 A.

### Phe92 constriction point in open pore

In the open NaK pore, Phe92 forms a constriction point with an ion-pathway diameter of about 6.5 A — narrower than the open [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) channel (~9.5 A). The F92A mutation increases the ion-conduction pathway diameter to 10.5 A and enhances ion conduction rates as measured by 86Rb flux assays.

### Inter- and intrasubunit rearrangements during gating

Comparison of closed and open NaK structures reveals distinct rearrangements. In the closed state, Phe92 contacts a hydrophobic patch on the neighboring helix; in the open state, the hydrophobic patch slides two helical turns and forms new van der Waals contacts with Phe85. Intrasubunit interactions between inner and outer helices remain similar.

### Conservation of gating mechanics with K+ channels

The closed NaK structure (PDB 2AHY) superimposes well with closed [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) (PDB 1K4C) with an r.m.s.d. of 0.73 A. The open NaKN delta 19 structure superimposes with open [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) (PDB 1LNQ) with an r.m.s.d. of 0.74 A. These structural correlations confirm that gating mechanics are conserved between NaK and K+ channels.

### Mechanism of Ca2+ specificity at the NaK selectivity filter

The external Ca2+ binding site is formed by four backbone carbonyl oxygen atoms from Gly-67 of each subunit. The conserved acidic residue Asp-66 does not directly chelate Ca2+ but instead forms a hydrogen bond with the amide nitrogen of the Gly-67/Asn-68 peptide bond, polarizing the backbone and placing a partial negative charge on the Gly-67 carbonyl oxygen. D66N abolished Ca2+ binding, D66E enhanced it, and D66AS70E restored it.

### Second Ca2+ binding site within the NaK selectivity filter

In addition to the external site, a second Ca2+ binding site was identified at site 3 within the NaK selectivity filter. This intrapore site lacks acidic residues and can also bind monovalent cations, providing a structural basis for Ca2+ permeation through the NaK pore. The existence of two Ca2+ binding sites is consistent with functional studies of CNG channels.

### Ca2+ permeation demonstrated by 45Ca flux assay

Direct measurement of Ca2+ permeation through NaK was achieved using 45Ca flux assays in liposomes. Time-dependent accumulation of 45Ca was observed in NaK-containing liposomes but not in control liposomes. These data support the 'permeating block' model where Ca2+ both blocks monovalent currents and permeates the channel.

### CNG channel pore architecture revealed by NaK2CNG chimeras

The NaK2CNG-D, NaK2CNG-E, and NaK2CNG-N chimeras faithfully represent the pore architecture of cyclic nucleotide-gated (CNG) channels. Their selectivity filters contain three contiguous ion binding sites with a distinct architecture intermediate between NaK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/). Although NaK2CNG chimeras permeate Na+ and K+ equally well, Na+ and K+ bind with different ion-ligand geometries.

### Ca2+ binding mechanism in CNG channel selectivity filter mimics

High-resolution structures of NaK2CNG chimeras reveal that Ca2+ is exclusively chelated by backbone carbonyl oxygen atoms and not directly by the conserved acidic side chain (Glu/Asp). In NaK2CNG-E, the glutamate side chain (Glu66) is oriented tangential to the ion conduction pathway. Ca2+ binding positions differ among chimeras: NaK2CNG-E binds Ca2+ at site 3 only, NaK2CNG-D binds Ca2+ at sites 2, 3, and above the external entrance, and NaK2CNG-N binds Ca2+ only at the external funnel.

### Selectivity filter architecture of NaK

The NaK selectivity filter preserves only two cation-binding sites equivalent to sites 3 and 4 of a K+ channel selectivity filter. Unlike K+ channel selectivity filters that contain four equivalent K+-binding sites, NaK's GDG residues adopt different backbone conformations.

### Structural basis of ion selectivity in K+ channels

Comparison of NaK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) provides experimental demonstration that electrostatic repulsion between carbonyl oxygen atoms is not the origin of K+ over Na+ selectivity. Instead, protein atoms surrounding the ion-binding site confer size-selectivity through geometric constraints.

### Number of contiguous ion binding sites determines K+ selectivity

Engineering of NaK-based cation channel pores with two (NaK), three (NaK2CNG-D), or four (NaK2K) contiguous ion binding sites demonstrated that only the channel with four sites is K+ selective. Single channel electrophysiology revealed that NaK2K has higher single channel conductance for K+ than NaK2CNG-D.

### Bridging hydrogen bond between Tyr55 and Asp68 is essential for K+ selectivity

The Tyr66 side chain in NaK2K points into a hydrophobic pocket and forms a hydrogen bond with Thr60. The Asp68 side chain forms a bridging hydrogen bond with Tyr55 on the pore helix. Both interactions work in concert to maintain the filter architecture in a K+ selective four-sited configuration. Single mutations at either position (D66Y or N68D alone) are insufficient to render NaK K+ selective. Neutralizing Asp68 to Asn or extending to Glu both abolish K+ selectivity, demonstrating that both the negative charge and precise distance are essential.

### Conservation of bridging H-bond in eukaryotic Kv channels

The equivalent Trp415-Asp428 hydrogen bond in rat Kv1.6 is also essential for K+ selectivity. Mutations that disrupt this bond (W415F, D428N, D428E) led to significant loss of K+ selectivity. The W415Y mutant preserved selectivity but exhibited fast C-type inactivation, suggesting that destabilization of filter packing can trigger inactivation.

### Kir channels use a distinct salt bridge mechanism

Inward-rectifier K+ (Kir) channels use a conserved acid-base salt bridge (Glu-Arg) instead of the Tyr-Asp bridging H-bond to stabilize the filter in a four-sited configuration. Kir-mimicking NaK mutants (V59E/D66Y/F69R) retained selectivity, but additional mutations (Y55L) were needed to fully recapitulate Kir properties.

### Structural plasticity of the selectivity filter enables nonselective cation conduction

The 1.53 A X-ray structure of NaKΔ19 crystallized in space group C2221 (PDB 6v8y) reveals asymmetric conformations of Asp66 and Asn68 in the selectivity filter between the two subunits in the asymmetric unit, demonstrating structural plasticity. This asymmetry reveals a previously unseen side-entry Na+ ion binding site adjacent to the SF, formed by a backbone carbonyl flip of Asp66. MD simulations and ssNMR data confirm the dynamic nature of the top part of the selectivity filter. K+ ions bind at sites 3 and 4 (coordinated by Thr63, Val64 carbonyls and Thr63 hydroxyls), while Na+ is found in the vestibule (site 2) and at the side-entry binding site. No Na+ permeation was observed in MD simulations even at high voltage, suggesting the Na+-conductive state requires larger conformational plasticity throughout the SF. The coupling between inner helix opening and SF width is weaker in NaK than in K+-selective channels.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — NaK shares sequence homology and overall architecture with KcsA; structural comparison reveals selectivity filter differences
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mthk/">MthK (Methanobacterium thermoautotrophicum K+ Channel)</a> — Open NaK structure superimposes with open MthK (PDB 1LNQ)
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside (DM)</a> — Detergent used for NaK channel purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Reconstitution buffer for functional studies
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Crystallization buffer for NaK structures
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel</a> — Related K+ channel family
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/">Shaker Kv1.2 Potassium Channel</a> — Related voltage-gated K+ channel
- <a href="/xray-mp-wiki/methods/quality-assessment/proteoliposome-reconstitution/">Proteoliposome Reconstitution</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/">NMG</a> — Additive used in purification or crystallization buffers
