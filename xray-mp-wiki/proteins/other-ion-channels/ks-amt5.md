---
title: "Ks-Amt5 Ammonium Sensor Histidine Kinase from Candidatus Kuenenia stuttgartiensis"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-02637-3]
verified: pdb-pass
uniprot_id: Q1Q357
---

# Ks-Amt5 Ammonium Sensor Histidine Kinase from Candidatus Kuenenia stuttgartiensis

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q1Q357">UniProt: Q1Q357</a>

<span class="expr-badge">Kuenenia stuttgartiensis</span>

## Overview

Ks-Amt5 (gene locus kust_3690) from the anammox bacterium "Candidatus Kuenenia stuttgartiensis" is a unique bifunctional membrane protein that combines an N-terminal ammonium transporter (Amt) domain with a C-terminal histidine kinase (HK) domain. Unlike canonical Amt/Rh family transporters that mediate ammonium uptake, Ks-Amt5 has been repurposed as an ammonium sensor/transducer. The Amt domain retains the conserved structural features of the Amt/Rh fold but contains a novel high-affinity ammonium binding site within the membrane core that is absent in assimilatory Amt proteins. The HK domain autophosphorylates at His406 in a manner modulated by ammonium binding to the Amt domain, enabling downstream signaling. The crystal structure of the Amt domain was determined at high resolution (PDB 6EU6), while the HK domains exhibited structural disorder in the crystal lattice.


## Publications

### doi/10.1038##s41467-017-02637-3

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6eu6">6EU6</a></td>
      <td>2.90</td>
      <td>P1</td>
      <td>Ks-Amt5 Amt domain (residues M1-A408)</td>
      <td>NH4+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length Ks-Amt5 with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Notes**: Also produced isolated Amt domain (residues M1-A408) and isolated HK domain (residues L426-K679) constructs

