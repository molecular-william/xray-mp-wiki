---
title: "Human Adenosine A1 Receptor (A1AR)"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.01.042, doi/10.1016##j.str.2017.06.012]
verified: false
---

# Human Adenosine A1 Receptor (A1AR)

## Overview

The human adenosine A1 receptor (A1AR) is a class A G protein-coupled receptor that plays a vital role in cardiac, renal, and neuronal processes. Structures have been solved for the A1AR bound to the selective covalent antagonist DU172 (3.2 A) and the thermostabilized A1R-StaR construct bound to the A1-selective xanthine antagonist PSB36 (3.3 A), revealing key determinants of ligand subtype selectivity.

## Publications

### doi/10.1016##j.cell.2017.01.042

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uen">5UEN</a></td>
      <td>3.2 A</td>
      <td>P1</td>
      <td>Human A1AR with M4 N-terminus insertion, BRIL fusion in ICL3, N159A mutation, C-terminal truncation after residue 311 with 3C protease site</td>
      <td>DU172</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus) for DU172 structure; Sf9 insect cells for StaR structure
- **Construct**: Human A1AR constructs: (1) A1AR with M4 N-terminus insertion, BRIL fusion in ICL3, N159A mutation, C-terminal truncation; (2) A1R-StaR-Delta3-b562RIL thermostabilized mutant with mutations A57L(2.52), T91A(3.36), Y205A(5.63), L236A(6.37), L240A(6.41), T277A(7.42)
- **Notes**: For DU172 structure: High-titer recombinant baculovirus used to infect Sf9 cells; cells harvested 48 hr post-infection; construct had 22 aa M4 muscarinic receptor N-terminus with N-glycosylation sites and 3C protease site; BRIL inserted in ICL3 between residues 211-220; N159A mutation; C-terminal truncation after residue 311 with 3C protease site

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
      <td>Expression and membrane preparation</td>
      <td>Baculovirus expression in Sf9 insect cells; cells harvested 48 hr post-infection, membranes prepared by homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors + --</td>
      <td>DU172 (0.2 uM) added to membranes before solubilization</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% sodium cholate, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 2 hr at 4C in presence of 0.2 uM DU172</td>
    </tr>
    <tr>
      <td>TALON IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% sodium cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 50 mM imidazole + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% sodium cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Eluted with 200 mM imidazole; 0.2 uM DU172 present throughout</td>
    </tr>
    <tr>
      <td>Anti-Flag M1 affinity</td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M1 <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> M1 affinity resin</td>
      <td>0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Detergent exchanged to <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> on resin</td>
    </tr>
    <tr>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.2 uM DU172 + 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Concentrated to ~50 mg/mL for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>A1AR-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion in complex with DU172 at ~50 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 wk</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>29 crystals merged into single dataset at 3.2 A resolution, space group P1; two receptor copies per asymmetric unit; structure solved by molecular replacement; lipid cubic phase method</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<<<<<<< HEAD
<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uen">5UEN</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPPP</span><span class="topo-inside">SISAF</span><span class="topo-membrane">QAAYIGIEVLIALVSVPGNVLVIW</span><span class="topo-outside">AVKVNQALRDATFC</span><span class="topo-membrane">FIVSLAVADVAVG</span></span>
<span class="topo-line"><span class="topo-membrane">ALVIPLAILINI</span><span class="topo-inside">GPQTYFH</span><span class="topo-membrane">TCLMVACPVLILTQSSILALLAIAV</span><span class="topo-outside">DRYLRVKIPLRYKMVV</span></span>
<span class="topo-line"><span class="topo-outside">TPRRAA</span><span class="topo-membrane">VAIAGCWILSFVVGLTPMFGWN</span><span class="topo-inside">NLSAVERAWAAAGSMGEPVIKCEFEKV</span><span class="topo-membrane">ISMEY</span></span>
<span class="topo-line"><span class="topo-membrane">MVYFNFFVWVLPPLLLMVLIYLE</span><span class="topo-outside">VFYLIRKQLADLEDNWETLNDN</span><span class="topo-unknown">LKVIEKADNAAQ</span><span class="topo-outside">VKD</span></span>
<span class="topo-line"><span class="topo-outside">ALTKMRAAALDA</span><span class="topo-unknown">QKATPPKLEDKSPDS</span><span class="topo-outside">PEMKDFRHGFDILVGQIDDALKLANEGKVKEAQ</span></span>
<span class="topo-line"><span class="topo-outside">AAAEQLKTTRNAYIQKYLERARSTLQKELKIAK</span><span class="topo-membrane">SLALILFLFALSWLPLHILNCITLF</span><span class="topo-inside">CP</span></span>
<span class="topo-line"><span class="topo-inside">SCHKPS</span><span class="topo-membrane">ILTYIAIFLTHGNSAMNPIVYAFR</span><span class="topo-outside">IQKFRVTFLKIWNDHFRCQPLEVLFQ</span></span>
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
      <td>4</td>
      <td>0</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>9</td>
      <td>4</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>33</td>
      <td>9</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>33</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>47</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>79</td>
      <td>72</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>104</td>
      <td>79</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>126</td>
      <td>104</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>148</td>
      <td>126</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>175</td>
      <td>148</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>203</td>
      <td>175</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>212</td>
      <td>203</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>225</td>
      <td>1001</td>
      <td>1013</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>237</td>
      <td>1014</td>
      <td>1025</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>238</td>
      <td>252</td>
      <td>1026</td>
      <td>1040</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>267</td>
      <td>1041</td>
      <td>1055</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>268</td>
      <td>318</td>
      <td>1056</td>
      <td>1106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>333</td>
      <td>220</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>358</td>
      <td>235</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>366</td>
      <td>260</td>
      <td>267</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>390</td>
      <td>268</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>416</td>
      <td>292</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>
