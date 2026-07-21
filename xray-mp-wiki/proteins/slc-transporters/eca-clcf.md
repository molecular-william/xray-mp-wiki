---
title: "Eca CLCF (CLC-type F-/H+ Antiporter from Enterococcus casseliflavus)"
created: 2026-06-22
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0082-0]
verified: agent
uniprot_id: C9CPP6
---

# Eca CLCF (CLC-type F-/H+ Antiporter from Enterococcus casseliflavus)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/C9CPP6">UniProt: C9CPP6</a>

<span class="expr-badge">Enterococcus casseliflavus (strain EC10)</span>

## Overview

Eca CLCF is a fluoride/proton (F-/H+) antiporter from the bacterium
Enterococcus casseliflavus, belonging to the CLCF clade of the CLC
superfamily of anion transport proteins. It exports F- from the
cytoplasm to combat fluoride toxicity. Unlike conventional Cl-/H+
CLC antiporters, Eca displays 1:1 F-/H+ stoichiometry (versus 2:1
for Cl- CLCs) and lacks the conserved Cl--coordinating serine
residue. Crystal structures were captured in two novel conformations
with simultaneous accessibility of F- and H+ via separate pathways
on opposite sides of the membrane, leading to a proposed 'windmill'
model of antiport.


## Publications

### doi/10.1038##s41594-018-0082-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d0j">6D0J</a></td>
      <td>3.0</td>
      <td>P2(1)2(1)2(1)</td>
      <td>WT Eca with M4I mutation, C-terminal His6; monobody chaperone X1</td>
      <td>F-</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d0k">6D0K</a></td>
      <td>3.35</td>
      <td>P2(1)2(1)2(1)</td>
      <td>E118Q mutant, C-terminal His6; monobody chaperone X1</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d0n">6D0N</a></td>
      <td>3.12</td>
      <td>P2(1)2(1)2(1)</td>
      <td>V319G mutant, C-terminal His6; monobody chaperone X1</td>
      <td>F-</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: BL21(DE3) E. coli
- **Construct**: Eca (GenBank EEV30821.1) with M4I mutation, C-terminal GSGG-HHHHHH in pASK90
- **Induction**: 0.2 µg/mL anhydrotetracycline for 3 h at 37°C
- **Media**: Terrific broth

**Purification:**

- **Expression system**: BL21(DE3) E. coli
- **Expression construct**: Eca with M4I mutation, C-terminal GSGG-HHHHHH tail
- **Tag info**: C-terminal hexahistidine, uncleaved

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
      <td>Cell harvest and lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>100 mM NaCl, 50 mM Tris pH 7.5, DNase, lysozyme</td>
      <td></td>
    </tr>
    <tr>
      <td>Detergent extraction</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>100 mM NaCl, 50 mM Tris pH 7.5 + 4% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (n-decylmaltoside)</td>
      <td>2 h at room temperature</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt resin (Takara Bio)</td>
      <td>100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 20 mM Tris pH 7.5</td>
      <td>Wash with 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase (GE Healthcare)</td>
      <td>10 mM HEPES, 100 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, pH 7 (functional assays) + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified in DM-containing buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Eca in 10 mM HEPES, 100 mM NaF, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, pH 7, with monobody X1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in 2-4 days; data collected at APS (Advanced Photon Source)</td>
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
      <td>7.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 3350: 18-22 % [precipitant] (PEG 3350)  
- Hepes: 100 mM [buffer]</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Eca E118Q mutant in 10 mM HEPES, 100 mM NaF, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, pH 7, with monobody X1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
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
      <td>7.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 3350: 18-22 % [precipitant] (PEG 3350)  
- Hepes: 100 mM [buffer]</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Eca V319G mutant in crystallization buffer with monobody X1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22</td>
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
      <td>7.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 3350: 18-22 % [precipitant] (PEG 3350)  
