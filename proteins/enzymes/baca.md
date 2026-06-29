---
title: "Undecaprenyl Pyrophosphate Phosphatase (UppP/BacA) from Escherichia coli"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41467-018-03547-8]
verified: false
---

# Undecaprenyl Pyrophosphate Phosphatase (UppP/BacA) from Escherichia coli

## Overview

Undecaprenyl pyrophosphate phosphatase (UppP, also known as BacA) is a 30 kDa polytopic integral membrane protein from Escherichia coli that catalyzes the dephosphorylation of undecaprenyl pyrophosphate (C55-PP) to undecaprenyl phosphate (C55-P), recycling the essential lipid carrier for bacterial cell wall peptidoglycan biosynthesis. The crystal structure of UppP from E. coli (EcUppP) was determined at 2.0 Å resolution, revealing an unexpected inverted topology repeat with interdigitated reentrant helices that form the active site deep within the membrane bilayer. The structure establishes Ser27 as the catalytic nucleophile, with Glu21, Glu17, and Arg174 playing critical roles in the phosphatase mechanism. UppP belongs to the PAP2 (type II phosphatidic acid phosphatase) family and was first identified in a screen for bacitracin resistance genes. The structure reveals a dimeric arrangement with each monomer containing ten transmembrane helices and two reentrant helix-loop-helix motifs that coordinate substrate binding and catalysis within the membrane mid-plane. Remarkably, the UppP fold shares structural similarity with cross-membrane transporters (ZIP zinc transporter, MFS transporters, ClC transporter, and CitS symporter), suggesting a potential dual function as both a phosphatase and a flippase for the C55-P reaction product.

## Publications

### doi/10.1038##s41467-018-03547-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6cb2">6CB2</a></td>
      <td>2.00</td>
      <td>C222</td>
      <td>Full-length EcUppP with N-terminal hexahistidine tag (removed by thrombin)</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3) (Sigma)
