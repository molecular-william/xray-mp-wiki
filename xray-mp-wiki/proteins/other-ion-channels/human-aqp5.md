---
title: "Human Aquaporin 5 (AQP5)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0801466105]
verified: agent
uniprot_id: P55064
---

# Human Aquaporin 5 (AQP5)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P55064">UniProt: P55064</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human Aquaporin 5 (HsAQP5) is a water-selective channel protein belonging to the aquaporin family of major intrinsic proteins (MIPs). AQP5 is primarily expressed in salivary glands, lacrimal glands, lungs, and sweat glands, where it facilitates water transport across epithelial cell membranes. The high-resolution X-ray structure of HsAQP5 was determined at 2.0 A resolution, revealing a tetrameric assembly with each protomer forming an independent water channel. The structure was solved in the presence of near-perfect pseudomerohedral twinning (46.3% twin fraction), requiring specialized refinement using SHELXL. The structure displays the canonical aquaporin fold with six transmembrane helices and two half-helices containing the conserved NPA (Asn-Pro-Ala) motifs, and reveals a short C-terminal helix that shows conformational flexibility between protomers. Potential phosphorylation sites in loop B, loop D, and the C-terminal region suggest mechanisms for channel regulation.


## Publications

### doi/10.1073##pnas.0801466105

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3d9s">3D9S</a></td>
      <td>2.0</td>
      <td>P2(1)2(1)2(1) (non-tagged construct); P312 (His-tagged construct)</td>
      <td>Full-length human AQP5 expressed in Pichia pastoris without affinity tag; His-tagged construct also produced for validation</td>
      <td>Water molecules; NG (n-nonyl-beta-D-glucopyranoside) detergent</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Full-length HsAQP5 (cDNA from IMAGE clone 5269384) subcloned into pPICZB via EcoRI/NotI with extra serine after start codon; amino acid numbering starts with Met-0
