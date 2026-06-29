---
title: "SagB-SpdC Complex"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41564-020-00808-5]
verified: false
---

# SagB-SpdC Complex

## Overview

The SagB-SpdC complex from Staphylococcus aureus is a membrane protein complex that functions as a peptidoglycan release factor during cell wall assembly. SagB is a membrane-anchored glucosaminidase (N-acetylglucosaminidase) that cleaves nascent peptidoglycan strands, while SpdC is an eight-transmembrane-helix protein similar to eukaryotic CAAX proteases that scaffolds SagB and regulates its cleavage activity. The crystal structure of the complex was determined at 2.6 A resolution (PDB: 6U0O) using the lipidic cubic phase (LCP) method, revealing that SpdC scaffolds SagB through its single transmembrane helix and orients the hydrolase active site at the membrane interface.


## Publications

### doi/10.1038##s41564-020-00808-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u0o">6U0O</a></td>
      <td>2.6</td>
      <td>C2</td>
      <td>Full-length SagB with SpdC residues 1-256 (truncated C-terminal domain)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: SagB-His6 and Flag-SpdC co-expressed from pDUET vector; Ulp1 protease co-expressed for SUMO tag removal
- **Notes**: Co-expression system with arabinose-inducible Ulp1 protease for Flag-SpdC

**Purification:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Expression construct**: SagB-His6 + Flag-SpdC (co-expression)
- **Tag info**: His6 tag on SagB, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) on SpdC

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
      <td>Fermentation</td>
      <td>—</td>
      <td></td>
      <td>Grown at 30°C to A600=0.6, shifted to 24°C, induced at A600=1.1 with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> and 0.2% arabinose for 16 h</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Differential centrifugation</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl</td>
      <td>Cells lysed by microfluidizer; membranes collected by ultracentrifugation at 100,000g</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% n-dodecyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes rocked at 4°C for 1 h</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 10 mM and 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elute with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 2 mM CaCl2</td>
    </tr>
    <tr>
      <td>Anti-Flag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>M1 anti-Flag resin</td>
      <td>50 mM HEPES pH 7.5, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM CaCl2 + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 20 mM HEPES pH 7.5, 500 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Sephadex S200 Increase 10/300 GL</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: 35-40 mg/mL SagB-SpdC complex in crystallization buffer
**Yield**: Not reported
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>LCP</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SagB-SpdC complex at 35-40 mg/mL</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-7 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Most crystals appeared within 36 h; complete in 3-7 days. Crystals flash-frozen in liquid nitrogen without additional cryoprotectant.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u0o">6U0O</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDLEVLFQGPGGSSTEYMKNNK</span><span class="topo-outside">ISGFQWAMT</span><span class="topo-membrane">IFVFFVITMALSIMLR</span><span class="topo-inside">DFQSIIGV</span></span>
<span class="topo-line"><span class="topo-inside">KHFIF</span><span class="topo-membrane">EVTDLAPLIAAIIC</span><span class="topo-outside">ILVFKYKKVQLAGLKFSISLKV</span><span class="topo-membrane">IERLLLALILPLIILII</span><span class="topo-inside">GM</span></span>
<span class="topo-line"><span class="topo-inside">YSFNTFADSFILLQSTGLSVPITHIL</span><span class="topo-membrane">IGHILMAFVVEFGFRSYLQ</span><span class="topo-outside">NIVETKMNT</span><span class="topo-membrane">FFASIV</span></span>
<span class="topo-line"><span class="topo-membrane">VGLMYSVFSA</span><span class="topo-inside">NTTYGTEFAA</span><span class="topo-membrane">YNFLYTFSFSMILGELIR</span><span class="topo-outside">ATKGRT</span><span class="topo-membrane">IYIATTFHASMTFG</span><span class="topo-inside">LI</span></span>
<span class="topo-line"><span class="topo-inside">FLFSEEIGDLFSIKVI</span><span class="topo-membrane">AISTAIVAVGYIGLSLI</span><span class="topo-outside">IR</span><span class="topo-unknown">GIA</span></span>
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
      <td>28</td>
      <td>36</td>
      <td>6</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>15</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>65</td>
      <td>31</td>
      <td>43</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>79</td>
      <td>44</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>58</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>80</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>97</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>165</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>174</td>
      <td>144</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>190</td>
      <td>153</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>200</td>
      <td>169</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>218</td>
      <td>179</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>224</td>
      <td>197</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>238</td>
      <td>203</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>256</td>
      <td>217</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>273</td>
      <td>235</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>275</td>
      <td>252</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6u0o">6U0O</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MNKHK</span><span class="topo-outside">KGSIFG</span><span class="topo-membrane">IIGLVVIFAVVSFLF</span><span class="topo-inside">FSMISDQIFFKHVKSDIKIEKLNVTLNDAAKKQI</span></span>
<span class="topo-line"><span class="topo-inside">NNYTSQQVSNKKNDAWRDASATEIKSAMDSGTFIDNEKQKYQFLDLSKYQGIDKNRIKRM</span></span>
<span class="topo-line"><span class="topo-inside">LVDRPTLLKHTDDFLKAAKDKHVNEVYLISHALLETGAVKSELANGVEIDGKKYYNFYGV</span></span>
<span class="topo-line"><span class="topo-inside">GALDKDPIKTGAEYAKKHGWDTPEKAISGGADFIHKHFLSSTDQNTLYSMRWNPKNPGEH</span></span>
<span class="topo-line"><span class="topo-inside">QYATDIKWAESNATIIADFYKNMKTEGKYFKYFVYKDDSKHLNKKLAAALEHH</span><span class="topo-unknown">HHHH</span></span>
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
      <td>6</td>
      <td>11</td>
      <td>6</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>293</td>
      <td>27</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Peptidoglycan release mechanism

The SagB-SpdC complex cleaves nascent peptidoglycan strands internally to produce free oligomers as well as lipid-linked oligomers that can undergo further elongation. The cleavage products retain a diphospholipid anchor at the reducing end, consistent with glucosaminidase cleavage leaving a terminal N-acetylmuramic acid. This complex meets the criteria for a peptidoglycan release factor, detaching newly synthesized peptidoglycan from the cell membrane for integration into the cell wall matrix.

### SpdC as a non-catalytic scaffold

SpdC functions primarily as a scaffolding protein rather than an active enzyme. Despite its similarity to eukaryotic CAAX proteases, SpdC lacks conserved catalytic residues required for proteolytic activity. The SagB catalytic glutamate (Glu155) is essential for cleavage activity, while conserved CAAX protease residues in SpdC (E135, R139, H210) are dispensable. SpdC controls the length of cleavage products through its scaffolding function.

### Structural basis of complex formation

The 2.6 A crystal structure shows SpdC as an eight-transmembrane-helix protein that scaffolds SagB through its single transmembrane helix and a juxtamembrane interface. The transmembrane domain of SpdC has similar topology to the eukaryotic CAAX protease Rce1, but the helices differ in length and loop conformations. The SagB-SpdC interface is crucial for complex formation - the SagB TM helix makes close contacts with SpdC TM3, and removing the TM helix or swapping it with the SagA TM helix disrupts complex formation.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
