---
title: "CasMATE (Camelina sativa MATE Transporter)"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.07.009]
verified: false
---

# CasMATE (Camelina sativa MATE Transporter)

## Overview

CasMATE is a multidrug and toxic compound extrusion (MATE) family transporter from the plant [Camelina sativa](/xray-mp-wiki/organisms/camelina-sativa) (false flax). It represents the first crystal structure of a eukaryotic MATE protein, providing structural insight into the architecture and substrate recognition mechanism of plant MATE transporters. CasMATE consists of 12 transmembrane helices assembled pseudo-symmetrically into an outward-facing V-shaped conformation with a negatively charged internal pocket for ligand binding.


## Publications

### doi/10.1016##j.str.2017.07.009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xjj">5XJJ</a></td>
      <td>2.9 A</td>
      <td>P212121</td>
      <td>CasMATE residues 15-468 (N-terminal 1-14 and C-terminal 469-475 deleted), C-terminal GFP-His8 tag (TEV-cleaved)</td>
      <td>None (apo form)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/organisms/pichia-pastoris) yeast strain SMD1168
- **Construct**: C-terminal GFP-His8 tag fusion, NCBI Reference sequence XP_010514235, linearized pPIC9K vector transformed by electroporation, induced with [Methanol](/xray-mp-wiki/reagents/additives/methanol) in BMMY medium at 20 C for 72 h

**Purification:**

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/organisms/pichia-pastoris) strain SMD1168
- **Expression construct**: CasMATE(15-468)-EFPGENLYFQGQFSKGE-GFP-His8
- **Tag info**: C-terminal GFP-His8 tag, cleaved with [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) at 4 C overnight

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
      <td>Cell culture and induction</td>
      <td>Fermentation in <a href="/xray-mp-wiki/organisms/pichia-pastoris">Pichia pastoris</a></td>
      <td>--</td>
      <td>BMGY medium for growth; BMMY medium for induction</td>
      <td>Transformants selected with <a href="/xray-mp-wiki/reagents/additives/g418">G418 (Geneticin)</a>; cultivated in 10 mL BMGY at 30 C for 24 h, then induced in 1 L BMMY at 20 C for 72 h</td>
    </tr>
    <tr>
      <td>Cell disruption and membrane fractionation</td>
      <td>Microfluidizer cell lysis and ultracentrifugation</td>
      <td>--</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 8.0, 10% glycerol, 1 mM PMSF, 5 mM beta-ME</td>
      <td>Cells disrupted by M-110EH Microfluidizer 5 times at 22,000 p.s.i.; supernatant ultracentrifuged at 40,000 rpm (Beckman 45 Ti rotor) for 2 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization of membrane fraction</td>
      <td>--</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 8.0, 10% glycerol + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (Glycon), 2 h incubation at 4 C</td>
      <td>Pellet resuspended in buffer with 2% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>; centrifuged at 130,000 x g at 4 C for 30 min; supernatant collected</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> cobalt affinity resin (Clontech)</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 7.0, 10% glycerol + 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> (Anatrace), 0.003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> (Anatrace), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
      <td>Washed with LMNG/CHS buffer containing 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; eluted with 200 mM imidazole</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> cobalt affinity resin (Clontech)</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 7.0, 10% glycerol + 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a>, 0.003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
      <td>GFP-His8 tag cleaved with <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> at 4 C overnight; flow-through collected (tag-free protein)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> 10/30 GL (GE Healthcare)</td>
      <td>300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 7.0, 1% glycerol, 0.03% LMNG, 0.003% CHS</td>
      <td>Major peak pooled and concentrated to 25 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CasMATE(15-468) at 25 mg/mL in 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a>, 20 mM HEPES-Na pH 7.0, 1% glycerol, 0.03% LMNG, 0.003% CHS; mixed with liquefied monoolein using twin-syringe mixing method</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> (NU-CHEK-PREP)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in reservoir solutions: (1) 30% PEG400, 100 mM sodium-chloride, 100 mM lithium-sulfate, 100 mM HEPES-Na pH 7.5; (2) 30% PEG400, 100 mM ADA pH 6.5, 300 mM lithium-sulfate; (3) 30% PEG300, 200 mM <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">Ammonium Sulfate</a>, 100 mM HEPES-Na pH 7.5</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xjj">5XJJ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKATWQ</span><span class="topo-inside">SGQLTAELKRVTRLA</span><span class="topo-membrane">APMATVTIAQYLLPVISVMVA</span><span class="topo-outside">GHNGELQLSGVALA</span><span class="topo-membrane">TSFT</span></span>