- **Notes**: Expressed in buffered glycerol complex medium, induced with buffered methanol complex medium at OD600=1; 0.5% methanol added every 24 h for 75 h

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
      <td>Bead beating and ultracentrifugation</td>
      <td>--</td>
      <td>Breaking buffer (50 mM NaH2PO4, 1 mM EDTA, 5% glycerol, 1 mM PMSF) + --</td>
      <td>Cells broken with Bead Beater (Bio Spec) using 200 ml glass beads (0.5 mm diameter), 12 x 30 s runs with 30 s cooling. Debris removed by 2 x 30 min at 1400 x g; membranes pelleted at 186,000 x g for 2 h. ~400 mg crude membrane protein/L culture recovered.</td>
    </tr>
    <tr>
      <td>Urea/alkali wash</td>
      <td>Peripheral protein removal</td>
      <td>--</td>
      <td>Buffer A (20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a>-NaOH pH 7.8, 50 mM NaCl, 10% glycerol, 2 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>) + --</td>
      <td>Urea/alkali wash according to Fotiadis et al. (2001); centrifugation extended to 1.5 h; pellet briefly washed with ddH2O after NaOH treatment</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.8, 50 mM NaCl, 10% glycerol, 2 mM beta-MeOH + 6% <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG (n-nonyl-beta-D-glucopyranoside)</a></td>
      <td>Solubilization screen identified NG and OTG (n-octyl-beta-D-thioglucopyranoside) as suitable detergents. Membranes (~30 mg protein) diluted dropwise with equal volume of solubilization buffer, stirred 1 h at RT. Nonsolubilized material removed at 140,000 x g for 30 min at 4 C.</td>
    </tr>
    <tr>
      <td>Cation exchange chromatography</td>
      <td>Ion exchange chromatography</td>
      <td>Resource S (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0, 15-500 mM NaCl gradient + 0.4% NG</td>
      <td>Supernatant diluted 1:3 with 20 mM MES pH 6.0, 10% glycerol, 2 mM beta-MeOH, 0.4% NG; pH adjusted to 6.0. Applied to Resource S column equilibrated with 20 mM MES pH 6.0, 15 mM NaCl, 0.4% NG. Eluted with gradient 15-500 mM NaCl at 1 ml/min. Fractions concentrated to <0.5 ml using Vivaspin 20 concentrator.</td>
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
      <td>Purified HsAQP5 in detergent (non-tagged construct for P2(1)2(1)2(1) crystals; His-tagged construct for P312 crystals)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in available raw text (crystallization conditions in main text not available)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified in available text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Non-tagged HsAQP5 crystallized in space group P2(1)2(1)2(1); His-tagged HsAQP5 crystallized in space group P312. Structure exhibited near-perfect pseudomerohedral twinning (46.3% twin fraction) with twin operator (0 1 0 1 0 0 0 0 -1) swapping a and b axes. Refinement performed using SHELXL. 3.0 A partially twinned data (twin fraction 13%) from His-tagged crystals used for validation. Data collected at 2.0 A (twinned). Full omit maps calculated using CNS model_map.twin script.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d9s">3D9S</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SKKEVCSVAFLKA</span><span class="topo-membrane">VFAEFLATLIFVFFGLGS</span><span class="topo-outside">ALKWPSALPTIL</span><span class="topo-membrane">QIALAFGLAIGTLAQALG</span><span class="topo-inside">PVS</span><span class="topo-unknown">GGHINPAITLALLVG</span><span class="topo-inside">NQISLLR</span><span class="topo-membrane">AFFYVAAQLVGAIAGAGIL</span><span class="topo-outside">YGVAPLNARGNLAV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NALNNNTTQGQAM</span><span class="topo-membrane">VVELILTFQLALCIFAS</span><span class="topo-inside">TDSRRTSPVG</span><span class="topo-membrane">SPALSIGLSVTLGHLVG</span><span class="topo-outside">IYFTGC</span><span class="topo-unknown">SMNPARSFGP</span><span class="topo-outside">AVVMNRFSPAHW</span><span class="topo-membrane">VFWVGPIVGAVLAAILY</span><span class="topo-inside">FYLLFPNSLSLSERVAII</span></span>
<span class="topo-ruler">       250       260      </span>
<span class="topo-line"><span class="topo-inside">KGTYEP</span><span class="topo-unknown">DEDWEEQREERKKTMELTTR</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
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
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>44</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>65</td>
      <td>62</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>80</td>
      <td>65</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>80</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>87</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>133</td>
      <td>106</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>133</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>160</td>
      <td>150</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>183</td>
      <td>177</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>193</td>
      <td>183</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>194</td>
      <td>205</td>
      <td>193</td>
      <td>204</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>222</td>
      <td>205</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>246</td>
      <td>222</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>266</td>
      <td>246</td>
      <td>265</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d9s">3D9S</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SKKEVCSVAFLKAV</span><span class="topo-membrane">FAEFLATLIFVFFGLGS</span><span class="topo-outside">ALKWPSALPTIL</span><span class="topo-membrane">QIALAFGLAIGTLAQALG</span><span class="topo-inside">PVSGG</span><span class="topo-unknown">HINPAITLAL</span><span class="topo-inside">LVGNQISLLRA</span><span class="topo-membrane">FFYVAAQLVGAIAGAGIL</span><span class="topo-outside">YGVAPLNARGNLAV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NALNNNTTQG</span><span class="topo-membrane">QAMVVELILTFQLALCIF</span><span class="topo-inside">ASTDSRRTSPVG</span><span class="topo-membrane">SPALSIGLSVTLGHLVGI</span><span class="topo-outside">YFTGC</span><span class="topo-unknown">SMNPARSFGPAVV</span><span class="topo-outside">MNRFSPAH</span><span class="topo-membrane">WVFWVGPIVGAVLAAIL</span><span class="topo-inside">YFYLLFPNSLSLSERVAII</span></span>
<span class="topo-ruler">       250       260      </span>
<span class="topo-line"><span class="topo-inside">KGTYEP</span><span class="topo-unknown">DEDWEEQREERKKTMELTTR</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
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
      <td>15</td>
      <td>1</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>44</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>62</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>77</td>
      <td>67</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>88</td>
      <td>77</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>106</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>130</td>
      <td>106</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>130</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>160</td>
      <td>148</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>160</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>183</td>
      <td>178</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>196</td>
      <td>183</td>
      <td>195</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>197</td>
      <td>204</td>
      <td>196</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>246</td>
      <td>221</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>266</td>
      <td>246</td>
      <td>265</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d9s">3D9S</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSK</span><span class="topo-inside">KEVCSVAFLKAV</span><span class="topo-membrane">FAEFLATLIFVFFGLGS</span><span class="topo-outside">ALKWPSALPTIL</span><span class="topo-membrane">QIALAFGLAIGTLAQALG</span><span class="topo-inside">PVSGG</span><span class="topo-unknown">HINPAITLAL</span><span class="topo-inside">LVGNQISLLRA</span><span class="topo-membrane">FFYVAAQLVGAIAGAGILYGV</span><span class="topo-outside">APLNARGNLAV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NALNNNTTQG</span><span class="topo-membrane">QAMVVELILTFQLALCIFAS</span><span class="topo-inside">TDSRRTSPVG</span><span class="topo-membrane">SPALSIGLSVTLGHLVGI</span><span class="topo-outside">YFTGC</span><span class="topo-unknown">SMNPARSFGPAVV</span><span class="topo-outside">MNRFSPAH</span><span class="topo-membrane">WVFWVGPIVGAVLAAIL</span><span class="topo-inside">YFYLLFPNSLSLSERVAII</span></span>
<span class="topo-ruler">       250       260      </span>
<span class="topo-line"><span class="topo-inside">KGTYEP</span><span class="topo-unknown">DEDWEEQREERKKTMELTTR</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
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
      <td>0</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>15</td>
      <td>3</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>44</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>67</td>
      <td>62</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>77</td>
      <td>67</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>88</td>
      <td>77</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>109</td>
      <td>88</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>109</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>150</td>
      <td>130</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>160</td>
      <td>150</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>160</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>183</td>
      <td>178</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>196</td>
      <td>183</td>
      <td>195</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>197</td>
      <td>204</td>
      <td>196</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>246</td>
      <td>221</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>266</td>
      <td>246</td>
      <td>265</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3d9s">3D9S</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SKKEVCSVAFLK</span><span class="topo-membrane">AVFAEFLATLIFVFFGLGS</span><span class="topo-outside">ALKWPSALPTIL</span><span class="topo-membrane">QIALAFGLAIGTLAQALG</span><span class="topo-inside">PVS</span><span class="topo-unknown">GGHINPAITLALLV</span><span class="topo-inside">GNQISLL</span><span class="topo-membrane">RAFFYVAAQLVGAIAGAGIL</span><span class="topo-outside">YGVAPLNARGNLAV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NALNNNTTQGQA</span><span class="topo-membrane">MVVELILTFQLALCIFAS</span><span class="topo-inside">TDSRRTSPVG</span><span class="topo-membrane">SPALSIGLSVTLGHLVG</span><span class="topo-outside">IYFTGC</span><span class="topo-unknown">SMNPARSFGP</span><span class="topo-outside">AVVMNRFSPAHW</span><span class="topo-membrane">VFWVGPIVGAVLAAILY</span><span class="topo-inside">FYLLFPNSLSLSERVAII</span></span>
<span class="topo-ruler">       250       260      </span>
<span class="topo-line"><span class="topo-inside">KGTYEP</span><span class="topo-unknown">DEDWEEQREERKKTMELTTR</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
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
      <td>13</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>32</td>
      <td>13</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>32</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>62</td>
      <td>44</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>65</td>
      <td>62</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>79</td>
      <td>65</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>79</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>106</td>
      <td>86</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>132</td>
      <td>106</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>150</td>
      <td>132</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>160</td>
      <td>150</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>183</td>
      <td>177</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>193</td>
      <td>183</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>194</td>
      <td>205</td>
      <td>193</td>
      <td>204</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>222</td>
      <td>205</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>246</td>
      <td>222</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>266</td>
      <td>246</td>
      <td>265</td>
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

### Tetrameric water channel architecture conserved in human AQP5

HsAQP5 forms a tetramer with each protomer containing an independent water channel. The structure displays the canonical aquaporin fold of six transmembrane helices and two half-helices (the NPA motif regions) forming the water-selective pore. The tetrameric assembly is typical of the aquaporin family. HOLE calculations of pore radii for the four protomers show similar profiles compared with BtAQP1.

### Short C-terminal helix exhibits conformational flexibility

A notable feature of HsAQP5 is a short C-terminal helix that shows conformational differences between protomers in the tetramer. This flexibility may be functionally relevant for channel regulation, as the C-terminal region contains potential phosphorylation sites (cAMP/cGMP-dependent protein kinase A sites, protein kinase C sites, and casein kinase II sites) identified by PROSCAN/PROSITE searches. The C-terminal helix of AQP5 differs in length and angle compared to BtAQP1 and OaAQP0.

### Potential phosphorylation sites in regulatory loops

Sequence analysis of HsAQP5 reveals potential phosphorylation sites in loop B, loop D, and the C-terminal region. These include cAMP- and cGMP-dependent protein kinase A sites (RKX[ST] motif), protein kinase C sites ([ST]X[RK] motif), and casein kinase II sites ([ST]XX[DE] motif). Phosphorylation of corresponding sites in the plant aquaporin SoPIP2;1 and mouse AQP4 has been shown to regulate channel gating, suggesting that similar regulatory mechanisms may operate in HsAQP5.

### Pseudomerohedral twinning in AQP5 crystals

The HsAQP5 structure was refined from crystals exhibiting near-perfect pseudomerohedral twinning (twin fraction 46.3%) with the twin operator swapping the a and b axes. Specialized refinement using SHELXL was employed, with test reflections selected in thin resolution shells to avoid biasing Rfree. A full omit map procedure (Artymiuk et al.) was developed to produce less biased electron density maps, involving dividing the asymmetric unit into boxes, omitting each in turn for detwinning and map calculation, then merging.

### Functional water transport and mercury inhibition

HsAQP5 reconstituted into proteoliposomes demonstrates water transport activity by stopped-flow light scattering. Rate constants of 21.32 s-1 (LPR 65) and 14.10 s-1 (LPR 130) were measured, compared to 9.14 s-1 for control liposomes. Water transport was inhibited by HgCl2 with an IC50 of 30 uM, and inhibition was reversed by 0.5 mM beta-mercaptoethanol.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — AQP5 is a member of the water-specific aquaporin subfamily; the structure reveals conserved aquaporin features including NPA motifs and tetrameric assembly
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp0/">Aquaporin 0 (AQP0)</a> — Related aquaporin for structural comparison of tetramer architecture and water selectivity
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">Aquaporin-1 (AQP1)</a> — Archetypal water-specific aquaporin with similar pore architecture used for HOLE pore radius comparison
- <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">n-Nonyl-beta-D-glucopyranoside (NG)</a> — Primary detergent used for solubilization and purification of HsAQP5
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — HEPES-NaOH pH 7.8 used in membrane preparation buffer A and solubilization buffer
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — MES pH 6.0 used as cation exchange column equilibration and binding buffer
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion Exchange Chromatography</a> — Resource S cation exchange used as the main purification step for AQP5
- <a href="/xray-mp-wiki/concepts/pseudomerohedral-twinning/">Pseudomerohedral Twinning</a> — HsAQP5 structure refined from crystals with near-perfect pseudomerohedral twinning (46.3%) using SHELXL
