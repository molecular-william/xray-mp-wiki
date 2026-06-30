---
title: "TpCorC Magnesium Transporter from Thermus parvatiensis"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abe6140]
verified: false
---

# TpCorC Magnesium Transporter from Thermus parvatiensis

## Overview

CorC is a prokaryotic member of the CNNM/CorC family of Mg2+ transporters, widely distributed in all domains of life. The CorC protein from Thermus parvatiensis (TpCorC) is a Mg2+ exporter that shares approximately 30% sequence identity with the S. aureus CorC orthologs MpfA and MpfB. TpCorC consists of a DUF21 transmembrane (TM) domain (3 TM helices per protomer forming a dimer), a cytoplasmic CBS domain, and a CorC/HlyC domain. The crystal structure of the TpCorC TM domain dimer revealed a fully dehydrated Mg2+ ion binding site with octahedral coordination geometry, distinct from the hydrated Mg2+ binding in MgtE and CorA channels. The CBS domain binds ATP with high affinity (~500 nM), and ATP binding is important for Mg2+ export activity. Mg2+ transport by TpCorC is Na+-dependent, suggesting Na+-coupled Mg2+ export.


## Publications

### doi/10.1126##sciadv.abe6140

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cff">7CFF</a></td>
      <td>2.0</td>
      <td>—</td>
      <td>TpCorC TM domain V101A mutant (residues 26-182)</td>
      <td>Mg2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cfg">7CFG</a></td>
      <td>3.2</td>
      <td>—</td>
      <td>TpCorC TM domain wild-type (residues 26-182)</td>
      <td>Mg2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cfh">7CFH</a></td>
      <td>Not specified</td>
      <td>—</td>
      <td>TpCorC CBS domain apo form (residues 183-361)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7cfi">7CFI</a></td>
      <td>Not specified</td>
      <td>—</td>
      <td>TpCorC CBS domain ATP-bound (residues 202-361)</td>
      <td>ATP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta (DE3)
- **Construct**: TpCorC TM domain (residues 26-182) with C-terminal [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) cleavage site, GFPuv, and octahistidine tag
- **Induction**: 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.6, 18C for 16 hours
- **Media**: LB medium with 50 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/)

**Purification:**

