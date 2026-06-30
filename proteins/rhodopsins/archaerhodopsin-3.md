---
title: "Archaerhodopsin-3 (AR3)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-20596-0]
verified: false
---

# Archaerhodopsin-3 (AR3)

## Overview

Archaerhodopsin-3 (AR3) is a light-driven proton pump from the archaebacterium Halorubrum sodomense. It has seven transmembrane helices and a single extracellular-facing two-stranded beta-sheet, with [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) covalently bound to Lys226 via a Schiff base linkage. AR3 is particularly suitable for optogenetics due to its faster photocycle kinetics compared to homologs like [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/). Two high-resolution crystal structures have been solved: the light-adapted (LA) ground state (6S6C, 1.1 A) and the dark-adapted (DA) desensitized state (6GUX, 1.3 A). These structures revealed that the DA state permits thermal equilibrium between [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomers, while the LA state favors [All-Trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/), and that internal water network dynamics underpin receptor sensitization.

## Publications

### doi/10.1038##s41467-020-20596-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6s6c">6S6C</a></td>
      <td>1.1 A</td>
      <td>not specified</td>
      <td>Wild-type AR3 from Halorubrum sodomense, full-length proton pump</td>
      <td>All-trans retinal (LA ground state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gux">6GUX</a></td>
      <td>1.3 A</td>
      <td>not specified</td>
      <td>Wild-type AR3 from Halorubrum sodomense, full-length proton pump in dark-adapted state</td>
      <td>Mixed 13-cis and all-trans retinal (70% cis, 30% trans)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Halorubrum sodomense (wild-type, non-genetically modified)
- **Construct**: Wild-type AR3 purified from native purple membrane

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
      <td>Membrane preparation</td>
      <td>Sucrose density gradient <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>--</td>
      <td>4 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> for resuspension; 0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> for dialysis; distilled water + --</td>
      <td>Cells collected by centrifugation, resuspended in 4 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, stirred 2 h, homogenized, dialyzed overnight in 0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>. <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> gradient (30-60% w/v) at 110,000 x g for 15 h at 15 C. AR3-rich membrane band collected, <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> removed by overnight dialysis. Final concentration 20 mg/ml, AR3 content 78 +/- 2% w/w.</td>
    </tr>
    <tr>
      <td>Crystallization</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization without detergents</td>
      <td>--</td>
      <td>Not applicable + --</td>
      <td>Purification and crystallization performed in absence of detergents. AR3 mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> at 40:60 volume ratio. Crystals grown in 30% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> pH 5.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 150 mM Ca2+ at 20 C.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Non-delipidated AR3 at 20 mg/ml mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> at 40:60 volume ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>All crystallization procedures performed under dim light. LA structure from crystals illuminated with white tungsten light for 2 min prior to cryo-freezing. DA structure from crystals not exposed to light. Data collected at Diamond Light Source I24 microfocus beamline.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6s6c">6S6C</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">?AGYDLLGDGRPE</span><span class="topo-membrane">TLWLGIGTLLMLIGTFYFLV</span><span class="topo-inside">RGWGVTDKDAREYY</span><span class="topo-membrane">AVTILVPGIASAAYLSMFFGIGL</span><span class="topo-outside">TEVTVGGEMLDI</span><span class="topo-membrane">YYARYADWLFTTPLLLLDLA</span><span class="topo-inside">LLAKVDRV</span><span class="topo-membrane">TIGTLVGVDA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LMIVTGLIGAL</span><span class="topo-outside">SHTAIAR</span><span class="topo-membrane">YSWWLFSTICMIVVLYFLATS</span><span class="topo-inside">LRSAAKERGPEVASTFNT</span><span class="topo-membrane">LTALVLVLWTAYPILWIIG</span><span class="topo-outside">TEGAGVVGL</span><span class="topo-membrane">GIETLLFMVLDVTAKVGFGFIL</span><span class="topo-inside">LRSRAILGDTEAP</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">E</span></span>
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
      <td>13</td>
      <td>7</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>33</td>
      <td>20</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>40</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>70</td>
      <td>54</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>82</td>
      <td>77</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>102</td>
      <td>89</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>110</td>
      <td>109</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>131</td>
      <td>117</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>138</td>
      <td>138</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>159</td>
      <td>145</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>177</td>
      <td>166</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>196</td>
      <td>184</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>205</td>
      <td>203</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>227</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>241</td>
      <td>234</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gux">6GUX</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">QAGYDLLGDGRPE</span><span class="topo-membrane">TLWLGIGTLLMLIGTFYFLV</span><span class="topo-inside">RGWGVTDKDAREYY</span><span class="topo-membrane">AVTILVPGIASAAYLSMFF</span><span class="topo-outside">GIGLTEVTVGGEMLDIY</span><span class="topo-membrane">YARYADWLFTTPLLLLDL</span><span class="topo-inside">ALLAKVDRV</span><span class="topo-membrane">TIGTLVGVDA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LMIVTGLIGA</span><span class="topo-outside">LSHTAIAR</span><span class="topo-membrane">YSWWLFSTICMIVVLYFLA</span><span class="topo-inside">TSLRSAAKERGPEVASTFNTL</span><span class="topo-membrane">TALVLVLWTAYPILWIIG</span><span class="topo-outside">TEGAGVVGLG</span><span class="topo-membrane">IETLLFMVLDVTAKVGFGFI</span><span class="topo-inside">LLRSRAILGDTEAP</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">E</span></span>
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
      <td>13</td>
      <td>7</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>33</td>
      <td>20</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>40</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>66</td>
      <td>54</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>83</td>
      <td>73</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>101</td>
      <td>90</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>110</td>
      <td>108</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>130</td>
      <td>117</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>138</td>
      <td>137</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>157</td>
      <td>145</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>164</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>196</td>
      <td>185</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>206</td>
      <td>203</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>226</td>
      <td>213</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>241</td>
      <td>233</td>
      <td>247</td>
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

### Dark-adapted state enables thermal retinal isomerization equilibrium

The DA state structure (6GUX) reveals both [13-Cis Retinal](/xray-mp-wiki/reagents/ligands/13-cis-retinal/) (70%) and all-trans (30%) [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomers in the binding pocket. QM/MM calculations show the [13-Cis Retinal](/xray-mp-wiki/reagents/ligands/13-cis-retinal/) isomer is energetically favored in the DA state (Delta G = -1.9 kcal/mol), consistent with thermal equilibrium established in the absence of light. In contrast, the LA state strongly favors [All-Trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (Delta G = 10.9 kcal/mol), requiring photon absorption for isomerization. The activation energy for interconversion is 4.4 kcal/mol higher in the LA state (21.5 vs 17.1 kcal/mol).

### Internal water network dynamics govern receptor sensitization

Comparison of DA and LA structures reveals subtle changes in the Schiff base electronic environment. In the LA state, the SB nitrogen atom moves 0.5 A, destabilizing a pentagonal H-bond network involving Wat402, Thr99, and Asp95. Wat402 becomes disordered in the LA state, and Asp95 adopts two conformations. W401 shows dual positions in both states (absent in [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) ground state). These water network changes reduce the activation energy for [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization in the DA state, enabling thermal equilibration between cis and trans isomers.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Closest homolog to AR3 (59% sequence identity); archaerhodopsin-1 (AR1, PDB: 1UAZ) used as molecular replacement search model
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans retinal</a> — Chromophore covalently bound to conserved Lys226 via Schiff base
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of the lipidic cubic phase crystallization matrix
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — Buffer (100 mM, pH 5.5) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt (150 mM) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — Calcium (150 mM) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">Polyethylene glycol 600 (PEG 600)</a> — Precipitant (30%) used in crystallization reservoir
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to grow AR3 crystals at 20 C
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Referenced in archaerhodopsin-3
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Referenced in archaerhodopsin-3
