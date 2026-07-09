---
title: "NavAe1p Prokaryotic Sodium Channel Pore"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2013.10.010]
verified: regex
uniprot_id: P02699
---

# NavAe1p Prokaryotic Sodium Channel Pore

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02699">UniProt: P02699</a>

<span class="expr-badge">Bos taurus</span>

## Overview

NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel NavAe1 from Alkalilimnicola ehrlichei, a bacterium found in Mono Lake, California. The crystal structure at 4.0 A resolution reveals a closed conformation of the complete pore domain with a cytoplasmic tail including a helical neck and coiled-coil region. Key findings include the S6 activation gate position, the role of the cytoplasmic tail neck in stabilizing the closed state, and an outer ion binding site at the selectivity filter that reveals a previously unknown calcium binding determinant conserved in eukaryotic voltage-gated calcium channels.

## Publications

### doi/10.1016##j.jmb.2013.10.010

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a></td>
      <td>4.0 A</td>
      <td>I222</td>
      <td>NavAe1p pore-only construct from Alkalilimnicola ehrlichei; includes transmembrane pore domain (S5, P1, P2, S6) and full cytoplasmic tail (neck + coiled-coil); homotetramer</td>
      <td>Calcium ion at outer ion binding site (selectivity filter outer mouth), coordinated by 4 Ser198 side-chain oxygens and 4 water molecules</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a></td>
      <td>3.8 A</td>
      <td>P4212</td>
      <td>NavAe1p pore-only construct, low-calcium crystallization condition</td>
      <td>None (no anomalous density at outer ion site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a></td>
      <td>4.0 A</td>
      <td>I222</td>
      <td>NavAe1p H245G mutant pore-only construct; no Ca2+ at neck ion or outer ion site</td>
      <td>None (no anomalous density for neck ion or outer ion)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK 293 mammalian cells (for functional electrophysiology); NavAe1p purified from prior publication (Shaya et al. 2011)
- **Construct**: NavAe1p pore-only construct (residues corresponding to pore domain S5-P1-P2-S6 plus cytoplasmic tail with neck and coiled-coil); full-length NavAe1 for electrophysiology; H245G mutant for structural comparison

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
      <td>Expression and solubilization</td>
      <td>Transient transfection of HEK 293 cells; membrane extraction and solubilization</td>
      <td>--</td>
      <td>Described in prior publication (Shaya et al. 2011) + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (N-Dodecyl-Beta-D-Maltoside) at 0.25-0.3 mM</td>
      <td>NavAe1p expressed and purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> as previously described in Shaya et al. 2011 (ref 19 in the paper). Full-length NavAe1 expressed in HEK 293 cells for functional studies.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>0.25 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 200 mM NaCl, 20 mM Na-HEPES pH 8.0 + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (N-Dodecyl-Beta-D-Maltoside) at 0.25 mM</td>
      <td>Final SEC buffer exchange prior to concentration for crystallization</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Ultrafiltration</td>
      <td>Amicon Ultra-15 100-kDa molecular mass cutoff (Millipore)</td>
      <td>0.25 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 200 mM NaCl, 20 mM Na-HEPES pH 8.0 + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> at 0.25 mM</td>
      <td>Concentrated to ~15 mg/ml for high-calcium condition; ~13.5 mg/ml for low-calcium condition</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>13.5 mg/ml NavAe1p, 0.25 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5 M TMAO, 200 mM NaCl, 20 mM Na-HEPES pH 8.0</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM CaCl2, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 100 mM Na-acetate pH 5.0 (high-calcium condition)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 weeks (high-calcium); crystals grew to ~200 um x 70 um x 15 um</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>I222 crystals. Protein-TMAO solution (0.7 ul) mixed with 0.7 ul mother liquor mixed with agarose (0.25% final) solidified at room temperature. Anomalous scattering confirmed Ca2+ at outer ion site.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>13.5 mg/ml NavAe1p, 0.25 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 200 mM NaCl, 20 mM Na-HEPES pH 8.0</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM MgCl2, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 100 mM MOPS pH 6.5 (low-calcium condition)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~2 weeks; crystals appeared in 2 days, grew to ~200 um x 50 um x 50 um</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P4212 crystals. No anomalous density at outer ion site.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSML</span><span class="topo-membrane">AAYMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-outside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-outside">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEK</span><span class="topo-membrane">EVTRMVIIMVIAFLICWLPYAGVAF</span><span class="topo-inside">YIFTHQGSDFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>40</td>
      <td>1</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>68</td>
      <td>66</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>96</td>
      <td>69</td>
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
      <td>150</td>
      <td>138</td>
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
      <td>248</td>
      <td>229</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>273</td>
      <td>249</td>
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
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Outside</td>
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

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSML</span><span class="topo-membrane">AAYMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-outside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-outside">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEK</span><span class="topo-membrane">EVTRMVIIMVIAFLICWLPYAGVAF</span><span class="topo-inside">YIFTHQGSDFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>40</td>
      <td>1</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>68</td>
      <td>66</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>96</td>
      <td>69</td>
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
      <td>150</td>
      <td>138</td>
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
      <td>248</td>
      <td>229</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>273</td>
      <td>249</td>
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
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Outside</td>
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

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSML</span><span class="topo-membrane">AAYMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-outside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCN</span><span class="topo-membrane">LEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLV</span><span class="topo-inside">GWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLVF</span><span class="topo-outside">TVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEK</span><span class="topo-membrane">EVTRMVIIMVIAFLICWLPYAGVAF</span><span class="topo-inside">YIFTHQGSDFGPIFMTI</span><span class="topo-membrane">PAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
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
      <td>40</td>
      <td>1</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>41</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>68</td>
      <td>66</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>96</td>
      <td>69</td>
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
      <td>150</td>
      <td>138</td>
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
      <td>248</td>
      <td>229</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>273</td>
      <td>249</td>
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
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Outside</td>
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

## Biological / Functional Insights

### S6 activation gate position at Met241

The intracellular gate is occluded by Met241 at the S6 C-terminus. Mutation of the equivalent residue (NavSp1 M220A) causes dramatic negative shifts in both activation (delta V1/2 = -49.8 mV) and inactivation (delta V1/2 = -40.0 mV) voltage dependence, indicating this residue is critical for stabilizing the closed state. Residues above the gate (F233, I237 equivalent to NavSp1 L212A and I216A) affect inactivation only, not activation, shifting inactivation voltage dependence by ~14 mV without affecting activation.

### Cytoplasmic tail neck stabilizes the closed state

The neck region (6 helical turns connecting S6 to the coiled-coil) is rich in charged/polar residues (15/20). Destabilizing the neck with [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) substitutions causes negative shifts in activation voltage dependence, with the largest perturbation (7Gly mutation) having effects comparable to activation gate disruption. The neck appears to stabilize the closed state through its helical structure, and opening proceeds with radial expansion of the gate region accompanied by an order-to-disorder transition in the neck.

### Outer ion binding site at the selectivity filter

A calcium ion binds at the selectivity filter outer mouth, coordinated by 4 Ser198 side-chain oxygens and 4 water molecules (coordination number 8). This "outer ion" site is 10.7 A from the inner ion site and marks the entry/dehydration point for ions entering the selectivity filter. The (+1) position serine is conserved and analogous to a previously unrecognized calcium binding determinant in mammalian voltage-gated calcium channels (CaV). Mutation of the equivalent residue in CaV1.2 (D707N) reduces calcium affinity by ~6-fold.

### Commonality between BacNav and eukaryotic VGICs

The structural and functional findings underscore deep evolutionary links between bacterial sodium channels (BacNav) and eukaryotic voltage-gated ion channels. The outer ion binding site architecture is conserved between BacNav and CaV channels. The cytoplasmic tail with its coiled-coil domain has parallels in eukaryotic Kv7 and TRP channels. Multiple ion binding sites in the selectivity filter support the multi-ion pore model shared across the VGIC superfamily.

### BacNav gating mechanism

A model for BacNav gating is proposed: in the closed state, the intracellular pore is occluded by the activation gate constriction (Met241). Opening proceeds with radial expansion of this region accompanied by an order-to-disorder transition in the neck. The abundance of polar and charged neck residues may aid the transition to the open/disordered state and assist in permeant ion escape into the cytoplasm. The neck and activation gate are strongly coupled, as mutations at both cause parallel shifts in activation and inactivation voltage dependence.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-Beta-D-Maltoside (DDM)</a> — Primary solubilization detergent used throughout purification (0.25-0.3 mM)
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)</a> — Purification and crystallization buffer at 20 mM pH 8.0
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> — Crystallization buffer at 100 mM pH 5.0 for high-calcium condition
- <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS (4-Morpholineethanesulfonic Acid)</a> — Crystallization buffer at 100 mM pH 6.5 for low-calcium condition
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol) 400</a> — Crystallization precipitant at 30% in both conditions
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride</a> — Crystallization additive (200 mM) in high-calcium condition; bound at outer ion site
- <a href="/xray-mp-wiki/reagents/additives/tmao/">Trimethylamine N-Oxide (TMAO)</a> — Crystallization additive (0.5 M) in high-calcium condition to stabilize protein
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Crystallization additive (200 mM) in low-calcium condition
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Prokaryotic ion channel with similar modular pore domain architecture
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/">Ilyobacter Tartaricus C-Subunit</a> — Prokaryotic membrane protein with coiled-coil cytoplasmic domain architecture