<span class="topo-line"><span class="topo-membrane">NVTGFSIMYGLVGALE</span><span class="topo-inside">TLCGQAYGAKQYEKIGTYTYSA</span><span class="topo-membrane">IASNIPICFIISIIWFYI</span><span class="topo-outside">ENIL</span></span>
<span class="topo-line"><span class="topo-outside">ISLGQDPDISRIAGS</span><span class="topo-membrane">YAFWLIPVLFAQAIVIPLTR</span><span class="topo-inside">FLLTQGLV</span><span class="topo-membrane">LPLLYTAVTTLLFHVFV</span></span>
<span class="topo-line"><span class="topo-membrane">CWVFVLVF</span><span class="topo-outside">VLGSN</span><span class="topo-membrane">GPAMATSVSFWFYAVILSC</span><span class="topo-inside">YVRFSSSCEKTRGFVSEDFVSCVKQF</span><span class="topo-membrane">FQ</span></span>
<span class="topo-line"><span class="topo-membrane">YGVPSAAMICLEWWLFELLI</span><span class="topo-outside">LCSGLLSNPKLETSVLS</span><span class="topo-membrane">ICLTTETLHYVISSGVAAAVS</span><span class="topo-inside">TR</span></span>
<span class="topo-line"><span class="topo-inside">VSNNLGAGNPQVARVSVLAG</span><span class="topo-membrane">LCLWLVESAFFSILLFTFRNII</span><span class="topo-outside">GYAFSNSKEVVDYVADL</span><span class="topo-membrane">S</span></span>
<span class="topo-line"><span class="topo-membrane">PLLCLSFILDGFTAVLNGVAR</span><span class="topo-inside">GSGW</span><span class="topo-membrane">QHIGAWNNIFSYYLVGAPVG</span><span class="topo-outside">VYLAFRHDLNGKGL</span><span class="topo-membrane">W</span></span>
<span class="topo-line"><span class="topo-membrane">CGVVIGSTVQATVLAIVT</span><span class="topo-inside">ASMNWKEQAEKARKRI</span><span class="topo-unknown">V</span></span>
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
      <td>7</td>
      <td>21</td>
      <td>20</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>42</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>56</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>70</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>98</td>
      <td>90</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>135</td>
      <td>130</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>149</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>163</td>
      <td>169</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>188</td>
      <td>177</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>193</td>
      <td>202</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>212</td>
      <td>207</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>238</td>
      <td>226</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>260</td>
      <td>252</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>277</td>
      <td>274</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>291</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>320</td>
      <td>312</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>342</td>
      <td>334</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>359</td>
      <td>356</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>381</td>
      <td>373</td>
      <td>394</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>385</td>
      <td>395</td>
      <td>398</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>405</td>
      <td>399</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>419</td>
      <td>419</td>
      <td>432</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>438</td>
      <td>433</td>
      <td>451</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>454</td>
      <td>452</td>
      <td>467</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Negatively charged internal pocket for cation binding

The internal pocket of CasMATE provides a negatively charged surface for ligand
binding. Key residues include E270, N74, E296, D383, E265, Q160, Q443, N406,
N390, R168, R394, and E89. The pocket size is approximately 13 x 22 x 22 A
(length x width x depth), sufficient for binding of metal ions such as cadmium
and organic cations like berberine (molecular weight 336). The position of amino
acid clusters is similar to the metal ion binding site of Vc-NorM. Water molecules
bind to residues E265, F269, E296, Y300, S379, D383, Y410, and V436, with E265
and D383 being conserved.

### V-shaped architecture with pseudo-symmetry

CasMATE consists of 12 transmembrane helices (TM 1-12), with the N-terminal
TM 1-6 (N lobe) and C-terminal TM 7-12 (C lobe) assembled pseudo-symmetrically.
The overall structure shows a V-shaped architecture formed by N-lobe and C-lobe
bundles. The extracellular and intracellular sides are open and closed, respectively,
in a manner similar to the outward-facing form of bacterial MATE proteins. TM 1,
2, and 4 of the N lobe and TM 7, 8, and 10 of the C lobe form the central pocket.

### NorM-like cation-binding site in eukaryotic MATE

Phylogenetic analysis shows CasMATE is classified into group B of plant MATE
proteins and is more closely related to prokaryotic group D (NorM-like) than
group E (DinF-like). Residue E261 (equivalent to Ng-NorM E270) is important
for cation binding and is conserved in groups A-D. Residues D41 and D184,
important for cation binding in Pf-DinF, are highly conserved in groups E and
F. The amino acid sequence of CasMATE is more closely related to prokaryote
group D, suggesting CasMATE possesses a NorM-like cation-binding site.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/ntmate2/">NtMATE2 (Nicotiana tabacum MATE2)</a> — Another eukaryotic MATE transporter from tobacco; NtMATE2 was crystallized using CasMATE (PDB 5XJJ) as the [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) search model
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — MATE transporters are secondary transporters related to MFS family in structural and mechanistic features
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism in MFS Transporters</a> — MATE transporters operate via the rocker-switch alternating-access mechanism
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (DDM)</a> — 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm) used for initial membrane solubilization of CasMATE
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) used throughout purification for protein stabilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — 0.003% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate) used during purification and LCP crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Monoolein used as the [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) matrix for LCP crystallization at 2:3 protein-to-lipid ratio
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) method used to grow CasMATE crystals
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> — Structure determination method used
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
