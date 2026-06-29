---
title: "iC++ (Designed Anion Channelrhodopsin)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0504-5]
verified: false
---

# iC++ (Designed Anion Channelrhodopsin)

## Overview

iC++ is a designed anion-conducting channelrhodopsin (dACR) created by structure-guided engineering of the C1C2 chimeric cation channelrhodopsin (CCR) through 10 mutations in transmembrane helices 1, 2, 3, and 7. Crystal structures were determined at pH 8.5 (3.2 A resolution) and pH 6.5 (3.2 A resolution), revealing the molecular basis for anion selectivity, pH dependence, and channel gating in both designed (dACRs) and natural (nACRs) anion channelrhodopsins. Comparison with the natural ACR [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) showed that iC++ extracellular vestibule shapes are more similar to nACRs than to its CCR parent C1C2. Structure-guided engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) led to FLASH (fast, light-activated anion-selective rhodopsin), integrating large photocurrents with fast kinetics. The structures provide insights into pore-surface electrostatics as the primary determinant of ion selectivity in channelrhodopsins.


## Publications

### doi/10.1038##s41586-018-0504-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6csn">6CSN</a></td>
      <td>3.2 A</td>
      <td>not specified</td>
      <td>iC++ with N61Q mutation, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> and C-terminal EGFP-His10 tag (pH 8.5, dark state)</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6cso">6CSO</a></td>
      <td>3.2 A</td>
      <td>not specified</td>
      <td>iC++ with N61Q mutation, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> and C-terminal EGFP-His10 tag (pH 6.5, dark state)</td>
      <td>all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system)
- **Construct**: iC++ with N61Q mutation, N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) (3C protease site), C-terminal EGFP-His10 tag (3C site)

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
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, protease inhibitors</td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 500 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, protease inhibitors + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.06% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM HEPES pH 7.5, 500 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Anti-FLAG <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-FLAG M1 resin</td>
      <td>0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM HEPES pH 7.5, 300 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM CaCl2</td>
      <td>Supplemented Ni-NTA eluent with 2 mM CaCl2 before loading</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6csn">6CSN</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">LFQTSYTLENQGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWISFALSALCLMFYG</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-unknown">QTWKS</span><span class="topo-inside">TCGWE</span><span class="topo-membrane">NIYVATIQMIKFIIEYF</span><span class="topo-outside">HSFDEPAVIYSSNGNKT</span><span class="topo-membrane">RWLRYASWLLTCPVI</span></span>
<span class="topo-line"><span class="topo-membrane">L</span><span class="topo-inside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAALS</span><span class="topo-outside">KGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFF</span><span class="topo-inside">N</span></span>
<span class="topo-line"><span class="topo-inside">AAKVYIEAYHTVPKGRCRQVVTGMAW</span><span class="topo-membrane">LFFVSWGMFPILFILG</span><span class="topo-outside">PEGFGVLSRYG</span><span class="topo-membrane">SNVGHTI</span></span>
<span class="topo-line"><span class="topo-membrane">IDLMSKQCWGL</span><span class="topo-inside">LGHYLRVLIHSHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-inside">IEVETLVEDE</span></span>
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
      <td>40</td>
      <td>51</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>61</td>
      <td>111</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>71</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>88</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>105</td>
      <td>139</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>156</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>140</td>
      <td>172</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>158</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>161</td>
      <td>209</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>179</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>206</td>
      <td>230</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>222</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>233</td>
      <td>273</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>251</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>276</td>
      <td>302</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>292</td>
      <td>333</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6csn">6CSN</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">LFQTSYTLENQGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWISFALSALCLMFYG</span></span>
<span class="topo-line"><span class="topo-inside">Y</span><span class="topo-unknown">QTWKS</span><span class="topo-inside">TCGWE</span><span class="topo-membrane">NIYVATIQMIKFIIEYF</span><span class="topo-outside">HSFDEPAVIYSSNGNKT</span><span class="topo-membrane">RWLRYASWLLTCPVI</span></span>
<span class="topo-line"><span class="topo-membrane">L</span><span class="topo-inside">IHLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAALS</span><span class="topo-outside">KGY</span><span class="topo-membrane">VRVIFFLMGLCYGIYTFF</span><span class="topo-inside">N</span></span>
<span class="topo-line"><span class="topo-inside">AAKVYIEAYHTVPKGRCRQVVTGMAW</span><span class="topo-membrane">LFFVSWGMFPILFILG</span><span class="topo-outside">PEGFGVLSRYG</span><span class="topo-membrane">SNVGHTI</span></span>
<span class="topo-line"><span class="topo-membrane">IDLMSKQCWGL</span><span class="topo-inside">LGHYLRVLIHSHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-inside">IEVETLVEDE</span></span>
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
      <td>40</td>
      <td>51</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>61</td>
      <td>111</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>71</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>88</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>105</td>
      <td>139</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>156</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>140</td>
      <td>172</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>158</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>161</td>
      <td>209</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>179</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>206</td>
      <td>230</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>222</td>
      <td>257</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>233</td>
      <td>273</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>251</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>276</td>
      <td>302</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>292</td>
      <td>333</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6cso">6CSO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYGGALSA</span><span class="topo-outside">VGLFQTSYTLENQGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWISF</span></span>