- Hepes: 100 mM [buffer]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0j">6D0J</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETTY</span><span class="topo-membrane">FELTALGLLSLVIGVLAGAVDTFFGKILLFLSAFRE</span><span class="topo-inside">SH</span><span class="topo-membrane">FLPLILFLPIIGICFTYLFQ</span><span class="topo-outside">KYGDRSPQG</span><span class="topo-unknown">MNLVFLVG</span><span class="topo-outside">QEEEKDI</span><span class="topo-membrane">PLRLIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EGVAVQLGATIANRLG</span><span class="topo-outside">NWVRLEKYAS</span><span class="topo-membrane">TLIMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEVLVIG</span><span class="topo-outside">K</span><span class="topo-membrane">FSHHALLPALLAAFTASTTSQWL</span><span class="topo-inside">GLEKFSLMLPQSVDLTI</span><span class="topo-membrane">PVFLKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCLETMK</span><span class="topo-outside">RIMKRRFPNP</span><span class="topo-membrane">LWRIGIGALALVLLFVLLYQG</span><span class="topo-inside">RYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEVTPLFAIGSSLG</span><span class="topo-unknown">VVLAPLF</span><span class="topo-inside">GLPIELV</span><span class="topo-membrane">AALGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-membrane">S</span><span class="topo-outside">T</span><span class="topo-membrane">LFAPIFIGGEV</span><span class="topo-inside">FGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISKPY</span><span class="topo-outside">SIYPLQKTS</span><span class="topo-unknown">AMGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>11</td>
      <td>14</td>
      <td>8</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>50</td>
      <td>12</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>48</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>72</td>
      <td>50</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>81</td>
      <td>70</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>79</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>87</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>146</td>
      <td>134</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>162</td>
      <td>144</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>178</td>
      <td>161</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>179</td>
      <td>176</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>202</td>
      <td>177</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>200</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>217</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>257</td>
      <td>245</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>276</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>340</td>
      <td>331</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>338</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>361</td>
      <td>345</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>362</td>
      <td>359</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>360</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>379</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>405</td>
      <td>394</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0j">6D0J</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETTY</span><span class="topo-membrane">FELTALGLLSLVIGVLAGAVDTFFGKILLFLSAFRE</span><span class="topo-inside">SH</span><span class="topo-membrane">FLPLILFLPIIGICFTYLFQ</span><span class="topo-outside">KYGDRSPQG</span><span class="topo-unknown">MNLVFLVG</span><span class="topo-outside">QEEEKDI</span><span class="topo-membrane">PLRLIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EGVAVQLGATIANRLG</span><span class="topo-outside">NWVRLEKYAS</span><span class="topo-membrane">TLIMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEVLVIG</span><span class="topo-outside">K</span><span class="topo-membrane">FSHHALLPALLAAFTASTTSQWL</span><span class="topo-inside">GLEKFSLMLPQSVDLTI</span><span class="topo-membrane">PVFLKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCLETMK</span><span class="topo-outside">RIMKRRFPNP</span><span class="topo-membrane">LWRIGIGALALVLLFVLLYQG</span><span class="topo-inside">RYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEVTPLFAIGSSLG</span><span class="topo-unknown">VVLAPLF</span><span class="topo-inside">GLPIELV</span><span class="topo-membrane">AALGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-membrane">S</span><span class="topo-outside">T</span><span class="topo-membrane">LFAPIFIGGEV</span><span class="topo-inside">FGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISKPY</span><span class="topo-outside">SIYPLQKTSA</span><span class="topo-unknown">MGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>11</td>
      <td>14</td>
      <td>8</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>50</td>
      <td>12</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>48</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>72</td>
      <td>50</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>81</td>
      <td>70</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>79</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>87</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>146</td>
      <td>134</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>162</td>
      <td>144</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>178</td>
      <td>161</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>179</td>
      <td>176</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>202</td>
      <td>177</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>200</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>217</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>257</td>
      <td>245</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>276</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>340</td>
      <td>331</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>338</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>361</td>
      <td>345</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>362</td>
      <td>359</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>360</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>379</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>406</td>
      <td>394</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0j">6D0J</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSVS</span><span class="topo-inside">SVPTKLEV</span><span class="topo-unknown">V</span><span class="topo-inside">AATPTSLLISWDASSS</span><span class="topo-unknown">SV</span><span class="topo-inside">SYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYQT</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29</td>
      <td>14</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>93</td>
      <td>32</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0j">6D0J</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSV</span><span class="topo-inside">SSVPTKLEVVAATPTSLLISWDASSSSVSYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYQT</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>93</td>
      <td>4</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0k">6D0K</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETT</span><span class="topo-membrane">YFELTALGLLSLVIGVLAGAVDTFFGKILLFLSAFRE</span><span class="topo-inside">SH</span><span class="topo-membrane">FLPLILFLPIIGICFTYLFQKYG</span><span class="topo-outside">DRSPQG</span><span class="topo-unknown">MNLVFLVG</span><span class="topo-outside">QEEEKDI</span><span class="topo-membrane">PLRLIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QGVAVQLGATIANRLGNWV</span><span class="topo-outside">RLEKY</span><span class="topo-membrane">ASTLIMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEVLVIG</span><span class="topo-outside">K</span><span class="topo-membrane">FSHHALLPALLAAFTASTTSQWL</span><span class="topo-inside">GLEKFSLMLPQSVDLTI</span><span class="topo-membrane">PVFLKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCLETMKRIMK</span><span class="topo-outside">RRFPNP</span><span class="topo-membrane">LWRIGIGALALVLLFVLLYQG</span><span class="topo-inside">RYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEVTPLFAIGSSLG</span><span class="topo-unknown">VVLAPLF</span><span class="topo-inside">GLPIELV</span><span class="topo-membrane">AALGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-membrane">S</span><span class="topo-outside">T</span><span class="topo-membrane">LFAPIFIGGEV</span><span class="topo-inside">FGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISKPY</span><span class="topo-outside">SIYPLQKTS</span><span class="topo-unknown">AMGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>11</td>
      <td>13</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>50</td>
      <td>11</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>48</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>75</td>
      <td>50</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>73</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>79</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>87</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>139</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>162</td>
      <td>142</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>178</td>
      <td>161</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>179</td>
      <td>176</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>202</td>
      <td>177</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>200</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>251</td>
      <td>217</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>257</td>
      <td>249</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>276</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>340</td>
      <td>331</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>338</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>361</td>
      <td>345</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>362</td>
      <td>359</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>360</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>379</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>405</td>
      <td>394</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0k">6D0K</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETT</span><span class="topo-membrane">YFELTALGLLSLVIGVLAGAVDTFFGKILLFLSAFRE</span><span class="topo-inside">SH</span><span class="topo-membrane">FLPLILFLPIIGICFTYLFQKYG</span><span class="topo-outside">DRSPQG</span><span class="topo-unknown">MNLVFLVG</span><span class="topo-outside">QEEEKDI</span><span class="topo-membrane">PLRLIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QGVAVQLGATIANRLGNWV</span><span class="topo-outside">RLEKY</span><span class="topo-membrane">ASTLIMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEVLVIG</span><span class="topo-outside">K</span><span class="topo-membrane">FSHHALLPALLAAFTASTTSQWL</span><span class="topo-inside">GLEKFSLMLPQSVDLTI</span><span class="topo-membrane">PVFLKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCLETMKRIMK</span><span class="topo-outside">RRFPNP</span><span class="topo-membrane">LWRIGIGALALVLLFVLLYQG</span><span class="topo-inside">RYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEVTPLFAIGSSLG</span><span class="topo-unknown">VVLAPLF</span><span class="topo-inside">GLPIELV</span><span class="topo-membrane">AALGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-membrane">S</span><span class="topo-outside">T</span><span class="topo-membrane">LFAPIFIGGEV</span><span class="topo-inside">FGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISKPY</span><span class="topo-outside">SIYPLQKTSA</span><span class="topo-unknown">MGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>11</td>
      <td>13</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>50</td>
      <td>11</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>48</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>75</td>
      <td>50</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>81</td>
      <td>73</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>79</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>87</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>139</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>137</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>162</td>
      <td>142</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>178</td>
      <td>161</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>179</td>
      <td>176</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>202</td>
      <td>177</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>200</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>251</td>
      <td>217</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>257</td>
      <td>249</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>278</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>276</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>340</td>
      <td>331</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>338</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>361</td>
      <td>345</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>362</td>
      <td>359</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>373</td>
      <td>360</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>379</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>406</td>
      <td>394</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0k">6D0K</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSVS</span><span class="topo-inside">SVPTKLEV</span><span class="topo-unknown">V</span><span class="topo-inside">AATPTSLLISWDASSS</span><span class="topo-unknown">SV</span><span class="topo-inside">SYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYQT</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>29</td>
      <td>14</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>93</td>
      <td>32</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0k">6D0K</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSV</span><span class="topo-inside">SSVPTKLEVVAATPTSLLISWDASSSSVSYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYQT</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>93</td>
      <td>4</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0n">6D0N</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETTYFEL</span><span class="topo-membrane">TALGLLSLVIGVLAGAVDTFFGKILLFLS</span><span class="topo-inside">AFRESHF</span><span class="topo-membrane">LPLILFLPIIGICFT</span><span class="topo-outside">YLFQKYGDRSPQGMNLVFLVGQEEEKDIPL</span><span class="topo-membrane">RLIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EGVAVQLGATIA</span><span class="topo-outside">NRLGNWVRLEKYASTL</span><span class="topo-membrane">IMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEV</span><span class="topo-outside">LVIGKF</span><span class="topo-membrane">SHHALLPALLAAFTASTTS</span><span class="topo-inside">QWLGLEKFSLMLPQSVDLTIPVF</span><span class="topo-membrane">LKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCL</span><span class="topo-outside">ETMKRIMKRRFPNPLWRI</span><span class="topo-membrane">GIGALALVLLFVLL</span><span class="topo-inside">YQGRYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEGTPLFAIGSSLG</span><span class="topo-inside">VVLAPLFGLPIELVAA</span><span class="topo-unknown">LGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-unknown">STLFAPIFIGGE</span><span class="topo-inside">VFGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISK</span><span class="topo-outside">PYSIYPLQKTS</span><span class="topo-unknown">AMGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>10</td>
      <td>-2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>17</td>
      <td>8</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>46</td>
      <td>15</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>44</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>68</td>
      <td>51</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>98</td>
      <td>66</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>114</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>113</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>148</td>
      <td>130</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>162</td>
      <td>146</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>174</td>
      <td>161</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>172</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>178</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>222</td>
      <td>197</td>
      <td>219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>220</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>241</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>275</td>
      <td>259</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>299</td>
      <td>273</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>349</td>
      <td>331</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>372</td>
      <td>347</td>
      <td>369</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>373</td>
      <td>379</td>
      <td>370</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>394</td>
      <td>377</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>405</td>
      <td>392</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>421</td>
      <td>403</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0n">6D0N</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAAAIEIKKQ</span><span class="topo-outside">ETTYFEL</span><span class="topo-membrane">TALGLLSLVIGVLAGAVDTFFGKILLFLS</span><span class="topo-inside">AFRESHF</span><span class="topo-membrane">LPLILFLPIIGICFT</span><span class="topo-outside">YLFQKYGDRSPQGMNLVFLVGQEEEKDIPLR</span><span class="topo-membrane">LIPFVMVGTWLTHLF</span><span class="topo-inside">G</span><span class="topo-membrane">GSAGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EGVAVQLGATIA</span><span class="topo-outside">NRLGNWVRLEKYASTL</span><span class="topo-membrane">IMIGMAAGFAGLFE</span><span class="topo-inside">T</span><span class="topo-membrane">PIAATFFALEV</span><span class="topo-outside">LVIGKF</span><span class="topo-membrane">SHHALLPALLAAFTASTTS</span><span class="topo-inside">QWLGLEKFSLMLPQSVDLTIPVF</span><span class="topo-membrane">LKLLVIGLIFGMVGGSFA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GCL</span><span class="topo-outside">ETMKRIMKRRFPNPLWRI</span><span class="topo-membrane">GIGALALVLLFVLL</span><span class="topo-inside">YQGRYSGLGTNLISASFTNQPIYS</span><span class="topo-membrane">YDWLLKLVLTVLTISS</span><span class="topo-outside">G</span><span class="topo-membrane">FLGGEGTPLFAIGSSLG</span><span class="topo-inside">VVLAPLFGLPIELVAA</span><span class="topo-unknown">LGYASVFGSAT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-unknown">STLFAPIFIGGE</span><span class="topo-inside">VFGFQNL</span><span class="topo-membrane">PFFVIVCSVAYFISK</span><span class="topo-outside">PYSIYPLQKTSA</span><span class="topo-unknown">MGQTRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>10</td>
      <td>-2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>11</td>
      <td>17</td>
      <td>8</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>46</td>
      <td>15</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>44</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>68</td>
      <td>51</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>99</td>
      <td>66</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>114</td>
      <td>97</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>113</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>148</td>
      <td>130</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>162</td>
      <td>146</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>163</td>
      <td>160</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>174</td>
      <td>161</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>180</td>
      <td>172</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>178</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>222</td>
      <td>197</td>
      <td>219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>220</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>261</td>
      <td>241</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>275</td>
      <td>259</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>299</td>
      <td>273</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>297</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>313</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>333</td>
      <td>314</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>349</td>
      <td>331</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>372</td>
      <td>347</td>
      <td>369</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>373</td>
      <td>379</td>
      <td>370</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>394</td>
      <td>377</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>406</td>
      <td>392</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>421</td>
      <td>404</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0n">6D0N</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSVS</span><span class="topo-inside">SVPTKLEV</span><span class="topo-unknown">V</span><span class="topo-inside">AATPTSLLISWDASSSSVSYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYRT</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>93</td>
      <td>14</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d0n">6D0N</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-unknown">GSV</span><span class="topo-inside">SSVPTKLEVVAATPTSLLISWDASSSSVSYYRITYGETGGNSPVQEFTVPGSSSTATISGLSPGVDYTITVYAHGWLQWYMSPISINYRT</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>93</td>
      <td>4</td>
      <td>93</td>
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

