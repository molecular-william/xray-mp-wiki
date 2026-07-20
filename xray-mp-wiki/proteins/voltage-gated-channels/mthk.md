---
title: "MthK (Methanobacterium thermoautotrophicum K+ Channel)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, potassium-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##417515a, doi/10.1038##nsmb.1865, doi/10.1038##ncomms3621, doi/10.1038##s41467-019-13227-w, doi/10.1073##pnas.2009624117]
verified: agent
uniprot_id: O27564
---

# MthK (Methanobacterium thermoautotrophicum K+ Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O27564">UniProt: O27564</a>

<span class="expr-badge">Methanothermobacter thermautotrophicus</span>

## Overview

MthK is a calcium-gated potassium channel from the archaeon Methanobacterium thermoautotrophicum. It belongs to the family of tetrameric cation channels and is a founding member of RCK (Regulator of Conductance for K+) domain-containing channels. The channel features a central pore formed by four membrane-spanning subunits and an intracellular gating ring composed of eight RCK domains that regulate channel opening in response to intracellular Ca2+ binding. MthK served as a prototype for understanding the mechanism of ligand-gated channel opening through the gating ring architecture. High-resolution structures of the isolated MthK pore at up to 1.45 A resolution revealed that the selectivity filter maintains a conductive conformation even in the absence of K+, and provided atomic-level insights into K+ selectivity and the anomalous mole-fraction effect in multi-ion pores. A comprehensive structural titration (X-ray crystallography at 150, 50, 11, and 6 mM K+) combined with molecular dynamics simulations revealed that the central S2 binding site has uniquely low K+ affinity (~50 mM) while S1, S3, and S4 have high affinity (sub-mM), leading to selective emptying of S2 at low K+ without SF collapse — explaining why MthK and [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) have different inactivation phenotypes despite identical selectivity filter sequences. Structural and functional analysis of the MthK RCK domain revealed allosteric coupling between two Ca2+-binding sites (C1 and C3) mediated by a carboxyl-carboxylate hydrogen bond between Glu259 and Glu133, providing a mechanism for tuning Ca2+ sensitivity.


## Publications