=======
| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and membrane preparation | Baculovirus expression in Sf9 insect cells; cells harvested 48 hr post-infection, membranes prepared by homogenization and ultracentrifugation | — | 10 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors + -- | DU172 (0.2 uM) added to membranes before solubilization |
| Solubilization | Detergent solubilization | -- | 10 mM HEPES pH 7.5, 150 mM NaCl + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% sodium cholate, 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 2 hr at 4C in presence of 0.2 uM DU172 |
| TALON IMAC | Immobilized metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin | 10 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% sodium cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 mM imidazole + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% sodium cholate, 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Eluted with 200 mM imidazole; 0.2 uM DU172 present throughout |
| Anti-Flag M1 affinity | Anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) M1 [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) M1 affinity resin | 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/)) + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Detergent exchanged to [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) on resin |
| SEC | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.2 uM DU172 + 0.05% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Concentrated to ~50 mg/mL for [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization |

#### Source: doi/10.1016##j.str.2017.06.012


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | HEK293T cell expression; membranes prepared in 40 mM Tris-HCl pH 7.6, 1 mM EDTA with protease inhibitors | -- | 40 mM Tris-HCl pH 7.6, 1 mM EDTA + -- | Cells expressed in HEK293T; 0.6 mg/L yield |
| Solubilization | Membranes solubilized with 1.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) for 1 hr at 4 C in presence of 10 uM PSB36 | -- | 40 mM Tris-HCl pH 7.6 + 1.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Incubated 1 hr at room temperature with PSB36 before solubilization |
| Ni-NTA affinity chromatography | Batch binding to 5 ml [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) superflow cartridge; washed with 5 CV of 8 mM imidazole, 25 CV of 68 mM imidazole; eluted with 272 mM imidazole | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) superflow cartridge (Qiagen) | 40 mM Tris-HCl pH 7.4, 400 mM NaCl, 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/), 5 uM PSB36 (binding); 8 mM imidazole (wash); 272 mM imidazole (elution)
 + 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/) | All buffers contained 5 uM PSB36 |
| Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL column | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | 40 mM Tris-HCl pH 7.4, 200 mM NaCl, 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/), 5 uM PSB36 + 0.15% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Fractions concentrated to ~37 mg/mL |


## Crystallization

### doi/10.1016##j.cell.2017.01.042

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization |
| Protein sample | A1AR-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion in complex with DU172 at ~50 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio |
| Temperature | 20 C |
| Growth time | 2 wk |
| Notes | 29 crystals merged into single dataset at 3.2 A resolution, space group P1; two receptor copies per asymmetric unit; structure solved by molecular replacement; lipid cubic phase method |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

</div>
### doi/10.1016##j.str.2017.06.012

<<<<<<< HEAD
**Structures:**
=======
| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) [crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | A1R-StaR-Delta3-b562RIL in complex with PSB36 at ~37 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio |
| Temperature | 20 C |
| Growth time | 2 crystals merged |
| Cryoprotection | -- |
| Notes | Crystallized in [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) at Diamond Light Source. Data collected at 3.3 A resolution, space group C22222, 2 crystals merged. Structure solved by molecular replacement.
 |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/--">--</a></td>
      <td>3.3 A</td>
      <td>C22222</td>
      <td>Human A1R-StaR-Delta3-b562RIL thermostabilized mutant (A57L, T91A, Y205A, L236A, L240A, T277A) with C-terminal truncation, b562RIL fusion</td>
      <td>PSB36</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus) for DU172 structure; Sf9 insect cells for StaR structure
