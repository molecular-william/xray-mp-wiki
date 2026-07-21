---
title: "Zebrafish SLC38A9 (drSLC38A9)"
created: 2026-05-29
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2020.11.014, doi/10.1038##s41594-018-0072-2]
verified: agent
uniprot_id: Q08BA4
---

# Zebrafish SLC38A9 (drSLC38A9)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q08BA4">UniProt: Q08BA4</a>

<span class="expr-badge">Danio rerio</span>

## Overview

Zebrafish SLC38A9 (drSLC38A9) is a lysosomal amino acid transporter from Danio rerio that functions as a sensor for luminal arginine and an activator of mTORC1 signaling. drSLC38A9 belongs to the SLC38 family of amino acid transporters and adopts a characteristic [LEUT](/xray-mp-wiki/proteins/enzymes/leut)-like pseudo-symmetry fold with five transmembrane-helix inverted topology repeats. Two crystal structures have been determined: an arginine-bound cytosol-open state at 2.8 A (PDB 6C08) and an N-plug inserted cytosol-closed state at 3.4 A (PDB 7KGV). The arginine-bound structure revealed the transporter in a cytosol-open conformation with the N-terminal domain released from the binding pocket, allowing substrate transport. The protein exhibits a unique N-plug mechanism in which its N-terminal domain inserts into the substrate-binding pocket in the absence of arginine, blocking transport. Upon arginine binding, the N-plug is released, allowing both arginine transport and interaction with the Rag GTPase complex to activate mTORC1. This ball-and-chain mechanism provides a direct link between lysosomal amino acid availability and cellular growth signaling.


## Publications

### doi/10.1016##j.str.2020.11.014

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7kgv">7KGV</a></td>
      <td>3.40</td>
      <td>P 1 21 1</td>
      <td>drSLC38A9 residues 71-549 with N-terminal octa-his tag, complexed with Fab fragment</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells
- **Construct**: drSLC38A9 residues 71-549 from NP_001073468.1 with N-terminal octa-his tag and thrombin cleavage site