**Purification:**

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length Ks-Amt5 with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Tag info**: C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (via LE linker)

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
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>Cell membranes isolated after cell disruption</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>n-Decyl-β-D-maltopyranoside (DM)</td>
      <td>Protein solubilized from membranes</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Standard Ni-NTA purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>0.09% CYMAL-5</td>
      <td>SEC in buffer containing 0.09% CYMAL-5. Protein eluted as a trimer.</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Ks-Amt5 in SEC buffer with 0.09% CYMAL-5
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Ks-Amt5 in 0.09% CYMAL-5</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in space group P1. The Amt domain (residues M1-A408) formed crystal contacts; the HK domains were structurally disordered.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eu6">6EU6</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MENIQININHLWVI</span><span class="topo-membrane">MAACMVFLMQLGFTSYE</span><span class="topo-inside">TGFSQSKNAISIA</span><span class="topo-membrane">LRNLVDTLISSLVFFSVGFGFM</span><span class="topo-outside">FGKSYMGLIGIDLFFANDLALHPNTLSYSFF</span><span class="topo-membrane">FFQMVFASTAATILTGA</span><span class="topo-inside">IAERSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FIP</span><span class="topo-membrane">NIAGTAFIVAIIYPIFGHWA</span><span class="topo-outside">WGNLFSPDQTGWLKELGFI</span><span class="topo-membrane">DFAGATVVHSIGGWFAMAA</span><span class="topo-inside">AIMVGPRIDKYNPDGSSNRIGLHNVPLA</span><span class="topo-membrane">TLGTFFLWFGWFGFNGGS</span><span class="topo-outside">LLRVSVNIGLV</span><span class="topo-membrane">IL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NTNMAAASAGVSALIFI</span><span class="topo-inside">YATRKRIEAGS</span><span class="topo-membrane">LFTAILAGLVAITASS</span><span class="topo-outside">NMVTP</span><span class="topo-membrane">VSAVAIGLITGILAIIAE</span><span class="topo-inside">GFIEKTLKIDDPV</span><span class="topo-membrane">SAIAVHGVGGVIGTLCVAIF</span><span class="topo-outside">AQKSYLLAENGSRMHQL</span><span class="topo-membrane">GIQ</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-membrane">ALGVIVAFSWSFGLGMLFFLCL</span><span class="topo-inside">KKVKRLRVTPEEEKRGLNVAEAA</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>45</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>97</td>
      <td>67</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>123</td>
      <td>115</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>143</td>
      <td>124</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>144</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>163</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>209</td>
      <td>182</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>238</td>
      <td>228</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>239</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>268</td>
      <td>258</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>285</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>307</td>
      <td>290</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>320</td>
      <td>308</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>340</td>
      <td>321</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>382</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>405</td>
      <td>383</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eu6">6EU6</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MENIQININHLWVI</span><span class="topo-membrane">MAACMVFLMQLGFTSYE</span><span class="topo-inside">TGFSQSKNAISIA</span><span class="topo-membrane">LRNLVDTLISSLVFFSVGFGFM</span><span class="topo-outside">FGKSYMGLIGIDLFFANDLALHPNTLSYSFF</span><span class="topo-membrane">FFQMVFASTAATILTGA</span><span class="topo-inside">IAERSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FIP</span><span class="topo-membrane">NIAGTAFIVAIIYPIFGHWA</span><span class="topo-outside">WGNLFSPDQTGWLKELGFI</span><span class="topo-membrane">DFAGATVVHSIGGWFAMAA</span><span class="topo-inside">AIMVGPRIDKYNPDGSSNRIGLHNVPLA</span><span class="topo-membrane">TLGTFFLWFGWFGFNGGS</span><span class="topo-outside">LLRVSVNIGLV</span><span class="topo-membrane">IL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NTNMAAASAGVSALIFI</span><span class="topo-inside">YATRKRIEAGS</span><span class="topo-membrane">LFTAILAGLVAITASS</span><span class="topo-outside">NMVTP</span><span class="topo-membrane">VSAVAIGLITGILAIIAE</span><span class="topo-inside">GFIEKTLKIDDPV</span><span class="topo-membrane">SAIAVHGVGGVIGTLCVAIF</span><span class="topo-outside">AQKSYLLAENGSRMHQL</span><span class="topo-membrane">GIQ</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-membrane">ALGVIVAFSWSFGLGMLFFLCL</span><span class="topo-inside">KKVKRLRVTPEEEKRGLNVAEAA</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>45</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>97</td>
      <td>67</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>123</td>
      <td>115</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>143</td>
      <td>124</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>144</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>163</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>209</td>
      <td>182</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>238</td>
      <td>228</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>239</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>268</td>
      <td>258</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>285</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>307</td>
      <td>290</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>320</td>
      <td>308</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>340</td>
      <td>321</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>382</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>405</td>
      <td>383</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eu6">6EU6</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MENIQININHLWVI</span><span class="topo-membrane">MAACMVFLMQLGFTSYE</span><span class="topo-inside">TGFSQSKNAISIA</span><span class="topo-membrane">LRNLVDTLISSLVFFSVGFGFM</span><span class="topo-outside">FGKSYMGLIGIDLFFANDLALHPNTLSYSFF</span><span class="topo-membrane">FFQMVFASTAATILTGA</span><span class="topo-inside">IAERSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FIP</span><span class="topo-membrane">NIAGTAFIVAIIYPIFGHWA</span><span class="topo-outside">WGNLFSPDQTGWLKELGFI</span><span class="topo-membrane">DFAGATVVHSIGGWFAMAA</span><span class="topo-inside">AIMVGPRIDKYNPDGSSNRIGLHNVPLA</span><span class="topo-membrane">TLGTFFLWFGWFGFNGGS</span><span class="topo-outside">LLRVSVNIGLV</span><span class="topo-membrane">IL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">NTNMAAASAGVSALIFI</span><span class="topo-inside">YATRKRIEAGS</span><span class="topo-membrane">LFTAILAGLVAITASS</span><span class="topo-outside">NMVTP</span><span class="topo-membrane">VSAVAIGLITGILAIIAE</span><span class="topo-inside">GFIEKTLKIDDPV</span><span class="topo-membrane">SAIAVHGVGGVIGTLCVAIF</span><span class="topo-outside">AQKSYLLAENGSRMHQL</span><span class="topo-membrane">GIQ</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-membrane">ALGVIVAFSWSFGLGMLFFLCL</span><span class="topo-inside">KKVKRLRVTPEEEKRGLNVAEAA</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>44</td>
      <td>32</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>45</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>97</td>
      <td>67</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>114</td>
      <td>98</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>123</td>
      <td>115</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>143</td>
      <td>124</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>162</td>
      <td>144</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>163</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>209</td>
      <td>182</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>238</td>
      <td>228</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>257</td>
      <td>239</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>268</td>
      <td>258</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>285</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>307</td>
      <td>290</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>320</td>
      <td>308</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>340</td>
      <td>321</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>382</td>
      <td>358</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>405</td>
      <td>383</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Repurposed ammonium transporter as a signal transducer