### doi/10.1038##417515a

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1lnq">1LNQ</a></td>
      <td>3.3</td>
      <td>P6_6 22</td>
      <td>MthK M107I mutant, residues 19-336</td>
      <td>Ca2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

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
      <td>Extraction</td>
      <td>Cell lysis and solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 100 mM KCl + 40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ affinity column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ resin</td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 20 mM Tris pH 8.0, 100 mM KCl</td>
      <td>Wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>His-tag cleavage</td>
      <td>Thrombin digestion</td>
      <td>—</td>
      <td></td>
      <td>1 unit thrombin per 3.0 mg channel, overnight at room temperature</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (10/30)</td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 20 mM Tris pH 8.0, 100 mM KCl</td>
      <td></td>
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
      <td>MthK M107I at 15 mg/mL in 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 20 mM Tris pH 8.0, 100 mM KCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>23-26% PEGMME, 100 mM MES pH 6.5, 200 mM CaCl2</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1lnq">1LNQ</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKV</span><span class="topo-outside">PATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGF</span><span class="topo-inside">HFIEGESWT</span><span class="topo-unknown">VSLYWTFVTIATVGY</span><span class="topo-inside">GDYSPSTPL</span><span class="topo-membrane">GMYFTVTLIVLGIGTFAVAV</span><span class="topo-outside">ERLLEFL</span><span class="topo-unknown">INREQMKLMGLIDVAKS</span><span class="topo-outside">RHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span></span>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>23</td>
      <td>19</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>24</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>47</td>
      <td>39</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>48</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>71</td>
      <td>63</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>336</td>
      <td>116</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1lnq">1LNQ</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKV</span><span class="topo-outside">PATRIL</span><span class="topo-membrane">LLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGY</span><span class="topo-inside">GDYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAV</span><span class="topo-outside">ERLLEFL</span><span class="topo-unknown">INREQMKLMGLIDVAKS</span><span class="topo-outside">RHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span></span>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>24</td>
      <td>19</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>62</td>
      <td>47</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>70</td>
      <td>63</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>336</td>
      <td>116</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1lnq">1LNQ</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKV</span><span class="topo-outside">PATRIL</span><span class="topo-membrane">LLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGY</span><span class="topo-inside">GDYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAV</span><span class="topo-outside">ERLLEFL</span><span class="topo-unknown">INREQMKLMGLIDVAKS</span><span class="topo-outside">RHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span></span>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>24</td>
      <td>19</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>62</td>
      <td>47</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>70</td>
      <td>63</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>336</td>
      <td>116</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1lnq">1LNQ</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKV</span><span class="topo-outside">PATRIL</span><span class="topo-membrane">LLVLAVIIYGTAGF</span><span class="topo-inside">HFIEGESWT</span><span class="topo-unknown">VSLYWTFVTIATVGY</span><span class="topo-inside">GDYSPSTPL</span><span class="topo-membrane">GMYFTVTLIVLGIGTFAVAV</span><span class="topo-outside">ERLLEFL</span><span class="topo-unknown">INREQMKLMGLIDVAKS</span><span class="topo-outside">RHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span></span>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>24</td>
      <td>19</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>38</td>
      <td>25</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>47</td>
      <td>39</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>48</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>71</td>
      <td>63</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>72</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>336</td>
      <td>116</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.1865

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a></td>
      <td>1.45</td>
      <td>P42_12</td>
      <td>MthK pore, S68H V77C mutant (K+ complex, 100 mM KCl)</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a></td>
      <td>1.45</td>
      <td>P42_12</td>
      <td>MthK pore, S68R V77C mutant (low-K+ complex, 1 mM KCl/99 mM NaCl)</td>
      <td>K+/Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a></td>
      <td>2.2</td>
      <td>P42_12</td>
      <td>MthK pore, S68H V77C mutant (Na+ complex, 100 mM NaCl)</td>
      <td>Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

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
      <td>Cell lysis and affinity purification</td>
      <td>—</td>
      <td>Standard buffer + <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (DM)</td>
      <td>MthK channel expressed and purified in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> as described previously</td>
    </tr>
    <tr>
      <td>Limited <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion</td>
      <td>Proteolysis</td>
      <td>—</td>
      <td></td>
      <td>Membrane-spanning pore obtained by limited <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion of MthK channel</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM KCl</td>
      <td></td>
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
      <td>Purified MthK pores in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> at ~8 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>3.0-3.5 M 1,6-hexanediol, 100 mM HEPES pH 7.5</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Wild-type crystals were space group I4 with anisotropic diffraction; V77C with S68R or S68H mutations improved packing yielding P42_12 space group</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ldc">3LDC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPHTP</span><span class="topo-membrane">LGMYFTCTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms3621

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4l73">4L73</a></td>
      <td>2.5</td>
      <td>P3_121</td>
      <td>WT MthK RCK domain, fully Ca2+-bound (C1, C2, C3 sites occupied)</td>
      <td>Ca2+ (3 ions per RCK domain)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4l73">4L73</a></td>
      <td>1.85</td>
      <td>P2_111</td>
      <td>WT MthK RCK domain, Ca2+ bound only at C1 site (200 mM CaCl2)</td>
      <td>Ca2+ (1 ion per RCK domain, at C1 site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4l73">4L73</a></td>
      <td>2.4</td>
      <td>P6_522</td>
      <td>D184N mutant MthK RCK domain, no Ca2+ at C1, Ca2+ bound at C3</td>
      <td>Ca2+ (C3 site only)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4l73">4L73</a></td>
      <td>3.0</td>
      <td>P6_522</td>
      <td>E212Q mutant MthK RCK domain, Ca2+ bound at both C1 and C3</td>
      <td>Ca2+ (C1 and C3 sites, altered coordination at C1)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

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
      <td>Cell growth and induction</td>
      <td>E. coli XL-1 Blue culture</td>
      <td>—</td>
      <td></td>
      <td>Induction with 0.4 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM Tris, 100 mM KCl, pH 7.6</td>
      <td>PMSF and Complete EDTA-free protease inhibitor cocktail added</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM Tris, 100 mM KCl, pH 7.6 + 50 mM decyl maltoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Incubation for 2 h, followed by centrifugation at 30,500 g for 45 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Co2+-charged HiTrap metal affinity column</td>
      <td>Co2+-charged HiTrap (GE Healthcare)</td>
      <td>20 mM Tris, 100 mM KCl, pH 7.6 + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>His-tag cleavage</td>
      <td>Thrombin digestion</td>
      <td>—</td>
      <td></td>
      <td>2.0 units thrombin per 3.0 mg eluted protein, 2 h at room temperature</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris, 100 mM KCl, pH 7.6 + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Concentrated to 5 mg/mL after <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified full-length MthK at 5 mg/mL

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MthK RCK domain after limited <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion and SEC</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>High CaCl2 buffer for WT-C1C2C3; 200 mM CaCl2 for WT-C1; 200 mM CaCl2 for D184N and E212Q mutants</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>WT-C1C2C3: P3_121, 2.5 A. WT-C1 (low Ca2+): P2_111, 1.85 A, Rwork/Rfree 0.211/0.253. D184N mutant: P6_522, 2.4 A, Rwork/Rfree 0.197/0.247. E212Q mutant: P6_522, 3.0 A, Rwork/Rfree 0.217/0.263. Mutant and WT RCK domains crystallized under identical conditions for direct comparison.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41467-019-13227-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6oly">6OLY</a></td>
      <td></td>
      <td></td>
      <td>Full-length MthK M107I mutant with thrombin-cleavable C-terminal 6×His-tag</td>
      <td>Ca2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oly">6OLY</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKVPATRI</span><span class="topo-inside">L</span><span class="topo-membrane">LLVLAVIIYGTAGFHFI</span><span class="topo-outside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-outside">DYSPSTPL</span><span class="topo-membrane">GMYFTVTLIVLGIGTFAVAVERLLEFLINRE</span><span class="topo-unknown">QMKLIGLI</span><span class="topo-inside">DVAKSRHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CGWSESTLECLRELRGSEVFVLAEDEN</span><span class="topo-unknown">VRKKVLRS</span><span class="topo-inside">GANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span><span class="topo-unknown">LVPRGSHHHHHH</span></span>
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
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>42</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>71</td>
      <td>64</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>102</td>
      <td>72</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>110</td>
      <td>103</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>147</td>
      <td>111</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>155</td>
      <td>148</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>336</td>
      <td>156</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oly">6OLY</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKVPATR</span><span class="topo-inside">I</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFIE</span><span class="topo-outside">GESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-outside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVERLLEFLINRE</span><span class="topo-inside">QMKLIGLIDVAKSRHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGK</span><span class="topo-unknown">PEEIERLKNY</span><span class="topo-inside">ISA</span><span class="topo-unknown">LVPRGSHHHHHH</span></span>
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
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>42</td>
      <td>24</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>46</td>
      <td>43</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>70</td>
      <td>64</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>102</td>
      <td>71</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>323</td>
      <td>103</td>
      <td>323</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>333</td>
      <td>324</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>334</td>
      <td>336</td>
      <td>334</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oly">6OLY</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKVPATRI</span><span class="topo-inside">L</span><span class="topo-membrane">LLVLAVIIYGTAG</span><span class="topo-outside">FHFIEGESWTVS</span><span class="topo-unknown">LYWTFVTIATVGYG</span><span class="topo-outside">DYSPSTPLGM</span><span class="topo-membrane">YFTVTLIVLGIGTFAVAVERLLEFLINRE</span><span class="topo-unknown">QMKLIGLI</span><span class="topo-inside">DVAKSRHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CGWSESTLECLRELRGSEVFVLAEDEN</span><span class="topo-unknown">VRKKVLRS</span><span class="topo-inside">GANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span><span class="topo-unknown">LVPRGSHHHHHH</span></span>
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
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>37</td>
      <td>25</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>38</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>63</td>
      <td>50</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>73</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>102</td>
      <td>74</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>110</td>
      <td>103</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>147</td>
      <td>111</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>155</td>
      <td>148</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>336</td>
      <td>156</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6oly">6OLY</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLVIEIIRKHLPRVLKVPATR</span><span class="topo-inside">I</span><span class="topo-membrane">LLLVLAVIIYGTAGFH</span><span class="topo-outside">FIEGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-outside">DYSPSTPLGM</span><span class="topo-membrane">YFTVTLIVLGIGTFAVAVERLLEFLINREQ</span><span class="topo-inside">MKLIGLIDVAKSRHVVI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CGWSESTLECLRELRGSEVFVLAEDENVRKKVLRSGANFVHGDPTRVSDLEKANVRGARAVIVDLESDSETIHCILGIRKIDESVRIIAEAERYENIEQLRMAGADQVISPFVISGRLMS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">RSIDDGYEAMFVQDVLAEESTRRMVEVPIPEGSKLEGVSVLDADIHDVTGVIIIGVGRGDELIIDPPRDYSFRAGDIILGIGKPEEIERLKNYISA</span><span class="topo-unknown">LVPRGSHHHHHH</span></span>
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
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>39</td>
      <td>24</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>46</td>
      <td>40</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>63</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>73</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>103</td>
      <td>74</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>336</td>
      <td>104</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.2009624117

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u9p">6U9P</a></td>
      <td><2</td>
      <td></td>
      <td>Wild-type MthK pore, 150 mM K+</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u9t">6U9T</a></td>
      <td><2</td>
      <td></td>
      <td>Wild-type MthK pore, 50 mM K+</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u9y">6U9Y</a></td>
      <td><2</td>
      <td></td>
      <td>Wild-type MthK pore, 11 mM K+</td>
      <td>K+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u9z">6U9Z</a></td>
      <td><2</td>
      <td></td>
      <td>Wild-type MthK pore, 6 mM K+</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli SG13009 (pREP4)
- **Construct**: Full-length MthK M107I mutant with C-terminal hexahistidine tag and thrombin cleavage site
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Standard LB medium

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
      <td>Cell lysis and extraction</td>
      <td>HiTrap Co2+ charged metal-affinity</td>
      <td>—</td>
      <td>100 mM KCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, pH 8.0 + <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td></td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>—</td>
      <td>100 mM KCl, 20 mM Hepes, pH 8.0 + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion</td>
      <td><a href="/xray-mp-wiki/methods/purification/limited-proteolysis/">Limited Proteolysis</a></td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> type I at 1:50 <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a>:MthK for 2 h. <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> inhibitor type II-O added at 2x mass of <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a>.</td>
    </tr>
    <tr>
      <td>Gel filtration (pore)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>—</td>
      <td>100 mM KCl, 10 mM Mops, pH 8.0 + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Detergent exchange</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td>100 mM KCl, 10 mM Mops, pH 8.0 + 10 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Dialysis (low K+)</td>
      <td>Dialysis</td>
      <td>—</td>
      <td>100 mM NaCl, 1 mM KCl, 10 mM Mops, pH 8.0 (NaOH), 10 mM <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>For low [K+] crystallization experiments only</td>
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
      <td>MthK pore at ~15 mg/mL in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Varied with [K+] condition</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals in 150, 50, 11, and 6 mM [K+]. Lower [K+] crystals were very small (~10-15 um) but high-resolution diffraction (<2 A) obtained for all conditions. 1 mM [K+] sample failed to crystallize without K+ supplementation. PDB 6U9P (150 mM), 6U9T (50 mM), 6U9Y (11 mM), 6U9Z (6 mM).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9p">6U9P</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9p">6U9P</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9p">6U9P</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9p">6U9P</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9t">6U9T</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9t">6U9T</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9t">6U9T</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9t">6U9T</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9y">6U9Y</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9y">6U9Y</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9y">6U9Y</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9y">6U9Y</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9z">6U9Z</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9z">6U9Z</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9z">6U9Z</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u9z">6U9Z</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-outside">VPATRI</span><span class="topo-membrane">LLLVLAVIIYGTAGFHFI</span><span class="topo-inside">EGESW</span><span class="topo-unknown">TVSLYWTFVTIATVGYG</span><span class="topo-inside">DYSPSTP</span><span class="topo-membrane">LGMYFTVTLIVLGIGTFAVAVE</span><span class="topo-unknown">RLLEFL</span><span class="topo-outside">I</span></span>
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
      <td>6</td>
      <td>18</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>24</td>
      <td>24</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>42</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>47</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>64</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>75</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>93</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>99</td>
      <td>99</td>
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

### Gating ring mechanism for Ca2+-dependent channel opening

The MthK channel structure revealed that eight RCK domains assemble into a gating ring at the intracellular membrane surface. Four RCK domains are attached to the pore-forming subunits (blue), and four are soluble domains assembled from solution (red). Two distinct protein-protein interfaces hold the ring together: a fixed interface (formed by helices alphaD and alphaE) and a flexible interface (formed by the C-terminal subdomain and helices alphaF and alphaG). Ca2+ binds at the base of a cleft between two RCK domains at the flexible interface, coordinated by Glu210, Glu212, and Asp184.

### Proposed mechanism of mechanical work by the gating ring

The gating ring converts the free energy of Ca2+ binding into mechanical work to open the pore. Ca2+ binding reshapes the ligand-binding cleft at the flexible interface, causing rigid RCK domain pairs (connected by fixed interfaces) to tilt and rotate. This movement expands the diameter of the gating ring, which in turn pulls open the pore's inner helices via the disordered linkers connecting the pore and gating ring. In the Ca2+-bound state, the MthK pore is wide open, with inner helix arrangements distinctly different from the closed [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) K+ channel.

### High-resolution structure of K+ selectivity and the anomalous mole-fraction effect

High-resolution (1.45 A) crystal structures of the MthK pore in three ionic conditions (K+ complex, low-K+/high-Na+ complex, and Na+ complex) revealed that the MthK selectivity filter maintains a conductive conformation even in the absence of K+, unlike the [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) channel whose filter collapses in low K+. At high K+ concentrations, two K+ ions equivalently occupy all four sites in the selectivity filter in 1,3 and 2,4 configurations. At low K+/high Na+ concentrations, a single K+ ion remains bound preferentially at site 1 or site 3, effectively blocking Na+ permeation. This provides the structural basis for the anomalous mole-fraction effect, a defining property of multi-ion pores where a second permeable ion species paradoxically blocks current carried by the first. Na+ ions coordinate in plane with carbonyl oxygen atoms of Tyr62 in a pyramidal geometry, with an additional water ligand from the extracellular side.

### Allosteric coupling between C1 and C3 Ca2+-binding sites in the RCK domain

Crystal structures of WT and mutant MthK RCK domains at varying Ca2+ occupancies revealed that two physically distinct Ca2+-binding sites (C1 in the N-lobe and C3 at the interface between adjacent RCK domains) are allosterically coupled. Ca2+ binding at C1 (the higher-affinity site in WT) makes Ca2+ binding at C3 relatively unfavourable. The D184N mutation, which abrogates Ca2+ binding at C1, makes Ca2+ binding at C3 more favourable. The E212Q mutation, which alters Ca2+ coordination geometry at C1 (Q212 is 3.3 A from Ca2+ vs 2.5 A for E212 in WT), also enhances C3 binding but without eliminating C1 binding, resulting in overall enhanced Ca2+ sensitivity of the channel.

### E259-E133 carboxyl-carboxylate hydrogen bond as mediator of allosteric coupling

Systematic comparison of WT and mutant RCK domain structures identified a carboxyl-carboxylate hydrogen bond between Glu259 and Glu133 that mediates allosteric communication between C1 and C3 calcium-binding sites. When Ca2+ is absent from C3, the Glu259-Glu133 distance is short (2.6-2.9 A, consistent with a hydrogen bond). When Ca2+ is bound at C3, this distance increases to 3.5-4.8 A. Mutation of Glu259 to Ala (E259A) enhances Ca2+ sensitivity similarly to E212Q, and the E212Q/E259A double mutant is indistinguishable from single mutants, indicating that disruption of either the E212-Ca2+ bond or the E259-E133 hydrogen bond is sufficient to abolish allosteric communication.

### Working model of sequential Ca2+ binding and RCK domain activation

A working model for allosteric activation of MthK was derived from structural and functional data. With Ca2+-binding sites empty, RCK domains exist in a range of conformations. Ca2+ initially binds to the C1 sites in the N-lobe (higher affinity), stabilizing a partially activated conformation. The Glu259-Glu133 interaction keeps the C-lobe in a conformation incompatible with Ca2+ binding at C3. At higher Ca2+ concentrations, Ca2+ binds to C3 sites, which bridge the C-lobes of adjacent RCK domains, requiring disruption of the Glu259-Glu133 interaction. Full occupancy of both C1 and C3 is required for maximal channel opening. This inhibitory interaction between two Ca2+-binding sites provides a structural mechanism for tuning Ca2+ sensitivity.

### Voltage-dependent gate localized at the selectivity filter

Electrophysiological analysis of MthK using quaternary ammonium (QA) blockers of varying sizes ([TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/), bTBA, bbTBA) revealed that the voltage-dependent gate is located at the selectivity filter rather than at the intracellular bundle crossing. [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) block displayed strong voltage dependence, with the blocker sensing ~65% of the transmembrane electric field, indicating that blockers access a binding site deep within the pore near the selectivity filter. In contrast, larger blockers (bTBA, bbTBA) showed reduced voltage dependence and trapped the channel in the open state during inactivation, consistent with a binding site at or above the selectivity filter. The apparent affinity of [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) increased substantially during inactivation gating (Kd from ~65 uM open state to ~6 uM inactivated state), suggesting that inactivation involves conformational changes at the selectivity filter that enhance blocker binding. These findings demonstrate that the selectivity filter of MthK serves as both the ion selectivity determinant and the primary voltage-dependent gate, providing a structural basis for C-type inactivation in potassium channels.

### Activation gate–selectivity filter coupling via I84–T59 hydrophobic contact

Systematic MD simulations of MthK at varying levels of activation gate opening, combined with crystal structures (including new structure 6OLY), revealed that ion conductance is primarily controlled at the selectivity filter (SF) rather than by a physical gate at the helix bundle crossing. The SF opening at threonine 59 (T59), which forms ion binding site S4, is coupled to activation gate opening through a collective motion of transmembrane helices M1 and M2. A hydrophobic contact between isoleucine 84 (I84) on the M2 helix and the T59 side chain mediates this allosteric communication. As the activation gate opens, I84 residues move apart, and T59 residues follow to maintain favorable hydrophobic interactions, widening the SF. Mutation of I84 to alanine (I84A) shifts the current–opening relationship to smaller AG openings, confirming the functional role of this interaction. At small AG openings, the SF imposes high energy barriers for ion permeation (especially between sites S4 and S3). At optimal openings, the SF widens sufficiently to lower barriers and enable efficient direct knock-on ion conduction, matching experimental single-channel currents (~25 pA at 200 mV). At wide AG openings beyond those observed in crystal structures, water enters the SF and disrupts the direct knock-on mechanism, reducing outward K+ current. This water-mediated current decline is associated with carbonyl flipping of valine 60 (V60) at the S3 binding site, proposed as the initial step of MthK C-type inactivation. The study establishes a unified gating model for SF-activated potassium channels including MthK, BK, and K2P channels, where the selectivity filter functions as the primary gate regulated allosterically by the activation gate.

### Uneven K+ titration across SF binding sites distinguishes MthK from KcsA

X-ray crystallography at 150, 50, 11, and 6 mM K+ revealed that MthK maintains a conductive SF
conformation across all conditions, unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) whose SF collapses at low K+. The S2 site
selectively loses K+ at low concentrations (apparent Kd ~50 mM), while S1, S3, and S4 remain
nearly fully occupied (sub-mM affinity). This uneven titration differs from [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) where all SF
sites show uniform occupancy decrease with K+ concentration.

