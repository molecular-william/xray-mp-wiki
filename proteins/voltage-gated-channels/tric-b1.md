---
title: "C. elegans TRIC-B1 Channel"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19767]
verified: false
---

# C. elegans TRIC-B1 Channel

## Overview

TRIC-B1 is an intracellular cation channel from Caenorhabditis elegans belonging to the Trimeric Intracellular Cation (TRIC) channel family. It forms a homotrimeric complex with endogenous phosphatidylinositol-4,5-biphosphate ([PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/)) lipid molecules. Each monomer contains an hourglass-shaped hydrophilic pore within a seven-transmembrane-helix domain. The channel is permeable to monovalent cations (K+ or Na+) and displays Ca2+-dependent gating behavior. Structural and functional analyses reveal the central role of [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) in stabilizing the cytoplasmic gate and a marked Ca2+-induced conformational change in a cytoplasmic loop above the gate.


## Publications

### doi/10.1038##nature19767

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5egi">5EGI</a></td>
      <td>3.3 A</td>
      <td>P41212</td>
      <td>CeTRIC-B1 (residues 1-247), C. elegans, Myc and 6His tags removed</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> (phosphatidylinositol-4,5-biphosphate), Ca2+ bound at trimeric center</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5eig">5EIG</a></td>
      <td>3.9 A</td>
      <td>C2221</td>
      <td>CeTRIC-B1 (residues 1-247), C. elegans, <a href="/xray-mp-wiki/reagents/additives/methylmercury-chloride/">Methylmercury Chloride</a> derivative for SAD phasing</td>
      <td>CH3HgCl derivative</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Genes encoding TRIC-B1 from C. elegans (UniProt: Q9NA75) were synthesized with optimized codon usage. Target cDNA was inserted between EcoRI/XhoI sites of pPICZ-A vector with C-terminal fusion of c-Myc epitope and 6His tag. For crystallization, 48 amino acid residues at the flexible C-terminal region plus the Myc epitope were truncated, yielding residues 1-247 covering the transmembrane domain. Point mutations introduced via Quikchange site-directed mutagenesis. Expression vectors linearized with PmeI and transformed into P. pastoris GS115 strain by electroporation.


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
      <td>High-pressure homogenization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 8.0), 150 mM KCl + --</td>
      <td>Frozen cell pellets suspended 1:10 (m:v), homogenized with T10 basic homogenizer, passed through high-pressure homogenizer at 1300 bar, 4 times</td>
    </tr>
    <tr>
      <td>Membrane collection and solubilization</td>
      <td>Centrifugation and detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 8.0), 150 mM KCl + Triton X-100 (1.5% v/v final concentration)</td>
      <td>Cell lysate stirred at room temperature for 2 h, insoluble debris removed by centrifugation at 37044g for 1 h</td>
    </tr>
    <tr>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt affinity beads (BD Science), 1 ml resin/30 g cell pellet</td>
      <td>150 mM KCl, 25 mM HEPES (pH 7.5), 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.5% beta-DM + 0.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (beta-DM, Anatrace)</td>
      <td>Pre-equilibrated resin, 1-h incubation at room temperature, washed with 5 column volumes of buffer A (150 mM KCl, 25 mM HEPES pH 7.5)</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> beads</td>
      <td>150 mM KCl, 25 mM HEPES (pH 7.5), <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.5% beta-DM</td>
      <td>Elution via <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CeTRIC-B1 (residues 1-247) in beta-DM with endogenous <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Ca2+ bound (CaCl2 present during crystallization)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group P41212, cell dimensions a=b=102.05 A, c=279.99 A. Wavelength 1.1000 A, resolution 32-3.3 A (shell 3.42-3.3), Rmerge 11.5% (80.4%), Rpim 3.7% (25.8%), I/sigmaI 11.1 (2.8), completeness 99.9% (100.0%), redundancy 10.5. SAD derivative (5EIG): space group C2221, <a href="/xray-mp-wiki/reagents/additives/methylmercury-chloride/">Methylmercury Chloride</a> derivative, wavelength 1.0073 A, resolution 46-3.9 A, Rmerge 11.7% (98.1%), completeness 99.6% (100%), redundancy 13.7.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5egi">5EGI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MVVPESF</span><span class="topo-outside">QLDQEILLDAGAQLHRLKM</span><span class="topo-membrane">YPYFDVAHYLLMIIEV</span><span class="topo-inside">RDDLGSAASIFSRKH</span><span class="topo-membrane">PLS</span></span>
