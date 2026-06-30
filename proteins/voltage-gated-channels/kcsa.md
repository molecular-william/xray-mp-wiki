---
title: "KcsA Potassium Channel"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1021##bi500525s, doi/10.1126##science.280.5360.69, doi/10.1016##j.jmb.2020.06.012, doi/10.1016##j.str.2012.03.027, doi/10.1038##nature09136, doi/10.1016##j.str.2016.02.021, doi/10.1038##35102009, doi/10.7554##eLife.28032, doi/10.1038##s41467-022-28866-9, doi/10.1038##NSMB929, doi/10.1038##nsmb.1703, doi/10.1073##pnas.0810663106, doi/10.1073##pnas.1314356110, doi/10.1073##pnas.1800559115, doi/10.1016##j.jmb.2021.167296, doi/10.1038##nsmb.1968, doi/10.1073##pnas.1105112108, doi/10.1371##journal.pbio.0050121, doi/10.1073##pnas.1901888116]
verified: false
---

# KcsA Potassium Channel

## Overview

KcsA is a prokaryotic potassium channel from Streptomyces lividans that serves as a model system for understanding potassium channel structure, gating, selectivity, and ion permeation. Cocrystal structures with symmetrical quaternary ammonium (QA) compounds TBA, THA, and TOA (Lenaeus et al., 2014) revealed a hydrophobic binding pocket between the inner helices and a lateral fenestration connecting the central cavity to the lipid bilayer. Long-chain QAs induce a nonconducting collapsed state of the selectivity filter, showing that QA compounds inhibit KcsA through both physical occlusion and allosteric regulation. The G77A and G77C mutant structures (PDB 6NFU, 6NFV) provided the first direct structural evidence for the 2,4-ion-bound configuration (water-K+-water-K+) within the selectivity filter, validating the alternating ion-bound configurations proposed by the canonical model of ion conduction. The channel forms a homotetramer with a central pore lined by the highly conserved TVGYG selectivity filter motif. It has been extensively studied by X-ray crystallography to understand ion conduction, selectivity, C-type inactivation, and the allosteric coupling between the activation gate and selectivity filter. Key studies have also revealed the structural basis of modal gating behavior, where Glu71 mutations stabilize distinct gating modes (high-Po, low-Po, and flicker) through changes in selectivity filter dynamics and ion occupancy.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1021##bi500525s (3 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2jks">2JKS</a></td>
      <td>2.40</td>
      <td>I4</td>
      <td>KcsA-L90C mutant with Fab, cocrystallized with TBA</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tetrabutylammonium/">TBA</a>, K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uuj">4UUJ</a></td>
      <td>2.40</td>
      <td>I4</td>
      <td>KcsA-L90C mutant with Fab, cocrystallized with THA</td>
      <td>THA, K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2w0f">2W0F</a></td>
      <td>2.40</td>
      <td>I4</td>
      <td>KcsA-L90C mutant with Fab, cocrystallized with TOA</td>
      <td>TOA, K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uuj">4UUJ</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110 </span>
<span class="topo-line"><span class="topo-inside">AAVALLLGSALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVT</span><span class="topo-membrane">LWGRCVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>16</td>
      <td>11</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>37</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>66</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uuj">4UUJ</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110 </span>
<span class="topo-line"><span class="topo-inside">AAVALLLGSALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVT</span><span class="topo-membrane">LWGRCVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>16</td>
      <td>11</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>37</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>66</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uuj">4UUJ</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110 </span>
<span class="topo-line"><span class="topo-inside">AAVALLLGSALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVT</span><span class="topo-membrane">LWGRCVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>16</td>
      <td>11</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>37</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>66</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4uuj">4UUJ</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110 </span>
<span class="topo-line"><span class="topo-inside">AAVALLLGSALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVT</span><span class="topo-membrane">LWGRCVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>16</td>
      <td>11</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>37</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>66</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2w0f">2W0F</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2w0f">2W0F</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2w0f">2W0F</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2w0f">2W0F</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
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
<summary><strong>doi/10.1126##science.280.5360.69 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1bl8">1BL8</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>Wild-type KcsA, L90C mutant used for native data collection</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity column</td>
      <td>—</td>
      <td></td>
      <td>Used for initial purification of KcsA</td>
    </tr>
    <tr>
      <td>Proteolytic cleavage</td>
      <td>Chymotrypsin proteolysis</td>
      <td>—</td>
      <td></td>
      <td>35 C-terminal amino acids cleaved</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified to homogeneity</td>
    </tr>
    <tr>
      <td>Detergent exchange</td>
      <td>Dialysis</td>
      <td>—</td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Final dialysis step against 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: KcsA in 5 mM [LDAO](/xray-mp-wiki/reagents/detergents/ldao/), 150 mM KCl, 50 mM Tris pH 7.5
**Purity**: Homogeneous by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KcsA at 5-10 mg/ml in 150 mM KCl, 50 mM Tris pH 7.5, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM CaCl2, 100 mM Hepes pH 7.5, 48% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals space group C2, a=128.8Å, b=68.9Å, c=112.0Å, beta=124.6°. For ion sites, crystals transferred to solutions where 150 mM KCl replaced by 150 mM RbCl or 150 mM CsCl.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1bl8">1BL8</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>28</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>40</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>56</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>97</td>
      <td>112</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1bl8">1BL8</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>28</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>40</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>56</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>97</td>
      <td>112</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1bl8">1BL8</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>28</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>56</td>
      <td>66</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>97</td>
      <td>112</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1bl8">1BL8</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       </span>
