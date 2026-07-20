---
title: "Synechocystis Halorhodopsin (SyHR)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-34019-9]
verified: agent
uniprot_id: A0A9X9ZA75
---

# Synechocystis Halorhodopsin (SyHR)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A9X9ZA75">UniProt: A0A9X9ZA75</a>

<span class="expr-badge">Synechocystis sp. PCC 7509</span>

## Overview

Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/) (SyHR) is a light-driven anion pump from the cyanobacterium Synechocystis sp. PCC 7509. It belongs to a clade of cyanobacterial anion-pumping [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) characterized by the TSD motif (T74, S78, D85 in helix C). SyHR is the only known natural microbial rhodopsin proposed to pump divalent anions such as sulfate in addition to monovalent halides like chloride. The protein functions as an inward Cl- pump and has potential as a next-generation optogenetics tool due to its high chloride affinity (Kd 0.112 mM) and ability to pump against strong concentration gradients. SyHR forms trimers in lipid membranes and contains a [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore covalently bound to K205 via a Schiff base.


## Publications

### doi/10.1038##s41467-022-34019-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zou">7ZOU</a></td>
      <td>1.57</td>
      <td>P 3 2 1</td>
      <td>Synechocystis <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> (residues 1-225 of 234), C-terminal 6xHis tag</td>
      <td>chloride ion in RSB region</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zov">7ZOV</a></td>
      <td>1.57</td>
      <td>P 3 2 1</td>
      <td>Synechocystis <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> (residues 1-225 of 234), C-terminal 6xHis tag</td>
      <td>sulfate ion (surface-bound, not in RSB region)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zow">7ZOW</a></td>
      <td>1.7</td>
      <td>P 3 2 1</td>
      <td>Synechocystis <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> (residues 1-225 of 234), C-terminal 6xHis tag</td>
      <td>K-state intermediate (<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> in 6-s-cis, 12-s-cis configuration)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zoy">7ZOY</a></td>
      <td>1.6</td>
      <td>P 3 2 1</td>
      <td>Synechocystis <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> (residues 1-225 of 234), C-terminal 6xHis tag</td>
      <td>O-state intermediate (anion-free)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41
- **Construct**: Codon-optimized SyHR gene (accession WP_009632765) in pET system with C-terminal 6xHis tag
- **Notes**: Autoinducing ZYP-5052 medium; 10 uM all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) added when [Glucose](/xray-mp-wiki/reagents/additives/glucose/) dropped below 10 mg/L; incubated at 20 C overnight

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
      <td>Cell disruption</td>
      <td>High-pressure homogenization</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5% Triton X-100, 50 mg/L DNase I + 0.5% Triton X-100</td>
      <td>Disrupted at 172.3 MPa; membrane fraction isolated by ultracentrifugation at 90,000g for 1h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 8.0, 0.1 M NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Stirred overnight; centrifuged at 90,000g for 1h</td>
    </tr>
    <tr>
      <td>IMAC purification</td>
      <td>Nickel-nitrilotriacetic acid <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> column (Qiagen)</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.2 M NaCl, 0.5 M <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted in imidazole-containing buffer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> prep grade 125 mL column (GE Healthcare)</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.2 M NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Protein-containing fractions pooled and concentrated to 60 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SyHR at 20 mg/mL in lipidic mesophase (<a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Hexagonal crystals grown over 2 months; reached 150 um in length and width. Red crystals cryoprotected in 1.6 M Ammonium Phosphate pH 4.6, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Violet crystals cryoprotected in 2.0 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 0.1 M HEPES pH 7.0, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Flash-cooled in liquid nitrogen.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zou">7ZOU</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLS</span><span class="topo-outside">MALGQGRSVIAGRPTVWV</span><span class="topo-membrane">RYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFV</span><span class="topo-outside">ATISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGHIW</span><span class="topo-membrane">YVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVW</span><span class="topo-outside">LLGNTGFNAVNQGTETM</span><span class="topo-membrane">FYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>39</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>70</td>
      <td>53</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>84</td>
      <td>71</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>126</td>
      <td>114</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>140</td>
      <td>127</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>178</td>
      <td>166</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>196</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zou">7ZOU</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLS</span><span class="topo-outside">MALGQGRSVIAGRPTVWV</span><span class="topo-membrane">RYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFV</span><span class="topo-outside">ATISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGHIW</span><span class="topo-membrane">YVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVW</span><span class="topo-outside">LLGNTGFNAVNQGTETM</span><span class="topo-membrane">FYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>39</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>70</td>
      <td>53</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>84</td>
      <td>71</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>126</td>
      <td>114</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>140</td>
      <td>127</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>178</td>
      <td>166</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>196</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zou">7ZOU</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLS</span><span class="topo-outside">MALGQGRSVIAGRPTVWV</span><span class="topo-membrane">RYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFV</span><span class="topo-outside">ATISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGHIW</span><span class="topo-membrane">YVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVW</span><span class="topo-outside">LLGNTGFNAVNQGTETM</span><span class="topo-membrane">FYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>39</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>70</td>
      <td>53</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>84</td>
      <td>71</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>113</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>126</td>
      <td>114</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>140</td>
      <td>127</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>178</td>
      <td>166</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>196</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zov">7ZOV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVWL</span><span class="topo-outside">LGNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>84</td>
      <td>70</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>140</td>
      <td>125</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>179</td>
      <td>166</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>193</td>
      <td>180</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>210</td>
      <td>194</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zov">7ZOV</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVWL</span><span class="topo-outside">LGNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>84</td>
      <td>70</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>140</td>
      <td>125</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>179</td>
      <td>166</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>193</td>
      <td>180</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>210</td>
      <td>194</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zov">7ZOV</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGI</span><span class="topo-inside">GAHNAKNERWKILFTI</span><span class="topo-membrane">NFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLIL</span><span class="topo-inside">DLTFLGKTSLPITA</span><span class="topo-membrane">SLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYL</span><span class="topo-inside">LVNQYRKQAERNYPQAKKVFRKLLS</span><span class="topo-membrane">VHLVLWTLYPIVWL</span><span class="topo-outside">LGNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGF</span><span class="topo-inside">LSLNSMHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>38</td>
      <td>23</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>54</td>
      <td>39</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>84</td>
      <td>70</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>98</td>
      <td>85</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>115</td>
      <td>99</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>140</td>
      <td>125</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>165</td>
      <td>141</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>179</td>
      <td>166</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>193</td>
      <td>180</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>210</td>
      <td>194</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>225</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zow">7ZOW</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGIGAHN</span><span class="topo-outside">AKNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-inside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-outside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-inside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-inside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-outside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-inside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-outside">MHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>225</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zow">7ZOW</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGIGAHN</span><span class="topo-outside">AKNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-inside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-outside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-inside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-inside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-outside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-inside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-outside">MHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>225</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zow">7ZOW</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">?AQIW</span><span class="topo-membrane">LWIGVIGMALGSIFFGIGAHN</span><span class="topo-outside">AKNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-inside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-outside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-inside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-inside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-outside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-inside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-outside">MHTLEKNTES</span><span class="topo-unknown">VSSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>26</td>
      <td>6</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>27</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>225</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>234</td>
      <td>226</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zoy">7ZOY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQI</span><span class="topo-membrane">WLWIGVIGMALGSIFFGIGAHNA</span><span class="topo-inside">KNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-inside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-inside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-outside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-inside">MHTLEKNTESV</span><span class="topo-unknown">SSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>27</td>
      <td>5</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>234</td>
      <td>227</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zoy">7ZOY</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQI</span><span class="topo-membrane">WLWIGVIGMALGSIFFGIGAHNA</span><span class="topo-inside">KNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-inside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-inside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-outside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-inside">MHTLEKNTESV</span><span class="topo-unknown">SSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>27</td>
      <td>5</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>234</td>
      <td>227</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zoy">7ZOY</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AQI</span><span class="topo-membrane">WLWIGVIGMALGSIFFGIGAHNA</span><span class="topo-inside">KNERWK</span><span class="topo-membrane">ILFTINFFICAIATGLYLSMA</span><span class="topo-outside">LGQGRSVIAGRPTVW</span><span class="topo-membrane">VRYITWFLSTPLLILDLTFL</span><span class="topo-inside">GKTSL</span><span class="topo-membrane">PITASLLGANAYMIATGFVAT</span><span class="topo-outside">ISADR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230    </span>
<span class="topo-line"><span class="topo-outside">TIGH</span><span class="topo-membrane">IWYVVSCFAFLATVYLLVNQYR</span><span class="topo-inside">KQAERNYPQAKKV</span><span class="topo-membrane">FRKLLSVHLVLWTLYPIVWLL</span><span class="topo-outside">GNTGFNAVNQGTE</span><span class="topo-membrane">TMFYTILDITS?VGFGFLSLNS</span><span class="topo-inside">MHTLEKNTESV</span><span class="topo-unknown">SSYESSTI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>27</td>
      <td>5</td>
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
      <td>69</td>
      <td>55</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>89</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>90</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>95</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>124</td>
      <td>116</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>146</td>
      <td>125</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>193</td>
      <td>181</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>194</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>216</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>234</td>
      <td>227</td>
      <td>234</td>
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

### Unique retinal isomerization in K state

The K state intermediate of SyHR reveals a unique 6-s-cis, 12-s-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) configuration never previously observed in [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). This isomerization causes the polyene chain to rotate 180 degrees from atoms C7 to C12, shifting C20 by 1.7 A toward L82 and the beta-ionone ring by almost 2 A toward the cytoplasmic side. W75 rotates 10 degrees and L82 reorients to accommodate the cofactor. This suggests a unique primary photochemical reaction in SyHR.

### Chloride release pathway through H167

SyHR contains a unique histidine residue H167 in helix F, absent in archaeal HRs and bacterial Cl- pumps. Two internal cavities (IC1 and IC2) near H167 form the putative chloride release pathway to the cytoplasm. IC2 is unique to SyHR and is a compact hydrophilic cavity filled by two water molecules coordinated by N104, T137, and H167. The mutation of the corresponding histidine in MrHR (H166A) dramatically decelerates L and N state decay, confirming H167's role in ion release.

### Sulfate pumping mechanism

SyHR's unique ability to pump sulfate is attributed to a large extracellular cavity serving as an ion uptake vestibule. The cavity protrudes from the extracellular space through a pore to R71. The key determinant is T183 at the cavity entrance; in MrHR, the bulky E182 blocks sulfate access. Mutating E182 to T or A in MrHR enables sulfate pumping, with E182A pumping even more efficiently than SyHR-like E182T. The larger cavities in SyHR compared to MrHR near H167 also facilitate translocation of the bulky divalent sulfate anion.


## Cross-References

- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/rhodopsins/halorhodopsin/">Halorhodopsin (HR) from Halobacterium salinarum</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
