---
title: "GluCl (C. elegans Glutamate-Gated Chloride Channel)"
created: 2026-06-02
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10139, doi/10.1038##emboj.2013.17]
verified: agent
uniprot_id: O17793
---

# GluCl (C. elegans Glutamate-Gated Chloride Channel)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O17793">UniProt: O17793</a>

<span class="expr-badge">Caenorhabditis elegans</span>

## Overview

GluCl is the glutamate-gated chloride channel from Caenorhabditis elegans, a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor superfamily. It mediates fast inhibitory neurotransmission and is the molecular target of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), a broad-spectrum antiparasitic agent used to treat river blindness. The first X-ray structure of an inhibitory anion-selective Cys-loop receptor was determined for the GluCl-Fab complex at 3.3 A resolution (Nature 2011), revealing mechanisms of activation, permeation, and allosteric modulation by [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), glutamate, and picrotoxin.


## Publications

### doi/10.1038##nature10139

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a></td>
      <td>3.3 A</td>
      <td>Not specified</td>
      <td>GluCl_cryst — residues 41–343 of C. elegans GluCl alpha with M3–M4 loop (K345–K402) replaced by Ala-Gly-Thr tripeptide; complexed with Fab</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a> (allosteric agonist), <a href="/xray-mp-wiki/reagents/substrates/l-glutamate/">L Glutamate</a>, picrotoxin</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus-infected Sf9 insect cells
- **Construct**: Codon-optimized full-length C. elegans GluCl alpha with native signal peptide and C-terminal 8xHis tag; M3–M4 loop (K345–K402) replaced by AGT tripeptide for crystallization; 41 N-terminal and 6 C-terminal residues deleted

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
      <td>Cell disruption</td>
      <td>Emulsiflex-C5 homogenization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a></td>
      <td>Cells harvested 72-96 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Differential centrifugation</td>
      <td>—</td>
      <td></td>
      <td>Crude membranes collected at 125,000g</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl + 0.25 g C12M (n-dodecyl-beta-D-maltopyranoside) per g membranes</td>
      <td>Solubilized membranes clarified at 125,000g</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> Co2+-affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 1 mM C12M, 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution)</td>
      <td></td>
    </tr>
    <tr>
      <td>Fab complex formation</td>
      <td>Mixing with excess Fab, size-exclusion chromatography</td>
      <td>Superose 6 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 1 mM C12M</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion at 4 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GluCl_cryst–Fab complex at 1–2 mg/ml with synthetic lipids (<a href="/xray-mp-wiki/reagents/lipids/popc/">Popc</a> or DPPC at 0.02%) and 0.1 mM <a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>21–23% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400, 50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> pH 4.5, 70 mM sodium chloride</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to ~3.3 A resolution. Additional structures obtained by soaking with glutamate, picrotoxin, or iodide. Fab derived from mouse monoclonal antibody against properly folded pentameric GluCl.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 400: 21–23 % [precipitant] (Peg 400)  