<span class="topo-line"><span class="topo-membrane">CWLSSMLMCFADAFLANFL</span><span class="topo-outside">LGEPVIAPFKRHDD</span><span class="topo-membrane">IILATIIWYLVFYAP</span><span class="topo-inside">FDGIYKIAKITP</span></span>
<span class="topo-line"><span class="topo-membrane">VKCVLAVMKEVKRAYKV</span><span class="topo-outside">SHGVSHAAKLYPNSYIVQV</span><span class="topo-membrane">LVGTAKGAGSGIVRTLEQLVR</span><span class="topo-inside">GVW</span></span>
<span class="topo-line"><span class="topo-inside">LPTHNELLR</span><span class="topo-membrane">PSFATKACVVAASV</span><span class="topo-outside">LALEKSGTYLTAPHDLVYL</span><span class="topo-membrane">VIVGFFVYFKLSAV</span><span class="topo-inside">ILH</span><span class="topo-unknown">V</span></span>
<span class="topo-line"><span class="topo-unknown">TDPFAPIENLFHHHHHH</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>26</td>
      <td>8</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>27</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Inside</td>
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
      <td>93</td>
      <td>80</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>94</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>120</td>
      <td>109</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>137</td>
      <td>121</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>156</td>
      <td>138</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>222</td>
      <td>204</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>236</td>
      <td>223</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>239</td>
      <td>237</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>240</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5egi">5EGI</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MVVPESFQL</span><span class="topo-outside">DQEILLDAGAQLHRLKM</span><span class="topo-membrane">YPYFDVAHYLLMIIEVR</span><span class="topo-inside">DDLGSAASIFS</span><span class="topo-membrane">RKHPLS</span></span>
<span class="topo-line"><span class="topo-membrane">CWLSSMLMCFADAFLANFL</span><span class="topo-outside">LGEPVIAPFKRHDD</span><span class="topo-membrane">IILATIIWYLVFYAP</span><span class="topo-inside">FDGIYKIAKITP</span></span>
<span class="topo-line"><span class="topo-membrane">VKCVLAVMKEVKRAYKVS</span><span class="topo-outside">HGVSHAAKLYPNSYIVQV</span><span class="topo-membrane">LVGTAKGAGSGIVRTLEQLVR</span><span class="topo-inside">GVW</span></span>
<span class="topo-line"><span class="topo-inside">LPTHNELLR</span><span class="topo-membrane">PSFATKACVVAASV</span><span class="topo-outside">LALEKSGTYLTAPHDLVY</span><span class="topo-membrane">LVIVGFFVYFKLSAV</span><span class="topo-inside">ILHV</span></span>
<span class="topo-line"><span class="topo-inside">TD</span><span class="topo-unknown">PFAPIENLFHHHHHH</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>10</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>43</td>
      <td>27</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>54</td>
      <td>44</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>79</td>
      <td>55</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>93</td>
      <td>80</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>94</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>120</td>
      <td>109</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>156</td>
      <td>139</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>221</td>
      <td>204</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>236</td>
      <td>222</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>242</td>
      <td>237</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>257</td>
      <td>243</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5egi">5EGI</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MVVPESF</span><span class="topo-outside">QLDQEILLDAGAQLHRLKM</span><span class="topo-membrane">YPYFDVAHYLLMIIEV</span><span class="topo-inside">RDDLGSAASIFSRKH</span><span class="topo-membrane">PLS</span></span>