- **Construct**: Full-length UppP from E. coli K-12 (ATCC 10798) in pET28a vector with N-terminal hexahistidine tag and thrombin cleavage site
- **Notes**: Overexpressed in ZYP-5052 autoinduction media at 37°C for 3 h, then 27°C overnight

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
      <td>1. Membrane preparation</td>
      <td>Cell lysis by Emulsiflex-C5 homogenizer; membranes collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 200,000 × g for 1 h</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a></td>
      <td>Cells resuspended with lysozyme, DNaseI, MgCl2, and protease inhibitors</td>
    </tr>
    <tr>
      <td>2. Solubilization</td>
      <td>Detergent solubilization for 1 h</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 1% (w/v) N-dodecyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Insoluble material removed by centrifugation</td>
    </tr>
    <tr>
      <td>3. <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Superflow</a> (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; eluted with 250 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a></td>
      <td>Column pre-equilibrated with 30 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a>; washed with 60 mM imidazole</td>
    </tr>
    <tr>
      <td>4. Desalting and tag removal</td>
      <td>Desalting and overnight thrombin cleavage</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 150 mM NaCl, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">Hexahistidine tag</a> removed by thrombin</td>
    </tr>
    <tr>
      <td>5. <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 150 mM NaCl, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified protein concentrated to 12 mg/mL using 50 kDa MWCO concentrator</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified UppP at 12 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 150 mM NaCl, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (Sigma), 2:3 (v/v) protein-to-lipid ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial crystals with 40% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 200, 100 mM NaCl, 100 mM LiSO4, 100 mM Na<a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> pH 5. Optimized crystals harvested using MicroMounts and frozen directly in liquid nitrogen. <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury</a> derivatized crystals: sixfold molar excess ethyl mercury phosphate incubated for 30 min at 4°C before <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> preparation. Crystals grown in 45% PEG 200, 150 mM MgCl2, 400 mM LiSO4, 100 mM NaCitrate pH 5.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6cb2">6CB2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMSD</span><span class="topo-outside">MHSLLIA</span><span class="topo-unknown">AILGVVEGLTEFLPVSSTGHM</span><span class="topo-outside">IIVGHLLGF</span></span>
<span class="topo-line"><span class="topo-outside">EGDTAKTFE</span><span class="topo-membrane">VVIQLGSILAVVVMFW</span><span class="topo-inside">RRLFGLIGIHFGRPLQHEGESKGRLTL</span><span class="topo-membrane">IHILLGMI</span></span>
<span class="topo-line"><span class="topo-membrane">PAVVLGLLFH</span><span class="topo-outside">DTIKSLFNPIN</span><span class="topo-membrane">VMYALVVGGLLLIAAE</span><span class="topo-inside">CLKPKEPRAPGLDDMTYRQA</span><span class="topo-unknown">FMI</span></span>
<span class="topo-line"><span class="topo-unknown">GCFQCLALWPGFSRSGATISGG</span><span class="topo-inside">MLMGVSRYAA</span><span class="topo-membrane">SEFSFLLAVPMMMGATAL</span><span class="topo-outside">DLYKSWGFLT</span></span>
<span class="topo-line"><span class="topo-outside">SGDIPMF</span><span class="topo-membrane">AVGFITAFVVALIAIKTF</span><span class="topo-inside">LQLIKRISF</span><span class="topo-membrane">IPFAIYRFIVAAAV</span><span class="topo-outside">YVVFF</span></span>
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
      <td>23</td>
      <td>-19</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>4</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>51</td>
      <td>11</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>32</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>85</td>
      <td>50</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>112</td>
      <td>66</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>130</td>
      <td>93</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>141</td>
      <td>111</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>157</td>
      <td>122</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>177</td>
      <td>138</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>202</td>
      <td>158</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>203</td>
      <td>212</td>
      <td>183</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>230</td>
      <td>193</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>247</td>
      <td>211</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>265</td>
      <td>228</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>274</td>
      <td>246</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>255</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>293</td>
      <td>269</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Inverted topology repeat and interdigitated architecture

EcUppP adopts an interdigitated inverted topology repeat (IITR) fold, the first observation of this fold in an enzyme. The N-repeat (residues 1-150) and C-repeat (residues 151-273) are related by a pseudo-twofold symmetry axis parallel to the membrane plane. Each repeat contains a reentrant helix-loop-helix motif (inner arch) followed by three transmembrane helices (outer arch). The repeats interdigitate such that the N-repeat's inner arch pairs with the C-repeat's outer arch and vice versa, creating two structural domains.

### Reentrant helix active site architecture

The active site is formed by two antiparallel reentrant helix-loop-helix motifs (first: Glu17-Arg35, second: Gly171-Leu181) that create a positively charged basin at the bottom of an electronegative funnel. The reentrant helices insert from opposite sides of the membrane with their N-termini meeting at the membrane mid-plane where the pyrophosphate substrate is coordinated. This architecture creates an internalized active site accessible from the periplasmic side via a deep cleft.

### Ser27 catalytic nucleophile and SRS motif

Ser27 is unambiguously identified as the catalytic nucleophile based on the 2.0 Å structure and mutagenesis (S27A completely abrogates activity). Ser27 projects from the N-terminal end of helix α2 into the active site. It is part of a highly conserved SRS (Ser-Arg-Ser) motif in the second reentrant loop that shows similarity to the P-loop motif of dual specificity phosphatases (DUSPs). Arg174 in this motif coordinates and polarizes the phosphate moiety.

### Glu21 as catalytic base with Glu17 carboxyl-carboxylate pair

Glu21 forms a hydrogen bond (3.1 Å) with the Ser27 side chain hydroxyl and is positioned to act as the activating general base for both the nucleophilic attack and subsequent hydrolysis steps. Glu17 is located directly adjacent to Glu21, forming a carboxyl-carboxylate interaction (2.8 Å) that modulates Glu21's pKa for its general base role. This carboxyl-carboxylate pair is a functionally important catalytic feature.

### His30 structural role and metal-dependent activity

His30, previously proposed as the catalytic nucleophile, actually plays a purely structural role. It forms hydrogen bonds with the backbone carbonyls of Val25 and Ser26 to stabilize the 3_10 helical nature of the N-terminal region of α2, and with Tyr260 to provide structural stabilization between α2 and α10. His30Ala reduces activity due to destabilization rather than loss of catalytic function. UppP activity is metal-dependent with strong preference for Mg2+ and Ca2+, with a putative cation-binding site coordinated by Ser173, Ser175, and backbone carbonyls.

### Structural similarity to cross-membrane transporters

DALI search revealed structural similarity to the ZIP zinc transporter (Z-score 4.1), MFS multidrug transporter MdfA (Z-score 4.1), ClC chloride transporter (Z-score 3.6), and CitS sodium-dependent citrate symporter (Z-score 3.5). These transporters share the inverted repeat topology and reentrant helical regions. The similarity to the ClC transporter is particularly notable as ClC uses reentrant helices to coordinate Cl- anions, analogous to how UppP coordinates the pyrophosphate moiety of C55-PP.

### Potential flippase function

The shared structural features with transporters — particularly the interlocked inverted repeat that enables alternating access — raise the intriguing possibility that UppP not only functions as a C55-PP phosphatase but also plays a role in recycling the C55-P product back across the membrane. A hydrophobic pocket formed by amphipathic helix α3b at the cytoplasmic interface may bind the C55 hydrophobic tail. Similar structural characteristics are observed in the MurJ lipid II flippase, which also binds lipidic substrates.


## Cross-References
