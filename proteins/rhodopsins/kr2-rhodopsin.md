---
title: "Krokinobacter eikastus Rhodopsin 2 (KR2) — Light-Driven Sodium Pump"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, transporter, membrane-protein]
sources: [doi/10.1038##s41586-020-2307-8]
verified: false
---

# Krokinobacter eikastus Rhodopsin 2 (KR2) — Light-Driven Sodium Pump

## Overview

Krokinobacter eikastus rhodopsin 2 (KR2) is a prototypical light-driven sodium pump from marine bacteria that actively transports small cations across cellular membranes. It converts light into membrane potential and has become a valuable optogenetic tool for neuronal inhibition. Using time-resolved serial femtosecond crystallography (TR-SFX) at SwissFEL, structural snapshots spanning from femtoseconds to milliseconds (10 time delays: 800 fs to 20 ms) were collected at up to 1.6 Å resolution, revealing how retinal isomerization drives sodium translocation against a concentration gradient. Resting state structures were determined at both acidic pH (PDB 6TK7) and neutral pH (PDB 6TK6). Five intermediate structures at combined time delays (800 fs+2 ps — 6TK5; 1 ns+16 ns — 6TK4; 30 µs+150 µs — 6TK3; 1 ms — 6TK2; 20 ms — 6TK1) show the stepwise mechanism: retinal isomerization within femtoseconds, structural rearrangements via V117 in helix C at microseconds, transient sodium binding between N112 and D251 at 1 ms, and a second sodium-binding site near E11/N106/E160 at 20 ms on the extracellular side.

## Publications

### doi/10.1038##s41586-020-2307-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk7">6TK7</a></td>
      <td>1.60</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>All-trans retinal, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk6">6TK6</a></td>
      <td>1.60</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>All-trans retinal, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk5">6TK5</a></td>
      <td>2.25</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>13-cis retinal, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk4">6TK4</a></td>
      <td>2.25</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>13-cis retinal, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk3">6TK3</a></td>
      <td>2.25</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>13-cis retinal, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk2">6TK2</a></td>
      <td>2.50</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>13-cis retinal, sodium (transient binding site near N112/D251)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tk1">6TK1</a></td>
      <td>2.50</td>
      <td>I4</td>
      <td>Full-length KR2 with C-terminal 6×His tag (TEV-cleavable)</td>
      <td>13-cis retinal, sodium (second binding site near E11/N106/E160)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: C41(DE3) Escherichia coli cells (pStaby1.2 vector)
- **Construct**: Full-length KR2 gene with TEV-cleavable C-terminal 6×His tag; expression with 10 µM all-trans retinal at 37°C overnight

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
      <td>Homogenization and <a href="/xray-mp-wiki/methods/purification/ultracentrifugation">ultracentrifugation</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">glycerol</a>, 0.5% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a>, DNase I</td>
      <td>Cells disrupted at 15,000 psi; membranes collected at 90,000g</td>
    </tr>
    <tr>
      <td>2. Membrane solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 300 mM NaCl, 1.0% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% CHS</td>
      <td>Overnight stirring at 4°C</td>
    </tr>
    <tr>
      <td>3. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 150 mM NaCl, 100-500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.04% CHS</td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a> step gradient</td>
    </tr>
    <tr>
      <td>4. <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> cleavage and dialysis</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> + dialysis</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.04% CHS</td>
      <td>Overnight dialysis in 8 kDa MWCO membrane</td>
    </tr>
    <tr>
      <td>5. Reverse IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> flow-through</td>
      <td>—</td>
      <td></td>
      <td>Cleaved His tag removed; flow-through collected</td>
    </tr>
    <tr>
      <td>6. <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>HiLoad Superdex 75 prep grade 16/600</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.04% CHS</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified KR2 in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> pH 8.0, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.04% CHS</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C (overnight in dark)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> formed with <a href="/xray-mp-wiki/reagents/lipids/monoolein">monoolein</a> at 4:7 v/v (protein:lipid). Blue plate-like crystals 10-30 × 10-25 × 1-3 µm³. Crystals treated by washing with 150 mM NaCl, 35% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 200 for neutral pH experiments. TR-<a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">SFX</a> data collected at SwissFEL; 158,832 dark and 496,904 light patterns analyzed. Data processed with CrystFEL, structures refined in PHENIX.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk7">6TK7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">TQELGNANFENFIGATEGFSEIAYQF</span><span class="topo-membrane">TSHILTLGYAVMLAGLLYFILTIK</span><span class="topo-outside">NVDKKFQ</span><span class="topo-membrane">MSNILSAVVMVSAFLLLYAQAQ</span><span class="topo-inside">NWTSSFTFNEEVGRYFLDPSGDLFNN</span><span class="topo-membrane">GYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFV</span><span class="topo-outside">VSLTTSKF</span><span class="topo-membrane">SSVRNQFWFSGAMMIITGYIGQ</span><span class="topo-inside">FYEVSNLTA</span><span class="topo-membrane">FLVWGAISSAFFFHILWVMKKVIN</span><span class="topo-outside">EGKEGISPAGQK</span><span class="topo-membrane">ILSNIWILFLISWTLYPGAYLM</span><span class="topo-inside">PYLTGVDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">ARQLVYTIADVSSKVIYGVLLGNL</span><span class="topo-outside">AITLSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>2</td>
      <td>27</td>
      <td>2</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>51</td>
      <td>28</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>58</td>
      <td>52</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>59</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>106</td>
      <td>81</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>127</td>
      <td>107</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>135</td>
      <td>128</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>166</td>
      <td>158</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>190</td>
      <td>167</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>202</td>
      <td>191</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>224</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>241</td>
      <td>225</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>265</td>
      <td>242</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>272</td>
      <td>266</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk6">6TK6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSHI</span><span class="topo-membrane">LTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKF</span><span class="topo-membrane">QMSNILSAVVMVSAFLLLYAQA</span><span class="topo-inside">QNWTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFV</span><span class="topo-outside">VSLTTSKFSSV</span><span class="topo-membrane">RNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSN</span><span class="topo-membrane">LTAFLVWGAISSAFFFHILWVMKKVIN</span><span class="topo-outside">EGKEGISPA</span><span class="topo-membrane">GQKILSNIWILFLISWTLYPGAYLM</span><span class="topo-inside">PYLTGVDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">MAR</span><span class="topo-membrane">QLVYTIADVSSKVIYGVLLGNLAIT</span><span class="topo-outside">LSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>31</td>
      <td>8</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>54</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>58</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>80</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>127</td>
      <td>106</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>138</td>
      <td>128</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>160</td>
      <td>139</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>161</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>190</td>
      <td>164</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>199</td>
      <td>191</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>224</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>268</td>
      <td>244</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>269</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk5">6TK5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSHI</span><span class="topo-membrane">LTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKF</span><span class="topo-membrane">QMSNILSAVVMVSAFLLLYAQA</span><span class="topo-inside">QNWTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFVV</span><span class="topo-outside">SLTTSKFSSV</span><span class="topo-membrane">RNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSN</span><span class="topo-membrane">LTAFLVWGAISSAFFFHILWVMKKVIN</span><span class="topo-outside">EGKEGISP</span><span class="topo-membrane">AGQKILSNIWILFLISWTLYPGAYLM</span><span class="topo-inside">PYLTGVDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">MAR</span><span class="topo-membrane">QLVYTIADVSSKVIYGVLLGNLAIT</span><span class="topo-outside">LSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>31</td>
      <td>8</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>54</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>58</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>80</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>128</td>
      <td>106</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>138</td>
      <td>129</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>160</td>
      <td>139</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>161</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>190</td>
      <td>164</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>198</td>
      <td>191</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>224</td>
      <td>199</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>268</td>
      <td>244</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>269</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk4">6TK4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSHI</span><span class="topo-membrane">LTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKF</span><span class="topo-membrane">QMSNILSAVVMVSAFLLLYAQA</span><span class="topo-inside">QNWTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFV</span><span class="topo-outside">VSLTTSKFSSV</span><span class="topo-membrane">RNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSN</span><span class="topo-membrane">LTAFLVWGAISSAFFFHILWVMKKVI</span><span class="topo-outside">NEGKEGISPAGQK</span><span class="topo-membrane">ILSNIWILFLISWTLYPGAYLMPYLTG</span><span class="topo-inside">VDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">MA</span><span class="topo-membrane">RQLVYTIADVSSKVIYGVLLGNLAI</span><span class="topo-outside">TLSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>31</td>
      <td>8</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>54</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>58</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>80</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>127</td>
      <td>106</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>138</td>
      <td>128</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>160</td>
      <td>139</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>161</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>189</td>
      <td>164</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>202</td>
      <td>190</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>229</td>
      <td>203</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>242</td>
      <td>230</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>267</td>
      <td>243</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>272</td>
      <td>268</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk3">6TK3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSH</span><span class="topo-membrane">ILTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKFQ</span><span class="topo-membrane">MSNILSAVVMVSAFLLLYAQAQN</span><span class="topo-inside">WTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILF</span><span class="topo-outside">VVSLTTSKFSS</span><span class="topo-membrane">VRNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSN</span><span class="topo-membrane">LTAFLVWGAISSAFFFHILWVMKKVI</span><span class="topo-outside">NEGKEGISPAGQK</span><span class="topo-membrane">ILSNIWILFLISWTLYPGAYLMPYLTG</span><span class="topo-inside">VDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-membrane">ARQLVYTIADVSSKVIYGVLLGNLA</span><span class="topo-outside">ITLSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>30</td>
      <td>8</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>31</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>58</td>
      <td>54</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>81</td>
      <td>59</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>126</td>
      <td>106</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>137</td>
      <td>127</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>160</td>
      <td>138</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>161</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>189</td>
      <td>164</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>202</td>
      <td>190</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>229</td>
      <td>203</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>241</td>
      <td>230</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>242</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>272</td>
      <td>267</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk2">6TK2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSH</span><span class="topo-membrane">ILTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKF</span><span class="topo-membrane">QMSNILSAVVMVSAFLLLYAQA</span><span class="topo-inside">QNWTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFV</span><span class="topo-outside">VSLTTSKFS</span><span class="topo-membrane">SVRNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSNL</span><span class="topo-membrane">TAFLVWGAISSAFFFHILWVMKKVI</span><span class="topo-outside">NEGKEGISPAGQK</span><span class="topo-membrane">ILSNIWILFLISWTLYPGAYLMPYLT</span><span class="topo-inside">GVDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">MA</span><span class="topo-membrane">RQLVYTIADVSSKVIYGVLLGNLAI</span><span class="topo-outside">TLSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>30</td>
      <td>8</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>31</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>54</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>58</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>80</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>127</td>
      <td>106</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>136</td>
      <td>128</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>160</td>
      <td>137</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>164</td>
      <td>161</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>202</td>
      <td>190</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>228</td>
      <td>203</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>242</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>267</td>
      <td>243</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>272</td>
      <td>268</td>
      <td>272</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tk1">6TK1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTQELGN</span><span class="topo-inside">ANFENFIGATEGFSEIAYQFTSH</span><span class="topo-membrane">ILTLGYAVMLAGLLYFILTIKNV</span><span class="topo-outside">DKKF</span><span class="topo-membrane">QMSNILSAVVMVSAFLLLYAQAQN</span><span class="topo-inside">WTSSFTFNEEVGRYFLDPSGDLFN</span><span class="topo-membrane">NGYRYLNWLIDVPML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFQILFV</span><span class="topo-outside">VSLTTSKFSS</span><span class="topo-membrane">VRNQFWFSGAMMIITGYIGQFYE</span><span class="topo-inside">VSNL</span><span class="topo-membrane">TAFLVWGAISSAFFFHILWVMKKVIN</span><span class="topo-outside">EGKEGISPA</span><span class="topo-membrane">GQKILSNIWILFLISWTLYPGAYLM</span><span class="topo-inside">PYLTGVDGFLYSEDGV</span></span>
<span class="topo-ruler">       250       260       270       280       290</span>
<span class="topo-line"><span class="topo-inside">MA</span><span class="topo-membrane">RQLVYTIADVSSKVIYGVLLGNLAIT</span><span class="topo-outside">LSKN</span><span class="topo-unknown">KELENLYFQSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>30</td>
      <td>8</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>31</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>54</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>81</td>
      <td>58</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>105</td>
      <td>82</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>127</td>
      <td>106</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>137</td>
      <td>128</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>160</td>
      <td>138</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>164</td>
      <td>161</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>165</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>199</td>
      <td>191</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>224</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>242</td>
      <td>225</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>243</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>269</td>
      <td>272</td>
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

### Retinal isomerization drives the photocycle

Retinal isomerization from all-trans to 13-cis is completed within femtoseconds. The isomerized retinal in KR2 points in the opposite direction compared to bacteriorhodopsin (bR): the C20 methyl group tilts towards helix C (via V117) instead of helix G (via W182 in bR). This early event translates light energy into structural changes in the protein.

### Electrostatic gating mechanism for unidirectional sodium transport

After retinal Schiff base (SB) deprotonation in the M intermediate, an electrostatic gate opens in microseconds. The proton transfer from SB to counterion D116 creates a transient sodium-binding site. At 1 ms, sodium binds between N112 and D251 (confirmed by QM/MM calculations showing the sodium ion produces a 55-66 nm red shift matching the O intermediate absorption). At 20 ms, a second sodium-binding site appears between E11, N106, and E160 near the extracellular exit. Reprotonation of the SB blocks backflow, ensuring unidirectional transport.

### V117 as the key mechanical transducer

Unlike bR where W182 in helix F mediates force transmission, KR2 uses V117 in helix C as the primary mechanical transducer. Starting at 1 µs, the retinal C20 methyl group pushes sideways against V117, causing a flip that propagates structural changes into helix C and the helical bundle. This represents a distinct mechanism for coupling retinal isomerization to protein conformational change.

### Sodium translocation pathway and gating

The program Caver identified a putative sodium translocation pathway across the membrane. A rotamer change of R109 and Q78, together with a shift of helix D at 20 ms, opens a connection between the retinal-proximal water-filled cavity and a second cavity near E11/N106/E160/R243 towards the extracellular exit. R109 corresponds to R82 in bR (critical for proton transfer), suggesting conserved functional sites across rhodopsin families.


## Cross-References