<span class="topo-line"><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>26</td>
      <td>26</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>43</td>
      <td>49</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>56</td>
      <td>66</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>64</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>97</td>
      <td>112</td>
      <td>119</td>
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
<summary><strong>doi/10.1016##j.jmb.2020.06.012 (5 structures, 20 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w0a">6W0A</a></td>
      <td>3.2</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Ba2+ (1 mM BaCl2, 5 mM KCl, open-gate, constricted filter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w0b">6W0B</a></td>
      <td>3.6</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Ba2+ (2 mM BaCl2, 5 mM KCl, open-gate, constricted filter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w0c">6W0C</a></td>
      <td>3.5</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Ba2+ (4 mM BaCl2, 5 mM KCl, open-gate, constricted filter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w0d">6W0D</a></td>
      <td>3.6</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Ba2+ (5 mM BaCl2, 5 mM KCl, open-gate, constricted filter)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w0e">6W0E</a></td>
      <td>3.5</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Ba2+ (10 mM BaCl2, 5 mM KCl, open-gate, constricted filter)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli XL-1 Blue
- **Expression construct**: Wild-type KcsA from pQE32 vector
- **Tag info**: Untagged

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
      <td>Avestin Emulsiflex C5 homogenizer</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 0.2 M NaCl, 1 mM PMSF, 20 ug/ml DNase I</td>
      <td>2L culture</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td>100,000g at 4 C for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM Tris pH 7.5, 0.15 M KCl + 40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (<a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>)</td>
      <td>Overnight incubation at 4 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion (soak)</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Solubilized wt KcsA in <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Wild-type KcsA crystallized in open-gate and closed-gate conformations under identical conditions. Open-gate obtained by soaking pre-grown crystals in BaCl2 solutions.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0a">6W0A</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">T</span><span class="topo-unknown">WFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>85</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>113</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0a">6W0A</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">T</span><span class="topo-unknown">WFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>85</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>113</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0a">6W0A</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">T</span><span class="topo-unknown">WFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>85</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>113</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0a">6W0A</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">T</span><span class="topo-unknown">WFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>85</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>113</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0b">6W0B</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-inside">A</span><span class="topo-unknown">LATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>109</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>110</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0b">6W0B</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-inside">A</span><span class="topo-unknown">LATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>109</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>110</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0b">6W0B</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-inside">A</span><span class="topo-unknown">LATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>109</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>110</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0b">6W0B</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-inside">A</span><span class="topo-unknown">LATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>109</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>92</td>
      <td>110</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0c">6W0C</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-outside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-outside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0c">6W0C</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-outside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-outside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0c">6W0C</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-outside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-outside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0c">6W0C</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-outside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-outside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0d">6W0D</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-unknown">TWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>112</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0d">6W0D</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-unknown">TWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>112</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0d">6W0D</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-unknown">TWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>112</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0d">6W0D</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-unknown">TWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>84</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>112</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0e">6W0E</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0e">6W0E</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0e">6W0E</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w0e">6W0E</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">AAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-unknown">ALATWFVGREQ</span><span class="topo-inside">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>35</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>59</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>92</td>
      <td>109</td>
      <td>119</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>120</td>
      <td>120</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1016##j.str.2012.03.027 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a></td>
      <td>2.4</td>
      <td>I4</td>
      <td>Y82C mutant of KcsA with Fab fragments</td>
      <td>Cd2+ (100 uM)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a></td>
      <td>2.5</td>
      <td>I4</td>
      <td>Y82C mutant of KcsA with nitroxide spin label and Fab</td>
      <td>Nitroxide spin label</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization / Cd2+ soaking with Fab</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Y82C-KcsA mutant in detergent</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3stl">3STL</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
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
<summary><strong>doi/10.1038##nature09136 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a></td>
      <td>3.3</td>
      <td>I4</td>
      <td>Wild-type KcsA</td>
      <td>Rb+ (fully open state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a></td>
      <td>3.2</td>
      <td>I4</td>
      <td>E71H-F103A double mutant</td>
      <td>Rb+ (closed state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3hpl">3HPL</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSALHW</span><span class="topo-outside">RAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVHTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVT</span><span class="topo-outside">AALATWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">RRGH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>120</td>
      <td>108</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>121</td>
      <td>124</td>
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
<summary><strong>doi/10.1016##j.str.2016.02.021 (5 structures, 20 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ec1">5EC1</a></td>
      <td>2.9</td>
      <td>I4</td>
      <td>KcsA V76ester mutant (S3 occupancy reduced)</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ec2">5EC2</a></td>
      <td>2.5</td>
      <td>I4</td>
      <td>KcsA V76ester + G77dA double mutant</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ebw">5EBW</a></td>
      <td>2.3</td>
      <td>I4</td>
      <td>KcsA G77ester mutant (S2 occupancy eliminated)</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ebl">5EBL</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>KcsA T75G mutant (S4 occupancy reduced)</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ebm">5EBM</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>KcsA backbone mutant</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec1">5EC1</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT?GY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec1">5EC1</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT?GY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec1">5EC1</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT?GY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec1">5EC1</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT?GY</span><span class="topo-inside">GDLCPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec2">5EC2</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-inside">ALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT??YG</span><span class="topo-outside">DLCPVT</span><span class="topo-membrane">LWGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>29</td>
      <td>23</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec2">5EC2</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-inside">ALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT??YG</span><span class="topo-outside">DLCPVT</span><span class="topo-membrane">LWGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>29</td>
      <td>23</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec2">5EC2</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-inside">ALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT??YG</span><span class="topo-outside">DLCPVT</span><span class="topo-membrane">LWGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>29</td>
      <td>23</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ec2">5EC2</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-inside">ALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATT??YG</span><span class="topo-outside">DLCPVT</span><span class="topo-membrane">LWGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>29</td>
      <td>23</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebw">5EBW</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGR</span><span class="topo-inside">HGSAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATTV?Y</span><span class="topo-outside">GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">R</span><span class="topo-unknown">RG</span></span>
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
      <td>19</td>
      <td>1</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>24</td>
      <td>20</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>123</td>
      <td>122</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebw">5EBW</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGR</span><span class="topo-inside">HGSAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATTV?Y</span><span class="topo-outside">GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">R</span><span class="topo-unknown">RG</span></span>
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
      <td>19</td>
      <td>1</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>24</td>
      <td>20</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>123</td>
      <td>122</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebw">5EBW</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGR</span><span class="topo-inside">HGSAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATTV?Y</span><span class="topo-outside">GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">R</span><span class="topo-unknown">RG</span></span>
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
      <td>19</td>
      <td>1</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>24</td>
      <td>20</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>123</td>
      <td>122</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebw">5EBW</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGR</span><span class="topo-inside">HGSAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWACETATTV?Y</span><span class="topo-outside">GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">R</span><span class="topo-unknown">RG</span></span>
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
      <td>19</td>
      <td>1</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>24</td>
      <td>20</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>115</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>123</td>
      <td>122</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebl">5EBL</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>124</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebl">5EBL</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>124</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebl">5EBL</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>124</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebl">5EBL</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-inside">RRGH</span><span class="topo-unknown">F</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>124</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebm">5EBM</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSA</span><span class="topo-outside">LHWRA</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>23</td>
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>24</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>50</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>109</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebm">5EBM</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSA</span><span class="topo-outside">LHWRA</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>23</td>
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>24</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>50</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>109</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebm">5EBM</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSA</span><span class="topo-outside">LHWRA</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>23</td>
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>24</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>50</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>109</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ebm">5EBM</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGSA</span><span class="topo-outside">LHWRA</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATGVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGH</span><span class="topo-unknown">F</span></span>
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
      <td>23</td>
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>24</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>50</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>108</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>109</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
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
<summary><strong>doi/10.1038##35102009 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1k4c">1K4C</a></td>
      <td>2.0</td>
      <td>I4</td>
      <td>KcsA-Fab complex, wild-type, high K+ (~200 mM)</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1k4d">1K4D</a></td>
      <td>2.3</td>
      <td>I4</td>
      <td>KcsA-Fab complex, wild-type, low K+ (~3 mM)</td>
      <td>K+, Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli

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
      <td>KcsA purification</td>
      <td>Affinity + size exclusion</td>
      <td>—</td>
      <td>50 mM Tris pH 7.5, 150 mM KCl + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>KcsA purified as described. 35 C-terminal amino acids cleaved by chymotrypsin.</td>
    </tr>
    <tr>
      <td>Fab purification</td>
      <td>Protein A affinity + ion exchange</td>
      <td>—</td>
      <td></td>
      <td>Mouse IgG from hybridoma culture. Fab by papain proteolysis + Q-Sepharose.</td>
    </tr>
    <tr>
      <td>KcsA-Fab complex formation</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>50 mM Tris pH 7.5, 150 mM KCl + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KcsA-Fab complex at 7-15 mg/mL in 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 50 mM magnesium acetate, 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a>, pH 5.0-5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> concentration increased to 40% in 2.5% increments</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4c">1K4C</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>24</td>
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4c">1K4C</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>24</td>
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4c">1K4C</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>24</td>
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4c">1K4C</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATWF</span><span class="topo-inside">VGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>24</td>
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>124</td>
      <td>115</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4d">1K4D</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4d">1K4D</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4d">1K4D</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1k4d">1K4D</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
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
<summary><strong>doi/10.7554##eLife.28032 (3 structures, 12 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vk6">5VK6</a></td>
      <td>2.25</td>
      <td>I4</td>
      <td>Locked-open KcsA E71A mutant (O/O state), chymotrypsin-truncated, Fab complex</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vke">5VKE</a></td>
      <td>2.37</td>
      <td>I4</td>
      <td>Locked-open KcsA Y82A mutant (O/I state), chymotrypsin-truncated, Fab complex</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vkh">5VKH</a></td>
      <td>2.25</td>
      <td>I4</td>
      <td>KcsA Y82A mutant, closed state, Fab complex</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli XL10-gold
- **Expression construct**: Locked-open KcsA (KcsA-OM, double-cysteine 28-118) with E71A or Y82A mutations, pQE70 vector
- **Tag info**: C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/), chymotrypsin-cleaved for crystallization

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
      <td>Overnight culture at 37 C with 2% <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> and 0.4 mg/ml <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a></td>
      <td>—</td>
      <td></td>
      <td>Diluted 100x next day</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Emulsiflex C3 homogenizer</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 150 mM KCl, 1 mM PMSF (Buffer A)</td>
      <td>Passed 3 times. Membranes collected at 100,000g for 1 hr.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>Buffer A + 20 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>2 hr incubation, insoluble spun down at 100,000g</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity resin</td>
      <td>—</td>
      <td>Buffer A, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 10 CV buffer A + 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. Eluted with buffer A + 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>.</td>
    </tr>
    <tr>
      <td>Fab complex formation and detergent exchange</td>
      <td>Chymotrypsin cleavage + Fab complex</td>
      <td>—</td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>Chymotrypsin-cut KcsA complexed with Fab antibody fragment. Exchanged into 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a> for crystallization.</td>
    </tr>
  </tbody>
</table>
**Final sample**: KcsA-Fab complex in 5 mM DM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Locked-open KcsA-Fab complex (E71A or Y82A mutant) in 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>24-27% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> (v/v), 50 mM magnesium acetate, 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 5.4-6.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E71A mutant diffracted to 2.25 A (PDB 5VK6), Y82A mutant to 2.37 A (PDB 5VKE), and Y82A-F103A closed mutant to 2.25 A (PDB 5VKH).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vk6">5VK6</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVATATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vk6">5VK6</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVATATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vk6">5VK6</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVATATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vk6">5VK6</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVATATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vke">5VKE</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRC</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>25</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vke">5VKE</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRC</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>25</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vke">5VKE</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRC</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>25</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vke">5VKE</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRC</span><span class="topo-membrane">AGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>25</td>
      <td>29</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vkh">5VKH</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vkh">5VKH</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vkh">5VKH</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vkh">5VKH</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSAGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1038##s41467-022-28866-9 (5 structures, 20 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mhr">7MHR</a></td>
      <td>2.9</td>
      <td>I4</td>
      <td>E71V KcsA mutant, closed-gate, 5 mM K+</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mhx">7MHX</a></td>
      <td>3.3</td>
      <td>I4</td>
      <td>E71V KcsA mutant, open-gate</td>
      <td>Ba2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mjt">7MJT</a></td>
      <td>2.7</td>
      <td>I4</td>
      <td>E71V KcsA mutant, closed-gate</td>
      <td>Ba2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mk6">7MK6</a></td>
      <td>3.0</td>
      <td>I4</td>
      <td>E71V KcsA mutant, open-gate, 0 mM K+/150 mM NaCl</td>
      <td>Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mub">7MUB</a></td>
      <td>3.0</td>
      <td>I4</td>
      <td>E71V KcsA mutant</td>
      <td>Ba2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion (soak)</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>E71V KcsA mutant in <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhr">7MHR</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhr">7MHR</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhr">7MHR</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhr">7MHR</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhx">7MHX</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhx">7MHX</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhx">7MHX</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mhx">7MHX</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mjt">7MJT</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-inside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>93</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mjt">7MJT</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-inside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>93</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mjt">7MJT</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-inside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>93</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mjt">7MJT</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-inside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>93</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mk6">7MK6</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mk6">7MK6</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mk6">7MK6</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mk6">7MK6</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mub">7MUB</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mub">7MUB</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mub">7MUB</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mub">7MUB</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-unknown">WR</span><span class="topo-outside">CAG</span><span class="topo-membrane">AATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVVTATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTA</span><span class="topo-outside">ALATWFVGQC</span><span class="topo-unknown">QQQ</span></span>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>25</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>83</td>
      <td>87</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>109</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>96</td>
      <td>119</td>
      <td>121</td>
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
<summary><strong>doi/10.1038##NSMB929 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2bob">2BOB</a></td>
      <td>2.75</td>
      <td>I4</td>
      <td>KcsA-L90C mutant with Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tetrabutylammonium/">TBA</a>, Tl+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2boc">2BOC</a></td>
      <td>2.75</td>
      <td>I4</td>
      <td>KcsA-L90C mutant with Fab</td>
      <td>TEAs, Tl+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Fab-KcsA-L90C complex at ~10 mg/ml in 150 mM TlNO3, 50 mM HEPES pH 7.5, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>, with 5 mM <a href="/xray-mp-wiki/reagents/ligands/tetrabutylammonium/">TBA</a> nitrate or 50 mM TEAs nitrate</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-25% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 50 mM magnesium acetate, 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a>, pH 5-5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Incrementally increasing precipitant, flash-cooled in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bob">2BOB</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bob">2BOB</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bob">2BOB</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bob">2BOB</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>124</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2boc">2BOC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2boc">2BOC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2boc">2BOC</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2boc">2BOC</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-outside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-outside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
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
<summary><strong>doi/10.1038##nsmb.1703 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a></td>
      <td>2.8</td>
      <td>I4</td>
      <td>Wild-type KcsA, Fab complex, Li+ only</td>
      <td>Li+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a></td>
      <td>2.75</td>
      <td>I4</td>
      <td>Wild-type KcsA, Fab complex, 3 mM K+ with Li+</td>
      <td>K+, Li+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3iga">3IGA</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHG</span><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALAT</span><span class="topo-inside">WFVGREQE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-inside">RRGH</span></span>
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
      <td>1</td>
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>25</td>
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>112</td>
      <td>87</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>124</td>
      <td>113</td>
      <td>124</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1073##pnas.0810663106 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a></td>
      <td>3.8</td>
      <td>I222</td>
      <td>Full-length KcsA (residues 22-160) with Fab2</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a></td>
      <td>2.6</td>
      <td>I4</td>
      <td>C-terminal domain fragment (residues 129-158) with Fab4</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression construct**: Full-length KcsA (residues 22-160)

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
      <td>Fab selection</td>
      <td>Phage display</td>
      <td>—</td>
      <td></td>
      <td>Biotinylated FL KcsA on streptavidin beads. 3 rounds selection.</td>
    </tr>
    <tr>
      <td>KcsA-Fab complex formation</td>
      <td>Complex formation</td>
      <td>—</td>
      <td>5 mM dodecyl maltopyranoside</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>FL KcsA-Fab2 complex (7 mg/ml) or FL KcsA-Fab4 complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>340 mM (NH4)2SO4, 11% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain K (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain M (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHW</span><span class="topo-membrane">RAAGAATVLLVIVLLAGSYLA</span><span class="topo-inside">VLAERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>27</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>44</td>
      <td>48</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>58</td>
      <td>66</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain N (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain K (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain M (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHW</span><span class="topo-membrane">RAAGAATVLLVIVLLAGSYLA</span><span class="topo-inside">VLAERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>27</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>44</td>
      <td>48</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>58</td>
      <td>66</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eff">3EFF</a> — Chain N (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWFVGREQERRGHFVRHSEKAAEEAYTRTT</span></span>
<span class="topo-ruler">       130         </span>
<span class="topo-line"><span class="topo-outside">RALHERFDRLERMLDDNRR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>41</td>
      <td>49</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>139</td>
      <td>108</td>
      <td>160</td>
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
<summary><strong>doi/10.1073##pnas.1314356110 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4msw">4MSW</a></td>
      <td>2.1</td>
      <td>—</td>
      <td>KcsA Y78-ester mutant (amide-to-ester at 2' bond, between Y78 and G79), Fab complex, 300 mM KCl</td>
      <td>K+ (reduced S2 occupancy)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli / in vitro
- **Expression construct**: KcsA residues 1-123, semisynthetic with ester substitutions at selectivity filter
- **Tag info**: Synthetic peptide with N-terminal Cys, recombinant thioester peptide (residues 1-69)

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
      <td>Protein semisynthesis</td>
      <td>Native chemical ligation</td>
      <td>—</td>
      <td></td>
      <td>Recombinant thioester peptide (residues 1-69) ligated to synthetic peptide (residues 70-123) containing ester linkage</td>
    </tr>
    <tr>
      <td>Folding</td>
      <td>Lipid vesicle folding</td>
      <td>—</td>
      <td></td>
      <td>Ligation product folded to native tetrameric state using lipid vesicles</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Lipid vesicle reconstitution</td>
      <td>—</td>
      <td></td>
      <td>Semisynthetic KcsA ester mutants purified and reconstituted into lipid vesicles for recording</td>
    </tr>
    <tr>
      <td>In vivo nonsense suppression (alternative)</td>
      <td>Amber suppression</td>
      <td>—</td>
      <td></td>
      <td>Used orthogonal tRNA/tRNA synthetase pair (Schultz group) to incorporate HPLA at amber stop codon, for full-length KcsA Y78-ester mutant</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Fab complex crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Y78-ester KcsA-Fab complex in 300 mM KCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> and refined to 2.1 A resolution. Electron density omit map confirmed transplanar Y78-ester linkage.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4msw">4MSW</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVG</span><span class="topo-outside">?GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>63</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4msw">4MSW</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVG</span><span class="topo-outside">?GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>63</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4msw">4MSW</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVG</span><span class="topo-outside">?GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>63</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4msw">4MSW</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALHWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVG</span><span class="topo-outside">?GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-inside">AALATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>8</td>
      <td>22</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>29</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>63</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>65</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>103</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1073##pnas.1800559115 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6by2">6BY2</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>KcsA T75A mutant, closed state, Fab complex</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6by3">6BY3</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>KcsA T75A mutant, locked-open (disulfide-bridged), open state</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6by2">6BY2</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLA</span><span class="topo-inside">VLAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATAVGYGDLYP</span><span class="topo-inside">VTLW</span><span class="topo-membrane">GRCVAVVVMVAGITSFGLVTAAL</span><span class="topo-outside">ATWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>26</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>41</td>
      <td>48</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>62</td>
      <td>63</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>66</td>
      <td>84</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>89</td>
      <td>88</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>103</td>
      <td>111</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6by3">6BY3</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-inside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLA</span><span class="topo-outside">VLAERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATAVGYGDLYP</span><span class="topo-outside">VTLW</span><span class="topo-membrane">GRCVAVVVMVAGITSFGLVTAAL</span><span class="topo-inside">ATWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>22</td>
      <td>28</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>48</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>58</td>
      <td>63</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>62</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>85</td>
      <td>88</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>96</td>
      <td>111</td>
      <td>121</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1016##j.jmb.2021.167296 (4 structures, 16 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a></td>
      <td>2.64</td>
      <td>P4</td>
      <td>KcsA W67F mutant, pre-open state, +TBA +Fab</td>
      <td>K+, <a href="/xray-mp-wiki/reagents/ligands/tetrabutylammonium/">TBA</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a></td>
      <td>2.72</td>
      <td>I4</td>
      <td>KcsA W67F mutant, locked-open (disulfide crosslinked), pre-inactivated state</td>
      <td>K+ (reduced occupancy at S2 site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m2j">7M2J</a></td>
      <td>3.20</td>
      <td>I4</td>
      <td>Wild-type KcsA, locked-open (disulfide crosslinked), inactivated state</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7rp0">7RP0</a></td>
      <td>not specified</td>
      <td>I4</td>
      <td>KcsA Y82A mutant, closed state, +TBA +Fab</td>
      <td>K+, <a href="/xray-mp-wiki/reagents/ligands/tetrabutylammonium/">TBA</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2h">7M2H</a> — Chain O (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPMLSGLLARLVKLLLGRHGS</span><span class="topo-outside">ALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQE</span></span>
<span class="topo-ruler">     </span>
<span class="topo-line"><span class="topo-outside">RRGHF</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>23</td>
      <td>25</td>
      <td>23</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>62</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>79</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>112</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2i">7M2I</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WR</span><span class="topo-membrane">CAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALFWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALATWFV</span><span class="topo-outside">GQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>2</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>25</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>90</td>
      <td>87</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2j">7M2J</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2j">7M2J</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2j">7M2J</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m2j">7M2J</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90      </span>
<span class="topo-line"><span class="topo-outside">WRCA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGQCQQQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>37</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>54</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>61</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>86</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>96</td>
      <td>112</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7rp0">7RP0</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7rp0">7RP0</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7rp0">7RP0</a> — Chain I (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7rp0">7RP0</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVETATTVGYG</span><span class="topo-outside">DLAPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVTAALA</span><span class="topo-inside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Inside</td>
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
<summary><strong>doi/10.1038##nsmb.1968 (2 structures, 8 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3or7">3OR7</a></td>
      <td>2.30</td>
      <td>I4</td>
      <td>KcsA E71I mutant in complex with Fab fragment</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3or6">3OR6</a></td>
      <td>2.70</td>
      <td>I4</td>
      <td>KcsA E71Q mutant in complex with Fab fragment</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: KcsA Glu71 mutants (E71I, E71Q) cloned in pQE32 vector
- **Tag info**: Co2+-based metal-chelate chromatography (Talon resin)

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
      <td>Cell growth and membrane preparation</td>
      <td>Homogenization and centrifugation</td>
      <td>—</td>
      <td>PBS buffer</td>
      <td>Cells homogenized, membranes pelleted at 100,000g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>PBS buffer + Dodecylmaltoside</td>
      <td>Membrane pellets solubilized with PBS buffer containing dodecylmaltoside at room temperature</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Co2+-based metal-chelate chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">Talon</a> resin (Clontech)</td>
      <td>PBS with dodecylmaltoside</td>
      <td>Purified via metal-chelate chromatography</td>
    </tr>
    <tr>
      <td>Quality check</td>
      <td>Gel-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/resins/superdex-200">Superdex-200</a> column (GE Healthcare)</td>
      <td></td>
      <td>Quality of purified protein checked by gel-exclusion chromatography</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KcsA E71I or E71Q mutant in complex with Fab fragment</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of E71I (2.3 A) and E71Q (2.7 A) obtained as Fab complexes. Structures solved by molecular replacement using WT KcsA (1K4C) as search model. Selectivity filter built with side chain density corresponding to Val76, Tyr78 and Asp80 as markers.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or7">3OR7</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVITATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>29</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>92</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or7">3OR7</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVITATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>29</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>92</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or7">3OR7</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVITATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>29</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>92</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or7">3OR7</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-inside">SAL</span><span class="topo-membrane">HWRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-outside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVITATTVGYG</span><span class="topo-outside">DLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALATW</span><span class="topo-inside">FVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>29</td>
      <td>25</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>63</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>80</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>92</td>
      <td>87</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>114</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or6">3OR6</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVQTATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or6">3OR6</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVQTATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or6">3OR6</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVQTATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3or6">3OR6</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100   </span>
<span class="topo-line"><span class="topo-outside">SALH</span><span class="topo-membrane">WRAAGAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITY</span><span class="topo-unknown">PRALWWSVQTATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRCVAVVVMVAGITSFGLVTAALA</span><span class="topo-outside">TWFVGREQERRGH</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>22</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>26</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>41</td>
      <td>51</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>90</td>
      <td>87</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>112</td>
      <td>124</td>
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
<summary><strong>doi/10.1073##pnas.1105112108 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3pjs">3PJS</a></td>
      <td>3.9</td>
      <td>I222</td>
      <td>Constitutively open FL KcsA mutant with Fab2, full-length (residues 22-160)</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>FL KcsA-Fab2 complex from constitutively open mutant</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M Na/K phosphate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/bis-tris-propane/">Bis-Tris Propane</a> pH 7.5, 10% PEG3350</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Series of modified well solutions with increasing glycerol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Isomorphous with closed FL KcsA-Fab2 (3EFF) crystals. Data collected at APS beamline 23ID, processed by HKL2000. Structure solved by molecular replacement using Fab2 and closed FL KcsA as search models. Refined with CNS.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjs">3PJS</a> — Chain K (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHPPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALQWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVL</span><span class="topo-inside">AERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWF</span></span>
<span class="topo-ruler">       130       140       150       160      </span>
<span class="topo-line"><span class="topo-outside">VGQEQQQQQQFVRHSEKAAEEAYTRTTRALHERFDRLERMLDDNRR</span></span>
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
      <td>1</td>
      <td>27</td>
      <td>-5</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>55</td>
      <td>30</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>71</td>
      <td>50</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>85</td>
      <td>66</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>113</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>166</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjs">3PJS</a> — Chain L (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHPPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALQWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAVLA</span><span class="topo-inside">ERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWF</span></span>
<span class="topo-ruler">       130       140       150       160      </span>
<span class="topo-line"><span class="topo-outside">VGQEQQQQQQFVRHSEKAAEEAYTRTTRALHERFDRLERMLDDNRR</span></span>
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
      <td>1</td>
      <td>27</td>
      <td>-5</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>30</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>71</td>
      <td>51</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>85</td>
      <td>66</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>113</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>166</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjs">3PJS</a> — Chain M (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHPPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALQWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGY</span><span class="topo-inside">GDLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWF</span></span>
<span class="topo-ruler">       130       140       150       160      </span>
<span class="topo-line"><span class="topo-outside">VGQEQQQQQQFVRHSEKAAEEAYTRTTRALHERFDRLERMLDDNRR</span></span>
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
      <td>1</td>
      <td>27</td>
      <td>-5</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>54</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>49</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>84</td>
      <td>66</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>92</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>113</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>166</td>
      <td>108</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3pjs">3PJS</a> — Chain N (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHPPMLSGLLARLVKLLLGRHG</span><span class="topo-outside">SALQWRAA</span><span class="topo-membrane">GAATVLLVIVLLAGSYLAV</span><span class="topo-inside">LAERGAPGAQLITYPRA</span><span class="topo-unknown">LWWSVETATTVGYG</span><span class="topo-inside">DLYPVTL</span><span class="topo-membrane">WGRLVAVVVMVAGITSFGLVT</span><span class="topo-outside">AALATWF</span></span>
<span class="topo-ruler">       130       140       150       160      </span>
<span class="topo-line"><span class="topo-outside">VGQEQQQQQQFVRHSEKAAEEAYTRTTRALHERFDRLERMLDDNRR</span></span>
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
      <td>1</td>
      <td>27</td>
      <td>-5</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>35</td>
      <td>22</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>54</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>49</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>85</td>
      <td>66</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>113</td>
      <td>87</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>166</td>
      <td>108</td>
      <td>160</td>
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
<summary><strong>doi/10.1371##journal.pbio.0050121 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: KcsA A98G mutant (referred to as wild-type), residues 1-123
- **Tag info**: Untagged, chymotrypsin-cleaved

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
      <td>Expression and lysis</td>
      <td>Standard KcsA expression and purification</td>
      <td>—</td>
      <td></td>
      <td>Expressed and purified as described in Zhou Y, MacKinnon R (2003)</td>
    </tr>
    <tr>
      <td>Proteolytic cleavage</td>
      <td>Chymotrypsin proteolysis</td>
      <td>—</td>
      <td></td>
      <td>C-terminal residues cleaved to produce truncated KcsA tetramer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>50 mM Tris pH 7.5, 20 mM KCl, 100 mM NaCl + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>)</td>
      <td>Purified tetramer concentrated to 10 mg/ml</td>
    </tr>
    <tr>
      <td>Buffer exchange</td>
      <td>Dialysis</td>
      <td>—</td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a></td>
      <td>Extensively dialyzed against desired <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> buffer (25 mM HEPES pH 7.5, 100 mM NaCl or LiCl, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm">DM</a>)</td>
    </tr>
  </tbody>
</table>
**Final sample**: KcsA at 71-142 uM in 25 mM HEPES pH 7.5, 100 mM NaCl (or LiCl), 5 mM DM
**Purity**: Homogeneous

</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1901888116 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and mutants from Streptomyces lividans, expressed from pQE32 vector
- **Notes**: Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 3 h. Also expressed using protein semisynthesis (native chemical ligation) for amide-to-ester mutants.

**Crystallization:**



</details>


## Biological / Functional Insights

### Hydrophobic binding pocket for quaternary ammonium compounds

Cocrystal structures of KcsA with TBA, THA, and TOA (PDB 2JKS, 4UUJ, 2W0F) reveal a hydrophobic binding pocket between the inner helices of KcsA. The pocket provides insight into the binding site and blocking mechanism of hydrophobic QAs. Access to the pocket is controlled by the rotameric state of residue F103, which is altered by binding of long-chain blockers. The octyl chain of TOA interacts with outer helix residue L36, demonstrating that drug binding is not confined to the inner helix but involves outer helix residues when the ligand penetrates deeply.

### Lateral fenestration connecting central cavity to lipid bilayer

Structures of KcsA with THA and TOA reveal a structurally hidden pathway between the central cavity and the outside membrane environment, reminiscent of lateral fenestrations observed in bacterial sodium channels. Access to this fenestration is controlled by small conformational changes in the pore wall, specifically the rotameric state of F103.

### Long-chain QAs induce selectivity filter collapse and nonconducting state

TBA binding does not alter the conductive state of the selectivity filter in the presence of 150 mM K+. In contrast, TOA (and THA) induce a collapsed, nonconducting conformation characterized by only two K+ ions bound, an altered hydrogen bond network, and binding of three water molecules. The octyl chain of TOA pushes the pore helix upward, forcing the selectivity filter into a nonconducting state. This demonstrates that long-chain QAs inhibit KcsA through two mechanisms: physical occlusion and allosteric regulation via promotion of slow inactivation.

### Increasing QA binding affinity with alkyl-chain length

Functional stopped-flow fluorescence assays with ANTS-loaded vesicles show incremental increase in QA binding affinity with increasing alkyl-chain length. TBA has an inhibition constant of ~120 uM. The number of van der Waals interactions increases incrementally from TBA to THA to TOA, consistent with the observed increase in affinity. The hexyl chain of THA interacts with T74, G99, I100, and F103; the octyl chain of TOA adds interactions with L36, S102, and additional main-chain contacts.

### Stabilization of the 2,4-ion-bound configuration by G77A and G77C mutants

Tilegenova et al. (2019) solved the crystal structures of KcsA G77A (PDB 6NFU, 2.09 A) and G77C (PDB 6NFV, 2.13 A) mutants that stabilize the 2,4-ion-bound configuration (water-K+-water-K+) of the selectivity filter. In these structures, K+ ions are bound only at the S2 and S4 sites, with water molecules at S1 and S3. This directly contradicts the direct knock-on model (which predicts 3 K+ ions bound in these mutants) and provides strong structural evidence for the canonical model of alternating 1,3- and 2,4-ion-bound configurations. The G77A mutant showed wild-type-like ion selectivity and apparent K+-binding affinity (Kd = 0.29 mM by [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/)), but lacked C-type inactivation and had markedly reduced single-channel conductance (~1.95 pS vs ~63 pS for WT).

### Inverted teepee architecture of the K+ channel pore

The KcsA structure revealed that four identical subunits create an inverted teepee, or cone, cradling the selectivity filter at its outer end. The inner helices are tilted ~25 degrees from the membrane normal and packed as a bundle near the intracellular side. This architecture likely generalizes to cyclic nucleotide-gated channels, Na+ and Ca2+ channels.

### Selectivity filter mechanism: carbonyl oxygen coordination and structural rigidity

The selectivity filter is lined exclusively by main chain carbonyl oxygen atoms from the K+ channel signature sequence (TVGYG). The filter is held open by structural constraints (aromatic cuff of Tyr and Trp residues acting like molecular springs) so that dehydrated K+ ions fit precisely but smaller Na+ ions cannot be properly coordinated. This explains the 10,000-fold selectivity for K+ over Na+.

### Water-filled cavity and helix dipoles overcome electrostatic barrier

A large 10-A diameter water-filled cavity at the membrane center surrounds a hydrated cation, overcoming the electrostatic destabilization of the low-dielectric bilayer. Four pore helices point at the cavity center with their C-termini, providing a cation-attractive helix dipole potential that further stabilizes the ion.

### Multi-ion conduction and electrostatic repulsion

The selectivity filter contains two K+ ions about 7.5 A apart. Electrostatic repulsion between the two ions overcomes the attractive force between each K+ and the carbonyl oxygens, allowing rapid conduction (up to 10^8 ions/s) despite high selectivity. This resolves the apparent paradox of how a highly selective filter can conduct at near-diffusion-limited rates.

### K+ hydration in the central cavity

The 2.0 A resolution KcsA-Fab structure revealed a fully hydrated K+ ion at the centre of the central cavity, coordinated by eight discrete water molecules in square antiprism geometry.

### Two selectivity filter structures under high and low K+

Low-K+ structure (1K4D, 3 mM K+) shows pinched non-conductive filter. High-K+ structure (1K4C, 200 mM K+) shows conductive conformation. This provides physical mechanism for filter response to channel gating.

### Individual ion binding sites play distinct roles in C-type inactivation

Amide-to-ester backbone mutagenesis reveals specific roles: V76ester (S3) slows recovery ~30-fold; G77ester and Y78ester (S2) impair inactivation; T75G (S4) slows recovery; G79ester (S1) has no effect on inactivation or recovery.

### S2 site occupancy is linked to C-type inactivation

Using amide-to-ester substitutions in the KcsA selectivity filter, the Y78-ester mutation (2' amide bond) eliminates K+ binding at the S2 site and dramatically reduces C-type inactivation. The G79-ester (1' amide bond) does not affect inactivation despite reduced S1 occupancy. The G77-ester (3' amide bond) also reduces inactivation. These results link C-type inactivation to ion occupancy specifically at the S2 site. A [KVAP](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) Y199-ester mutant (equivalent to Y78 in KcsA) also shows slowed inactivation, demonstrating conservation of the S2-dependent mechanism.

### Open-gate conformation of wild-type KcsA

Wild-type KcsA crystallized in both open-gate and closed-gate conformations. Open-gate has C-alpha distance at Thr112 of ~23 A vs closed-gate ~12 A.

### Cd2+-induced C-type inactivation and metal bridge formation

External Cd2+ enhances C-type inactivation rate in Y82C-KcsA via metal-bridge formation between adjacent subunits.

### Conformational coupling between activation gate and selectivity filter

The gating cycle of K+ channels is defined by four kinetic states. Opening of the activation gate stabilizes the non-conductive filter conformation; filter inactivation stabilizes the closed activation gate.

### TEA blockade mechanism via potassium analog mechanism

Co-crystal structures with [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) (2BOB) and TEAs (2BOC) reveal [TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) blocks by acting as a potassium analog at the dehydration transition step.

### Full-length KcsA C-terminal 4-helix bundle structure

Full-length KcsA (3.8 A) reveals a well-defined 4-helix bundle projecting ~70 A toward cytoplasm, formed by residues 136-160.

### Ion selectivity by size recognition rather than charge density

Using isothermal titration calorimetry ([ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/)) and X-ray crystallography, Lockless et al. (2007) showed that KcsA selectivity depends on ion size (volume) rather than charge density. K+ (1.33 A) and Rb+ (1.48 A) bind and stabilize the conductive filter conformation, while Na+ (0.95 A) cannot. Ba2+ (1.35 A) binds like K+ despite double charge, while smaller Mg2+ (0.65 A) and Ca2+ (0.99 A) do not bind. This demonstrates the channel recognizes ionic radius, not electrostatic field strength, consistent with the "snug fit" hypothesis.

### Atomic-resolution gating cycle of KcsA

The gating cycle comprises four states: C/O (closed-conductive), O/O (open-conductive), O/I (open-inactivated), and C/I (closed-inactivated). The Locked-open E71A mutant (PDB 5VK6, 2.25 A) captures the transient O/O state with a fully conductive selectivity filter containing 4 K+ ions in canonical 1,3 and 2,4 configurations and a 22 A activation gate opening. The Locked-open Y82A mutant (PDB 5VKE, 2.37 A) captures the O/I state with collapsed filter at Gly77 (6 A Cα-Cα vs 8 A in conductive), Val76 carbonyl flipped out, and 2 K+ ions at positions 1 and 4 only.

### Inactivating water network stabilizes collapsed filter

Three 'inactivating water molecules' were resolved behind the selectivity filter in the O/I state, hydrogen-bonded to Val76 carbonyl, Glu71 carbonyl, Gly77 amide nitrogen, and Asp80 side chains. These waters stabilize the collapsed filter conformation. Diffusion of water into the 'inactivation cavity' guarded by Tyr82 (Thr449 in Shaker) determines the rate and magnitude of C-type inactivation.

### Allosteric coupling between activation gate and selectivity filter

Phe103 clashes with Ile100 and Thr74/75 of the signature sequence upon gate opening, deforming the pore helix and triggering compensatory structural changes at the selectivity filter. This coupling underlies the mechanistically-linked activation and C-type inactivation gating processes.

### T75A mutation inverts allosteric coupling between activation gate and selectivity filter

Substitution of the second Threonine (Thr75 in KcsA, Thr480 in hKv1.5, Thr442 in Shaker) within the TTVGYGD signature sequence with Alanine inverts the allosteric coupling between the activation gate and selectivity filter. In these T-to-A mutants, the selectivity filter is inactive (C-type inactivated) in the closed state and becomes conductive and noninactivating upon activation gate opening. Crystal structures of KcsA T75A closed (PDB 6BY2) show a deep C-type inactivated conformation with filter constriction at Gly77 and only two K+ ions bound, while the open T75A structure (PDB 6BY3) shows a fully conductive filter with three K+ ions bound, essentially identical to the noninactivating E71A mutant (PDB 5VK6). This demonstrates that closed-state inactivation can occur via structural collapse of the selectivity filter.

### W67F mutation reveals pre-open and pre-inactivated gating intermediates

The KcsA W67F mutant (Trp67Phe in the pore helix) shows severely reduced C-type inactivation and enhanced activation rate. The 2.64 A structure (PDB 7M2H) captures a "pre-open" state — an intermediate along the activation gate opening trajectory where the F103 side chain has flipped but the inner helices are only partially displaced. The 2.72 A locked-open structure (PDB 7M2I) captures a "pre-inactivated" state where the E71 side chain has switched to the rotamer associated with filter constriction, but the selectivity filter remains conductive because S2 site ion occupancy is lost. CW-EPR spectroscopy shows altered pH dependence of activation (pKa 4.51 vs 4.18 for WT). These findings identify F103, E71, and the S2 site as three key nodes in the allosteric pathway coupling the activation gate to the selectivity filter.

### Glu71 mutations stabilize three distinct gating modes in KcsA

Chakrapani et al. (2011) showed that mutations at the pore-helix position Glu71 unmask a series of kinetically distinct gating modes in KcsA in a side chain-specific way. E71A stabilizes high-Po (open probability) mode with long opening bursts and few short intraburst closures. E71I stabilizes a low-Po mode with similar mean open and closed times. E71Q stabilizes a high-frequency flicker mode with very short open and closed sojourns. These three gating modes mirror those seen in wild-type KcsA and are defined by three nonconductive states: slow inactive (Is, tau ~100 ms), intermediate inactive (Ii, tau 1-10 ms), and flicker (F, tau 0.1-0.5 ms). The results demonstrate that specific interactions in the side chain network surrounding the selectivity filter, in concert with ion occupancy, alter the relative stability of pre-existing conformational states of the pore.

### Crystal structures of E71I and E71Q reveal subtle changes in ion occupancy

Crystal structures of KcsA E71I (PDB 3OR7, 2.3 A) and E71Q (PDB 3OR6, 2.7 A) show no major backbone conformational changes in the selectivity filter, which adopts a conductive conformation similar to closed KcsA structures. However, one-dimensional electron density profiles along the central symmetry axis reveal subtle differences in ion occupancy at binding sites S1-S4. The E71Q mutant shows altered ion distribution compared to WT, with changes in the relative peak heights at the K+ binding sites. These occupancy differences correlate with the distinct gating kinetics observed electrophysiologically.

### Val76 carbonyl reorientation associated with flicker gating in E71Q

Molecular dynamics simulations of KcsA mutants revealed that only the flicker-prone E71Q mutant shows a considerable increase in the frequency and lifetime of Val76 carbonyl reorientation compared to WT, E71A, and E71I. The dwell-time ratio between the flicker and open states in E71Q (~40:60) mirrors the ratio of outward-facing to straight conformations of the Val76 carbonyl. This suggests that reorientation of the Val76 carbonyl is associated with the conformational changes leading to short-lived flicker states in single-channel recordings.

### Asp80 side chain flipping in gating mode mutants

Molecular dynamics simulations show that the Cα-Cα distance between Glu71 and Asp80 has a very narrow distribution in WT KcsA, indicative of a strong interaction. In contrast, E71Q and E71I show a broader distribution with a distinct second population corresponding to channels with flipped Asp80 side chain. This dual-population behavior is observed in all gating mode mutants at position 71, suggesting that overall mobility of the Asp80 side chain is enhanced when interaction with Glu71 is lost.

### Open conformation of full-length KcsA solved at 3.9 A

Using a constitutively open mutant and chaperone-assisted crystallography with Fab2 antibody fragments, the structure of full-length KcsA in the open conformation was determined at 3.9 A resolution in space group I222. The crystals were highly isomorphous with the closed FL KcsA-Fab2 form (3EFF), allowing direct comparison via Fourier difference maps in the same unit cell. The structure reveals that the activation gate expands approximately 20 A and generates side windows large enough to accommodate hydrated K+ ions.

### Activation gate expansion strains C-terminal bulge helices

Movement of the inner gate helix (TM2) is transmitted to the C-terminus as a straightforward expansion, leading to an upward movement and insertion of the top third of the bulge helix (residues 118-135) into the membrane. The four-helix bundle of the C-terminal domain (residues 136-160) preserves its fourfold symmetry during opening, while the bulge helix region undergoes a twofold-symmetric expansion.

### C-terminal domain modulates C-type inactivation kinetics

Patch clamp experiments on reconstituted KcsA with varying C-terminal domain stability revealed that the C-terminal domain modulates the rate and extent of C-type inactivation. In the absence of the C-terminal domain (truncated KcsA), the channel inactivates rapidly and fully. The presence of the C-terminus slows inactivation and increases steady-state current three- to fourfold. Additional strain from Fab4 binding further slows inactivation, reaching ~40% steady-state current. This demonstrates that the steric limits imposed by the C-terminal bundle determine the degree of gate opening, which in turn controls C-type inactivation at the selectivity filter.

### EPR spectroscopy confirms partial bundle expansion during gating

Site-directed spin labeling and EPR spectroscopy of the C-terminal domain showed that the extent of spectral broadening due to dipolar coupling decreases throughout the C-terminal domain during opening, but does not disappear. This confirms that the bundle expands partially but remains as a unit. There is no significant rotation in either the bulge helix or the lower bundle associated with the opening conformation, suggesting that the inner gate helix motion is directly transmitted to the C-terminus as a simple radial expansion without rotation.

### Physiological gate opening likely intermediate between truncated and Fab-bound states

The fact that steady-state inactivation of full-length KcsA displays an intermediate value between truncated KcsA (rapid inactivation) and Fab-bound KcsA (slow inactivation) suggests that under physiological conditions, the inner bundle gate in WT KcsA opens at an intermediate level between 21 and 32 A. This generates side windows that easily accommodate hydrated ions and small blockers like 4-aminopyridine and quaternary ammonium ions.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Crystallization detergent (5 mM) for KcsA-Fab complex
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Solubilization detergent (20 mM) for KcsA extraction from membranes
- <a href="/xray-mp-wiki/reagents/additives/barium-chloride/">Barium Chloride</a> — Ba2+ blocker used in soak experiments (0-10 mM)
- <a href="/xray-mp-wiki/reagents/additives/cadmium-chloride/">Cadmium Chloride</a> — Cd2+ ions form metal bridges in Y82C-KcsA
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — KcsA is the primary model system for studying C-type inactivation
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kvap/">KvAP Voltage-Dependent Potassium Channel</a> — Selectivity filter structure essentially identical; glycine-gating hinge mechanism shared
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — Conformational coupling between activation gate and selectivity filter
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/">NaK Channel from Bacillus cereus</a> — Closed NaK superimposes with KcsA (r.m.s.d. 0.73 A)
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mthk/">MthK Potassium Channel</a> — Open NaK superimposes with open MthK; glycine-gating hinge comparison
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/modal-gating-in-k-channels/">Modal Gating in K+ Channels</a> — KcsA Glu71 mutant structures (3OR7, 3OR6) reveal structural basis of modal gating