<span class="topo-line"><span class="topo-membrane">CWLSSMLMCFADAFLANFLL</span><span class="topo-outside">GEPVIAPFKRHD</span><span class="topo-membrane">DIILATIIWYLVFYAP</span><span class="topo-inside">FDGIYKIAKITP</span></span>
<span class="topo-line"><span class="topo-membrane">VKCVLAVMKEVKRAYKVS</span><span class="topo-outside">HGVSHAAKLYPNSYI</span><span class="topo-membrane">VQVLVGTAKGAGSGIVRTLEQLVR</span><span class="topo-inside">GVW</span></span>
<span class="topo-line"><span class="topo-inside">LPTHNELLR</span><span class="topo-membrane">PSFATKACVVAASV</span><span class="topo-outside">LALEKSGTYLTAPHDLV</span><span class="topo-membrane">YLVIVGFFVYFKLS</span><span class="topo-inside">AVILH</span><span class="topo-unknown">V</span></span>
<span class="topo-line"><span class="topo-unknown">TDPFAPIENLFHHHHHH</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>26</td>
      <td>8</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>27</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>80</td>
      <td>58</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>92</td>
      <td>81</td>
      <td>92</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>108</td>
      <td>93</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>120</td>
      <td>109</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>153</td>
      <td>139</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>177</td>
      <td>154</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>178</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>203</td>
      <td>190</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>234</td>
      <td>221</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>239</td>
      <td>235</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>240</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### PIP2-dependent cytoplasmic gate stabilization

[PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) acts as a lipid cofactor necessary for regulating the channel function. Its head group binds directly to conserved basic amino acid residues from TRIC-B1 and is located on the surface of the cytoplasmic vestibule of the pore. [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding stabilizes the closed state of the cytoplasmic gate. The PIP2-binding site is buried inside each monomer, distinct from the peripheral binding seen in Kir channels. Mutation of PIP2-binding residues (K129A/R133L) abolishes [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding and impairs channel function, as shown by fluorescence-based K+ flux assays and single-channel electrophysiology.

### Homotrimeric architecture with hourglass-shaped pore

TRIC-B1 forms a symmetrical homotrimer with a C3 axis running through its center and perpendicular to the membrane plane. Each monomer contains seven transmembrane helices (M1-7) with a 3+3+1 organization pattern: M1-3 and M4-6 form inverted repeats, while M7 is standalone and fills the crevice between M4 and M6. The ion permeation pathway traverses through the central pore within each monomer, not along the trimeric C3 axis. The pore has an hourglass shape with two bottlenecks near lysine residues and the [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) molecule. Pore-lining residues Met38, Ala126, and Ser166 (on M1, M4, and M5) were confirmed by cysteine accessibility testing with [MTSET](/xray-mp-wiki/reagents/additives/mtset/).

### Ca2+-induced conformational change in M5-6 loop

TRIC-B1 contains a Ca2+ binding site at the trimeric center, surrounded by three Trp180 residues. Upon Ca2+ binding, Trp180 switches its side chain rotamer to form a cradle-like pocket measuring ~13 A wide. Accompanying the rotamer switch, the M5-6 loop swings towards the pore region and covers the [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) head group. This conformational change was verified by disulfide-cross-linking experiments with A49C/N185C mutant. Mutation of Trp180 to Ala abolishes Ca2+ sensitivity. The M5-6 loop fences the cytoplasmic entrance of the pore and presents a patch of electronegative surface.

### Multi-state gating mechanism

Single-channel electrophysiology reveals multiple open states (O1, O2, O3) corresponding to one, two, or three monomers being open within the trimer. Wild-type TRIC-B1 shows fast transition from closed to the third open state, while the K129A/R133L mutant shows stepwise opening with dwelling on intermediate states. The channel exhibits voltage-dependent gating with sensitivity to Ca2+ applied on the cytosolic side (stimulated) and luminal side (inhibited). A mechanistic model proposes M5-6 loop as the Ca2+-sensing motif and M4 as the potential voltage-sensing helix.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol/">Phosphatidylinositol</a> — PIP2 is a phosphorylated derivative of phosphatidylinositol; structural comparison with Kir channels shows different PIP2-binding modes
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary detergent (beta-DM, 0.5%) used throughout purification and crystallization of TRIC-B1
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Used at 1.5% for solubilization of membrane proteins from P. pastoris cell lysate
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer component (25 mM, pH 7.5) used in purification buffers
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Structural comparison with canonical tetrameric K+ channel (KcsA, PDB 1BL8) used to highlight unique TRIC architecture
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Homologous prokaryotic potassium channel; PIP2 binding compared with Kir2.2 channel
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> — Buffer component (50 mM, pH 8.0) used in cell lysis buffer
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — Ca2+-induced conformational change in M5-6 loop allosterically affects pore gating via PIP2 interaction
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
