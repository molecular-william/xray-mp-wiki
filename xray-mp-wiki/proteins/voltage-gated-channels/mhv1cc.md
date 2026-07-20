---
title: "mHv1cc Mouse Voltage-Gated Proton Channel"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2783]
verified: agent
uniprot_id: Q3U2S8
---

# mHv1cc Mouse Voltage-Gated Proton Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q3U2S8">UniProt: Q3U2S8</a>

<span class="expr-badge">Mus musculus</span>

## Overview

mHv1cc is a crystallizable construct of the mouse voltage-gated proton channel (mHv1, also known as VSOP) that includes the coiled-coil (CC) cytoplasmic domain fused to the transmembrane core. Voltage-gated proton channels play critical roles in regulating intracellular pH, facilitating the respiratory burst in phagocytes, and controlling sperm capacitation. The crystal structure of mHv1cc at 3.45 A resolution reveals a dimeric arrangement mediated by a coiled-coil interaction in the cytoplasmic C-terminal domain. The structure features a long S4 helix that extends from the transmembrane region into the cytoplasm, and double hydrophobic layers that may prevent proton leakage in the resting state while allowing proton conduction upon S4 movement.


## Publications

### doi/10.1038##nsmb.2783

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3wkv">3WKV</a></td>
      <td>3.45</td>
      <td>P6_3</td>
      <td>mHv1cc (S76-mHv1cc construct), Se-Met labeled for MAD phasing</td>
      <td>none (apo structure; Zn2+ binding analyzed by anomalous signals)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: mHv1cc (S76-mHv1cc construct) with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) labeling for MAD phasing

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
      <td>Protein expression and purification</td>
      <td>Standard E. coli expression and purification</td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td>Selenomethionine-labeled protein expressed in E. coli for <a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a> phasing; multiple crystal forms grown (Cryst-A, Cryst-B, Se-Met1-3 variants)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Multiple crystal forms obtained: native Cryst-B (S76-mHv1cc) at 3.45 A resolution; <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> derivatives Se-Met1 (L107M L118M), Se-Met2, and Se-Met3 (L182M) for MAD phasing; and zinc-bound crystals (Cryst-Z1, Cryst-Z2). All crystals in space group P6_3. Initial phasing by Se-MAD at 4.3 A resolution. Native data collected to 3.45 A.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wkv">3WKV</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGGSHHHHHHHHGENLYFQGLESTPRQSLD</span><span class="topo-outside">FRSRLRKLFS</span><span class="topo-unknown">S</span><span class="topo-outside">HRF</span><span class="topo-membrane">QVIIICLVVLDALLVLAELL</span><span class="topo-inside">LDLK</span><span class="topo-unknown">IIEPDEQDYA</span><span class="topo-inside">VTAFHYM</span><span class="topo-membrane">SFAILVFFMLDLGLRIFAYG</span><span class="topo-unknown">PKN</span><span class="topo-outside">F</span><span class="topo-unknown">F</span><span class="topo-outside">TNP</span><span class="topo-membrane">WEVADGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190      </span>
<span class="topo-line"><span class="topo-membrane">IVVVSFVLDLVLL</span><span class="topo-inside">F</span><span class="topo-unknown">KSHH</span><span class="topo-inside">FEA</span><span class="topo-membrane">LGLLILLRLWRVARIING</span><span class="topo-outside">IIISRMKQLEDKIEELLSKIYHLENEIARL</span><span class="topo-unknown">KKLIGER</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>30</td>
      <td>54</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>40</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>41</td>
      <td>94</td>
      <td>94</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>95</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>64</td>
      <td>98</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>68</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>78</td>
      <td>122</td>
      <td>131</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>132</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>139</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>108</td>
      <td>159</td>
      <td>161</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>109</td>
      <td>162</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>110</td>
      <td>162</td>
      <td>162</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>133</td>
      <td>166</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>134</td>
      <td>186</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>138</td>
      <td>187</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>141</td>
      <td>191</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>189</td>
      <td>212</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>196</td>
      <td>242</td>
      <td>248</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wkv">3WKV</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGGSHHHHHHHHGENLYFQGLESTPRQSLD</span><span class="topo-outside">FRSRLRKLFS</span><span class="topo-unknown">S</span><span class="topo-outside">HRF</span><span class="topo-membrane">QVIIICLVVLDALLVLAELL</span><span class="topo-inside">LDLK</span><span class="topo-unknown">IIEPDEQDYA</span><span class="topo-inside">VTAFHYM</span><span class="topo-membrane">SFAILVFFMLDLGLRIFAYG</span><span class="topo-unknown">PKN</span><span class="topo-outside">F</span><span class="topo-unknown">F</span><span class="topo-outside">TNP</span><span class="topo-membrane">WEVADGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190      </span>
