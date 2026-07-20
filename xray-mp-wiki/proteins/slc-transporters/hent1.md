---
title: "Human Equilibrative Nucleoside Transporter 1 (hENT1)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-019-0245-7]
verified: agent
uniprot_id: Q99808
---

# Human Equilibrative Nucleoside Transporter 1 (hENT1)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q99808">UniProt: Q99808</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

hENT1 (SLC29A1) is the founding member of the SLC29 family of equilibrative nucleoside transporters. It mediates the energy-independent facilitative diffusion of adenosine and other nucleosides across cellular membranes, playing crucial roles in adenosine signaling, nucleoside salvage for DNA/RNA synthesis, and cellular uptake of nucleoside-derived anticancer and antiviral drugs. hENT1 is the target of adenosine reuptake inhibitors (AdoRIs), clinically used as vasodilators and antithrombotic agents. The crystal structures of hENT1 in complex with [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) and [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) revealed an 11-TM helix architecture with a pseudo-symmetric 6+5 topology distinct from the canonical 12-TM [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) fold, representing the first experimental structures of any SLC29 family member.


## Publications

### doi/10.1038##s41594-019-0245-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ob7">6OB7</a></td>
      <td>2.3 A</td>
      <td>P3_221</td>
      <td>hENT1_cryst (mutations L168F, P175A, N288K, loop <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> Delta243-274)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/dilazep/">Dilazep</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ob6">6OB6</a></td>
      <td>2.9 A</td>
      <td>P6_1</td>
      <td>hENT1_cryst (mutations L168F, P175A, N288K, loop <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> Delta243-274)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/nbmpr/">NBMPR</a> (S-(4-Nitrobenzyl)-6-thioinosine)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI-/- cells, BacMam viral transduction
- **Construct**: Codon-optimized hENT1_cryst with C-terminal GFP-FLAG-His10 tag in [PEG](/xray-mp-wiki/reagents/additives/peg/) BacMam vector. hENT1_cryst contains mutations L168F, P175A, N288K and TM6-7 loop [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) Delta243-274. Cleavable by Precission Protease.

- **Notes**: Cells harvested 72 h post-infection
- **Induction**: 10 mM [Sodium Butyrate](/xray-mp-wiki/reagents/additives/sodium-butyrate/) + 10 uM [Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) (for dilazep-bound) at 24 h post-infection

**Purification:**

