---
title: "GR (Halobacterium sp. GR Bacteriorhodopsin)"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8177]
verified: false
---

# GR (Halobacterium sp. GR Bacteriorhodopsin)

## Overview

GR (Halobacterium sp. GR [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin)) is a [Light-Driven Proton Pump](/xray-mp-wiki/concepts/light-driven-proton-pump/) from Halobacterium sp. strain GR. It is a member of the [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) family and functions as a [Light-Driven Proton Pump](/xray-mp-wiki/concepts/light-driven-proton-pump/). GR was engineered with point mutations to create blue-shifted variants using the same rational design principle applied to C1C2 and [HwBR (Halomonas Water Bacteriorhodopsin)](/xray-mp-wiki/proteins/hwbr). The wild-type GR exhibits a characteristic absorption maximum typical of bacteriorhodopsins. GR was expressed in E. coli BL21(DE3) using [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) induction and purified using standard membrane protein purification protocols.

## Publications

### doi/10.1038##ncomms8177

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>GR wild-type and mutant variants</td>
      <td>all-trans retinal</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: GR expression plasmid constructed as previously described
- **Notes**: Transformed E. coli BL21(DE3) cells grown at 18 C overnight in LB medium containing [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin) (50 ug/ml) and 5 uM [All-trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/). [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) induction (0.5 mM) used for GR expression (as opposed to L-arabinose for AR3 and [HwBR (Halomonas Water Bacteriorhodopsin)](/xray-mp-wiki/proteins/hwbr)).
- **Induction**: 0.5 mM [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) ([IPTG](/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside))

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
      <td>Cell disruption and membrane fractionation</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> (pH 6.5) containing 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> + --</td>
      <td>Cells harvested by centrifugation at 4 C, disrupted by sonication or French press passage</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> (pH 6.5), 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> + n-<a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>)</td>
      <td>Cell membranes solubilized by <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+ affinity column (GE Healthcare)</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>Purified by chromatography on Ni2+ affinity column</td>
    </tr>
    <tr>
      <td>Concentration and buffer exchange</td>
      <td>Ultrafiltration concentration</td>
      <td>--</td>
      <td>1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Hydroxymethyl) Aminomethane</a>-Cl (pH 7.0) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>Purified sample concentrated using Amicon Ultra filter</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PDYVFHRAHERMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CG</span><span class="topo-membrane">WEEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RYAEWLLTCPVILIHL</span><span class="topo-outside">SNLTGLANDYNKR</span><span class="topo-membrane">TMGLLVSDIGGIVWATTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNAA</span><span class="topo-outside">KVYIEAYHTVPKGRCRQVVT</span><span class="topo-membrane">GMAWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300    </span>
<span class="topo-line"><span class="topo-inside">LSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLLGH</span><span class="topo-outside">YLRVLIHEHILIHGDIRKTTK</span><span class="topo-unknown">LNIGGTE</span><span class="topo-outside">IEVETLVEDE</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>52</td>
      <td>39</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>81</td>
      <td>118</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>100</td>
      <td>120</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>149</td>
      <td>175</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>233</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>253</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>245</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>305</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzi">4YZI</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PDYVFHRAHERMLFQTSYTLENNGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWITFALSALCLMFY</span><span class="topo-unknown">GYQTWKST</span><span class="topo-outside">CG</span><span class="topo-membrane">WEEIYVATIEMIKFIIEYF</span><span class="topo-inside">HEFDEPAVIYSSNGNKT</span><span class="topo-membrane">VWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RYAEWLLTCPVILIHL</span><span class="topo-outside">SNLTGLANDYNKR</span><span class="topo-membrane">TMGLLVSDIGGIVWATTAAL</span><span class="topo-inside">SKGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFFNAA</span><span class="topo-outside">KVYIEAYHTVPKGRCRQVVT</span><span class="topo-membrane">GMAWLFFVSWGMFPILFILG</span><span class="topo-inside">PEGFGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300    </span>
<span class="topo-line"><span class="topo-inside">LSVYG</span><span class="topo-membrane">STVGHTIIDLMSKNCWGLLGH</span><span class="topo-outside">YLRVLIHEHILIHGDIRKTTK</span><span class="topo-unknown">LNIGGTE</span><span class="topo-outside">IEVETLVEDE</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>52</td>
      <td>39</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>71</td>
      <td>91</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>81</td>
      <td>118</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>100</td>
      <td>120</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>139</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>149</td>
      <td>175</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>169</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>208</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>214</td>
      <td>233</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>253</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>245</td>
      <td>273</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>305</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>304</td>
      <td>333</td>
      <td>342</td>
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

### Blue-shifted GR variants created by rational design

GR was engineered with point mutations to create blue-shifted variants using the rational design principle established for C1C2. The mutations at positions equivalent to C1C2 residues 198 and 202 induce rotation of the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal) chromophore, producing blue-shifted absorption spectra. GR variants were characterized by absorption spectroscopy in the presence of [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) at pH 7.0, demonstrating the transferability of the design principle across different [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) families.

### GR as a platform for optogenetics tool development

GR [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin) was identified as a suitable platform for rational design of blue-shifted variants. The successful engineering of GR with blue-shifted spectral properties demonstrates the generality of the atomistic design approach across diverse [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) families, including bacteriorhodopsins from different Halobacterium strains.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/">Archaerhodopsin-2</a> — AR3 shares high sequence similarity with HwBR; same design principle applied to GR
- <a href="/xray-mp-wiki/proteins/rhodopsins/c1c2ga/">C1C2GA (C1C2 T198G/G202A)</a> — GR was engineered using the same design principle as C1C2GA
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — GR is a bacteriorhodopsin from Halobacterium sp.
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Detergent used for membrane solubilization and protein purification
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-morpholino)ethanesulfonic acid (MES)</a> — Buffer (50 mM, pH 6.5) used in cell lysis and membrane preparation
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Isopropyl-beta-D-thiogalactoside (IPTG)</a> — IPTG induction (0.5 mM) used for GR expression in E. coli
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans retinal</a> — Chromophore covalently bound to conserved lysine via protonated Schiff base
- <a href="/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside">IPTG</a> — Referenced in gr
- <a href="/xray-mp-wiki/concepts/light-driven-proton-pump/">Light-Driven Proton Pump</a> — Referenced in gr
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in gr