<span class="topo-line"><span class="topo-membrane">IVVVSFVLDLVLL</span><span class="topo-inside">F</span><span class="topo-unknown">KSHH</span><span class="topo-inside">FEA</span><span class="topo-membrane">LGLLILLRLWRVARIING</span><span class="topo-outside">IIISRMKQLEDKIEELLSKIYHLENEIARL</span><span class="topo-unknown">KKLIGER</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>30</td>
      <td>54</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>40</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>41</td>
      <td>94</td>
      <td>94</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>95</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>64</td>
      <td>98</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>68</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>78</td>
      <td>122</td>
      <td>131</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>132</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>139</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>108</td>
      <td>159</td>
      <td>161</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>109</td>
      <td>162</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>110</td>
      <td>162</td>
      <td>162</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>133</td>
      <td>166</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>134</td>
      <td>186</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>138</td>
      <td>187</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>141</td>
      <td>191</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>189</td>
      <td>212</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>196</td>
      <td>242</td>
      <td>248</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wkv">3WKV</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGGSHHHHHHHHGENLYFQGLESTPRQSLD</span><span class="topo-outside">FRSRLRKLFS</span><span class="topo-unknown">S</span><span class="topo-outside">HRF</span><span class="topo-membrane">QVIIICLVVLDALLVLAELL</span><span class="topo-inside">LDLK</span><span class="topo-unknown">IIEPDEQDYA</span><span class="topo-inside">VTAFHYM</span><span class="topo-membrane">SFAILVFFMLDLGLRIFAYG</span><span class="topo-unknown">PKN</span><span class="topo-outside">F</span><span class="topo-unknown">F</span><span class="topo-outside">TNP</span><span class="topo-membrane">WEVADGL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190      </span>
<span class="topo-line"><span class="topo-membrane">IVVVSFVLDLVLL</span><span class="topo-inside">F</span><span class="topo-unknown">KSHH</span><span class="topo-inside">FEA</span><span class="topo-membrane">LGLLILLRLWRVARIING</span><span class="topo-outside">IIISRMKQLEDKIEELLSKIYHLENEIARL</span><span class="topo-unknown">KKLIGER</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>30</td>
      <td>54</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>40</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>41</td>
      <td>94</td>
      <td>94</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>44</td>
      <td>95</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>64</td>
      <td>98</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>68</td>
      <td>118</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>78</td>
      <td>122</td>
      <td>131</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>132</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>139</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>108</td>
      <td>159</td>
      <td>161</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>109</td>
      <td>162</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>110</td>
      <td>162</td>
      <td>162</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>113</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>133</td>
      <td>166</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>134</td>
      <td>186</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>138</td>
      <td>187</td>
      <td>190</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>141</td>
      <td>191</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>189</td>
      <td>212</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>196</td>
      <td>242</td>
      <td>248</td>
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

### Zn2+ binding and S4 position

Zinc ions bind to the voltage-gated proton channel and modulate its activity. Bijvoet anomalous difference maps of Zn2+ were calculated at 5.0 sigma contoured level, confirming the position of S4 within the channel. The S4 helix consists of a 3_10 helix (Arg201-Arg204) and an alpha helix (Arg204-Arg207), with three arginine residues (Arg201, Arg204, Arg207) serving as gating charges.

### Double hydrophobic layers for proton conduction

The presence of two hydrophobic layers in the channel may have implications for proton permeation. Minimum S4 motion upon activation could allow protons to be conducted by recruiting water molecules into a continuous water-wire across the channel, while proton leakage is prevented in the resting state. This resembles the case of the M2 proton channel of influenza A virus, which also shows two barriers built by His37 and Trp41.

### Coiled-coil dimer interface

The cytoplasmic domain of mHv1cc forms a coiled-coil dimer interface. Sequence alignment using the 'abcdefg' heptad repeat convention shows that the dimer-interface residues (positions a and d) are conserved. Superimposition of the mHv1cc coiled-coil region (Ile225-Leu242) with the mouse Hv1 cytoplasmic coiled-coil (Ile224-Gly266) shows an RMSD of 0.670 A. The trimer observed in crystal packing is distinct from the functional dimeric assembly.

### Sequence conservation of gating-associated residues

Alignment of mHv1cc with related voltage-gated proton channels from multiple species (mouse, human, Ciona, zebrafish, etc.) shows conserved S1-S4 transmembrane segments. The gating arginine residues and the coiled-coil dimer interface are highly conserved. A table of accessibility by MTS reagent or Zn2+ maps the up-state (activated) and down-state (resting) conformations of the S4 helix.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating</a> — mHv1cc is a voltage-gated proton channel with S4-based gating mechanism
- <a href="/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel/">Influenza A M2 Proton Channel</a> — M2 proton channel also uses double hydrophobic barrier mechanism for proton conduction
- <a href="/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/">Voltage-Sensor Paddle</a> — mHv1cc contains a voltage-sensing S4 helix with gating arginines
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