- **Expression system**: HEK293S GnTI-/- cells
- **Expression construct**: hENT1_cryst-GFP-FLAG-His10
- **Tag info**: FLAG-His10 tag, cleaved by Precission Protease

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
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.5 mM TCEP + 40 mM n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>1 hour solubilization, followed by centrifugation at 16,000 rpm for 25 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M2 affinity</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M2 affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.5 mM TCEP, 1.0 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1.0 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>High salt wash (500 mM NaCl) then low salt wash, elution with 0.2 mg/mL <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide. 10 uM <a href="/xray-mp-wiki/reagents/ligands/dilazep/">Dilazep</a> or <a href="/xray-mp-wiki/reagents/ligands/nbmpr/">NBMPR</a> included throughout.</td>
    </tr>
    <tr>
      <td>Tag cleavage and deglycosylation</td>
      <td>Protease treatment</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5 mM TCEP + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>1:10 Precission Protease and 1:10 <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a> for 2 hours at 0.75 mg/mL</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5 mM TCEP + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>10 uM <a href="/xray-mp-wiki/reagents/ligands/dilazep/">Dilazep</a> or 1.0 uM <a href="/xray-mp-wiki/reagents/ligands/nbmpr/">NBMPR</a> included in gel filtration buffer. For apo (proteoliposome), 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> used in final step.</td>
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
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40:60 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-5 days (<a href="/xray-mp-wiki/reagents/ligands/dilazep/">Dilazep</a>); 7 days (<a href="/xray-mp-wiki/reagents/ligands/nbmpr/">NBMPR</a>)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Directly cooled in LN2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Dilazep-bound: Concentrated to 40 mg/mL, mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> 40:60. Reservoir: 35-50% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.0, 0.5 M NaCl. Plate-like crystals 50x20 um appeared after 12 h. For <a href="/xray-mp-wiki/reagents/ligands/nbmpr/">NBMPR</a>: Reservoir 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 500 MME, 0.1 M MgCl2, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ob7">6OB7</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MATTSHQ</span><span class="topo-inside">PQDRYKAVW</span><span class="topo-membrane">LIFFMLGLGTLLPWNFFM</span><span class="topo-outside">TATQYFTNRLDMSQN</span><span class="topo-unknown">VSLVTAELSKDAQASAAPAAPLPER</span><span class="topo-outside">NSLSAIFNNVMT</span><span class="topo-membrane">LCAMLPLLLFTYLNSFLH</span><span class="topo-inside">QRIPQ</span><span class="topo-membrane">SVRILGSLVAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLVFLI</span><span class="topo-outside">TAILVKVQLDALPFFVITMI</span><span class="topo-membrane">KIVLINSFGAILQGSLFG</span><span class="topo-inside">LAGLFPASY</span><span class="topo-membrane">TAAIMSGQGLAGFFASV</span><span class="topo-outside">AMICAIASGSELSESAFGY</span><span class="topo-membrane">FITACAVIILTIICYLG</span><span class="topo-inside">LPRLEFYRYYQQLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-unknown">EGPTNESH</span><span class="topo-inside">SIKAILKKIS</span><span class="topo-membrane">VLAFSVCFIFTITIGMFP</span><span class="topo-outside">AVTVEVKSSIAGSSTWERYFIPVSCF</span><span class="topo-membrane">LTFNIFDWLGRSLTAVFMWP</span><span class="topo-inside">GKDSR</span><span class="topo-membrane">WLPSLVLARLVFVPLL</span><span class="topo-outside">LLCNIKPRRYLTVVFE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440  </span>
<span class="topo-line"><span class="topo-outside">HDAWFI</span><span class="topo-membrane">FFMAAFAFSNGYLASLCMC</span><span class="topo-inside">FGPKKVKPAEAETAG</span><span class="topo-membrane">AIMAFFLCLGLALGAVFS</span><span class="topo-outside">FLF</span><span class="topo-unknown">RAIVGTELLQVDTNSLEVLFQ</span></span>
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
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>7</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>34</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>49</td>
      <td>34</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>74</td>
      <td>49</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>74</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>86</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>109</td>
      <td>104</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>126</td>
      <td>109</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>146</td>
      <td>126</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>164</td>
      <td>146</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>173</td>
      <td>164</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>190</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>209</td>
      <td>190</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>226</td>
      <td>209</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>241</td>
      <td>226</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>249</td>
      <td>241</td>
      <td>248</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>250</td>
      <td>259</td>
      <td>281</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>277</td>
      <td>291</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>303</td>
      <td>309</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>323</td>
      <td>335</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>328</td>
      <td>355</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>344</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>366</td>
      <td>376</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>385</td>
      <td>398</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>400</td>
      <td>417</td>
      <td>431</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>418</td>
      <td>432</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>421</td>
      <td>450</td>
      <td>452</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>442</td>
      <td>453</td>
      <td>473</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ob6">6OB6</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MATTSHQ</span><span class="topo-outside">PQDRY</span><span class="topo-membrane">KAVWLIFFMLGLGTLLPWNFFMTAT</span><span class="topo-inside">QYFTNRLDM</span><span class="topo-unknown">SQNVSLVTAELSKDAQASAAPAAPLPER</span><span class="topo-inside">NSLSAI</span><span class="topo-membrane">FNNVMTLCAMLPLLLFTYLNSFLH</span><span class="topo-outside">QRIPQ</span><span class="topo-membrane">SVRILGSLVAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLVFLITAILVKV</span><span class="topo-inside">QLDALP</span><span class="topo-membrane">FFVITMIKIVLINSFGAILQGSLFGLA</span><span class="topo-outside">GLFPA</span><span class="topo-membrane">SYTAAIMSGQGLAGFFASVAMICA</span><span class="topo-inside">IASGSELSES</span><span class="topo-membrane">AFGYFITACAVIILTIICYLGL</span><span class="topo-outside">PRLEFYRYYQQ</span><span class="topo-unknown">LK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">LEGPTNESH</span><span class="topo-outside">SIKAILKKIS</span><span class="topo-membrane">VLAFSVCFIFTITIGMFPAVTV</span><span class="topo-inside">EVKSS</span><span class="topo-unknown">IAGSSTWE</span><span class="topo-inside">RYFIP</span><span class="topo-membrane">VSCFLTFNIFDWLGRSLTAVFMWPG</span><span class="topo-outside">KDS</span><span class="topo-membrane">RWLPSLVLARLVFVPLLLLC</span><span class="topo-inside">NIKPRRYLTVVFE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440  </span>