<span class="topo-line"><span class="topo-membrane">ALSALCLMFYG</span><span class="topo-unknown">YQTWKS</span><span class="topo-inside">TCGWE</span><span class="topo-membrane">NIYVATIQMIKFIIEYF</span><span class="topo-outside">HSFDEPAVIYSSNGNKT</span><span class="topo-membrane">RWLR</span></span>
<span class="topo-line"><span class="topo-membrane">YASWLLTCPVILI</span><span class="topo-inside">HLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAALS</span><span class="topo-outside">KGY</span><span class="topo-membrane">VRVIFFLM</span></span>
<span class="topo-line"><span class="topo-membrane">GLCYGIYTFF</span><span class="topo-inside">NAAKVYIEAYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-outside">PEGFGVL</span></span>
<span class="topo-line"><span class="topo-outside">SRYG</span><span class="topo-membrane">SNVGHTIIDLMSKQCWGL</span><span class="topo-inside">LGHYLRVLIHSHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-inside">IEVETLV</span></span>
<span class="topo-line"><span class="topo-inside">EDE</span><span class="topo-unknown">AEAGAV</span></span>
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
      <td>10</td>
      <td>51</td>
      <td>49</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>82</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>99</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>139</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>151</td>
      <td>173</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>209</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>230</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>273</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>287</td>
      <td>302</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>303</td>
      <td>333</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6cso">6CSO</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MDYGGALSA</span><span class="topo-outside">VGLFQTSYTLENQGSVICIPNNGQCFCLAWLKSNGTNAEKLA</span><span class="topo-membrane">ANILQWISF</span></span>
<span class="topo-line"><span class="topo-membrane">ALSALCLMFYG</span><span class="topo-unknown">YQTWKS</span><span class="topo-inside">TCGWE</span><span class="topo-membrane">NIYVATIQMIKFIIEYF</span><span class="topo-outside">HSFDEPAVIYSSNGNKT</span><span class="topo-membrane">RWLR</span></span>
<span class="topo-line"><span class="topo-membrane">YASWLLTCPVILI</span><span class="topo-inside">HLSNLTGLANDYNKRTMG</span><span class="topo-membrane">LLVSDIGTIVWGTTAALS</span><span class="topo-outside">KGY</span><span class="topo-membrane">VRVIFFLM</span></span>
<span class="topo-line"><span class="topo-membrane">GLCYGIYTFF</span><span class="topo-inside">NAAKVYIEAYHTVPKGRCRQVVTGM</span><span class="topo-membrane">AWLFFVSWGMFPILFILG</span><span class="topo-outside">PEGFGVL</span></span>
<span class="topo-line"><span class="topo-outside">SRYG</span><span class="topo-membrane">SNVGHTIIDLMSKQCWGL</span><span class="topo-inside">LGHYLRVLIHSHILIHGDIRKTTKL</span><span class="topo-unknown">NIGGTE</span><span class="topo-inside">IEVETLV</span></span>
<span class="topo-line"><span class="topo-inside">EDE</span><span class="topo-unknown">AEAGAV</span></span>
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
      <td>10</td>
      <td>51</td>
      <td>49</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>91</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>82</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>99</td>
      <td>122</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>139</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>156</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>151</td>
      <td>173</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>172</td>
      <td>209</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>212</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>230</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>233</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>273</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>262</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>287</td>
      <td>302</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>303</td>
      <td>333</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Structural basis of anion selectivity

Both iC++ and [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) structures revealed that anion selectivity is governed by pore-surface electrostatics rather than specific residue interactions. Positively charged residues lining the extracellular and intracellular surfaces create an electropositive pore that favors anion conduction. Reverse engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) to conduct cations confirmed this model.

### pH-dependent chromophore occupancy

iC++ exhibited reduced all-trans-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) occupancy at alkaline pH (8.5) compared to pH 6.5. The Schiff base is deprotonated and ATR is hydrolyzed at pH values above 7.5, consistent with reduced dACR activity at alkaline pH. The E129Q and E162S mutations destabilize the Schiff base, enabling ATR hydrolysis.

### Extracellular constriction sites

Two extracellular vestibules (EV1 and EV2) with constriction sites (ECS1 and ECS2) regulate ion access to the central pore. In iC++, the E140S mutation breaks a hydrogen bond with Gln95, allowing EV1 to extend to the central constriction site (CCS), while EV2 is occluded at ECS2 by Arg156-Arg281 interactions.

### Design of FLASH (fast light-activated anion-selective rhodopsin)

Structure-guided engineering of [GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/) produced FLASH ([GtACR1 Anion Channelrhodopsin from Guillardia theta](/xray-mp-wiki/proteins/rhodopsins/gtacr1/)(R83Q/N239Q)), which combines large photocurrents with fast kinetics for optogenetic single-spike inhibition. FLASH showed more efficient net inhibition of spontaneous spiking than ZipACR in vivo in mouse hippocampus and thalamus.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — iC++ is derived from C1C2 via 10 structure-guided mutations
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/">Channelrhodopsin Photocycle</a> — iC++ photocycle includes K, M, and O intermediates
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/rhodopsins/gtacr1/">GtACR1 Anion Channelrhodopsin from Guillardia theta</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> — Buffer component in purification or crystallization
