---
title: "Cysteinyl Leukotriene Receptor 2 (CysLT2R)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-13348-2]
verified: regex
uniprot_id: Q9NS75
---

# Cysteinyl Leukotriene Receptor 2 (CysLT2R)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9NS75">UniProt: Q9NS75</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Cysteinyl leukotriene receptor type 2 (CysLT2R) is a class A G protein-coupled receptor (GPCR) that mediates pro-inflammatory responses to cysteinyl leukotrienes LTC4 and LTD4. Four crystal structures of CysLT2R were determined in complex with three dual CysLT1R/CysLT2R antagonists (ONO-2570366, ONO-2770372, and ONO-2080365) at resolutions of 2.4-2.7 A using lipidic cubic phase (LCP) crystallization. The structures, combined with comprehensive mutagenesis and computational modeling, reveal molecular determinants of ligand selectivity between [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) and CysLT2R subtypes and provide structural explanations for disease-associated single nucleotide variants including M201V (atopic asthma) and L129Q (uveal melanoma).


## Publications

### doi/10.1038##s41467-019-13348-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rz6">6RZ6</a></td>
      <td>2.4</td>
      <td>P 21 21 21</td>
      <td>Human CysLT2R with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> fusion in ICL3, N- and C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a>, W51V, D84N, F137Y mutations; complex with ONO-2570366 (cpd 11a)</td>
      <td>ONO-2570366 (cpd 11a, antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rz7">6RZ7</a></td>
      <td>2.4</td>
      <td>Not specified</td>
      <td>Human CysLT2R with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> fusion in ICL3, N- and C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a>, W51V, D84N, F137Y mutations; complex with ONO-2570366 (cpd 11a)</td>
      <td>ONO-2570366 (cpd 11a, antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rz8">6RZ8</a></td>
      <td>2.7</td>
      <td>Not specified</td>
      <td>Human CysLT2R with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> fusion in ICL3, N- and C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a>, W51V, D84N, F137Y mutations; complex with ONO-2770372 (cpd 11b)</td>
      <td>ONO-2770372 (cpd 11b, antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rz9">6RZ9</a></td>
      <td>2.7</td>
      <td>Not specified</td>
      <td>Human CysLT2R with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> fusion in ICL3, N- and C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a>, W51V, D84N, F137Y mutations; complex with ONO-2080365 (cpd 11c)</td>
      <td>ONO-2080365 (cpd 11c, antagonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Human CysLT2R (UniProt Q9NS75) with N-terminal HA-FLAG-10xHis-TEV, N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (1-16), C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (323-346), [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in ICL3 (between E232 and V240), W51V/D84N/F137Y mutations
- **Notes**: Bac-to-Bac baculovirus expression system. Cells infected at MOI 5-10, harvested 48-50 h post-infection. 3 uM BayCysLT2 ligand added at infection.


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
      <td>Cell lysis</td>
      <td>Hypotonic lysis</td>
      <td></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 20 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a></td>
      <td>Cells washed with hypotonic and high osmotic buffers with <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitors</a></td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td></td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 25 uM ligand, 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilization for 3.5 h at 4 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> (<a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin</td>
      <td>Wash 1 - 100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 250 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 8 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> / Wash 2 - 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 250 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (wash 1) / 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (wash 2)</td>
      <td>Overnight batch binding with 10 CV washes</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Gel filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 25 uM ligand + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Peak fractions pooled and concentrated</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase (LCP) crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CysLT2R in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a>-based <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested and flash-cooled in <a href="/xray-mp-wiki/concepts/methods-techniques/cryocooling/">liquid nitrogen</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Four structures determined: CysLT2R-11a in two space groups (2.4 A each, PDB 6RZ6 and 6RZ7), CysLT2R-11b (2.7 A, PDB 6RZ8), and CysLT2R-11c (2.7 A, PDB 6RZ9). Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using CysLT1R-pranlukast as search model.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rz6">6RZ6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEPNGTFSNNNS</span><span class="topo-inside">RNCTIENFKREF</span><span class="topo-membrane">FPIVYLIIFFVGVLGNGLSIYVFLQ</span><span class="topo-outside">PYKKSTS</span><span class="topo-membrane">VNVFMLNLAISNLLFISTLPFRAD</span><span class="topo-inside">YYLRGSNWIFGDL</span><span class="topo-membrane">ACRIMSYSLYVNMYSSIYFLTVLSVVR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">LAMVHPFR</span><span class="topo-unknown">LLH</span><span class="topo-outside">VTSI</span><span class="topo-membrane">RSAWILCGIIWILIMASSIMLLD</span><span class="topo-inside">S</span><span class="topo-unknown">GS</span><span class="topo-inside">EQNGSVTSCLELNLYKIAKLQT</span><span class="topo-membrane">MNYIALVVGCLLPFFTLSICYLLII</span><span class="topo-outside">RVLLKVEADLEDNWETLNDNLKVIEKA</span><span class="topo-unknown">DN</span><span class="topo-outside">AA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QVKDALTKMRAAALDAQ</span><span class="topo-unknown">KATPPKLEDKSPDSPE</span><span class="topo-outside">MKDFRHGFDILVGQIDDALKL</span><span class="topo-unknown">ANEGK</span><span class="topo-outside">VKEAQAAAEQLKTTRNAYIQKYLVSHRKA</span><span class="topo-membrane">LTTIIITLIIFFLCFLPYHTLRTV</span><span class="topo-inside">HLTTWKVG</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-inside">LCKDRLHKA</span><span class="topo-membrane">LVITLALAAANACFNPLLYYFAG</span><span class="topo-outside">ENFKDRLKSALRK</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>12</td>
      <td>17</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>24</td>
      <td>29</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>49</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>66</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>80</td>
      <td>73</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>93</td>
      <td>97</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>121</td>
      <td>110</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>129</td>
      <td>138</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>132</td>
      <td>146</td>
      <td>148</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>133</td>
      <td>136</td>
      <td>149</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>153</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>176</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>162</td>
      <td>177</td>
      <td>178</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>184</td>
      <td>179</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>209</td>
      <td>201</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>216</td>
      <td>226</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>236</td>
      <td>1001</td>
      <td>1020</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>238</td>
      <td>1021</td>
      <td>1022</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>1023</td>
      <td>1041</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>273</td>
      <td>1042</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>1058</td>
      <td>1078</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>299</td>
      <td>1079</td>
      <td>1083</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>300</td>
      <td>322</td>
      <td>1084</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>328</td>
      <td>240</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>369</td>
      <td>270</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>392</td>
      <td>287</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>405</td>
      <td>310</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rz7">6RZ7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEPNGTFSNNNSRN</span><span class="topo-inside">CTIENFKREF</span><span class="topo-membrane">FPIVYLIIFFVGVLGNGLSIYVFLQ</span><span class="topo-outside">PYKKSTS</span><span class="topo-membrane">VNVFMLNLAISNLLFISTLPFRAD</span><span class="topo-inside">YYLRGSNWIFGDL</span><span class="topo-membrane">ACRIMSYSLYVNMYSSIYFLTVLSVVR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">LAMVHP</span><span class="topo-unknown">FRLLH</span><span class="topo-outside">VTSIR</span><span class="topo-membrane">SAWILCGIIWILIMASSIMLLD</span><span class="topo-inside">S</span><span class="topo-unknown">GSEQNG</span><span class="topo-inside">SVTSCLELNLYKIAKL</span><span class="topo-membrane">QTMNYIALVVGCLLPFFTLSICYLLII</span><span class="topo-outside">RVLLKVEADLEDNWETLNDNLKVIEKADNAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QVKDALTKMRAAALD</span><span class="topo-unknown">AQKATPPKLEDKSPDSPEMK</span><span class="topo-outside">DFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLVSHRKA</span><span class="topo-membrane">LTTIIITLIIFFLCFLPYHTLRTV</span><span class="topo-inside">HLTTWKVG</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-inside">LCKDRLHK</span><span class="topo-membrane">ALVITLALAAANACFNPLLYYFAG</span><span class="topo-outside">ENFKDRLKSALRK</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>14</td>
      <td>17</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>24</td>
      <td>31</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>49</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>66</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>80</td>
      <td>73</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>93</td>
      <td>97</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>121</td>
      <td>110</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>127</td>
      <td>138</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>132</td>
      <td>144</td>
      <td>148</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>133</td>
      <td>137</td>
      <td>149</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>159</td>
      <td>154</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>176</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>166</td>
      <td>177</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>182</td>
      <td>183</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>209</td>
      <td>199</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>216</td>
      <td>226</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>255</td>
      <td>1001</td>
      <td>1039</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>1040</td>
      <td>1059</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>276</td>
      <td>322</td>
      <td>1060</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>328</td>
      <td>240</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>368</td>
      <td>270</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>392</td>
      <td>286</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>405</td>
      <td>310</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rz8">6RZ8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEPNGTFSNNNSRN</span><span class="topo-inside">CTIENFKREF</span><span class="topo-membrane">FPIVYLIIFFVGVLGNGLSIYVFLQP</span><span class="topo-outside">YKKS</span><span class="topo-membrane">TSVNVFMLNLAISNLLFISTLPFRA</span><span class="topo-inside">DYYLRGSNWIFGDLACR</span><span class="topo-membrane">IMSYSLYVNMYSSIYFLTVLSVVR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">LAMVH</span><span class="topo-unknown">PFRLLHV</span><span class="topo-outside">TS</span><span class="topo-membrane">IRSAWILCGIIWILIMASSIMLL</span><span class="topo-inside">DSGSEQNGSVTSCLELNLYKIAKL</span><span class="topo-membrane">QTMNYIALVVGCLLPFFTLSICYLL</span><span class="topo-outside">IIRVLLKVEADLEDNWETLNDNLKVIEKADNAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QVKDALTKMRAAALDAQKATP</span><span class="topo-unknown">PKLEDKSPD</span><span class="topo-outside">SPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLVSHRKAL</span><span class="topo-membrane">TTIIITLIIFFLCFLPYHTLRTVH</span><span class="topo-inside">LTTWKVG</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-inside">LCKDRLHK</span><span class="topo-membrane">ALVITLALAAANACFNPLLYYFAGE</span><span class="topo-outside">NFK</span><span class="topo-unknown">DRLKSALRK</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>17</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>24</td>
      <td>31</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>50</td>
      <td>41</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>67</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>79</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>121</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>126</td>
      <td>138</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>133</td>
      <td>143</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>135</td>
      <td>150</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>158</td>
      <td>152</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>182</td>
      <td>175</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>207</td>
      <td>199</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>216</td>
      <td>224</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>261</td>
      <td>1001</td>
      <td>1045</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>270</td>
      <td>1046</td>
      <td>1054</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>271</td>
      <td>322</td>
      <td>1055</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>329</td>
      <td>240</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>353</td>
      <td>247</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>368</td>
      <td>271</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>393</td>
      <td>286</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>396</td>
      <td>311</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>405</td>
      <td>314</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rz9">6RZ9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEPNGTFSNNNSRN</span><span class="topo-inside">CTIENFKREF</span><span class="topo-membrane">FPIVYLIIFFVGVLGNGLSIYVFLQ</span><span class="topo-outside">PYKKST</span><span class="topo-membrane">SVNVFMLNLAISNLLFISTLPFRA</span><span class="topo-inside">DYYLRGSNWIFGDLACRI</span><span class="topo-membrane">MSYSLYVNMYSSIYFLTVLSVVR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YL</span><span class="topo-outside">AMVHPFR</span><span class="topo-unknown">LL</span><span class="topo-outside">HVTS</span><span class="topo-membrane">IRSAWILCGIIWILIMASSIMLL</span><span class="topo-inside">DS</span><span class="topo-unknown">GS</span><span class="topo-inside">EQNGSVTSCLELNLYKIAKLQTM</span><span class="topo-membrane">NYIALVVGCLLPFFTLSICYLLIIR</span><span class="topo-outside">VLLKVEADLEDNWETLNDNLKVIEKA</span><span class="topo-unknown">DN</span><span class="topo-outside">AA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QVKDALTKMRAAALDAQ</span><span class="topo-unknown">KATPPKLEDKSPDSPE</span><span class="topo-outside">MKDFRHGFDILVGQIDDALKL</span><span class="topo-unknown">ANEGK</span><span class="topo-outside">VKEAQAAAEQLKTTRNAYIQKYLVSHRK</span><span class="topo-membrane">ALTTIIITLIIFFLCFLPYHTLRT</span><span class="topo-inside">VHLTTWKVG</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-inside">LCKDRLHKA</span><span class="topo-membrane">LVITLALAAANACFNPLLYYFAGE</span><span class="topo-outside">NFKDRLKSALR</span><span class="topo-unknown">K</span></span>
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
      <td>14</td>
      <td>17</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>24</td>
      <td>31</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>49</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>55</td>
      <td>66</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>79</td>
      <td>72</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>97</td>
      <td>96</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>122</td>
      <td>114</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>129</td>
      <td>139</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>131</td>
      <td>146</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>135</td>
      <td>148</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>158</td>
      <td>152</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>160</td>
      <td>175</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>162</td>
      <td>177</td>
      <td>178</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>179</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>210</td>
      <td>202</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>216</td>
      <td>227</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>236</td>
      <td>1001</td>
      <td>1020</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>238</td>
      <td>1021</td>
      <td>1022</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>1023</td>
      <td>1041</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>273</td>
      <td>1042</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>1058</td>
      <td>1078</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>299</td>
      <td>1079</td>
      <td>1083</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>300</td>
      <td>322</td>
      <td>1084</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>327</td>
      <td>240</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>351</td>
      <td>245</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>369</td>
      <td>269</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>393</td>
      <td>287</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>404</td>
      <td>311</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>405</td>
      <td>322</td>
      <td>322</td>
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

### Ligand-binding pocket architecture

CysLT2R adopts the canonical seven-transmembrane helical bundle. All three antagonists share the same 3,4-dihydro-2H-1,4-benzoxazine scaffold and bind in similar conformations. Y119(3.33) is a key anchoring residue forming multiple polar contacts with the benzoxazine part, carboxylic group, and amide linker. The N-linked carboxypropyl moiety makes salt bridges with K37(1.31) and H284(7.32) that are specific to CysLT2R.

### Antagonist selectivity determinants between CysLTR subtypes

Docking of 18 scaffold derivatives revealed structural basis for selectivity. [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) has F150(4.52) which restricts the subpocket near TM4, while CysLT2R has L165(4.52) which creates a more open cleft. For the N-substituent, CysLT1R's Y26(1.35) forms a hydrogen bond with carboxyl groups (as in cpd 13e, 1800-fold selective for [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/)), while CysLT2R has F41(1.35) which cannot form such interactions, explaining selectivity preferences.

### Atopic asthma-associated M201V polymorphism

M201(5.38) together with M172(4.59), L173(4.60), and L198(5.35) define the hydrophobic part of the ligand-binding pocket. The M201V variant (atopic asthma-associated) still responds to LTD4 stimulation but with significantly decreased potency and efficacy compared to wild-type. Substitution with alanine or leucine results in nonresponsive mutants, indicating the specific effect of the valine substitution.

### Oncogenic L129Q constitutive activation

L129(3.43)Q mutation is associated with uveal melanoma and blue nevi. This mutation displays constitutive activity for the Gq pathway with a fourfold increase in basal IP1 accumulation and is unresponsive to LTD4 stimulation. Position 3.43 mutations to R, K, A, E, or Q induce constitutive activation in several GPCRs.

### Intracellular helix H8 in CysLT receptors

CysLT2R displays a well-resolved intracellular helix H8, while [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) does not. The difference stems from [Cyslt1R](/xray-mp-wiki/proteins/gpcr/cyslt1r/) having a flexible GG(8.48) motif at the TM7-H8 junction, whereas CysLT2R has GE(8.48). This structural insight helps explain differences in receptor stability and signaling properties between the two subtypes.

### Mapping of disease-associated SNVs

Structural mapping of 117 missense SNV positions from the ExAC database revealed that 9 belong to the ligand-binding pocket, 7 are activation-related microswitches or in the sodium-binding site, and 9 reside on the G protein and beta-arrestin-binding interface. Most ExAC mutations are very rare (MAF < 10^-4), making disease association difficult.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/cyslt1r/">Cysteinyl Leukotriene Receptor 1 (CysLT1R)</a> — Closely related GPCR subtype; companion paper describes CysLT1R structures with zafirlukast and pranlukast
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for CysLT2R solubilization and purification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (In Meso) Crystallization</a> — Crystallization method used for all CysLT2R structures
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Additive used in purification to stabilize the receptor
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/">GPCR G Protein Coupling</a> — CysLT2R is a GPCR that signals through Gq/11 pathway
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> — Referenced in context related to Bril
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> — Referenced in context related to Truncation
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in context related to Hepes
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a> — Referenced in context related to Mgcl2
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Referenced in context related to Iodoacetamide
