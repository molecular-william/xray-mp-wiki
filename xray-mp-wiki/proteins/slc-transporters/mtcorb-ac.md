---
title: "MtCorB Delta-C from Methanoculleus thermophilus"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-24282-7]
verified: agent
uniprot_id: A0A1G8XA46
---

# MtCorB Delta-C from Methanoculleus thermophilus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A1G8XA46">UniProt: A0A1G8XA46</a>

<span class="expr-badge">Methanoculleus thermophilus</span>

## Overview

MtCorB Delta-C is a CNNM/CorB family magnesium transporter from the thermophilic archaeon *Methanoculleus thermophilus*. CNNM/CorB proteins are a broadly conserved family of integral membrane proteins implicated in Mg2+ homeostasis and divalent cation transport, with mutations in human CNNM proteins linked to genetic diseases including hypomagnesemia and Jalili syndrome. This archaeal ortholog shares 26% sequence identity to the conserved core of human CNNM2. The structure was determined in two conformations: an Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) bound state and an apo state (via a disease-mimicking R235L mutant homologous to the human CNNM4 Jalili syndrome mutant R407L). The transmembrane domain exists in an inward-facing conformation with a negatively charged cavity and a conserved pi-helical turn that coordinates a Mg2+ ion. The CBS-pair domain undergoes major conformational rearrangements upon Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) binding, switching from an elongated dimeric configuration to a disc-like dimeric form. Functional liposome-based assays demonstrated direct Mg2+ transport by CorB proteins through an electroneutral antiporter mechanism.


## Publications

### doi/10.1038##s41467-021-24282-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7msu">7MSU</a></td>
      <td>1.60</td>
      <td>P 1 21 1</td>
      <td>MtCorB CBS-pair domain (residues 199-322) in complex with Mg2+-ATP</td>
      <td>Mg2+-ATP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m1t">7M1T</a></td>
      <td>3.25</td>
      <td>C 1 21 1</td>
      <td>MtCorB Delta-C Delta-loop (residues 5-322) in complex with Mg2+-ATP</td>
      <td>Mg2+-ATP, UDM</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7m1u">7M1U</a></td>
      <td>3.80</td>
      <td>P 1 21 1</td>
      <td>MtCorB Delta-C R235L mutant (residues 5-322) in apo state</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: MtCorB Delta-C (residues 1-322, C-terminal CorC domain deletion) with internal loop deletion
- **Notes**: Codon-optimized cDNA subcloned into pET29a vector with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag). Expressed in E. coli and purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm), optimized to [UDM](/xray-mp-wiki/reagents/detergents/udm) for crystallization.

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
      <td>1</td>
      <td>Cell lysis by sonication</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.0, 0.5 mM Na-<a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride">MgCl2</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membrane fraction collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>2</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta))</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) Superflow (Qiagen)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> purification</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
      <td>Final purification step for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20 mg/mL MtCorB Delta-C Delta-loop in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>, 5 mM Mg2+-<a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 0.1 M Li2SO4, 0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride">MgCl2</a>, 34% <a href="/xray-mp-wiki/reagents/additives/peg-400">PEG400</a>, 5 mM <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of 7M1T obtained after construct and detergent optimization</td>
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
      <td>5.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>293 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Citrate: 0.1 M [buffer]  
- Sodium Chloride: 0.1 M [salt]  
- Magnesium Chloride: 20 mM [salt]  
- Peg 400: 34 % [precipitant] (PEG400)  
- Atp: 5 mM [additive]</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20 mg/mL MtCorB Delta-C R235L mutant in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 50 mM Li2SO4, 11% <a href="/xray-mp-wiki/reagents/additives/peg-400">PEG400</a>0, 10 mM MgSO4</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo state captured via disease-mimicking R235L mutant</td>
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
      <td>5.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>293 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Citrate: 0.1 M [buffer]  
- Peg 4000: 11 % [precipitant] (PEG4000)  
- Magnesium Sulfate: 10 mM [additive]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m1t">7M1T</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVVI</span><span class="topo-outside">DLL</span><span class="topo-membrane">IVEVVLFIAALLFSG</span><span class="topo-inside">FFSSSEVALISITRAKVHALQSQGRKGAKALDTLKRSTDAIQITTLI</span><span class="topo-membrane">GSTIANVAVASLATAIG</span><span class="topo-outside">ITLYGNLG</span><span class="topo-membrane">IAVGLVVAAVLVLVFGE</span><span class="topo-inside">IGPKMYASR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-unknown">TEELALRVSRPILFFSKL</span><span class="topo-inside">L</span><span class="topo-unknown">YPVLWVT</span><span class="topo-inside">DRIEQQFAFRPGVTEPVVTEEEIKEWIDVGEEEGTIEEEERDMLYSVLRFGDTTAREVMTPRVDVVMIEDTATLESALAIFNETGFSRIPVYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320      </span>
<span class="topo-line"><span class="topo-inside">ERIDNIVGLLNVKDVFSAQTSATIRDLMYEPYFIPESKKIDELLKELQVKKQHMAVVLDEYGSFAGIVTVEDMLEELVLEHHHHH</span><span class="topo-unknown">H</span></span>
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
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>22</td>
      <td>8</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>69</td>
      <td>23</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>94</td>
      <td>87</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>95</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>121</td>
      <td>112</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>139</td>
      <td>122</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>140</td>
      <td>140</td>
      <td>140</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>325</td>
      <td>148</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m1t">7M1T</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVV</span><span class="topo-outside">IDLLI</span><span class="topo-membrane">VEVVLFIAALLFSGF</span><span class="topo-inside">FSSSEVALISITRAKVHALQSQGRKGAKALDTLKRSTDAIQITTLI</span><span class="topo-membrane">GSTIANVAVASLATAIG</span><span class="topo-outside">ITLYGNL</span><span class="topo-membrane">GIAVGLVVAAVLVLVFGE</span><span class="topo-inside">IGPKMYASR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">YTEELALRV</span><span class="topo-unknown">SRPILFFSKL</span><span class="topo-inside">LYPVLWVTDRIEQQF</span><span class="topo-unknown">AFRPG</span><span class="topo-inside">VTEPVVTEEEIKEWIDVGEEEGTIEEEERDMLYSVLRFGDTTAREVMTPRVDVVMIEDTATLESALAIFNETGFSRIPVYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320      </span>