Ks-Amt5 represents the prototype of a modular sensor-transducer system that evolved from a ubiquitous ammonium transporter into a specific receptor for NH4+ cations. The Amt domain initiates a transport cycle at the selectivity filter but diverts two substrate cations into a high-affinity binding site within the membrane core, triggering conformational changes that modulate the fused histidine kinase domain.

### Novel high-affinity ammonium binding site

A unique cation-binding site situated within the membrane (~10 Å from the membrane boundary) coordinates two ammonium cations through a network of residues: Q24, E31 (helix h1), N47, D50, T51 (helix h2), and T109, T112 (helix h4). Only two acidic residues (E31 and D50) provide charge compensation. The binding geometry with five ligands per cation and short bond distances (2.2-2.4 Å) is distinct from octahedral Na+ coordination.

### Trimeric architecture with trimeric HK association

Ks-Amt5 elutes as a trimer in SEC, consistent with the strictly trimeric architecture of all Amt family members. The association of HK modules in a trimeric protein core is unprecedented, as most known HKs function as dimers. The elongated loop 5 (G186-N205, 19 residues) in the Amt domain is substantially longer than the 10-12 residues found in other Amt/Rh family members and is positioned near the C-terminus of the neighboring monomer, suggesting a mechanistic coupling between the two domains.

### Ammonium-dependent modulation of kinase activity

The in vitro kinase activity of full-length Ks-Amt5 shows strong modulation by NH4+ concentration: phosphorylation levels increase steeply at low NH4+ concentrations, followed by a decrease at high concentrations. This biphasic response is consistent with a sensor optimized for detecting low external ammonium levels. The isolated HK domain is insensitive to NH4+, confirming that the Amt domain mediates signal reception.

### Loss of transport function

Unlike canonical Amt transporters that conduct NH3, Ks-Amt5 does not translocate ammonium/methylammonium ions efficiently. The translocation pathway is obstructed by bulkier side chains (F27, Y30, F34) in helix h1 compared to Af-Amt1 (V23, F26, M30), and by a ~0.8 Å shift of the His pair (H171, H326) into the channel. This arrangement leaves the selectivity filter intact but prevents NH4+ from traversing the membrane.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/">Rh/Amt/MEP Protein Family</a> — Ks-Amt5 is a member of the Amt/Rh family with conserved structural features
- <a href="/xray-mp-wiki/concepts/signaling-receptors/two-component-signaling-system/">Two-Component Signaling System (TCS) in Membrane Sensors</a> — Ks-Amt5 functions as an ammonium sensor histidine kinase, a novel TCS architecture
- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">Ammonium Transporter AmtB (E. coli)</a> — Structural comparison with canonical Amt transporter
- <a href="/xray-mp-wiki/proteins/other-ion-channels/a-fulgidus-amt1/">Amt-1 ammonium transporter from Archaeoglobus fulgidus</a> — Structural comparison; Ks-Amt5 Amt domain aligns with 1.2 Å RMSD to Af-Amt1
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> — Fusion tag for crystallization or purification