**Purification:**

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells

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
      <td>Cell culture</td>
      <td>Bac-to-Bac Baculovirus Expression System</td>
      <td>—</td>
      <td>—</td>
      <td>Sf-9 cells infected, harvested at 60 hours post-infection</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Homogenization in low salt buffer</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, cOmplete Protease Inhibitor Cocktail</td>
      <td>Homogenized and ultra-centrifuged at 130,000 x g for 1 hour</td>
    </tr>
    <tr>
      <td>Membrane fractionation</td>
      <td>Ultra-centrifugation and high salt wash</td>
      <td>—</td>
      <td>1.0 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0</td>
      <td>Pellet washed and resuspended in low salt buffer, frozen in liquid nitrogen at -80 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction at 4 C for 4 hours</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 500 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">GLYCEROL</a>, 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">[DDM</a>](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/), 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Ultra-centrifuged at 130,000 x g for 1 hour after solubilization</td>
    </tr>
    <tr>
      <td>Affinity capture</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Metal Affinity Resin incubation at 4 C overnight</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Metal Affinity Resin (Clontech)</td>
      <td>20 mM Tris pH 8.0, 500 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">GLYCEROL</a>, 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Incubated overnight at 4 C</td>
    </tr>
    <tr>
      <td>Wash</td>
      <td>Column wash</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Metal Affinity Resin (Clontech)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a>, 20 mM Tris pH 8.0, 500 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>5 column volumes wash</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>In-column thrombin digestion</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Metal Affinity Resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 500 mM NaCl, 0.4% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Thrombin at enzyme:protein molar ratio of 1:1000, overnight at 4 C. Cleaved protein in flow-through.</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase</a> 10/300 GL (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS-HCL</a> pH 8.0, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Peak fractions pooled and concentrated to 5 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>drSLC38A9-Fab complex at 5 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS-HCL</a> pH 8.0, 150 mM NaCl, 0.2% DM</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not reported</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not reported</td>
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
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7kgv">7KGV</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDEDSKPLLGSVPTGDYYTDSLDPKQRRPFHVEPRNIVGEDVQERVSAEAAVLSSRVHYYSRLTGSSDRLLAPPDHVIPSHEDIYIYSPLGTAFKVQGGD</span><span class="topo-inside">SHEDKNPSIVTI</span><span class="topo-membrane">FAIWNTMM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GTSILSI</span><span class="topo-unknown">PWGIKQA</span><span class="topo-outside">GFTLG</span><span class="topo-membrane">IIIIVLMGLLTLYC</span><span class="topo-inside">CYRVLKS</span><span class="topo-unknown">TKSIPYVDTSDWEFPD</span><span class="topo-inside">VCKYYFGGFGKWSSLVF</span><span class="topo-membrane">SLVSLIGAMVVYWVLMS</span><span class="topo-outside">NFLFNTGKFIFN</span><span class="topo-unknown">YVHNVQTSDAFGTQG</span><span class="topo-outside">TER</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VICPYPD</span><span class="topo-unknown">VDPHGQSSTSLYSGSDQSTGL</span><span class="topo-outside">EFDHWWS</span><span class="topo-membrane">KTNTIPFYLILL</span><span class="topo-inside">L</span><span class="topo-unknown">LPLLNFRSA</span><span class="topo-inside">SFF</span><span class="topo-membrane">ARFTFLGTISVIYLIF</span><span class="topo-outside">LVTYKAIQLGFHLEFHWFDSSMFFVPEFRTLF</span><span class="topo-membrane">PQLSGVLTLAFF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">I</span><span class="topo-inside">HNCIITLMKN</span><span class="topo-unknown">NKHQENN</span><span class="topo-inside">VRDLS</span><span class="topo-membrane">LAYLLVGLTYLYV</span><span class="topo-outside">GVLIFAAFPSPPLSKECIEPNFLDNFPSSDILVFVA</span><span class="topo-membrane">RTFLLFQMTTVYPLLG</span><span class="topo-inside">YLVRVQ</span><span class="topo-unknown">LMGQIFGNHYPGFL</span><span class="topo-inside">HVF</span><span class="topo-membrane">VLNVFVVGA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550</span>
<span class="topo-line"><span class="topo-membrane">GVLMA</span><span class="topo-outside">RFYPNI</span><span class="topo-membrane">GSIIRYSGALCGLALVFV</span><span class="topo-inside">LPSLIHMVSLK</span><span class="topo-unknown">RRGELRW</span><span class="topo-inside">TSTL</span><span class="topo-membrane">FHGFLILLGVANLLGQFF</span><span class="topo-outside">M</span></span>
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
      <td>101</td>
      <td>112</td>
      <td>80</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>127</td>
      <td>112</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>134</td>
      <td>127</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>135</td>
      <td>139</td>
      <td>134</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>153</td>
      <td>139</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>160</td>
      <td>153</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>193</td>
      <td>176</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>210</td>
      <td>193</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>222</td>
      <td>210</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>247</td>
      <td>237</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>275</td>
      <td>268</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>287</td>
      <td>275</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>288</td>
      <td>287</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>300</td>
      <td>297</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>316</td>
      <td>300</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>348</td>
      <td>316</td>
      <td>347</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>361</td>
      <td>348</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>371</td>
      <td>361</td>
      <td>370</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>383</td>
      <td>378</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>396</td>
      <td>383</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>432</td>
      <td>396</td>
      <td>431</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>448</td>
      <td>432</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>454</td>
      <td>448</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>471</td>
      <td>468</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>471</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>491</td>
      <td>485</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>492</td>
      <td>509</td>
      <td>491</td>
      <td>508</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>510</td>
      <td>520</td>
      <td>509</td>
      <td>519</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>528</td>
      <td>531</td>
      <td>527</td>
      <td>530</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>532</td>
      <td>549</td>
      <td>531</td>
      <td>548</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>550</td>
      <td>550</td>
      <td>549</td>
      <td>549</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41594-018-0072-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c08">6C08</a></td>
      <td>2.80</td>
      <td>P 1 21 1</td>
      <td>drSLC38A9 residues 71-549 with N-terminal deletion (Delta-N), complexed with Fab fragment</td>
      <td>arginine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells
- **Construct**: drSLC38A9 residues 71-549 from NP_001073468.1 with N-terminal octa-his tag and thrombin cleavage site

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6c08">6C08</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LAPPDHVIPSHEDIYIYSPLGTAFKVQGGDSPIKNPS</span><span class="topo-inside">IVTI</span><span class="topo-membrane">FAIWNTMMGTSILSIP</span><span class="topo-outside">WGIKQAGFT</span><span class="topo-membrane">LGIIIIVLMGLLTLYCC</span><span class="topo-inside">YRVL</span><span class="topo-unknown">KSTKSIPYVDTSDWEFPD</span><span class="topo-inside">VCKYYFGGFGKWS</span><span class="topo-membrane">SL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VFSLVSLIGAMVVYWVLMSNFL</span><span class="topo-outside">FNTGKFIFN</span><span class="topo-unknown">YVHNVQTSDAFGTQG</span><span class="topo-outside">TERVICPYPDV</span><span class="topo-unknown">DPHGQSSTSLYSGSDQST</span><span class="topo-outside">GLEFDHWWS</span><span class="topo-membrane">KTNTIPFYLILL</span><span class="topo-unknown">LLPLLNFR</span><span class="topo-inside">SASF</span><span class="topo-membrane">FARFTFLGTISV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">IYLIFLVTY</span><span class="topo-outside">KAIQLGFHLEFH</span><span class="topo-unknown">WFDS</span><span class="topo-outside">SMFFVPEFRTLF</span><span class="topo-membrane">PQLSGVLTLAFFIHN</span><span class="topo-inside">CIITLMKNNKHQE</span><span class="topo-unknown">N</span><span class="topo-inside">NVRDLS</span><span class="topo-membrane">LAYLLVGLTYLYVGVL</span><span class="topo-outside">IFAAFPSPPLSKECIEPNFLDNFPSSDILVF</span><span class="topo-membrane">V</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470         </span>
<span class="topo-line"><span class="topo-membrane">ARTFLLFQMTTVYPLLGYLVRV</span><span class="topo-inside">QLMGQ</span><span class="topo-unknown">IFGNHYPGF</span><span class="topo-inside">LHV</span><span class="topo-membrane">FVLNVFVVGAGVLMA</span><span class="topo-outside">RFYPNI</span><span class="topo-membrane">GSIIRYSGALCGLALVFVL</span><span class="topo-inside">PSLIHMVSLK</span><span class="topo-unknown">RRGEL</span><span class="topo-inside">RWTST</span><span class="topo-membrane">LFHGFLILLGVANLLGQFF</span><span class="topo-outside">M</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>38</td>
      <td>41</td>
      <td>108</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>112</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>66</td>
      <td>128</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>83</td>
      <td>137</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>154</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>118</td>
      <td>176</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>142</td>
      <td>189</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>151</td>
      <td>213</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>177</td>
      <td>237</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>204</td>
      <td>266</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>216</td>
      <td>275</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>295</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>249</td>
      <td>299</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>320</td>
      <td>331</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>277</td>
      <td>336</td>
      <td>347</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>292</td>
      <td>348</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>305</td>
      <td>363</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>312</td>
      <td>377</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>328</td>
      <td>383</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>329</td>
      <td>359</td>
      <td>399</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>382</td>
      <td>430</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>387</td>
      <td>453</td>
      <td>457</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>399</td>
      <td>467</td>
      <td>469</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>414</td>
      <td>470</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>420</td>
      <td>485</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>439</td>
      <td>491</td>
      <td>509</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>440</td>
      <td>449</td>
      <td>510</td>
      <td>519</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>459</td>
      <td>525</td>
      <td>529</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>478</td>
      <td>530</td>
      <td>548</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>479</td>
      <td>549</td>
      <td>549</td>
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

### Arginine-bound cytosol-open state (PDB 6C08)

The crystal structure of drSLC38A9 bound to arginine at 2.8 A resolution revealed the transporter in a cytosol-open conformation. In this state, the N-terminal domain is released from the substrate-binding pocket, and arginine is bound in a binding site located approximately halfway across the membrane. The binding site is formed by residues from TM1a, TM3, TM6a, and TM8. The structure shows a wide vestibule open to the cytosolic side, consistent with a cytosol-open state of the transport cycle. The Delta-N-truncated construct (residues 71-549) was used to obtain the arginine-bound structure, complexed with a Fab fragment that binds on the luminal side. Comparison with the bacterial arginine transporter AdiC (PDB 3L1L) shows structural similarity (r.m.s.d. 3.57 A over 72 C-alpha residues). Two luminal gating clusters were identified: cluster 1 (W128, K131, Q132, R344, E411, P415) and cluster 2 (P348, G491, R495, N542, Q546) that may regulate substrate access from the lysosomal lumen.

### N-plug inserted conformation blocks substrate binding site

The N-terminal domain (residues 1-96) of drSLC38A9 folds into a beta hairpin structure that inserts deep into the transmembrane domain, occupying the substrate binding pocket where arginine normally binds. The N-plug is stabilized by inter-domain hydrogen bonds with the transmembrane bundle and intra-domain hydrogen bonds between Ser80 and Glu82, His76, and Tyr85. This inserted state represents a cytosol-closed conformation of the transporter, effectively blocking substrate access from the cytoplasmic side. The vestibule into which the N-plug inserts measures approximately 20 A in diameter.

### Ball-and-chain model for mTORC1 activation

drSLC38A9 operates via a ball-and-chain mechanism linking luminal arginine levels to mTORC1 activation. At low luminal arginine, the N-plug dynamically samples both inserted and released states as an equilibrium. When arginine concentration increases, arginine molecules enter the substrate binding site from the luminal side, and the N-plug remains in the exposed state while arginine transport occurs. In the released state, the N-plug becomes available for binding to the Rag GTPase complex (drRagA and drRagC), which activates mTORC1 signaling. The 85PDH87 motif on the N-plug is essential for Rag GTPase interaction, corresponding to a conserved region on the beta hairpin structure.

### N-plug modulates arginine transport efficiency

Functional assays in reconstituted proteoliposomes demonstrated that the N-plug plays an inhibitory role in downregulating arginine transport. Mutants with disrupted N-plug binding (V77W, H81W, Y87F single mutants and V77W+H81W+Y87F triple mutant) displayed significantly higher arginine transport efficiency. The triple site mutant showed a 2-fold decrease in Km for arginine without significant change in Vmax. The superposition of the N-plug bound structure with the arginine-bound structure (PDB: 6C08) showed that the same set of backbone atoms are used for binding both the N-plug and arginine, supporting competitive binding between the N-plug and arginine.

### Arginine-enhanced leucine transport requires intact N-plug

drSLC38A9 exhibits higher affinity for leucine than arginine, and transport of leucine is arginine-regulated. The characteristic arginine-enhanced leucine transport was lost when the N-plug was deleted or its structure altered by mutation. Only drSLC38A9 with an intact N-terminal plug in its native beta hairpin structure showed enhanced leucine uptake in the presence of supplemented arginine. This indicates that the N-plug conformational change is required for the coordinated efflux of multiple essential amino acids from lysosomes.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate</a> — Lipid additive used during solubilization
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside</a> — Detergent used in SEC buffer and tag removal
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> — Affinity resin for His-tag purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase</a> — SEC resin for final purification step
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer used throughout purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Stabilizer in solubilization buffer
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Eluent competitor in TALON affinity purification
- <a href="/xray-mp-wiki/proteins/enzymes/leut">LEUT</a> — Structurally related membrane protein
- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS-HCL</a> — Reagent used in this study
