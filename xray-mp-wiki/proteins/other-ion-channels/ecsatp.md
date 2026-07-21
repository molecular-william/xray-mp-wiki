---
title: "EcSatP — Bacterial Succinate-Acetate Transporter (AceTr Family)"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein]
sources: [doi/10.1074##jbc.RA118.003876]
verified: agent
uniprot_id: P0AC98
---

# EcSatP — Bacterial Succinate-Acetate Transporter (AceTr Family)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AC98">UniProt: P0AC98</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

SatP (also known as yaaH) is a member of the  uptake transporter (AceTr) family
(TC 2.A.96) from *Escherichia coli*. It functions as a -/proton symporter
and forms a hexameric UreI-like channel structure. The crystal structure of ecSatP was
determined at 2.8 Å resolution using [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with a predicted model from
Baker's group. Each protomer contains six transmembrane (TM) helices surrounding a
central channel pore, with three conserved hydrophobic residues (F17, Y72, L131 — the
"FLY" motif) forming a constriction site in the TM region. Single-channel conductance
recordings of purified ecSatP reconstituted into lipid bilayers demonstrated a conductance
of 1.2 ± 0.34 nS with bidirectional channel activity and substrate selectivity for
carboxylates and chloride. Three conserved polar residues in TM1 (T21, N25, N28) were
shown to be critical for  translocation activity.


## Publications

### doi/10.1074##jbc.RA118.003876

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a></td>
      <td>2.80</td>
      <td>P3_2</td>
      <td>Full-length ecSatP (residues 1-182)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length ecSatP in modified pET15b vector with DrICE cutting site
- **Notes**: Cells induced with 0.2 mM  at 22 °C overnight

**Purification:**

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: Full-length ecSatP with N-terminal 6×His tag

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
      <td>Membrane solubilization</td>
      <td>1% (w/v)  + 1 mM , 1.5 h at 4 °C</td>
      <td>—</td>
      <td></td>
      <td>Ultracentrifugation at 150,000×g for 30 min to remove insoluble fraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>—</td>
      <td></td>
      <td>Eluted with 270 mM  in 25 mM  pH 7.0, 150 mM NaCl, 0.05% </td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200 Increase [SEC</a> Resin](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300</td>
      <td>—</td>
      <td>25 mM  pH 7.0, 150 mM NaCl, 0.05% (w/v) </td>
      <td>N-terminal His tag removed using DrICE prior to crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ecSatP in 25 mM  pH 8.0, 150 mM NaCl, 0.4% (w/v) beta-NG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.05 M  pH 9.8, 27% (v/v) , 0.1 M NaCl with 0.15 mM n-nonyl-beta-D-thioglucoside</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Dehydration by adding  to 40% (v/v) over 24 h</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Hexagonal-shaped crystals. Additive screening with n-nonyl-beta-D-thioglucoside improved diffraction. Dehydration trials critical for reaching 2.8 Å resolution.</td>
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
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Sodium Chloride: 0.1 M [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLAN</span><span class="topo-membrane">PAPLGLMGFGMTTILLNL</span><span class="topo-outside">HNVGYFALDGIIL</span><span class="topo-membrane">AMGIFYGGIAQIFAGLL</span><span class="topo-inside">EYKKGNTF</span><span class="topo-membrane">GLTAFTSYGSFWLTL</span><span class="topo-outside">VAILLMPKLGLTDAPNAQFL</span><span class="topo-membrane">GVYLGLWGVFTLFMF</span><span class="topo-inside">FGTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGAR</span><span class="topo-membrane">VLQFVFFSLTVLFALLAI</span><span class="topo-outside">GNIAGNAAIIH</span><span class="topo-membrane">FAGWIGLICGASAIYLAM</span><span class="topo-inside">GEVLNEQFGRTVLPIGE</span><span class="topo-unknown">SH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>41</td>
      <td>27</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>40</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>66</td>
      <td>57</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>81</td>
      <td>65</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>101</td>
      <td>80</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>100</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>115</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>123</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>153</td>
      <td>141</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>188</td>
      <td>170</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>190</td>
      <td>187</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLAN</span><span class="topo-membrane">PAPLGLMGFGMTTIL</span><span class="topo-outside">LNLHNVGYFALDGIILA</span><span class="topo-membrane">MGIFYGGIAQIFAGLL</span><span class="topo-inside">EYKKGNT</span><span class="topo-membrane">FGLTAFTSYGSFWLTL</span><span class="topo-outside">VAILLMPKLGLTDAPNAQFLG</span><span class="topo-membrane">VYLGLWGVFTLFMFF</span><span class="topo-inside">GTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGA</span><span class="topo-membrane">RVLQFVFFSLTVLFALLA</span><span class="topo-outside">IGNIAGNAAIIHF</span><span class="topo-membrane">AGWIGLICGASAIYLAMG</span><span class="topo-inside">EVLNEQFGRTVLPIGE</span><span class="topo-unknown">SH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>9</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>42</td>
      <td>24</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>58</td>
      <td>41</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>57</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>64</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>102</td>
      <td>80</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>117</td>
      <td>101</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>116</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>141</td>
      <td>122</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>154</td>
      <td>140</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>153</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>188</td>
      <td>171</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>190</td>
      <td>187</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLANP</span><span class="topo-membrane">APLGLMGFGMTTILLNL</span><span class="topo-outside">HNVGYFALDGIIL</span><span class="topo-membrane">AMGIFYGGIAQIFAGLL</span><span class="topo-inside">EYKKGNTF</span><span class="topo-membrane">GLTAFTSYGSFWLTLV</span><span class="topo-outside">AILLMPKLGLTDAPNAQFL</span><span class="topo-membrane">GVYLGLWGVFTLFMF</span><span class="topo-inside">FGTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGARVLQ</span><span class="topo-membrane">FVFFSLTVLFALLAI</span><span class="topo-outside">GNIAGNAAIIH</span><span class="topo-membrane">FAGWIGLICGASAIYLAM</span><span class="topo-inside">GEVLNEQFGRTVLPIG</span><span class="topo-unknown">ESH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>11</td>
      <td>5</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>28</td>
      <td>10</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>41</td>
      <td>27</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>40</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>66</td>
      <td>57</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>82</td>
      <td>65</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>81</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>100</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>127</td>
      <td>115</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>142</td>
      <td>126</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>153</td>
      <td>141</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>187</td>
      <td>170</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>190</td>
      <td>186</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLAN</span><span class="topo-membrane">PAPLGLMGFGMTTIL</span><span class="topo-outside">LNLHNVGYFALDGIILA</span><span class="topo-membrane">MGIFYGGIAQIFAGLLE</span><span class="topo-inside">YKKGNT</span><span class="topo-membrane">FGLTAFTSYGSFWLT</span><span class="topo-outside">LVAILLMPKLGLTDAPNAQFLGVY</span><span class="topo-membrane">LGLWGVFTLFMFFGT</span><span class="topo-inside">L</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGA</span><span class="topo-membrane">RVLQFVFFSLTVLFAL</span><span class="topo-outside">LAIGNIAGNAAIIHFAG</span><span class="topo-membrane">WIGLICGASAIYLAMG</span><span class="topo-inside">EVLNEQFGRTVLPIGE</span><span class="topo-unknown">SH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>9</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>42</td>
      <td>24</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>59</td>
      <td>41</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>65</td>
      <td>58</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>80</td>
      <td>64</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>104</td>
      <td>79</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>119</td>
      <td>103</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>139</td>
      <td>122</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>156</td>
      <td>138</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>172</td>
      <td>155</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>188</td>
      <td>171</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>190</td>
      <td>187</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLAN</span><span class="topo-membrane">PAPLGLMGFGMTTI</span><span class="topo-outside">LLNLHNVGYFALDGIILA</span><span class="topo-membrane">MGIFYGGIAQIFAGLLE</span><span class="topo-inside">YKKGNT</span><span class="topo-membrane">FGLTAFTSYGSFWLT</span><span class="topo-outside">LVAILLMPKLGLTDAPNAQFLGV</span><span class="topo-membrane">YLGLWGVFTLFMFFGT</span><span class="topo-inside">L</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGA</span><span class="topo-membrane">RVLQFVFFSLTVLFAL</span><span class="topo-outside">LAIGNIAGNAAIIHFAG</span><span class="topo-membrane">WIGLICGASAIYLAMGEVL</span><span class="topo-inside">NEQFGRTVLPIGE</span><span class="topo-unknown">SH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>9</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>42</td>
      <td>23</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>59</td>
      <td>41</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>65</td>
      <td>58</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>80</td>
      <td>64</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>103</td>
      <td>79</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>119</td>
      <td>102</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>139</td>
      <td>122</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>156</td>
      <td>138</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>175</td>
      <td>155</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>188</td>
      <td>174</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>190</td>
      <td>187</td>
      <td>188</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zug">5ZUG</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AHMGNT</span><span class="topo-inside">KLAN</span><span class="topo-membrane">PAPLGLMGFGMTTILLNL</span><span class="topo-outside">HNVGYFALDGIIL</span><span class="topo-membrane">AMGIFYGGIAQIFAGLL</span><span class="topo-inside">EYKKGNT</span><span class="topo-membrane">FGLTAFTSYGSFWLTL</span><span class="topo-outside">VAILLMPKLGLTDAPNAQFLG</span><span class="topo-membrane">VYLGLWGVFTLFMFF</span><span class="topo-inside">GTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190</span>
<span class="topo-line"><span class="topo-inside">KGAR</span><span class="topo-membrane">VLQFVFFSLTVLFALLA</span><span class="topo-outside">IGNIAGNAAIIH</span><span class="topo-membrane">FAGWIGLICGASAIYLAM</span><span class="topo-inside">GEVLNEQFGRTVLPIG</span><span class="topo-unknown">ESH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>-1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>5</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>41</td>
      <td>27</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>40</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>65</td>
      <td>57</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>81</td>
      <td>64</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>102</td>
      <td>80</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>117</td>
      <td>101</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>124</td>
      <td>116</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>141</td>
      <td>123</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>153</td>
      <td>140</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>187</td>
      <td>170</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>190</td>
      <td>186</td>
      <td>188</td>
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

### Hexameric channel architecture of AceTr family

The ecSatP structure reveals a hexameric arrangement forming a compact cylinder
(~95 Å diameter, ~45 Å height) with a central pore occupied by lipid/detergent.
The protomer serves as the functional unit with six TM helices forming an
hourglass-shaped channel. This architecture is similar to the  channel UreI
but with reverse topology (N/C termini cytoplasmic vs periplasmic in UreI).

### FLY constriction gate and substrate selectivity

Three conserved hydrophobic residues (F17, Y72, L131) form a constriction site
narrowing to ~0.8 Å in the closed state. The "FLY" motif is highly conserved
in the AceTr family. Mutations at L131 (corresponding to L131V) alter substrate
specificity, suggesting the constriction site contributes to substrate selectivity.

### Substrate recognition by TM1 polar residues

Three conserved polar residues in TM1 (T21, N25, N28) on the periplasmic side
are critical for  translocation. Single-channel conductance assays of
T21A and N25A mutants showed reduced substrate blockade frequency compared to
wild-type, with N28A failing to form functional channels, demonstrating their
essential role in substrate recognition and transport.

### Channel-like mechanism vs. transporter

Single-channel conductance measurements (~10^7 ions/s, 1.2 nS conductance)
combined with the channel-like structure suggest ecSatP functions as an 
channel rather than a classical transporter, despite the AceTr family being
annotated as transporters. The bidirectional permeation observed contrasts with
the unidirectional transport reported for the close homolog ckSatP.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/succinate/">Succinate</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a> — Referenced in ecsatp text
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Referenced in ecsatp text