<span class="topo-line"><span class="topo-inside">HD</span><span class="topo-membrane">AWFIFFMAAFAFSNGYLASLCMCFG</span><span class="topo-outside">PKKVKPAEAETAG</span><span class="topo-membrane">AIMAFFLCLGLALGAVFSF</span><span class="topo-unknown">LFRAIVGTELLQVDTNSLEVLFQ</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>7</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>37</td>
      <td>12</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>46</td>
      <td>37</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>74</td>
      <td>46</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>75</td>
      <td>80</td>
      <td>74</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>104</td>
      <td>80</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>109</td>
      <td>104</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>133</td>
      <td>109</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>139</td>
      <td>133</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>166</td>
      <td>139</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>171</td>
      <td>166</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>195</td>
      <td>171</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>205</td>
      <td>195</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>227</td>
      <td>205</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>238</td>
      <td>227</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>249</td>
      <td>238</td>
      <td>248</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>250</td>
      <td>259</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>291</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>286</td>
      <td>313</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>294</td>
      <td>318</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>295</td>
      <td>299</td>
      <td>326</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>324</td>
      <td>331</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>327</td>
      <td>356</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>347</td>
      <td>359</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>362</td>
      <td>379</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>387</td>
      <td>394</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>400</td>
      <td>419</td>
      <td>431</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>419</td>
      <td>432</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>420</td>
      <td>442</td>
      <td>451</td>
      <td>473</td>
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

### SLC29 family architecture

hENT1 is composed of 11 transmembrane helices with a pseudo-symmetric 6+5 topology, distinct from the canonical 12-TM [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) fold. The N-domain (TM1-TM6) and C-domain (TM7-TM11) form the central cavity accessible from the extracellular side. An extracellular thin gate (Met33-Pro308) and intracellular thick gate (including Arg111-Glu428 salt bridge) define the outward-facing conformation.

### Adenosine reuptake inhibitor mechanisms

[Dilazep](/xray-mp-wiki/reagents/ligands/dilazep/) occupies the orthosteric site and an opportunistic site 1 at the extracellular thin gate, sterically preventing gate closure and locking the transporter in an outward-facing state. [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/), an adenosine analog, occupies the orthosteric site and an opportunistic site 2 (a deep hydrophobic pocket in the N-domain), allowing thin gate closure but preventing domain reorientation. Gly154 in opportunistic site 2 is a key determinant of [NBMPR](/xray-mp-wiki/reagents/ligands/nbmpr/) isoform specificity.

### Nucleoside recognition

Adenosine recognition by hENT1 involves conserved charged residues Arg345 and Asp341 for ribose coordination, Gln158 for nucleobase recognition (N-1/N-3 coordination), and hydrophobic contacts (Leu26, Met89, Leu92, Leu442) surrounding the purine moiety. Leu442Ile mutation converts nucleoside preference from adenosine to uridine.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/slc29-family/">SLC29 Family of Nucleoside Transporters</a> — hENT1 is the founding member of the SLC29 family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — hENT1 utilizes rocker-switch-like reorientation for transport
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Primary solubilization and purification detergent
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used to crystallize hENT1
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/endoh/">ENDOH</a> — Additive used in purification or crystallization buffers