- Citrate: 50 mM [buffer]  
- Sodium Chloride: 70 mM [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYL</span><span class="topo-membrane">LQLYIPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQSA</span><span class="topo-outside">GINSQLPPVSYIKAID</span><span class="topo-membrane">VWIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYWSR</span><span class="topo-outside">FGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>217</td>
      <td>1</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>262</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>340</td>
      <td>338</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYL</span><span class="topo-membrane">LQLYIPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQSA</span><span class="topo-outside">GINSQLPPVSYIKAID</span><span class="topo-membrane">VWIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYWSR</span><span class="topo-outside">FGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>217</td>
      <td>1</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>262</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>340</td>
      <td>338</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYL</span><span class="topo-membrane">LQLYIPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQSA</span><span class="topo-outside">GINSQLPPVSYIKAID</span><span class="topo-membrane">VWIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYWSR</span><span class="topo-outside">FG</span><span class="topo-unknown">HHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>217</td>
      <td>1</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>262</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>339</td>
      <td>338</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>347</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYL</span><span class="topo-membrane">LQLYIPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQSA</span><span class="topo-outside">GINSQLPPVSYIKAID</span><span class="topo-membrane">VWIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYWSR</span><span class="topo-outside">FGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>217</td>
      <td>1</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>262</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>340</td>
      <td>338</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rif">3RIF</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYL</span><span class="topo-membrane">LQLYIPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQSA</span><span class="topo-outside">GINSQLPPVSYIKAID</span><span class="topo-membrane">VWIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYWSR</span><span class="topo-outside">FGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>217</td>
      <td>1</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>237</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>242</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>277</td>
      <td>262</td>
      <td>277</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>316</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>340</td>
      <td>338</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##emboj.2013.17

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a></td>
      <td>3.3 A</td>
      <td>Not specified in supplementary paper</td>
      <td>Full-length GluCl from Caenorhabditis elegans</td>
      <td>GABA, <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus-infected Sf9 insect cells
- **Construct**: Codon-optimized full-length C. elegans GluCl alpha with native signal peptide and C-terminal 8xHis tag; M3–M4 loop (K345–K402) replaced by AGT tripeptide for crystallization; 41 N-terminal and 6 C-terminal residues deleted

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYLLQLY</span><span class="topo-membrane">IPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQ</span><span class="topo-outside">SAGINSQLPPVSYIKAIDV</span><span class="topo-membrane">WIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILY</span><span class="topo-outside">WSRFGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>221</td>
      <td>1</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>237</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>260</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>335</td>
      <td>340</td>
      <td>335</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYLLQLY</span><span class="topo-membrane">IPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQ</span><span class="topo-outside">SAGINSQLPPVSYIKAIDV</span><span class="topo-membrane">WIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILY</span><span class="topo-outside">WSRFGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>221</td>
      <td>1</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>237</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>260</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>335</td>
      <td>340</td>
      <td>335</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYLLQLY</span><span class="topo-membrane">IPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQ</span><span class="topo-outside">SAGINSQLPPVSYIKAIDV</span><span class="topo-membrane">WIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYW</span><span class="topo-outside">SRFG</span><span class="topo-unknown">HHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>221</td>
      <td>1</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>237</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>260</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>335</td>
      <td>316</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>339</td>
      <td>336</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>347</td>
      <td>340</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYLLQLY</span><span class="topo-membrane">IPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQ</span><span class="topo-outside">SAGINSQLPPVSYIKAIDV</span><span class="topo-membrane">WIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILYW</span><span class="topo-outside">SRFGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>221</td>
      <td>1</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>237</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>260</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>335</td>
      <td>316</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>340</td>
      <td>336</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rhw">3RHW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">SDSKILAHLFTSGYDFRVRPPTDNGGPVVVSVNMLLRTISKIDVVNMEYSAQLTLRESWIDKRLSYGVKGDGQPDFVILTVGHQIWMPDTFFPNEKQAYKHTIDKPNVLIRIHNDGTVLY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SVRISLVLSCPMYLQYYPMDVQQCSIDLASYAYTTKDIEYLWKEHSPLQLKVGLSSSLPSFQLTNTSTTYCTSVTNTGIYSCLRTTIQLKREFSFYLLQLY</span><span class="topo-membrane">IPSCMLVIVSWVSFWF</span><span class="topo-inside">DRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">IPARVTLGVTTLLTMTAQ</span><span class="topo-outside">SAGINSQLPPVSYIKAIDV</span><span class="topo-membrane">WIGACMTFIFCALLEFALVN</span><span class="topo-inside">HIANAGTTEWNDISKRV</span><span class="topo-membrane">DLISRALFPVLFFVFNILY</span><span class="topo-outside">WSRFGH</span><span class="topo-unknown">HHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>221</td>
      <td>1</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>237</td>
      <td>222</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>238</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>242</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>278</td>
      <td>260</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>315</td>
      <td>299</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>334</td>
      <td>316</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>335</td>
      <td>340</td>
      <td>335</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>347</td>
      <td>341</td>
      <td>347</td>
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

### First structure of an inhibitory anion-selective Cys-loop receptor

The 3.3 A X-ray structure of the GluCl-Fab complex with [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) represents the first three-dimensional structure of an inhibitory anion-selective Cys-loop receptor. The homopentameric receptor reveals the architecture of the neurotransmitter-binding sites, the transmembrane pore, and the allosteric [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site at the protein-lipid interface between M1, M2, and M3 helices.

### Ivermectin binds at subunit interfaces in the transmembrane domain

[Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/), a macrocyclic lactone used to treat river blindness, binds at each GluCl subunit interface on the periphery of the transmembrane domains, wedged between M3 on the principal (+) subunit and M1 on the complementary (-) subunit. It makes hydrogen bonds with the main-chain carbonyl of Leu218 (M1) and contacts with M2 and the M2-M3 loop. [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) acts as a partial allosteric agonist, stabilizing an open-pore conformation and pre-organizing the glutamate binding site ~30 A away.

### Glutamate binding site and specificity

Glutamate binds in the classical agonist site at subunit interfaces in the extracellular domain, between loops from the (+) subunit and beta strands from the (-) subunit. Loop C adopts a closed conformation. The alpha-amino group interacts with Tyr200 via cation-pi interaction, and the alpha- and gamma-carboxylates are coordinated by Arg37 and Arg56. The binding pocket has strong positive electrostatic potential and is selective for small dicarboxylate L-amino acids.

### Picrotoxin occludes the open pore

Picrotoxin, an open-channel blocker, binds at the cytosolic base of the transmembrane pore on the five-fold symmetry axis. The fused tricyclic rings point toward the extracellular side near 2' Thr residues, while the isoprenyl tail points toward the cytoplasm near -2' Pro residues. Picrotoxin binding confirms the pore is in an open, conducting conformation with a minimum diameter of ~4.6 A at the -2' Pro girdle.

### Ion selectivity mechanism

The pore constriction at -2' Pro residues (diameter ~4.6 A) and positive electrostatic potential from oriented M2 helix dipoles confer anion selectivity without any positively charged pore-lining residues. Four iodide (heavy atom analog of chloride) binding sites were identified at the cytosolic base of the pore in electropositive pockets formed by -2' Pro, -1' Ala, and -3' Ile residues. The -1' position preserves the anion pocket in chloride- selective channels, while cation channels have a conserved glutamate at this position that fills the pocket and imposes negative potential.

### Comparison of GluCl with GLIC reveals conserved pore architecture

The 3.3 A resolution structure of GluCl was used as a comparison to the 2.4 A [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) structure in molecular dynamics simulations and electrostatics calculations. AquaSol and MD simulations of GluCl revealed anion density within the pore, with the Thr6' and Thr2' side chains actively contributing to anion translocation. This contrasts with [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/), where Ser6' and Thr2' contribute to cation translocation. The conserved cis-proline in the Cys-loop was also confirmed in GluCl, with the Phe/Tyr-Pro motif at the apex of the Cys-loop adopting a cis conformation that forms a hydrogen bond with M3, similar to [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/).

### Ivermectin binding site in GluCl (archetypal eukaryotic pLGIC)

GluCl serves as the archetypal eukaryotic pLGIC structure, revealing an [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site at the interface between the extracellular and transmembrane domains. This site is distinct from the orthosteric neurotransmitter-binding site and represents an allosteric modulator pocket. The GluCl structure has been instrumental in understanding the mechanism of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) action as an antiparasitic agent and its selectivity for invertebrate channels.

### Cis-proline in the Cys-loop of GluCl

The high-resolution [Glic](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) structure confirmed that the conserved proline residue in the Phe/Tyr-Pro-Phe/Met motif at the apex of the Cys-loop adopts a cis conformation in GluCl, contrary to earlier structures that built it in trans. Residual electron density in the original GluCl structure showed both positive and negative peaks near the carbonyl group of this proline, indicating the trans conformation should be inverted. The cis conformation makes the residual density vanish after refinement. This cis-proline forms a hydrogen bond with residue 20' in the M3 helix, extending M3 through the Cys-loop and articulating the transmembrane domain with respect to the extracellular domain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC (Gloeobacter violaceus Ion Channel)</a> — Bacterial pLGIC homolog; used for direct structural comparison
- <a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a> — High-affinity allosteric modulator of GluCl; antiparasitic drug target
- <a href="/xray-mp-wiki/reagents/ligands/glutamate/">L-Glutamate</a> — Endogenous neurotransmitter that activates GluCl
- <a href="/xray-mp-wiki/reagents/ligands/picrotoxin/">Picrotoxin</a> — Open-channel blocker confirming the pore is in an open conformation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating via Plug Domain Displacement</a> — Related gating mechanism in Cys-loop receptors
- <a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a> — Referenced in glucl text
- <a href="/xray-mp-wiki/reagents/substrates/l-glutamate/">L Glutamate</a> — Referenced in glucl text
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Referenced in glucl text
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a> — Referenced in glucl text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in glucl text
