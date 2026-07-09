---
title: "Salmonella enterica Citrate/Sodium Symporter (SeCitS)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.09375]
verified: regex
uniprot_id: G4BX92
---

# Salmonella enterica Citrate/Sodium Symporter (SeCitS)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G4BX92">UniProt: G4BX92</a>

<span class="expr-badge">Salmonella ENTERICA</span>

## Overview

SeCitS is a [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)/sodium symporter from the human pathogen *Salmonella enterica*. It belongs to the 2-hydroxycarboxylate transporter (2-HCT) family and mediates sodium-dependent uptake of [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (HCit2-) as a carbon source. The 2.5 A X-ray structure revealed an asymmetric dimer with three distinct conformational states -- one outward-facing and two inward-facing -- which together elucidated a six-step transport mechanism involving a 31-degree rigid-body rotation of a helix bundle that translocates substrates by 16 A across the membrane.


## Publications

### doi/10.7554##eLife.09375

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a></td>
      <td>2.5</td>
      <td>P1</td>
      <td>Full-length SeCitS with N-terminal His10-tag (cleaved by thrombin)</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a></td>
      <td>3.9</td>
      <td>P21</td>
      <td>Selenomethionine-substituted SeCitS</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41-(DE3)
- **Construct**: N-terminal His10-tag, thrombin cleavage site
- **Induction**: Autoinduction (native); [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.5 (SeMet)
- **Media**: ZYM-5052 autoinduction medium (native); defined medium with methionine biosynthesis inhibition (SeMet)

**Purification:**

- **Expression system**: E. coli C41-(DE3)
- **Expression construct**: Full-length SeCitS, N-His10-thrombin
- **Tag info**: His10-tag removed by on-column thrombin cleavage

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
      <td>Microfluidizer (M-110L)</td>
      <td>—</td>
      <td>20 mM Tris/HCl pH7.4, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 5 mM beta-ME</td>
      <td>Cells resuspended after harvest</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>20 mM Tris/HCl, 140 mM <a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> chloride, 250 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 1 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 5 mM beta-ME</td>
      <td>100,000 g for 1 h; resuspended at 15 mg/ml total protein</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM Tris/HCl pH7.4, 150 mM NaCl, 1 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 5 mM beta-ME + 1.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td>1:1 dilution of membranes with 3% DM buffer; 100,000 g clarification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>Ni-NTA agarose</td>
      <td>20 mM Tris/HCl pH7.4, 300 mM NaCl, 45 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 0.15% DM, 5 mM beta-ME</td>
      <td>On-column thrombin cleavage overnight at 4 C (1 U/mg)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris/HCl pH8.2, 150 mM NaCl, 1 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 0.15% DM, 1 mM TCEP</td>
      <td>Concentrated to 5 mg/ml (50 kDa cutoff) before SEC</td>
    </tr>
  </tbody>
</table>
**Final sample**: 5 mg/ml in 20 mM Tris/HCl pH8.2, 150 mM NaCl, 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 0.15% DM, 1 mM TCEP

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Native SeCitS supplemented with 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (OG)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES pH6.5, 200 mM NaCl, 29% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C (room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-7 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Al's oil</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Rhombic crystals, ~150 um</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SeMet SeCitS supplemented with 2% <a href="/xray-mp-wiki/reagents/detergents/n-heptyl-beta-d-glucopyranoside/">HG</a> (HG)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES pH6.5, 250 mM NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Up to 7 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Thin needle-like crystals, ~400 um; vitrified directly in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTNMTQASATERKGA</span><span class="topo-inside">SDLLRFKIFGMPL</span><span class="topo-membrane">PLYAFALITLLLSH</span><span class="topo-outside">FYNAIPTD</span><span class="topo-membrane">LVGGFALMFVMGAIFGEIGKRL</span><span class="topo-inside">P</span><span class="topo-membrane">IFNKYIGGAPVMIFLVAAYF</span><span class="topo-outside">VYAGIFT</span><span class="topo-unknown">QKEIDAISNVM</span><span class="topo-outside">DKS</span><span class="topo-membrane">NFLNLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IAVLITGAIL</span><span class="topo-inside">SVNRKLL</span><span class="topo-membrane">LKSLLGYIPTILAGIVGASLF</span><span class="topo-outside">GIVIGLCFGIP</span><span class="topo-unknown">VDRIMML</span><span class="topo-outside">YVLPIMGGGNGAGAVPLSEIYHSVTGRSREEYYSTAIAILTIA</span><span class="topo-membrane">NIFAIIFAALLDMV</span><span class="topo-inside">GKKYTWL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGEGELVRKASFKTEDDEKAGQITHRETA</span><span class="topo-membrane">VGMVLSTTCFLLAYVVA</span><span class="topo-outside">KKILPSIGGVSI</span><span class="topo-membrane">HYFAWMVLIVAALNAS</span><span class="topo-inside">GLCSPEIKAGAKRL</span><span class="topo-membrane">SDFFSKQLLWVLMVGVGV</span><span class="topo-outside">CYTDLQEIIDALTF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-outside">ANVVIAA</span><span class="topo-membrane">IIVVGAVVGAAIGGWLIGFY</span><span class="topo-inside">P</span><span class="topo-membrane">IESSITAGLCMANR</span><span class="topo-outside">G</span><span class="topo-membrane">GSGDLEVLSACNRM</span><span class="topo-inside">N</span><span class="topo-membrane">LISYAQISSRLGGGI</span><span class="topo-outside">VLVIASIVFSMMVLE</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>50</td>
      <td>43</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>93</td>
      <td>74</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>100</td>
      <td>94</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>111</td>
      <td>101</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>114</td>
      <td>112</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>115</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>137</td>
      <td>131</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>169</td>
      <td>159</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>176</td>
      <td>170</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>177</td>
      <td>219</td>
      <td>177</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>220</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>269</td>
      <td>234</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>286</td>
      <td>270</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>298</td>
      <td>287</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>314</td>
      <td>299</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>328</td>
      <td>315</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>346</td>
      <td>329</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>367</td>
      <td>347</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>387</td>
      <td>368</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>388</td>
      <td>388</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>402</td>
      <td>389</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>403</td>
      <td>403</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>417</td>
      <td>404</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>418</td>
      <td>418</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>433</td>
      <td>419</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>448</td>
      <td>434</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTNMTQASATERKGA</span><span class="topo-inside">SDLLRFKIFGMPL</span><span class="topo-membrane">PLYAFALITLLLSHF</span><span class="topo-outside">YNAIPTD</span><span class="topo-membrane">LVGGFALMFVMGAIFGEIGK</span><span class="topo-inside">RL</span><span class="topo-unknown">PIFNKY</span><span class="topo-membrane">IGGAPVMIFLVAAYFV</span><span class="topo-outside">YAGIFT</span><span class="topo-unknown">QKEIDAISNVM</span><span class="topo-outside">DKS</span><span class="topo-membrane">NFLNLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IAVLITGAI</span><span class="topo-inside">LSVN</span><span class="topo-unknown">RKLLLKS</span><span class="topo-inside">LLGYIPTI</span><span class="topo-membrane">LAGIVGASLFGIVIGLCFGIP</span><span class="topo-outside">V</span><span class="topo-membrane">DRIMMLYVLPIMGG</span><span class="topo-inside">G</span><span class="topo-membrane">NGAGAVPLSEIY</span><span class="topo-outside">HSVTGRSREEY</span><span class="topo-membrane">YSTAIAILTIANIF</span><span class="topo-inside">AIIFAALLDMVGKKYTWL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGEGELVRK</span><span class="topo-unknown">ASFKTED</span><span class="topo-inside">DEKAGQITHRETA</span><span class="topo-membrane">VGMVLSTTCFLLAYVVA</span><span class="topo-outside">KKILPSIGGV</span><span class="topo-membrane">SIHYFAWMVLIVAAL</span><span class="topo-inside">NASGLCS</span><span class="topo-unknown">PEIKAGAKRLSDF</span><span class="topo-membrane">FSKQLLWVLMVGVGVCYT</span><span class="topo-outside">D</span><span class="topo-membrane">LQEIIDALTF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-membrane">ANVVIAAIIVVGA</span><span class="topo-inside">VVGAAIGGWLIGFYPIESSITAGLCMANRGGSGDLEVLSACNRMNLISYAQISS</span><span class="topo-membrane">RLGGGIVLVIASIVFSM</span><span class="topo-outside">MVLE</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>29</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>50</td>
      <td>44</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>70</td>
      <td>51</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>72</td>
      <td>71</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>78</td>
      <td>73</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>79</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>100</td>
      <td>95</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>111</td>
      <td>101</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>114</td>
      <td>112</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>115</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>133</td>
      <td>130</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>141</td>
      <td>148</td>
      <td>141</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>184</td>
      <td>171</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>185</td>
      <td>185</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>197</td>
      <td>186</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>208</td>
      <td>198</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>222</td>
      <td>209</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>249</td>
      <td>223</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>269</td>
      <td>257</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>286</td>
      <td>270</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>296</td>
      <td>287</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>311</td>
      <td>297</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>318</td>
      <td>312</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>331</td>
      <td>319</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>349</td>
      <td>332</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>350</td>
      <td>350</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>373</td>
      <td>351</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>427</td>
      <td>374</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>428</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTNMTQASATERKGA</span><span class="topo-inside">SDLLRFKIFGMPL</span><span class="topo-membrane">PLYAFALITLLLSH</span><span class="topo-outside">FYNAIPTD</span><span class="topo-membrane">LVGGFALMFVMGAIFGEIGKRL</span><span class="topo-inside">P</span><span class="topo-membrane">IFNKYIGGAPVMIFLVAAYF</span><span class="topo-outside">VYAGIFT</span><span class="topo-unknown">QKEIDAISNVM</span><span class="topo-outside">DKS</span><span class="topo-membrane">NFLNLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IAVLITGAIL</span><span class="topo-inside">SVNRKLL</span><span class="topo-membrane">LKSLLGYIPTILAGIVGASLF</span><span class="topo-outside">GIVIGLCFGIP</span><span class="topo-unknown">VDRIMML</span><span class="topo-outside">YVLPIMGGGNGAGAVPLSEIYHSVTGRSREEYYSTAIAILTIA</span><span class="topo-membrane">NIFAIIFAALLDMV</span><span class="topo-inside">GKKYTWL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGEGELVRKASFKTEDDEKAGQITHRETA</span><span class="topo-membrane">VGMVLSTTCFLLAYVVA</span><span class="topo-outside">KKILPSIGGVSI</span><span class="topo-membrane">HYFAWMVLIVAALNAS</span><span class="topo-inside">GLCSPEIKAGAKRL</span><span class="topo-membrane">SDFFSKQLLWVLMVGVGV</span><span class="topo-outside">CYTDLQEIIDALTF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-outside">ANVVIAA</span><span class="topo-membrane">IIVVGAVVGAAIGGWLIGFY</span><span class="topo-inside">P</span><span class="topo-membrane">IESSITAGLCMANR</span><span class="topo-outside">G</span><span class="topo-membrane">GSGDLEVLSACNRM</span><span class="topo-inside">N</span><span class="topo-membrane">LISYAQISSRLGGGI</span><span class="topo-outside">VLVIASIVFSMMVLE</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>50</td>
      <td>43</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>93</td>
      <td>74</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>100</td>
      <td>94</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>111</td>
      <td>101</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>114</td>
      <td>112</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>130</td>
      <td>115</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>137</td>
      <td>131</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>169</td>
      <td>159</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>176</td>
      <td>170</td>
      <td>176</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>177</td>
      <td>219</td>
      <td>177</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>220</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>269</td>
      <td>234</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>286</td>
      <td>270</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>298</td>
      <td>287</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>314</td>
      <td>299</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>328</td>
      <td>315</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>346</td>
      <td>329</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>367</td>
      <td>347</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>387</td>
      <td>368</td>
      <td>387</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>388</td>
      <td>388</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>402</td>
      <td>389</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>403</td>
      <td>403</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>417</td>
      <td>404</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>418</td>
      <td>418</td>
      <td>418</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>433</td>
      <td>419</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>448</td>
      <td>434</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5a1s">5A1S</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTNMTQASATERKGA</span><span class="topo-inside">SDLLRFKIFGMPL</span><span class="topo-membrane">PLYAFALITLLLSHF</span><span class="topo-outside">YNAIPTD</span><span class="topo-membrane">LVGGFALMFVMGAIFGEIGK</span><span class="topo-inside">RL</span><span class="topo-unknown">PIFNKY</span><span class="topo-membrane">IGGAPVMIFLVAAYFV</span><span class="topo-outside">YAGIFT</span><span class="topo-unknown">QKEIDAISNVM</span><span class="topo-outside">DKS</span><span class="topo-membrane">NFLNLF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IAVLITGAI</span><span class="topo-inside">LSVN</span><span class="topo-unknown">RKLLLKS</span><span class="topo-inside">LLGYIPTI</span><span class="topo-membrane">LAGIVGASLFGIVIGLCFGIP</span><span class="topo-outside">V</span><span class="topo-membrane">DRIMMLYVLPIMGG</span><span class="topo-inside">G</span><span class="topo-membrane">NGAGAVPLSEIY</span><span class="topo-outside">HSVTGRSREEY</span><span class="topo-membrane">YSTAIAILTIANIF</span><span class="topo-inside">AIIFAALLDMVGKKYTWL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SGEGELVRK</span><span class="topo-unknown">ASFKTED</span><span class="topo-inside">DEKAGQITHRETA</span><span class="topo-membrane">VGMVLSTTCFLLAYVVA</span><span class="topo-outside">KKILPSIGGV</span><span class="topo-membrane">SIHYFAWMVLIVAAL</span><span class="topo-inside">NASGLCS</span><span class="topo-unknown">PEIKAGAKRLSDF</span><span class="topo-membrane">FSKQLLWVLMVGVGVCYT</span><span class="topo-outside">D</span><span class="topo-membrane">LQEIIDALTF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-membrane">ANVVIAAIIVVGA</span><span class="topo-inside">VVGAAIGGWLIGFYPIESSITAGLCMANRGGSGDLEVLSACNRMNLISYAQISS</span><span class="topo-membrane">RLGGGIVLVIASIVFSM</span><span class="topo-outside">MVLE</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>16</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>29</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>50</td>
      <td>44</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>70</td>
      <td>51</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>72</td>
      <td>71</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>78</td>
      <td>73</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>79</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>100</td>
      <td>95</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>111</td>
      <td>101</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>114</td>
      <td>112</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>115</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>133</td>
      <td>130</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>134</td>
      <td>140</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>141</td>
      <td>148</td>
      <td>141</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>184</td>
      <td>171</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>185</td>
      <td>185</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>197</td>
      <td>186</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>208</td>
      <td>198</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>222</td>
      <td>209</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>249</td>
      <td>223</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>269</td>
      <td>257</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>286</td>
      <td>270</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>287</td>
      <td>296</td>
      <td>287</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>311</td>
      <td>297</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>318</td>
      <td>312</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>331</td>
      <td>319</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>332</td>
      <td>349</td>
      <td>332</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>350</td>
      <td>350</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>373</td>
      <td>351</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>427</td>
      <td>374</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>428</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>448</td>
      <td>445</td>
      <td>448</td>
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

### Asymmetric dimer with three conformational states

The SeCitS crystal structure captured an asymmetric dimer where one protomer is in the outward-facing state and two are in different inward-facing states (B and B'). This is unique for a membrane transporter crystal structure. The dimer asymmetry cannot be attributed to crystal packing as both dimers in the asymmetric unit are almost identical (rmsd 0.5 A).

### Six-step transport mechanism

A six-step transport cycle was deduced: (1) Two Na+ ions bind to the outward-facing empty transporter; (2) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (HCit2-) binds from the external medium; (3) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) binding triggers a 31-degree arc-like rigid-body rotation of the helix bundle, translocating bound substrates by 16 A; (4) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is released to the cytoplasm; (5) Na+ ions are released (Na2 before Na1); (6) The empty protomer reverts to the outward-facing state. The process is electroneutral and driven by the inward-directed Na+ gradient.

### Substrate binding and release order

[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is released before Na+ ions in the inward-facing state. Comparison of protomers B and B' shows unambiguous evidence: B' has an empty Na2 site while [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is already partially released. The Na2 site empties before Na1. Both Na+ ions must bind before [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) can bind to the outward-facing state.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES (2-(N-Morpholino)ethanesulfonic Acid)</a> — MES was used as crystallization buffer for SeCitS
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-beta-D-Maltoside (DM)</a> — DM was used for solubilization and purification of SeCitS
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