### Glu_g (E118) Gating Glutamate and Anion Selectivity

The critical gating glutamate E118 (Glu_g) controls both H+ and F-
transport. Mutation to glutamine (E118Q) or alanine (E118A)
completely inhibits F- and H+ transport while unexpectedly
allowing rapid uncoupled Cl- flux (~350-370 ions/s), reversing
the normal F- over Cl- selectivity. The shorter side chain in
E118D impairs transport (16 F-/s vs 150 F-/s for WT).
Replacement of E118 with glutamine or alanine reverses anion
selectivity, demonstrating that the gating glutamate is a key
determinant of F-/Cl- discrimination.

### Ion-Swapped Conformations and the Windmill Model

Two novel conformations were captured: (1) WT structure with
Glu_g in the Up position, exposing F- to the intracellular side
while Glu_g is accessible from the extracellular side for proton
exchange; (2) V319G mutant with Glu_g in the Down position,
occluding F- extracellularly while Glu_g faces the intracellular
vestibule for proton exchange. These structures reveal separate
ion-specific pathways for F- and H+ on opposite sides of the
membrane simultaneously. The proposed 'windmill' model involves a
clockwise rotary trajectory of the Glu_g side chain through Up,
Middle, and Down positions to couple F- export to H+ import with
1:1 stoichiometry.

### F- Binding Site and Selectivity

The F- ion at the extracellular binding site (F-ex) is coordinated
by backbone amides and a hydrogen bond from T320. The conserved
methionine M79 (replacing the Cl--coordinating serine found in
conventional CLCs) contributes to F- specificity. Mutation Y396A
unexpectedly preserved H+ coupling, contrasting with the
equivalent mutation in Cl- CLCs. V319G weakens F- binding
affinity ~5-fold (Kd ~1 mM vs ~0.2 mM WT) and partially
uncouples F-/H+ transport.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/clc-proton-transport-mechanism/">CLC Proton Transport Mechanism</a> — Eca CLCF is a CLC superfamily antiporter with a distinct 1:1 F-/H+ stoichiometry
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/clc-chloride-channel-glutamate-gating/">CLC Chloride Channel Glutamate Gating</a> — The gating glutamate E118 plays a central role in F-/H+ coupling and selectivity in Eca
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/gluex-conformational-states-clc/">Glu_ex Conformational States in CLC Proteins</a> — Eca structures capture Glu_g in Up (WT) and Down (V319G) conformations, distinct from typical Cl- CLCs
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