### MD simulations show MthK SF can collapse but only when all K+ is removed

Molecular dynamics simulations revealed that the MthK SF can collapse similarly to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), but
only when all K+ ions are removed from the SF. A single K+ ion binding at any SF site
(except S4) is sufficient to rescue the conductive state. The SF collapse involves loss of
water at S2, water binding behind the SF, and 180-degree carbonyl rotations at the central
[Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G61), analogous to [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)'s Gly77 flipping.

### S2 low K+ affinity arises from weaker carbonyl coordination by pore helix interactions

[Free Energy Perturbation](/xray-mp-wiki/methods/structure-determination/free-energy-perturbation/) (FEP) calculations showed K+ preferentially occupies S3 over S2
(Delta_G = -2.5 kcal/mol for vacancy-mediated). The reduced S2 affinity is due to weaker
coordination by G61 and T59 carbonyl groups, arising from different interactions with the
pore helix and water behind the SF. MthK lacks the equivalent of [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)'s E71 residue,
which stabilizes G77 carbonyl orientation via H-bond with the amide of G77-Y78. Without
this interaction, MthK's Y62 amide binds more weakly to a mobile water molecule.

### Functional significance of low-affinity S2 site for K+ conduction

The existence of a low-affinity K+ binding site at S2 (~50 mM apparent Kd) is important for
rapid K+ conduction — during transport, the low affinity in S2 allows fast release of K+,
enabling high ionic throughput. This site was previously proposed in BK channels as the
"enhancement" site. Under a driving force, ions may exit the SF faster than refilling,
transiently emptying the SF and leading to collapse, which may explain the voltage-dependent
gating observed in MthK.


## Cross-References

- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type inactivation</a> — MthK undergoes C-type-like inactivation at the selectivity filter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Selectivity filter</a> — The SF is the primary gate controlling K+ ion conduction in MthK
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel gating</a> — AG-SF coupling is a fundamental gating mechanism in potassium channels
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — KcsA is the prototypical K+ channel for AG-SF coupling studies referenced in this work
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel</a> — TRAAK shows similar SF activation behavior as MthK
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-ion-bound-configurations/">Alternating Ion-Bound Configurations</a> — Ion occupancy patterns in the SF determine conduction and inactivation states
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — SF-TM2 coupling mediates allosteric communication during gating and inactivation
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Primary method for structural titration at 4 K+ concentrations (6-150 mM)
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations revealed SF collapse mechanism and ion occupancy effects on gating
- <a href="/xray-mp-wiki/methods/structure-determination/free-energy-perturbation/">Free Energy Perturbation</a> — FEP calculations quantified K+ binding preferences between S2 and S3 sites
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decyl maltoside (DM)</a> — Used for MthK solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Used as purification buffer in all MthK preparations