- **Expression system**: E. coli Rosetta (DE3)
- **Expression construct**: TpCorC TM domain residues 26-182 with C-terminal HRV 3C site, GFPuv, His8 tag
- **Tag info**: Octahistidine tag, cleaved by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/)

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
      <td>Cell culture and harvest</td>
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>Induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at OD600 0.6, cultured at 18C for 16 hours, harvested at 5000g for 15 min</td>
    </tr>
    <tr>
      <td>Cell disruption</td>
      <td>High-pressure homogenization</td>
      <td>—</td>
      <td>150 mM NaCl, 50 mM Tris pH 8.0, 1 mM PMSF</td>
      <td>Cells disrupted in buffer A</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>150 mM NaCl, 50 mM Tris pH 8.0</td>
      <td>Low-speed spin at 20000g for 30 min; membrane pellet isolated at 180000g for 1 hour</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>150 mM NaCl, 50 mM Tris pH 8.0 + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside)</td>
      <td>Homogenized membranes solubilized for 1 hour at 4C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (Ni-NTA)</td>
      <td>Ni-NTA agarose</td>
      <td>Buffer B: 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Column washed with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; protein eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage and reverse IMAC</td>
      <td>Protease cleavage and subtractive IMAC</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> digestion to remove His8-GFPuv tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> (SEC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>150 mM NaCl, 50 mM Tris pH 8.0, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted in buffer C</td>
    </tr>
  </tbody>
</table>
**Final sample**: TpCorC TM domain in 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TpCorC TM domain (wild-type or V101A mutant) in 150 mM NaCl, 50 mM Tris pH 8.0, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M MgCl2, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 5.0, 12-18% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (protein:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 200 and 50 mM MgCl2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared specifically in the presence of Mg2+ ions. Crystallization was also tested with Ca2+, Co2+, Ni2+, and Mn2+ but only Mg2+ yielded well-diffracting crystals.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TpCorC CBS domain (residues 183-361 or 202-361)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.4 M ammonium thiocyanate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> pH 4.5, 15% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000; or 0.1 M CaCl2, 0.1 M HEPES pH 7.5, 5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 8000</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, reservoir components</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CBS domain crystallized in apo and ATP-bound forms. ATP-bound structure used construct residues 202-361 with Y255A mutation.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cff">7CFF</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASP</span><span class="topo-outside">ENP</span><span class="topo-membrane">WLWAVLVLLLALSAFFSASE</span><span class="topo-inside">TAITTLYPWKLKELAESKNG</span><span class="topo-unknown">PFRLLAE</span><span class="topo-inside">DITR</span><span class="topo-membrane">FLTTILVGNNLVNIAATALATELA</span><span class="topo-outside">TQAFGSA</span><span class="topo-membrane">GVGVATGAMTFLILFFGEITPKSL</span><span class="topo-inside">AVHHAEA</span></span>
<span class="topo-ruler">       130       140       150       160       170</span>
<span class="topo-line"><span class="topo-inside">IARLAAWPIYGLSVL</span><span class="topo-unknown">FYPVGRFFSLVSGGLLRL</span><span class="topo-inside">LGLEPRL</span><span class="topo-unknown">ESSGLEVLFQ</span></span>
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
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>47</td>
      <td>51</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>71</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>78</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>82</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>89</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>135</td>
      <td>137</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>153</td>
      <td>159</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>160</td>
      <td>177</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cff">7CFF</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASP</span><span class="topo-outside">ENP</span><span class="topo-membrane">WLWAVLVLLLALSAFFSASE</span><span class="topo-inside">TAITTLYPWKLKELAESKNG</span><span class="topo-unknown">PFRLLAE</span><span class="topo-inside">DITR</span><span class="topo-membrane">FLTTILVGNNLVNIAATALATELA</span><span class="topo-outside">TQAFGSA</span><span class="topo-membrane">GVGVATGAMTFLILFFGEITPKSL</span><span class="topo-inside">AVHHAEA</span></span>
<span class="topo-ruler">       130       140       150       160       170</span>
<span class="topo-line"><span class="topo-inside">IARLAAWPIYGLSVL</span><span class="topo-unknown">FYPVGRFFSLVSGGLLRL</span><span class="topo-inside">LGLEPRL</span><span class="topo-unknown">ESSGLEVLFQ</span></span>
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
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>27</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>47</td>
      <td>51</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>71</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>78</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>82</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>89</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>113</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>135</td>
      <td>137</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>153</td>
      <td>159</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>154</td>
      <td>160</td>
      <td>177</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cfg">7CFG</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSP</span><span class="topo-outside">ENP</span><span class="topo-membrane">WLWAVLVLLLALSAFFSASE</span><span class="topo-inside">TAITTLYPWKLKELAESKNG</span><span class="topo-unknown">PFRLLAE</span><span class="topo-inside">DITRF</span><span class="topo-membrane">LTTILVGNNLVNIAATALVTELA</span><span class="topo-outside">TQAFGSA</span><span class="topo-membrane">GVGVATGAMTFLILFFGEITPKSL</span><span class="topo-inside">AVHHAEAI</span></span>
<span class="topo-ruler">       130       140       150       160         </span>
<span class="topo-line"><span class="topo-inside">ARL</span><span class="topo-unknown">AAWPIYGLSVL</span><span class="topo-inside">F</span><span class="topo-unknown">YPVGRFFSLVSGGLLRLLGL</span><span class="topo-inside">EPRL</span><span class="topo-unknown">ESSGLEVLFQ</span></span>
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
      <td>4</td>
      <td>6</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>26</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>46</td>
      <td>51</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>71</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>58</td>
      <td>78</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>81</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>88</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>123</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>134</td>
      <td>148</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>135</td>
      <td>159</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>160</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>159</td>
      <td>180</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7cfg">7CFG</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSP</span><span class="topo-outside">ENP</span><span class="topo-membrane">WLWAVLVLLLALSAFFSASE</span><span class="topo-inside">TAITTLYPWKLKELAESKNG</span><span class="topo-unknown">PFRLLAE</span><span class="topo-inside">DITRF</span><span class="topo-membrane">LTTILVGNNLVNIAATALVTELA</span><span class="topo-outside">TQAFGSA</span><span class="topo-membrane">GVGVATGAMTFLILFFGEITPKSL</span><span class="topo-inside">AVHHAEAI</span></span>
<span class="topo-ruler">       130       140       150       160         </span>
<span class="topo-line"><span class="topo-inside">ARL</span><span class="topo-unknown">AAWPIYGLSVL</span><span class="topo-inside">F</span><span class="topo-unknown">YPVGRFFSLVSGGLLRLLGL</span><span class="topo-inside">EPRL</span><span class="topo-unknown">ESSGLEVLFQ</span></span>
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
      <td>4</td>
      <td>6</td>
      <td>28</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>26</td>
      <td>31</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>46</td>
      <td>51</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>71</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>54</td>
      <td>58</td>
      <td>78</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>81</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>88</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>123</td>
      <td>137</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>134</td>
      <td>148</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>135</td>
      <td>159</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>160</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>159</td>
      <td>180</td>
      <td>183</td>
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

### Mg2+ binding site with fully dehydrated Mg2+ ion

The TpCorC TM domain contains a single Mg2+ binding site per protomer with fully dehydrated Mg2+ coordinated in octahedral geometry. Mg2+ is directly coordinated by side chains of Ser43, Ser47, Asn90, and Glu130 and the main chain carbonyl oxygens of Ser43 and Gly129. Bonding distances are 2.1-2.2 A, consistent with canonical Mg2+-oxygen distances. All five residues are strictly conserved in human CNNM2 and CNNM4. Alanine substitution at these positions (S43A, S47A, N90A, G129A, E130A) severely impairs or abolishes Mg2+ export activity. This fully dehydrated Mg2+ recognition contrasts with MgtE and CorA channels where Mg2+ remains hydrated, accounting for differences in transport kinetics between channels and transporters.

### Novel DUF21 TM domain fold with belt helix

The TpCorC TM domain presents a novel protein fold distinct from any previously reported membrane protein structure. Each protomer has three TM helices plus three cytoplasmic helices (CH1, CH2, and belt helix). The belt helix following TM3 is approximately 35 residues long, amphipathic, and nearly parallel to the membrane plane. It interacts with TM1 and TM2 within the protomer and with TM3 of the neighboring subunit. The protein forms a dimer with close intersubunit contacts at the periplasmic side (TM2 and TM3) but loose contacts at the cytoplasmic side, adopting an inward-open conformation.

### Na+-dependent Mg2+ transport

Mg2+ export by TpCorC is Na+-dependent. Depletion of Na+ from the bath solution induces loss of Mg2+ export activity, suggesting the Na+ gradient is a potential driving force for Mg2+ export. The dimer interface near the Mg2+ binding site, containing multiple Asn residues (Asn91, Asn94), is a candidate Na+ binding site. Asn94 is conserved in human CNNM2 and CNNM4, and the N94A mutation reduces Na+ sensitivity and Mg2+ transport activity.

### ATP binding to CBS domain regulates Mg2+ transport

The TpCorC CBS domain binds ATP with high affinity (Kd ~500 nM). ATP is bound at the interface between two tandem CBS repeats, with the adenine base recognized by hydrogen bonds with Val235 and Arg257, and stacking with Tyr255. The ribose interacts with Asp339, and phosphate groups interact with Ser256, Arg257, and Thr336. Mg2+ ions stabilize phosphate conformation. ATP-binding site mutants (Y255A, T336I) reduce ATP binding and impair Mg2+ export activity. Given cytoplasmic ATP concentrations in the millimolar range, ATP likely binds constitutively as a regulatory cofactor.

### CNNM/CorC family disease associations

All five residues of the Mg2+ binding site are strictly conserved in human CNNM2 (Ser269, Ser273, Asn323, Gly356, Glu357) and CNNM4 (Ser196, Ser200, Asn250, Gly283, Glu284). Many known disease-associated mutations in CNNM2 and CNNM4 map to the Mg2+ binding site. CNNM2 mutations cause dominant hypomagnesemia; CNNM4 mutations cause Jalili syndrome. The CNNM2 T568I mutant (corresponding to TpCorC T336I) loses both ATP binding and Mg2+ export activity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/magnesium-transport/">Magnesium Transport</a> — Concept for Mg2+ transport mechanisms in membrane proteins (placeholder for future creation)
- <a href="/xray-mp-wiki/proteins/other-ion-channels/mgt-e-thermus-thermophilus/">MgtE (Magnesium Transport Channel)</a> — Comparison of fully dehydrated Mg2+ binding in CorC vs hydrated Mg2+ in MgtE channel
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