- **Construct**: Human A1AR constructs: (1) A1AR with M4 N-terminus insertion, BRIL fusion in ICL3, N159A mutation, C-terminal truncation; (2) A1R-StaR-Delta3-b562RIL thermostabilized mutant with mutations A57L(2.52), T91A(3.36), Y205A(5.63), L236A(6.37), L240A(6.41), T277A(7.42)
- **Notes**: For DU172 structure: High-titer recombinant baculovirus used to infect Sf9 cells; cells harvested 48 hr post-infection; construct had 22 aa M4 muscarinic receptor N-terminus with N-glycosylation sites and 3C protease site; BRIL inserted in ICL3 between residues 211-220; N159A mutation; C-terminal truncation after residue 311 with 3C protease site

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
      <td>HEK293T cell expression; membranes prepared in 40 mM Tris-HCl pH 7.6, 1 mM EDTA with protease inhibitors</td>
      <td>--</td>
      <td>40 mM Tris-HCl pH 7.6, 1 mM EDTA + --</td>
      <td>Cells expressed in HEK293T; 0.6 mg/L yield</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membranes solubilized with 1.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> for 1 hr at 4 C in presence of 10 uM PSB36</td>
      <td>--</td>
      <td>40 mM Tris-HCl pH 7.6 + 1.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Incubated 1 hr at room temperature with PSB36 before solubilization</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Batch binding to 5 ml <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> superflow cartridge; washed with 5 CV of 8 mM imidazole, 25 CV of 68 mM imidazole; eluted with 272 mM imidazole</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> superflow cartridge (Qiagen)</td>
      <td>40 mM Tris-HCl pH 7.4, 400 mM NaCl, 0.15% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 5 uM PSB36 (binding); 8 mM imidazole (wash); 272 mM imidazole (elution)
 + 0.15% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>All buffers contained 5 uM PSB36</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL (GE Healthcare)</td>
      <td>40 mM Tris-HCl pH 7.4, 200 mM NaCl, 0.15% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 5 uM PSB36 + 0.15% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Fractions concentrated to ~37 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>A1R-StaR-Delta3-b562RIL in complex with PSB36 at ~37 mg/mL mixed with monoolein and cholesterol at 40:54:6 (w:w:w) ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 crystals merged</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> at Diamond Light Source. Data collected at 3.3 A resolution, space group C22222, 2 crystals merged. Structure solved by molecular replacement.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### A1AR-DU172 structure reveals wider extracellular cavity

The 3.2 A crystal structure of human A1AR bound to the covalent antagonist DU172 (PDB 5UEN) reveals a strikingly wider extracellular cavity compared to the A2AR structure. Major differences were found in the ECL2 conformation and extracellular loop regions. The wider cavity accommodates both orthosteric and allosteric ligands, suggesting a structural basis for allosteric modulation. Drug selectivity between A1 and A2A receptor subtypes appears to be primarily determined by binding site shape/conformation rather than residue composition. The DU172 compound forms a covalent benzene-sulfonate linkage with Y271(7.36) in the binding pocket.

### Xanthine binding mode in A1AR

PSB36 occupies the orthosteric ligand binding pocket of A1AR with the xanthine core sandwiched between F171 and L250(6.51). Two hydrogen bonds form between PSB36 and N254(6.55). The butyl substituent at N1 points toward a hydrophobic pocket formed by V87(3.32), L88(3.33), A91(3.36), M180(5.38), W247(6.48), and H251(6.52). The noradamantyl group at C8 points toward the extracellular face, contacting L253(6.54), T257(6.58), T270(7.35), and E172.

### T270(7.35) gatekeeper residue

Threonine at position 7.35 in A1AR (vs methionine in A2AR) is the primary determinant of xanthine selectivity. M270T mutation in A2AR increases A1-selective ligand affinity, while T270M in A1AR decreases it. The bulky methionine in A2AR creates unfavorable steric interactions with the C8 noradamantyl group of PSB36.

### Narrower binding channel in A2AR

The channel accommodating the N1 butyl chain of PSB36 is narrower in A2AR than in A1AR, preventing deep binding of PSB36 in A2AR. This contributes to the submicromolar affinity of PSB36 for A2AR compared to subnanomolar affinity for A1AR.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/psb36/">PSB36</a> — A1-selective xanthine antagonist used in crystallization (3.3 A structure)
- <a href="/xray-mp-wiki/reagents/ligands/du172/">DU172</a> — Covalent antagonist used in prior A1AR structure (PDB 5UEN, 3.2 A)
- <a href="/xray-mp-wiki/reagents/ligands/dpcpx/">DPCPX (8-Cyclopentyl-1,3-dipropylxanthine)</a> — A1-selective antagonist used in mutagenesis binding assays
- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor (A2AR)</a> — Comparison structure for selectivity determinants
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Detergent used for solubilization and purification at 0.15%
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in purification and membrane preparation
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL Fusion Protein</a> — b562RIL fusion partner used in StaR construct
