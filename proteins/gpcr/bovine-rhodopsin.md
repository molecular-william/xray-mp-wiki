---
title: "Bovine Rhodopsin"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.289.5480.739, doi/10.1073##pnas.0608022103, doi/10.1016##J.JMB.2004.08.090, doi/10.1038##NATURE09795, doi/10.1038##s41586-023-05863-6, doi/10.1073##pnas.1718084115, doi/10.1038##s41467-023-40911-9, doi/10.1073##pnas.082666399, doi/10.1073##pnas.1114089108, doi/10.1107##S0907444908017162, doi/10.1073##pnas.1617446114]
verified: false
---

# Bovine Rhodopsin

## Overview

Rhodopsin is the photoreceptor GPCR in vertebrate retina rod cells, responsible for dim-light vision. The landmark crystal structure of bovine rhodopsin, the first X-ray structure of any GPCR, was determined at 2.8 A resolution (Palczewski et al., 2000, PDB 1F88), revealing the canonical seven-transmembrane helix bundle with 11-cis-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) covalently bound via a protonated Schiff base to Lys296. A subsequent dark-state structure (PDB 1GZM) was determined at 2.65 A resolution in space group P3_1. Stenkamp (2008) later reinterpreted the space-group symmetry of the P3_1 crystal forms (1gzm and 2j4y) as hexagonal P6_4 with one molecule in the asymmetric unit (PDB 3C9L and 3C9M). The protein consists of 7 transmembrane helices with kinks at proline and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) motifs in H7, and the E(D)RY motif in H3. The structure of the constitutively active M257Y mutant in complex with GalphaCT peptide at 3.3 A revealed the active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) conformation obtained by light activation, showing how the introduced tyrosine at position 6.40 stabilizes the G protein binding site through interactions with Y223(5.58), Y306(7.53), and R135(3.50). Ultrafast time-resolved SFX captured the bathorhodopsin intermediate at 1 ps after photoactivation.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.289.5480.739 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1f88">1F88</a></td>
      <td>2.8</td>
      <td>P4(1)</td>
      <td>Bovine rhodopsin, full-length (348 residues), purified from bovine retina rod outer segments</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via protonated Schiff base)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

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
      <td>Rod outer segment (ROS) preparation</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> gradient centrifugation from bovine retina</td>
      <td>—</td>
      <td>not specified + --</td>
      <td>Standard ROS preparation from fresh bovine retinae under dim red light</td>
    </tr>
    <tr>
      <td>Rhodopsin solubilization and purification</td>
      <td>Concanavalin A (ConA) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>ConA-agarose</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/og/">OTG</a> (mixed micelles)</td>
      <td>Rhodopsin eluted with methyl-alpha-D-mannopyranoside. Final sample in mixed micelles for crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Mixed micelle crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bovine rhodopsin, solubilized from rod outer segment membranes, purified by ConA chromatography, in mixed micelles of <a href="/xray-mp-wiki/reagents/detergents/og/">OTG</a> and other detergents</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals cryocooled for data collection at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belonged to space group P4(1) with unit cell a=97.25, c=149.54 A. Two molecules per asymmetric unit. Data collected at SPring-8 BL45XU (<a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a>, 3.3 A) and APS 19-ID (high-resolution, 2.8 A). <a href="/xray-mp-wiki/methods/structure-determination/mad-phasing/">MAD</a> phasing using Hg derivative (soaking). Merohedral twinning was significant; least twinned data selected for phasing. Structure refined to R=23.3%, R_free=28.8% at 2.8 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1f88">1F88</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQHK</span><span class="topo-outside">KL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFT</span><span class="topo-inside">TTLYTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-inside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFV</span><span class="topo-membrane">IYMFVVHFIIPLIVIFFCYGQLV</span><span class="topo-outside">FTVKEAAA</span><span class="topo-unknown">QQQE</span><span class="topo-outside">S</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAF</span><span class="topo-inside">YIFTHQGSDFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKNP</span><span class="topo-unknown">LGDDEA</span><span class="topo-outside">STTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>66</td>
      <td>40</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>68</td>
      <td>67</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>92</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>112</td>
      <td>93</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>137</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>170</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>204</td>
      <td>171</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>227</td>
      <td>205</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>235</td>
      <td>228</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>239</td>
      <td>236</td>
      <td>239</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>240</td>
      <td>250</td>
      <td>240</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>290</td>
      <td>274</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>310</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>327</td>
      <td>311</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>328</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>334</td>
      <td>348</td>
      <td>334</td>
      <td>348</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.0608022103 (3 structures, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2i37">2I37</a></td>
      <td>4.15</td>
      <td>P3(1)12</td>
      <td>Highly delipidated bovine rhodopsin (purified by immunoaffinity chromatography)</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (deprotonated Schiff base, covalently bound to Lys296)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2i36">2I36</a></td>
      <td>4.10</td>
      <td>P3(1)12</td>
      <td>Highly delipidated bovine rhodopsin (ground state, same crystal form)</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (protonated Schiff base)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2i35">2I35</a></td>
      <td>3.80</td>
      <td>R32</td>
      <td>Highly delipidated bovine rhodopsin (ground state, rhombohedral form)</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (protonated Schiff base)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

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
      <td>Purification</td>
      <td>Immuno<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Rho1D4 antibody column</td>
      <td>25 mM bis-<a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a>-propane (pH 7.5) + n-Octyl-beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Highly delipidated rhodopsin purified from bovine retina. Delipidation critical for crystallizability.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Highly delipidated bovine rhodopsin, immunoaffinity purified, in octyl-beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>) detergent</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals frozen in liquid nitrogen after light exposure for photoactivation</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystal forms obtained: rhombohedral R32 (3.8 A, one molecule per ASU) and trigonal P3(1)12 (4.1-4.2 A, three molecules per ASU). Crystals photoactivated by light exposure.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2i37">2I37</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-outside">QHKKLRTPLN</span><span class="topo-membrane">YILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-inside">HGYFVFGPT</span><span class="topo-membrane">GCNLEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAI</span><span class="topo-outside">ERYVVVCKPMS</span><span class="topo-unknown">NFRFG</span><span class="topo-outside">ENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPLVGWSRYIPE</span><span class="topo-inside">GMQCSCGIDYYTPHEET</span><span class="topo-membrane">NNESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-outside">QLVFTVKEAA</span><span class="topo-unknown">AQQ</span><span class="topo-outside">QE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-outside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIYIMM</span><span class="topo-outside">NKQFRNCMVTTLCCGKNP</span><span class="topo-unknown">LGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>74</td>
      <td>64</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>100</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>100</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>134</td>
      <td>109</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>145</td>
      <td>134</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>150</td>
      <td>145</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>151</td>
      <td>155</td>
      <td>150</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>182</td>
      <td>155</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>199</td>
      <td>182</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225</td>
      <td>199</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>235</td>
      <td>225</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>238</td>
      <td>235</td>
      <td>237</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>239</td>
      <td>253</td>
      <td>238</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>278</td>
      <td>253</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>287</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>287</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>328</td>
      <td>310</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>349</td>
      <td>328</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2i36">2I36</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTL</span><span class="topo-inside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIE</span><span class="topo-outside">RY</span><span class="topo-unknown">VVVCKPMSNF</span><span class="topo-outside">RFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPL</span><span class="topo-inside">VGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQ</span><span class="topo-outside">LVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-outside">SATTQKAEKEVTRM</span><span class="topo-membrane">VIIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPIF</span><span class="topo-membrane">MTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCG</span><span class="topo-unknown">KNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>39</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>72</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>96</td>
      <td>72</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>113</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>135</td>
      <td>113</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>137</td>
      <td>135</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>147</td>
      <td>137</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>151</td>
      <td>147</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>203</td>
      <td>173</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>226</td>
      <td>203</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>254</td>
      <td>226</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>275</td>
      <td>254</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>288</td>
      <td>275</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>311</td>
      <td>288</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>325</td>
      <td>311</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>349</td>
      <td>325</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2i35">2I35</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAY</span><span class="topo-membrane">MFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLEGF</span><span class="topo-membrane">FATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-inside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVI</span><span class="topo-membrane">YMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-inside">TVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKE</span><span class="topo-membrane">VTRMVIIMVIAFLICWLPYAG</span><span class="topo-outside">VAFYIFTHQGSDFGPIFMTIP</span><span class="topo-membrane">AFFAKTSAVYNPVIYIMMNK</span><span class="topo-inside">QFRNCMVTTLCCGKN</span><span class="topo-unknown">PLG</span><span class="topo-inside">DD</span><span class="topo-unknown">EASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>44</td>
      <td>1</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>44</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>69</td>
      <td>66</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>116</td>
      <td>93</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>138</td>
      <td>116</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>151</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>206</td>
      <td>171</td>
      <td>205</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>229</td>
      <td>206</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>250</td>
      <td>229</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>250</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>271</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>312</td>
      <td>292</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>327</td>
      <td>312</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>330</td>
      <td>327</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>331</td>
      <td>332</td>
      <td>330</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>349</td>
      <td>332</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##J.JMB.2004.08.090 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1gzm">1GZM</a></td>
      <td>2.65</td>
      <td>P31</td>
      <td>Bovine rhodopsin (residues 1-326 of 348)</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via protonated Schiff base)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1gzm">1GZM</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTL</span><span class="topo-outside">YTSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-inside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-outside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLV</span><span class="topo-inside">FTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMNK</span><span class="topo-inside">QFRNCMVTTLCCGKN</span><span class="topo-unknown">PLG</span><span class="topo-inside">DD</span><span class="topo-unknown">EASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>40</td>
      <td>1</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>66</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>69</td>
      <td>66</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>96</td>
      <td>69</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>96</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>138</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>151</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>203</td>
      <td>174</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>228</td>
      <td>203</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>251</td>
      <td>228</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>289</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>327</td>
      <td>312</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>330</td>
      <td>327</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>331</td>
      <td>332</td>
      <td>330</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>349</td>
      <td>332</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##NATURE09795 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2x72">2X72</a></td>
      <td>3.00</td>
      <td>not specified</td>
      <td>Bovine rhodopsin E113Q mutant (constitutively active) with N2C/D282C stabilizing disulfide, in complex with GalphaCT peptide (11 residues, K341L mutation); all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> bound non-covalently in <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>-binding pocket; HEK293S GnTI- cell expression</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (non-covalently bound); GalphaCT peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2x72">2X72</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLQ</span><span class="topo-membrane">GFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>69</td>
      <td>66</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>93</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>137</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>252</td>
      <td>225</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>275</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>275</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2x72">2X72</a> — Chain D (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLQ</span><span class="topo-membrane">GFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>69</td>
      <td>66</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>93</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>137</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>252</td>
      <td>225</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>275</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>275</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41586-023-05863-6 (5 structures, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zbe">7ZBE</a></td>
      <td>1.80</td>
      <td>P 2 2 2</td>
      <td>Bovine rhodopsin, dark state, room temperature SFX structure from LCP-grown microcrystals</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via protonated Schiff base)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7zbc">7ZBC</a></td>
      <td>1.80</td>
      <td>P 2 2 2</td>
      <td>Bovine rhodopsin, dark state, room temperature SFX structure from LCP-grown microcrystals (SACLA dataset)</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via protonated Schiff base)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8a6c">8A6C</a></td>
      <td>1.80</td>
      <td>P 2 2 2</td>
      <td>Bovine rhodopsin, 1 ps after photoactivation (Batho-Rh intermediate), TR-SFX at SwissFEL, extrapolated 21% activation</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (twisted, covalently bound to Lys296)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8a6d">8A6D</a></td>
      <td>1.80</td>
      <td>P 2 2 2</td>
      <td>Bovine rhodopsin, 10 ps after photoactivation, TR-SFX at SwissFEL, extrapolated 20% activation</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (partially relaxed, covalently bound to Lys296)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8a6e">8A6E</a></td>
      <td>1.80</td>
      <td>P 2 2 2</td>
      <td>Bovine rhodopsin, 100 ps after photoactivation, TR-SFX at SACLA, extrapolated 22% activation</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (more relaxed, covalently bound to Lys296)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

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
      <td>Rod outer segment (ROS) membrane isolation</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> gradient centrifugation</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS (3-(N-Morpholino)propanesulfonic Acid)</a>, 30 mM NaCl, 60 mM KCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 40% (w/w) <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> + None (native membranes)</td>
      <td>200 frozen bovine retinae used as starting material. Two-step centrifugation: 4,000g for 30 min, then 24,000g for 30 min. ROS membrane layers collected from 23-29% interface on 34%/29% <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> gradient, 110,000g for 90 min.</td>
    </tr>
    <tr>
      <td>ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (optimized)</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Concanavalin A (ConA) resin, scale-up 3x</td>
      <td>50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a>, 150 mM NaCl, 3 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, 3 mM MnCl2, 3 mM CaCl2, 1 mM Na2-<a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM 2-mercaptoethanol, pH 6.0 + 1% n-octyl-beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Starting material ~180 mg rhodopsin. Reversed flow used for second half of elution to sharpen elution profile.</td>
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
      <td>Bovine rhodopsin purified via ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a>, detergent exchanged to 0.21% n-decyl-N,N-dimethylamine-N-oxide (DAO) in 50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a>, 150 mM NaCl, 3 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, pH 6.0. Concentrated to 20-25 mg/ml.</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> viscous medium (no cryoprotectant, room temperature data collection)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>-based) for TR-<a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">SFX</a>. Crystal pla<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> approximately 20 um large and 1.5 um thick. Type I lattice (P 2 2 2 space group). Photoactivation at 480 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> pump laser. Data collected at SwissFEL (1 ps, 10 ps) and SACLA (100 ps) <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">X-ray free-electron laser</a>s.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zbe">7ZBE</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERY</span><span class="topo-outside">VVVCKP</span><span class="topo-unknown">MSNF</span><span class="topo-outside">RFGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFFCYGQ</span><span class="topo-outside">LVFT</span><span class="topo-unknown">VKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-unknown">ATT</span><span class="topo-outside">QKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPIF</span><span class="topo-membrane">MTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLC</span><span class="topo-unknown">CGKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>111</td>
      <td>97</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>136</td>
      <td>112</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>142</td>
      <td>137</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>146</td>
      <td>143</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>151</td>
      <td>147</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>152</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>201</td>
      <td>174</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>225</td>
      <td>202</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>229</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>243</td>
      <td>230</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>244</td>
      <td>251</td>
      <td>244</td>
      <td>251</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>277</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>287</td>
      <td>278</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>288</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>322</td>
      <td>311</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>348</td>
      <td>323</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7zbc">7ZBC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPT</span><span class="topo-membrane">GCNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIER</span><span class="topo-outside">YVVVCKP</span><span class="topo-unknown">MSNF</span><span class="topo-outside">RFGENHA</span><span class="topo-membrane">IMGVAFTWVMALACAAPPLVGWSRY</span><span class="topo-inside">IPEGMQCSCGIDYYTPHEET</span><span class="topo-membrane">NNESFVIYMFVVHFIIPLIVIFFCYGQ</span><span class="topo-outside">LVFT</span><span class="topo-unknown">VKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-unknown">ATTQ</span><span class="topo-outside">KAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLC</span><span class="topo-unknown">CGKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>135</td>
      <td>109</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>142</td>
      <td>136</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>146</td>
      <td>143</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>153</td>
      <td>147</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>178</td>
      <td>154</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>198</td>
      <td>179</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>225</td>
      <td>199</td>
      <td>225</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>229</td>
      <td>226</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>244</td>
      <td>230</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>277</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>288</td>
      <td>278</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>310</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>322</td>
      <td>311</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>348</td>
      <td>323</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8a6c">8A6C</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKP</span><span class="topo-unknown">MSNF</span><span class="topo-outside">RFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-outside">T</span><span class="topo-unknown">VKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-unknown">ATT</span><span class="topo-outside">QKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPIFMT</span><span class="topo-membrane">IPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLC</span><span class="topo-unknown">CGKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>111</td>
      <td>97</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>137</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>142</td>
      <td>138</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>146</td>
      <td>143</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>150</td>
      <td>147</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>173</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>202</td>
      <td>174</td>
      <td>202</td>
      <td>Inside</td>
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
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>243</td>
      <td>230</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>244</td>
      <td>250</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>275</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>310</td>
      <td>290</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>322</td>
      <td>311</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>348</td>
      <td>323</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8a6d">8A6D</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKP</span><span class="topo-unknown">MSNF</span><span class="topo-outside">RFGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-outside">T</span><span class="topo-unknown">VKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-unknown">ATTQ</span><span class="topo-outside">KAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLC</span><span class="topo-unknown">CGKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>111</td>
      <td>97</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>137</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>142</td>
      <td>138</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>146</td>
      <td>143</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>151</td>
      <td>147</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>152</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>202</td>
      <td>174</td>
      <td>202</td>
      <td>Inside</td>
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
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>244</td>
      <td>230</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>250</td>
      <td>245</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>310</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>322</td>
      <td>311</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>348</td>
      <td>323</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8a6e">8A6E</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKP</span><span class="topo-unknown">MSNF</span><span class="topo-outside">RFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-unknown">TVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-unknown">SATTQ</span><span class="topo-outside">KAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLC</span><span class="topo-unknown">CGKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>40</td>
      <td>402</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>441</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>72</td>
      <td>466</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>97</td>
      <td>473</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>112</td>
      <td>498</td>
      <td>512</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>138</td>
      <td>513</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>143</td>
      <td>539</td>
      <td>543</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>147</td>
      <td>544</td>
      <td>547</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>151</td>
      <td>548</td>
      <td>551</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>552</td>
      <td>574</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>203</td>
      <td>575</td>
      <td>603</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>604</td>
      <td>629</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>245</td>
      <td>631</td>
      <td>645</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>251</td>
      <td>646</td>
      <td>651</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>652</td>
      <td>675</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>676</td>
      <td>689</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>690</td>
      <td>711</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>323</td>
      <td>712</td>
      <td>723</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>349</td>
      <td>724</td>
      <td>749</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1718084115 (8 structures, 9 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fk6">6FK6</a></td>
      <td>2.36</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> (residues 1-326 of 348) in complex with pharmacological chaperone RS01 (S-RS1)</td>
      <td>S-RS1 (non-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> pharmacological chaperone)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fk7">6FK7</a></td>
      <td>2.62</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS06</td>
      <td>RS06</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fk8">6FK8</a></td>
      <td>2.87</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS08</td>
      <td>RS08</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fk9">6FK9</a></td>
      <td>2.63</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS09</td>
      <td>RS09</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fka">6FKA</a></td>
      <td>2.70</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS11</td>
      <td>RS11</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fkb">6FKB</a></td>
      <td>3.03</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS13</td>
      <td>RS13</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fkc">6FKC</a></td>
      <td>2.46</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS15</td>
      <td>RS15</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fkd">6FKD</a></td>
      <td>2.49</td>
      <td>P 21 21 21</td>
      <td>N2C/D282C stabilized bovine <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> in complex with RS16</td>
      <td>RS16</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

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
      <td>HEK293S GnTI- cell expression</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.0, 150 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + --</td>
      <td>Cells grown in suspension culture. N2C/D282C double mutant provides thermal stability for crystallization.</td>
    </tr>
    <tr>
      <td>ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Concanavalin A (ConA) resin</td>
      <td>50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> pH 6.0, 150 mM NaCl, 3 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, 3 mM MnCl2, 3 mM CaCl2 + 1% n-octyl-beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>) for solubilization, then exchanged to 0.05% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) during wash</td>
      <td>Solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>. Protein eluted with 0.2 M methyl-alpha-D-mannopyranoside. Detergent exchanged to 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> during on-column washes.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>N2C/D282C stabilized <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a>, purified via ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a>, in 0.05% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 0.1 M LiSO4, 24-34% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 1000, or 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> pH 5.0-5.5, 0.15-0.2 M (NH4)2SO4, 27-32% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 1000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryoprotected by soaking in reservoir solution supplemented with 25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> or ethylene glycol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>N2C/D282C double mutant. Co-crystallization with compounds RS01-RS16 at 0.5-1 mM. All structures in P 21 21 21 space group.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fk6">6FK6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-outside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-inside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-outside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-inside">TVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span></span>
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
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>39</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>72</td>
      <td>65</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>97</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>112</td>
      <td>97</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>138</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>151</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>203</td>
      <td>174</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>203</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>251</td>
      <td>229</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fk7">6FK7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLEG</span><span class="topo-membrane">FFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>66</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>93</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>93</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>115</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>253</td>
      <td>225</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>275</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fk7">6FK7</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLEG</span><span class="topo-membrane">FFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>66</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>93</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>93</td>
      <td>114</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>115</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>253</td>
      <td>225</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>275</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fk8">6FK8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-inside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPW</span><span class="topo-membrane">QFSMLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTPLN</span><span class="topo-membrane">YILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-inside">HGYFVFGPTG</span><span class="topo-membrane">CNLEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIE</span><span class="topo-outside">RYVVVCKPMSNFRFGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLVGWS</span><span class="topo-inside">RYIPEGMQCSCGIDYYTPHEETN</span><span class="topo-membrane">NESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-outside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-outside">SATTQKAEKEVTRMV</span><span class="topo-membrane">IIMVIAFLICWLPYAGVAFYIFTHQ</span><span class="topo-inside">GSCFGP</span><span class="topo-membrane">IFMTIPAFFAKTSAVYNPVIYIMM</span><span class="topo-outside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>36</td>
      <td>1</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>65</td>
      <td>36</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>74</td>
      <td>65</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>100</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>110</td>
      <td>100</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>135</td>
      <td>110</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>152</td>
      <td>135</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>177</td>
      <td>152</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>200</td>
      <td>177</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>225</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>255</td>
      <td>225</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>280</td>
      <td>255</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>286</td>
      <td>280</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>310</td>
      <td>286</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>327</td>
      <td>310</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fk9">6FK9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-outside">TSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-inside">VVCKPMSNFRF</span><span class="topo-membrane">GENHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNESF</span><span class="topo-membrane">VIYMFVVHFIIPLIVIFFCYGQLV</span><span class="topo-inside">FTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSCFGPIF</span><span class="topo-membrane">MTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>39</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>69</td>
      <td>65</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>97</td>
      <td>69</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>113</td>
      <td>97</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>149</td>
      <td>138</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>171</td>
      <td>149</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>204</td>
      <td>171</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>228</td>
      <td>204</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>252</td>
      <td>228</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>278</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>288</td>
      <td>278</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>311</td>
      <td>288</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fka">6FKA</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSML</span><span class="topo-membrane">AAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-inside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTL</span><span class="topo-outside">YTSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAI</span><span class="topo-inside">ERYVVVCKPMSNFRFGENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPLVGWS</span><span class="topo-outside">RYIPEGMQCSCGIDYYTPHEETNN</span><span class="topo-membrane">ESFVIYMFVVHFIIPLIVIFF</span><span class="topo-inside">CYGQLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSCFGPIF</span><span class="topo-membrane">MTIPAFFAKTSAVYNPVIYIMM</span><span class="topo-inside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>41</td>
      <td>1</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>64</td>
      <td>41</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>75</td>
      <td>64</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>96</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>96</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>134</td>
      <td>112</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>155</td>
      <td>134</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>177</td>
      <td>155</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>201</td>
      <td>177</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>201</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>256</td>
      <td>222</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>278</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>288</td>
      <td>278</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>310</td>
      <td>288</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>327</td>
      <td>310</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fkb">6FKB</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-inside">QHKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLYTS</span><span class="topo-outside">LHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-inside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-outside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-inside">TVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-unknown">KQFRNCMVTT</span><span class="topo-inside">LCCGKNPL</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>72</td>
      <td>64</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>99</td>
      <td>72</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>112</td>
      <td>99</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>138</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>151</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>203</td>
      <td>174</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>203</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>251</td>
      <td>229</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>311</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>322</td>
      <td>329</td>
      <td>321</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fkc">6FKC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-inside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPW</span><span class="topo-membrane">QFSMLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLR</span><span class="topo-membrane">TPLNYILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-inside">HGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRF</span><span class="topo-membrane">GENHAIMGVAFTWVMALACAAPPL</span><span class="topo-inside">VGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQL</span><span class="topo-outside">VFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-outside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIMVIAFLICWLPYAGVAFYIFTH</span><span class="topo-inside">QGSCFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>36</td>
      <td>1</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>65</td>
      <td>36</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>70</td>
      <td>65</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>100</td>
      <td>70</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>112</td>
      <td>100</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>138</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>149</td>
      <td>138</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>173</td>
      <td>149</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>203</td>
      <td>173</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>227</td>
      <td>203</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>253</td>
      <td>227</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>279</td>
      <td>253</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>287</td>
      <td>279</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>287</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6fkd">6FKD</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKLRTPL</span><span class="topo-membrane">NYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-outside">TSLHGYFVFGPTG</span><span class="topo-membrane">CNLEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLVGWSRY</span><span class="topo-outside">IPEGMQCSCGIDYYTPHEETNN</span><span class="topo-membrane">ESFVIYMFVVHFIIPLIVIFFCYGQLV</span><span class="topo-inside">FTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSCFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>40</td>
      <td>1</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>73</td>
      <td>65</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>97</td>
      <td>73</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>110</td>
      <td>97</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>137</td>
      <td>110</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>152</td>
      <td>137</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>179</td>
      <td>152</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>201</td>
      <td>179</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>228</td>
      <td>201</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>252</td>
      <td>228</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>278</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>289</td>
      <td>278</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##s41467-023-40911-9 (3 structures, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8fcz">8FCZ</a></td>
      <td>3.7</td>
      <td>P3(2)21</td>
      <td>Bovine rhodopsin (native, from ROS) in complex with Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>; ground-state (dark) structure</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound via protonated Schiff base), Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8fd1">8FD1</a></td>
      <td>4.25</td>
      <td>P3(2)21</td>
      <td>Bovine rhodopsin (native, from ROS) in complex with Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>; photoactivated (Meta I-like) state</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound via protonated Schiff base), Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8fdo">8FDO</a></td>
      <td>3.7</td>
      <td>P3(2)21</td>
      <td>Bovine rhodopsin (native, from ROS) in complex with Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>; apo-<a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> state</td>
      <td>Nb2 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> (no retinal)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

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
      <td>ROS membrane preparation</td>
      <td>Step-<a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient centrifugation from dark-adapted bovine retinas</td>
      <td>—</td>
      <td></td>
      <td>ROS isolated and washed with isotonic and hypotonic buffers; kept in dark</td>
    </tr>
    <tr>
      <td>Nb2 expression and purification</td>
      <td>Periplasmic expression in <a href="/xray-mp-wiki/organisms/e-coli/">E. coli</a> WK6 cells; <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity followed by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Nb2 with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> expressed in <a href="/xray-mp-wiki/organisms/e-coli/">E. coli</a> WK6; induced with 1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> overnight at 28 C; periplasmic fraction extracted with <a href="/xray-mp-wiki/reagents/buffers/tes/">TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)</a> buffer</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>Mixing bRho (from ROS) with Nb2 in detergent solution</td>
      <td>—</td>
      <td>10% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>bRho/Nb2 complex formed in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Immuno<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (for recombinant Rho)</td>
      <td>1D4-immuno<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>1D4 antibody conjugated to CNBr-activated Sepharose 4B</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.4, 0.25 M NaCl + 10% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Used for recombinant Rho expressed in HEK293 cells. Eluted with C-terminal nonapeptide.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>bRho/Nb2 complex (native rhodopsin from ROS, purified by ConA/<a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a>, in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> detergent)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M Tricine pH 7.8, 25.5% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 600</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Ground-state bRho/Nb2 crystals grown in dark. Photoactivated bRho*/Nb2 crystals obtained by illuminating ground-state crystals with intense green light (~200 uW at 500 nm) for 6 min at 4 C.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8fcz">8FCZ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPW</span><span class="topo-membrane">QFSMLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-inside">HGYFVFGPTG</span><span class="topo-membrane">CNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIE</span><span class="topo-outside">RYVVVCKPMSNFR</span><span class="topo-unknown">FGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNN</span><span class="topo-membrane">ESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-outside">QLVFTV</span><span class="topo-unknown">KEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRM</span><span class="topo-membrane">VIIMVIAFLICWLPYAGVAFYIFTH</span><span class="topo-inside">QGSDF</span><span class="topo-membrane">GPIFMTIPAFFAKTSAVYNPVIYIM</span><span class="topo-outside">MNKQFRNCMVTTLCC</span><span class="topo-unknown">GKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>64</td>
      <td>36</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>99</td>
      <td>72</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>109</td>
      <td>100</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>134</td>
      <td>110</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>147</td>
      <td>135</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>150</td>
      <td>148</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>152</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>200</td>
      <td>174</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>224</td>
      <td>201</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>230</td>
      <td>225</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>240</td>
      <td>231</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>241</td>
      <td>253</td>
      <td>241</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>278</td>
      <td>254</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>283</td>
      <td>279</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>308</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>323</td>
      <td>309</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>324</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8fcz">8FCZ</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAE</span><span class="topo-membrane">PWQFSMLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-outside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-inside">HGYFVFGPTG</span><span class="topo-membrane">CNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIE</span><span class="topo-outside">RYVVVCKPMS</span><span class="topo-unknown">NFRF</span><span class="topo-outside">GE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNN</span><span class="topo-membrane">ESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-outside">QLVF</span><span class="topo-unknown">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRM</span><span class="topo-membrane">VIIMVIAFLICWLPYAGVAFYIFTH</span><span class="topo-inside">QGSDF</span><span class="topo-membrane">GPIFMTIPAFFAKTSAVYNPVIYIM</span><span class="topo-outside">MNKQFRNCMVTTLCC</span><span class="topo-unknown">GKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>33</td>
      <td>1</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>64</td>
      <td>34</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>99</td>
      <td>72</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>109</td>
      <td>100</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>134</td>
      <td>110</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>144</td>
      <td>135</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>145</td>
      <td>148</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>149</td>
      <td>150</td>
      <td>149</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>173</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>200</td>
      <td>174</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>224</td>
      <td>201</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>225</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>240</td>
      <td>229</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>241</td>
      <td>253</td>
      <td>241</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>278</td>
      <td>254</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>283</td>
      <td>279</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>308</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>323</td>
      <td>309</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>324</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8fd1">8FD1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-unknown">QHKKLR</span><span class="topo-outside">TPLN</span><span class="topo-membrane">YILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-outside">ERYVVVCKPMSNFR</span><span class="topo-unknown">FGE</span><span class="topo-outside">NH</span><span class="topo-membrane">AIMGVAFTWVMALACAAP</span><span class="topo-inside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNESF</span><span class="topo-membrane">VIYMFVVHFIIPLIVIFFCY</span><span class="topo-outside">GQLVFTV</span><span class="topo-unknown">KEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRMV</span><span class="topo-membrane">IIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIY</span><span class="topo-outside">IMMNKQFRNCMVTTLCC</span><span class="topo-unknown">GKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>38</td>
      <td>1</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>69</td>
      <td>65</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>70</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>74</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>97</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>147</td>
      <td>134</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>150</td>
      <td>148</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>151</td>
      <td>152</td>
      <td>151</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>170</td>
      <td>153</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>203</td>
      <td>171</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>204</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>230</td>
      <td>224</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>240</td>
      <td>231</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>241</td>
      <td>254</td>
      <td>241</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>286</td>
      <td>275</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>306</td>
      <td>287</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>324</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8fd1">8FD1</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPW</span><span class="topo-membrane">QFSMLAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-outside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-outside">ERYVVVCKPMS</span><span class="topo-unknown">NFRF</span><span class="topo-outside">GENHA</span><span class="topo-membrane">IMGVAFTWVMALACAAPP</span><span class="topo-inside">LVGWSRYIPEGMQCSCGIDYYTPHEETNNESF</span><span class="topo-membrane">VIYMFVVHFIIPLIVIFFC</span><span class="topo-outside">YGQLVF</span><span class="topo-unknown">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIY</span><span class="topo-outside">IMMNKQFRNCMVTTLCC</span><span class="topo-unknown">GKNPLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>35</td>
      <td>1</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>63</td>
      <td>36</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>64</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>97</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>144</td>
      <td>134</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>148</td>
      <td>145</td>
      <td>148</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>149</td>
      <td>153</td>
      <td>149</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>154</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>172</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>222</td>
      <td>204</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>228</td>
      <td>223</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>240</td>
      <td>229</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>306</td>
      <td>287</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>324</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.082666399 (1 structure, 1 sequence)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1l9h">1L9H</a></td>
      <td>2.6</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Bovine rhodopsin, full-length (348 residues), purified from bovine retina rod outer segments</td>
      <td>11-cis <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via protonated Schiff base)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bovine rhodopsin, purified from rod outer segments by ConA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a>, in mixed micelles containing nonyl glucoside and heptanetriol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained at 4 C. Crystal quality was poor with isomorphism issues; twin fractions ranged from 0.1 to 0.4. Three data sets collected independently.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1l9h">1L9H</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKLRTPL</span><span class="topo-membrane">NYILLNLAVADLFMVFGGFTTTLYTS</span><span class="topo-outside">LHGYFVFGPT</span><span class="topo-membrane">GCNLEGFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAI</span><span class="topo-inside">ERYVVVCKPMSNFRFGENHA</span><span class="topo-membrane">IMGVAFTWVMALACAAPPLVGWS</span><span class="topo-outside">RYIPEGMQCSCGIDYYTPHEETN</span><span class="topo-membrane">NESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAA</span><span class="topo-unknown">QQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-unknown">S</span><span class="topo-inside">ATTQKAEKEVTR</span><span class="topo-membrane">MVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSDFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIYIMM</span><span class="topo-inside">NKQFRNCMVTTLCCGKNPLGD</span><span class="topo-unknown">DEA</span><span class="topo-inside">STTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>39</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>73</td>
      <td>65</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>99</td>
      <td>73</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>109</td>
      <td>99</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>134</td>
      <td>109</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>154</td>
      <td>134</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>177</td>
      <td>154</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>200</td>
      <td>177</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>225</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>236</td>
      <td>225</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>241</td>
      <td>236</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>242</td>
      <td>253</td>
      <td>241</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>278</td>
      <td>253</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>287</td>
      <td>278</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>287</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>331</td>
      <td>310</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>334</td>
      <td>331</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>335</td>
      <td>349</td>
      <td>334</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1114089108 (1 structure, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4a4m">4A4M</a></td>
      <td>3.3</td>
      <td>not specified</td>
      <td>Bovine rhodopsin with N2C/D282C/M257Y mutations, expressed in HEK293S-GnTI+ cells, reconstituted with 11-cis-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, light-activated (>515 nm), complexed with GalphaCT peptide (ILENLKDCGLF, K341L mutation)</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (covalently bound to Lys296 via Schiff base, 15-anti conformation); GalphaCT peptide (11 residues)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (under previously reported conditions)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bovine rhodopsin N2C/D282C/M257Y mutant, expressed in HEK293S-GnTI+ cells, reconstituted with 11-cis-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, solubilized and purified in detergent, mixed with dried brain lipid extract, supplemented with GalphaCT peptide (ILENLKDCGLF), selectively activated using >515 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> long-pass filter</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals frozen under dim red light</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown under dim red light. Data collected using focused microbeam. Phases obtained by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using E113Q/GalphaCT structure as search model. One complex per asymmetric unit. R=0.22, R_free=0.26 at 3.3 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4a4m">4A4M</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLE</span><span class="topo-membrane">GFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIYVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>66</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>93</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>93</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>137</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>253</td>
      <td>225</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>275</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>275</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4a4m">4A4M</a> — Chain D (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">-</span><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAA</span><span class="topo-membrane">YMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-inside">KKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFT</span><span class="topo-outside">TTLYTSLHGYFVFGPTGCNLE</span><span class="topo-membrane">GFFATL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAP</span><span class="topo-outside">PLVGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340         </span>
<span class="topo-line"><span class="topo-inside">SATTQKAEKEVTR</span><span class="topo-membrane">MVIIYVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSCFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>2</td>
      <td>43</td>
      <td>1</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>66</td>
      <td>43</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>72</td>
      <td>66</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>93</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>114</td>
      <td>93</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>137</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>151</td>
      <td>137</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>171</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>203</td>
      <td>171</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>225</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>253</td>
      <td>225</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>275</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>275</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>349</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1107##S0907444908017162 (2 structures, 2 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3c9l">3C9L</a></td>
      <td>2.65</td>
      <td>P6_4</td>
      <td>Ground-state bovine rhodopsin, P6_4 untwinned model</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3c9m">3C9M</a></td>
      <td>2.65</td>
      <td>P6_4</td>
      <td>N2C/D282C mutant bovine rhodopsin, P6_4 twinned model</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c9l">3C9L</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-outside">TSLHGYFVFGPT</span><span class="topo-membrane">GCNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGENH</span><span class="topo-membrane">AIMGVAFTWVMALACAAPPLVGWS</span><span class="topo-outside">RYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-inside">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">ATTQKAEKEV</span><span class="topo-membrane">TRMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-outside">IFTHQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLG</span><span class="topo-inside">DD</span><span class="topo-unknown">EASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>64</td>
      <td>40</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>108</td>
      <td>97</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>136</td>
      <td>109</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>152</td>
      <td>137</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>176</td>
      <td>153</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>201</td>
      <td>177</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>228</td>
      <td>202</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>250</td>
      <td>229</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>310</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>329</td>
      <td>327</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>330</td>
      <td>331</td>
      <td>330</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>348</td>
      <td>332</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3c9m">3C9M</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MCGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFS</span><span class="topo-membrane">MLAAYMFLLIMLGFPINFLTLYVTVQ</span><span class="topo-inside">HKKLRTP</span><span class="topo-membrane">LNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-outside">TSLHGYFVFGPTG</span><span class="topo-membrane">CNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERY</span><span class="topo-inside">VVVCKPMSNFRFGEN</span><span class="topo-membrane">HAIMGVAFTWVMALACAAPPLVGWS</span><span class="topo-outside">RYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFFCYGQL</span><span class="topo-inside">VFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">ATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSCFGPIF</span><span class="topo-membrane">MTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-unknown">KQFRNCMVTTLC</span><span class="topo-inside">CGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>38</td>
      <td>1</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>64</td>
      <td>39</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>71</td>
      <td>65</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>72</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>109</td>
      <td>97</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>136</td>
      <td>110</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>151</td>
      <td>137</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>176</td>
      <td>152</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>201</td>
      <td>177</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>226</td>
      <td>202</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>251</td>
      <td>227</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>277</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>287</td>
      <td>278</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>288</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>322</td>
      <td>311</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>323</td>
      <td>326</td>
      <td>323</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1617446114 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: Bovine retina rod cells (disc membrane) for native rhodopsin; HEK293S GnTI- cells for recombinant N2C/D282C stabilized [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant; HEK293S-GnTI+ cells for M257Y mutant
- **Construct**: Native rhodopsin holoprotein with 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore; N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant for pharmacological chaperone studies; N2C/D282C/M257Y triple mutant for constitutively active [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) structure

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop and sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Rh6mr (bovine rhodopsin regenerated with 6-carbon-ring <a href="/xray-mp-wiki/reagents/ligands/retinal/">retinal</a>) or <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a>, solubilized by zinc/alkyl-glucoside extraction method in 1% NG or 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, purified by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL in 50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.4 with 1% NG or 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>2.8-3.4 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a> in 0.05-0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.1-6.6 or 0.05-0.1 M NaAcO buffer pH 5.2-5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals transferred directly from mother liquor into dual-thickness microloops and plunged into liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared after 4-5 days at 4 C, reaching 50-200 um in 7 days. <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> was crystallized under the same conditions excluding 6mr. B-factor sharpening (beta_shar = -178 A^2) applied to diffraction data.</td>
    </tr>
  </tbody>
</table>
</details>


## Biological / Functional Insights

### First X-ray crystal structure of a GPCR

The 2.8 A crystal structure of bovine rhodopsin (Palczewski et al., 2000, PDB 1F88) was the first atomic-resolution structure of any G protein-coupled receptor. The structure revealed the canonical seven-transmembrane helix bundle with the 11-cis-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore covalently bound via a protonated Schiff base to Lys296.

### Stabilized G protein binding site in the M257Y constitutively active mutant

The 3.3 A structure of the M257Y/GalphaCT complex (doi/10.1073##pnas.1114089108) reveals the molecular basis for constitutive activity of the M257Y(6.40) substitution. The introduced tyrosine side chain forms specific interactions with Y223(5.58) in TM5, Y306(7.53) of the NPxxY motif, and R135(3.50) of the E(D)RY motif, selectively stabilizing the open G protein binding site. These aromatic-aromatic and hydrogen bond interactions are unique to the tyrosine substitution, explaining why M257Y shows higher constitutive activity than other substitutions. The light-activated structure crystallized under dim red light with selective >515 [NM](/xray-mp-wiki/reagents/detergents/nm/) photoactivation is virtually identical to [Metarhodopsin II](/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/) obtained by native activation, supporting the use of ligand soaking for GPCR structure determination.

### Agonist-bound active state of rhodopsin (E113Q/GalphaCT complex)

The 3.0 A structure of the constitutively active E113Q mutant in complex with the GalphaCT peptide revealed how all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) acts as an agonist.

### Water-mediated hydrogen bond network reorganization in activation

The active state structure reveals a reorganization of ordered water molecules connecting the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/)-binding pocket to the G-protein-binding surface.

### Ultrafast retinal isomerization captured at 1 ps by TR-SFX

Time-resolved serial femtosecond crystallography at room temperature (1.8 A resolution) captured the bathorhodopsin intermediate at 1 ps after photoactivation.

### Pharmacological chaperones rescue misfolded rhodopsin mutants

Non-[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) small molecules discovered by virtual and thermofluor screening stabilize the N2C/D282C [Opsin (Retinal-Free Rhodopsin Apoprotein)](/xray-mp-wiki/proteins/gpcr/opsin/) mutant.

### Extracellular nanobody Nb2 allosterically modulates rhodopsin activation

Crystal structures of Nb2 in complex with bovine rhodopsin revealed that Nb2 binds to the extracellular surface, interacting with EL2, the N-terminus, and native glycans.

### Photocyclic GPCR activation by Rh6mr with atypical isomerization mechanism

Bovine rhodopsin regenerated with a six-carbon-ring [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore (6mr) featuring a C11=C12 double bond locked in its cis conformation (Rh6mr) employs an atypical isomerization mechanism. Instead of cis-trans isomerization, Rh6mr converts 11-cis to an 11,13-dicis configuration upon light absorption, enabling prolonged Gt activation. The 11,13-dicis isomer thermally reisomerizes to the 11-cis configuration on a slow timescale, allowing Rh6mr to function in a photocyclic manner similar to microbial rhodopsins. The Rh6mr structure was determined by X-ray crystallography, revealing the 11-cis 6mr isomer covalently linked to Lys296 in the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/)-binding pocket.

### Space-group reinterpretation of rhodopsin crystal forms as hexagonal P6_4

Stenkamp (2008, doi/10.1107##S0907444908017162) re-examined two rhodopsin crystal structures originally reported in space group P3_1 (PDB 1gzm and 2j4y). The noncrystallographic twofold axes parallel to the c axis in the trigonal models can be treated as crystallographic symmetry operations in space group P6_4, halving the asymmetric unit and making all protein molecules equivalent. Merohedral twinning correction was also applied for one structure (2j4y/3c9m). The two non-isomorphous crystal structures differ in packing interactions between helix 5 of neighboring molecules via 'sliding' translocation along helical axes, analogous to interactions in Nup58/45.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin)</a> — Apoprotein form of rhodopsin
- <a href="/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/">Metarhodopsin II (Active State)</a> — Later intermediate in rhodopsin photoactivation pathway
- <a href="/xray-mp-wiki/proteins/gpcr/human-rhodopsin-e113q-m257y/">Human Rhodopsin E113Q/M257Y (Constitutively Active)</a> — Related constitutively active mutant GPCR structure
- <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">Squid Rhodopsin</a> — Invertebrate rhodopsin structural comparison
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">Squid Rhodopsin (Primary Photochemical Reaction States)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin Apoprotein)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/human-rhodopsin-e113q-m257y/">Human Rhodopsin E113Q/M257Y Mutant</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/">Metarhodopsin II</a> — Related protein structure