<span class="topo-line"><span class="topo-inside">ERIDNIVGLLNVKDVFSAQTSATIRDLMYEPYFIPESKKIDELLKELQVKKQHMAVVLDEYGSFAGIVTVEDMLEELVLEHHHH</span><span class="topo-unknown">HH</span></span>
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
      <td>4</td>
      <td>8</td>
      <td>4</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>23</td>
      <td>9</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>69</td>
      <td>24</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>93</td>
      <td>87</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>112</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>139</td>
      <td>130</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>140</td>
      <td>154</td>
      <td>140</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>324</td>
      <td>160</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m1u">7M1U</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">VVIDLL</span><span class="topo-membrane">IVEVVLFIAALLFSGF</span><span class="topo-outside">FSSSEVALISITRAKVHALQSQGRKGAKALDTLKRSTDAIQITTLI</span><span class="topo-membrane">GSTIANVAVASLATAIGI</span><span class="topo-inside">TLYGNL</span><span class="topo-membrane">GIAVGLVVAAVLVLVFGE</span><span class="topo-outside">IGPKMYASR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YTEELALRVS</span><span class="topo-unknown">RPILFFSKL</span><span class="topo-outside">LYPVLWVTDRIE</span><span class="topo-unknown">QQFAFRPGVTEP</span><span class="topo-outside">VVTEEEIKEWIDVGEEEGTIEEEERDMLYSVLRFGDTTAREVMTPRVDVVMIEDTATLESALAIFNETGFSLIPVYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320        </span>
<span class="topo-line"><span class="topo-outside">ERIDNIVGLLNVKDVFSAVFRQQTSATIRDLMYEPYFIPESKKIDELLKELQVKKQHMAVVLDEYGSFAGIVTVEDMLEELVHH</span><span class="topo-unknown">HHHH</span></span>
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
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>23</td>
      <td>8</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>69</td>
      <td>24</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>93</td>
      <td>88</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>130</td>
      <td>112</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>139</td>
      <td>131</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>140</td>
      <td>151</td>
      <td>140</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>324</td>
      <td>164</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7m1u">7M1U</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVVIDL</span><span class="topo-membrane">LIVEVVLFIAALLFSG</span><span class="topo-outside">FFSSSEVALISITRAKVHALQSQ</span><span class="topo-unknown">GRKG</span><span class="topo-outside">AKALDTLKRSTDAIQITTLI</span><span class="topo-membrane">GSTIANVAVASLATAIGI</span><span class="topo-inside">TLYGNL</span><span class="topo-membrane">GIAVGLVVAAVLVLVFG</span><span class="topo-outside">EIGPKMYASR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YTEELALRVSRPILFFSKLL</span><span class="topo-unknown">YPVLWVT</span><span class="topo-outside">D</span><span class="topo-unknown">RIEQQFAFRPGVTEPVVTEE</span><span class="topo-outside">EIKEWIDVGEEEGTIEEEERDMLYSVLRFGDTTAREVMTPRVDVVMIEDTATLESALAIFNETGFSLIPVYH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320        </span>
<span class="topo-line"><span class="topo-outside">ERIDNIVGLLNVKDVFSAVFRQQTSATIRDLMYEPYFIPESKKIDELLKELQVKKQHMAVVLDEYGSFAGIVTVEDMLEELVHH</span><span class="topo-unknown">HHHH</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>22</td>
      <td>7</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>45</td>
      <td>23</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>69</td>
      <td>50</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>70</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>93</td>
      <td>88</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>94</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>140</td>
      <td>111</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>324</td>
      <td>169</td>
      <td>324</td>
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

### Mg2+-ATP sensing and transport mechanism

MtCorB demonstrates a rocker-switch transport mechanism. In the apo state, the CBS-pair domain adopts an elongated dimeric configuration and the acidic helical bundle (AHB) dissociates, forming a CBS-TMD contact that locks the transmembrane domain in the inward-facing conformation, inactivating the transporter. Upon Mg2+-[ATP](/xray-mp-wiki/reagents/ligands/atp) binding, the CBS-pair domain switches to a disc-like dimeric configuration, disrupting the CBS-TMD contact and allowing the transporter to transition to other conformational states required for Mg2+ transport. The Mg2+ ion in the transmembrane cavity is coordinated by Ser21, Ser25, Ser71, Glu111, and main-chain carbonyls of Ser21 and Gly110. A conserved pi-helical turn in TM3 (involving Pro114) is essential for transport activity.

### Direct Mg2+ transport by CorB proteins

Liposome-based Mg2+ transport assays with [MAG](/xray-mp-wiki/reagents/lipids/mag)-fura-2 demonstrated that CorB proteins mediate direct Mg2+ transport, resolving a longstanding debate in the field. The transport occurs through an electroneutral antiporter mechanism, as shown by the lack of [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin)-sensitive enhancement (unlike the electrogenic CorA channel). Mutations near the pi-helical turn (S117A, E118A, P121G, K122A) consistently reduced transport activity, while mutations in the Mg2+ binding site (S26A, S30A, N76A) increased activity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/valinomycin">Valinomycin</a> — Entity mentioned in text
