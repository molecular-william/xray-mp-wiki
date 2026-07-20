---
title: "GLIC (Gloeobacter violaceus Ion Channel)"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature07461, doi/10.1038##nature07462, doi/10.1016##j.str.2012.08.009, doi/10.1016##j.str.2016.02.014, doi/10.1085##jgp.201711803, doi/10.1038##emboj.2013.17, doi/10.1073##pnas.1314997111, doi/10.1073##pnas.1813378116, doi/10.1074##jbc.M116.766964, doi/10.7554##eLife.23886, doi/10.1038##NSMB.1933]
verified: agent
uniprot_id: Q7NDN8
---

# GLIC (Gloeobacter violaceus Ion Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7NDN8">UniProt: Q7NDN8</a>

<span class="expr-badge">Gloeobacter violaceus</span>

## Overview

GLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the cyanobacterium Gloeobacter violaceus. It is a proton-gated ion channel that serves as a bacterial homolog of eukaryotic Cys-loop receptors including nicotinic acetylcholine receptors, GABA-A receptors, and 5-HT3 receptors. GLIC is activated by low pH and inhibited by general anesthetics including ketamine, propofol, and volatile anesthetics. It has been widely used as a model system for understanding pLGIC gating, ion permeation, and anesthetic action. FD/DH electrostatics and FTIR spectroscopy identified E35 as the key proton sensor, with gating mediated by two distinct water-mediated and hydrophobic networks connecting E35 through the ECD-TMD interface to the M2 helix and M2-M3 loop region, bypassing the canonical orthosteric site.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature07461 (1 structure)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>Full-length GLIC wild-type</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature07462 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>Full-length GLIC residues 6-315 (MBP fusion cleaved)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length GLIC with MBP fusion and thrombin cleavage site
- **Tag info**: MBP fusion tag cleaved by thrombin

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
      <td>Protein expression</td>
      <td>E. coli expression</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction and solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (2%/0.02%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Amylose affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Amylose resin</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.02%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography (first)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.02%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Thrombin cleavage</td>
      <td>Protease cleavage</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.02%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography (second)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.02%)</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: GLIC pentamer in 0.02% DDM buffer

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDMVSP</span><span class="topo-outside">PPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-outside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>7</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>217</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>221</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDMVSP</span><span class="topo-outside">PPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-outside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>7</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>217</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>221</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDMVSP</span><span class="topo-outside">PPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-outside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>7</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>217</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>221</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDMVSP</span><span class="topo-outside">PPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-outside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>7</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>217</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>221</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ehz">3EHZ</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDMVSP</span><span class="topo-outside">PPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-outside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>7</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>217</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>221</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>244</td>
      <td>250</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>275</td>
      <td>293</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>294</td>
      <td>316</td>
      <td>Membrane</td>
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
<summary><strong>doi/10.1016##j.str.2012.08.009 (2 structures, 10 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a></td>
      <td>3.25</td>
      <td>P21212</td>
      <td>Full-length GLIC residues 1-355</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a></td>
      <td>2.99</td>
      <td>—</td>
      <td>Full-length GLIC co-crystallized with ketamine</td>
      <td>Ketamine (1 mM, 5 sites per pentamer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GLIC (~10 mg/ml) pre-equilibrated with 0.5 mg/ml E. coli polar lipids</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10%-12% PEG 4000, 225 mM ammonium sulfate, 50 mM sodium acetate buffer pH 3.9-4.1</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>61</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir supplemented with 20% glycerol</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3eam">3EAM</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASIT</span><span class="topo-membrane">RASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>276</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASIT</span><span class="topo-membrane">RASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>276</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f8h">4F8H</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASIT</span><span class="topo-membrane">RASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>276</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
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
<summary><strong>doi/10.1016##j.str.2016.02.014 (2 structures, 10 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a></td>
      <td>2.95</td>
      <td>C2</td>
      <td>Full-length GLIC, MBP fusion cleaved</td>
      <td>Bromoform (pore site, locally closed)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a></td>
      <td>3.15</td>
      <td>C2</td>
      <td>Full-length GLIC, MBP fusion cleaved</td>
      <td>Bromoform (open conformation, intra-subunit sites)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>256</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>256</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>256</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcj">5HCJ</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>256</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETCLPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>276</td>
      <td>255</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETCLPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>276</td>
      <td>255</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETCLPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>276</td>
      <td>255</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETCLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>256</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5hcm">5HCM</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETCLPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>276</td>
      <td>255</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
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
<summary><strong>doi/10.1085##jgp.201711803 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a></td>
      <td>3.12</td>
      <td>—</td>
      <td>Full-length GLIC C27S + K33C + I9'A + N21'C quadruple mutant</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQTLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSY</span><span class="topo-membrane">IPNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLAAHIAFNIL</span><span class="topo-outside">VETCLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">KTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLF</span><span class="topo-outside">FGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>190</td>
      <td>8</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>198</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>214</td>
      <td>218</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>287</td>
      <td>276</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>307</td>
      <td>295</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>310</td>
      <td>315</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQTLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLAAHIAFNIL</span><span class="topo-outside">VETCLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">KTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-outside">FFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>191</td>
      <td>8</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>211</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>287</td>
      <td>276</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>306</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>314</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQTLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLAAHIAFNIL</span><span class="topo-outside">VETCLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">KTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-outside">FFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>191</td>
      <td>8</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>199</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>214</td>
      <td>218</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>287</td>
      <td>276</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>306</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>314</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQTLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFW</span><span class="topo-inside">STSY</span><span class="topo-membrane">EANVTLVVSTLAAHIAFNIL</span><span class="topo-outside">VETCLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">KTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-outside">FFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>191</td>
      <td>8</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>199</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>214</td>
      <td>218</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>287</td>
      <td>276</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>306</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>314</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v6n">5V6N</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">PPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQTLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLAAHIAFNIL</span><span class="topo-outside">VETCLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310</span>
<span class="topo-line"><span class="topo-outside">KTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-outside">FFGF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>191</td>
      <td>8</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>211</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>214</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>242</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>287</td>
      <td>276</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>306</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>314</td>
      <td>317</td>
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
<summary><strong>doi/10.1038##emboj.2013.17 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a></td>
      <td>2.4</td>
      <td>C2</td>
      <td>Full-length GLIC residues 1-355</td>
      <td>Br-, Cs+, acetate, sulfate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASIT</span><span class="topo-membrane">RASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>276</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hfi">4HFI</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASIT</span><span class="topo-membrane">RASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>255</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>276</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
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
<summary><strong>doi/10.1073##pnas.1314997111 (2 structures, 10 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a></td>
      <td>4.35</td>
      <td>P21</td>
      <td>Full-length GLIC from G. violaceus, wild-type</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a></td>
      <td>not specified</td>
      <td>P212121</td>
      <td>Full-length GLIC with C-terminal His10 tag, expressed in insect cells</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

**Purification:**

- **Expression system**: E. coli / Insect cells (Sf9)
- **Expression construct**: Full-length GLIC (untagged) for pH 7 structure; GLIC_His10 (C-terminal His10) for pH 4 structure
- **Tag info**: His10 for GLIC_His10 expressed in insect cells

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
      <td>Expression</td>
      <td>E. coli expression for pH 7 GLIC</td>
      <td>—</td>
      <td></td>
      <td>GLIC expressed and purified as described in Bocquet et al., 2009</td>
    </tr>
    <tr>
      <td>Expression (alternative)</td>
      <td>Insect cell (Sf9) expression for GLIC_His10</td>
      <td>—</td>
      <td></td>
      <td>GLIC fused to C-terminal His10 tag produced in insect cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Standard GLIC purification protocol</td>
      <td>—</td>
      <td></td>
      <td>Purified as per ref. 8 (Bocquet et al., 2007)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion with dehydrating cryoprotection</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified GLIC at neutral pH</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial diffraction to 8.5 A. Elaborate dehydrating cryoprotection protocol and extensive screening improved diffraction to 4.35 A. Space group P21 with four pentamers per asymmetric unit (~6200 residues). NCS averaging over 20 chains and B-factor sharpening improved map quality.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GLIC_His10 at pH 4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>GLIC_His10 produced in insect cells, crystallized at pH 4. Space group P212121. Shows coexistence of locally closed and open conformations.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4npp">4NPP</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AQDM</span><span class="topo-outside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-inside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320         </span>
<span class="topo-line"><span class="topo-outside">LVETNLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-inside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-outside">FF</span><span class="topo-unknown">GFGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>222</td>
      <td>240</td>
      <td>Membrane</td>
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
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>329</td>
      <td>316</td>
      <td>329</td>
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
<summary><strong>doi/10.1073##pnas.1813378116 (7 structures, 35 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>2.95</td>
      <td>—</td>
      <td>GLIC Q193M mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>3.39</td>
      <td>—</td>
      <td>GLIC Q193L mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>2.58</td>
      <td>—</td>
      <td>GLIC Q193C mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>GLIC Y197F mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>GLIC K248C mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>GLIC K248A mutant</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>GLIC E243C mutant</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hzw">6HZW</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQY</span><span class="topo-membrane">FSYIPNIILPMLFILFISWTAFW</span><span class="topo-outside">STSYE</span><span class="topo-membrane">ANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LVET</span><span class="topo-inside">NLPKTPY</span><span class="topo-membrane">MTYTGAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>5</td>
      <td>194</td>
      <td>5</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>251</td>
      <td>245</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>275</td>
      <td>252</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
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
<summary><strong>doi/10.1074##jbc.M116.766964 (3 structures, 15 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a></td>
      <td>3.3</td>
      <td>C2</td>
      <td>GLIC K33C-L246C locally-closed (LC) mutant</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bromobarbital">Bromobarbital</a> (pore site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a></td>
      <td>2.99</td>
      <td>C2</td>
      <td>GLIC K33C-L246C locally-closed (LC) mutant</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/selenocyanobarbital">Selenocyanobarbital</a> (pore site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a></td>
      <td>3.5</td>
      <td>C2</td>
      <td>GLIC K33C-L246C locally-closed (LC) mutant</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/thiopental">Thiopental</a> (pore site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYIPNII</span><span class="topo-membrane">LPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFN</span><span class="topo-inside">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNCPKTPYMTYTGAI</span><span class="topo-membrane">IFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIIL</span><span class="topo-inside">AFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>202</td>
      <td>5</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>222</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>240</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>259</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>311</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYIPNII</span><span class="topo-membrane">LPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFN</span><span class="topo-inside">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNCPKTPYMTYTGAI</span><span class="topo-membrane">IFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIIL</span><span class="topo-inside">AFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>202</td>
      <td>5</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>222</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>240</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>311</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYIPNII</span><span class="topo-membrane">LPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFN</span><span class="topo-inside">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNCPKTPYMTYTGAI</span><span class="topo-membrane">IFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIIL</span><span class="topo-inside">AFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>202</td>
      <td>5</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>222</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>240</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>311</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYIPNII</span><span class="topo-membrane">LPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFN</span><span class="topo-inside">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNCPKTPYMTYTGAI</span><span class="topo-membrane">IFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIIL</span><span class="topo-inside">AFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>202</td>
      <td>5</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>222</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>240</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>259</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>311</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4h">5L4H</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYIPNII</span><span class="topo-membrane">LPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFN</span><span class="topo-inside">I</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-inside">LVETNCPKTPYMTYTGAI</span><span class="topo-membrane">IFMIYLFYFVAVIEVTVQ</span><span class="topo-outside">HYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIIL</span><span class="topo-inside">AFLFF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>202</td>
      <td>5</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>222</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>258</td>
      <td>240</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>259</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>291</td>
      <td>277</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>311</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAF</span><span class="topo-outside">WSTSYEA</span><span class="topo-membrane">NVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>223</td>
      <td>217</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
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
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAF</span><span class="topo-outside">WSTSYEA</span><span class="topo-membrane">NVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>223</td>
      <td>217</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>274</td>
      <td>256</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAF</span><span class="topo-outside">WSTSYEA</span><span class="topo-membrane">NVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>223</td>
      <td>217</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>274</td>
      <td>256</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAF</span><span class="topo-outside">WSTSYEA</span><span class="topo-membrane">NVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>223</td>
      <td>217</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l47">5L47</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAF</span><span class="topo-outside">WSTSYEA</span><span class="topo-membrane">NVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTY</span><span class="topo-membrane">TGAIIFMIYLFYFVAVIEVT</span><span class="topo-outside">VQHYLKVESQPARAASITRA</span><span class="topo-membrane">SRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>216</td>
      <td>199</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>223</td>
      <td>217</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>254</td>
      <td>243</td>
      <td>254</td>
      <td>Inside</td>
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
      <td>294</td>
      <td>275</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>313</td>
      <td>295</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l4e">5L4E</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GQDM</span><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIESYSLDDCAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FDSQTLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTAFWS</span><span class="topo-outside">TSY</span><span class="topo-membrane">EANVTLVVSTLIAHIAFNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       </span>
<span class="topo-line"><span class="topo-membrane">LV</span><span class="topo-inside">ETNCPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIEVTV</span><span class="topo-outside">QHYLKVESQPARAASI</span><span class="topo-membrane">TRASRIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span><span class="topo-unknown">GF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>5</td>
      <td>198</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>218</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>221</td>
      <td>219</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>242</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>291</td>
      <td>276</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>315</td>
      <td>314</td>
      <td>315</td>
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
<summary><strong>doi/10.7554##eLife.23886 (1 structure, 5 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a></td>
      <td>3.25</td>
      <td>C121</td>
      <td>Full-length GLIC wild-type, co-crystallized with DHA</td>
      <td>Docosahexaenoic acid (DHA); phospholipid (PLC)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

**Purification:**

- **Expression system**: E. coli (C43)
- **Expression construct**: Full-length GLIC with N-terminal MBP fusion and HRV 3C protease cleavage site, in modified pET26b vector
- **Tag info**: MBP tag cleaved by HRV 3C protease

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
      <td>Protein expression</td>
      <td>E. coli (C43) expression in terrific broth with 50 ug/ml kanamycin, induced with 0.2 mM IPTG at 18 C overnight</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Homogenization and centrifugation at 100,000 x g</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>100 mM NaCl, 20 mM Tris-HCl pH 7.4, protease inhibitors + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (40 mM)</td>
      <td></td>
    </tr>
    <tr>
      <td>Amylose affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Amylose resin</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.5 mM)</td>
      <td>Eluted with 20 mM maltose</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>HRV 3C protease cleavage</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.5 mM)</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>100 mM NaCl, 20 mM Tris-HCl pH 7.4 + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.5 mM)</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: GLIC pentamer in 100 mM NaCl, 20 mM Tris-HCl pH 7.4, 0.5 mM DDM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GLIC (9-10 mg/ml) pre-incubated with 50 uM DHA and 0.5 mg/ml E. coli polar extract for 1 hr on ice</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>225 mM ammonium sulfate, 50 mM sodium acetate pH 3.9-4.2, 9-12% PEG4000</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>61</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir supplemented with 30% ethyleneglycol</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTA</span><span class="topo-outside">FWSTSYEAN</span><span class="topo-membrane">VTLVVSTLIAHIAFNI</span><span class="topo-inside">LVET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-inside">NLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIE</span><span class="topo-outside">VTVQHYLKVESQPARAASITRAS</span><span class="topo-membrane">RIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>211</td>
      <td>199</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>220</td>
      <td>216</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>236</td>
      <td>225</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>268</td>
      <td>256</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>273</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTA</span><span class="topo-outside">FWSTSYEAN</span><span class="topo-membrane">VTLVVSTLIAHIAFNI</span><span class="topo-inside">LVET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-inside">NLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIE</span><span class="topo-outside">VTVQHYLKVESQPARAASITRAS</span><span class="topo-membrane">RIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>211</td>
      <td>199</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>220</td>
      <td>216</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>236</td>
      <td>225</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>268</td>
      <td>256</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>273</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTA</span><span class="topo-outside">FWSTSYEANV</span><span class="topo-membrane">TLVVSTLIAHIAFNI</span><span class="topo-inside">LVET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-inside">NLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIE</span><span class="topo-outside">VTVQHYLKVESQPARAASITRAS</span><span class="topo-membrane">RIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>211</td>
      <td>199</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>221</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>236</td>
      <td>226</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>268</td>
      <td>256</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>273</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTA</span><span class="topo-outside">FWSTSYEANV</span><span class="topo-membrane">TLVVSTLIAHIAFNI</span><span class="topo-inside">LVET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-inside">NLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIE</span><span class="topo-outside">VTVQHYLKVESQPARAASITRAS</span><span class="topo-membrane">RIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>211</td>
      <td>199</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>221</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>236</td>
      <td>226</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>268</td>
      <td>256</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>273</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5j0z">5J0Z</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">VSPPPPIADEPLTVNTGIYLIECYSLDDKAETFKVNAFLSLSWKDRRLAFDPVRSGVRVKTYEPEAIWIPEIRFVNVENARDADVVDISVSPDGTVQYLERFSARVLSPLDFRRYPFDSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TLHIYLIVRSVDTRNIVLAVDLEKVGKNDDVFLTGWDIESFTAVVKPANFALEDRLESKLDYQLRISRQYFSYI</span><span class="topo-membrane">PNIILPMLFILFISWTA</span><span class="topo-outside">FWSTSYEANV</span><span class="topo-membrane">TLVVSTLIAHIAFNI</span><span class="topo-inside">LVET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310 </span>
<span class="topo-line"><span class="topo-inside">NLPKTPYMTYT</span><span class="topo-membrane">GAIIFMIYLFYFVAVIE</span><span class="topo-outside">VTVQHYLKVESQPARAASITRAS</span><span class="topo-membrane">RIAFPVVFLLANIILAFL</span><span class="topo-inside">FF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>194</td>
      <td>5</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>211</td>
      <td>199</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>221</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>236</td>
      <td>226</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>241</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>268</td>
      <td>256</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>291</td>
      <td>273</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>309</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>311</td>
      <td>314</td>
      <td>315</td>
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
<summary><strong>doi/10.1038##NSMB.1933 (0 structures)</strong></summary>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from G. violaceus expressed as MBP fusion
- **Notes**: MBP preceded by E. coli pELB signal sequence and decahistidine (His10) tag. Also expressed in insect cells (Sf9) for GLIC_His10 with C-terminal His10 tag.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length GLIC with MBP-His10 fusion and E. coli pELB signal sequence
- **Tag info**: MBP-His10, cleaved by HRV 3C protease

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
      <td>Protein expression</td>
      <td>E. coli expression</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>HRV 3C protease cleavage</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>MBP cleaved off, removed by rebinding to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>10 mM Tris pH 7.5, 150 mM NaCl + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/ml in 10 mM Tris pH 7.5, 150 mM NaCl, 0.5 mM DDM

</details>


## Biological / Functional Insights

### Open conformation of GLIC reveals gating mechanism of pLGICs

The 2.9 A GLIC structure at pH 4.6 reveals open conformation. Key rearrangements: quaternary twist of pentamer, rotation of each extracellular beta-sandwich domain, tilt of M2 and M3 away from pore axis.

### Ketamine binding to an intersubunit cavity

Ketamine binds to a pre-existing cavity between adjacent subunits in the extracellular domain. Five molecules per pentamer. Site near homologous orthosteric agonist-binding site.

### Resting state structure of GLIC at neutral pH

The pH 7 (neutral) structure of GLIC reveals the resting state at 4.35 A resolution. The ECD displays large intrinsic structural flexibility with significant deviations from C5 symmetry (rmsd 1.2 A in ECD vs 0.2 A in TMD). The pore is closed by an upper bend of helix M2 (as in locally closed form) and a kink of helix M1. A marked quaternary change is observed involving both a twist and a blooming motion. Detachment of inner and outer beta sheets reshapes the ligand-binding cavity and a cavity near a known divalent cation binding site.

### Open and LC forms coexist at pH 4

GLIC_His10 crystallized at pH 4 in space group P212121 shows both locally closed and open conformations coexisting as discrete states. The M2 helix and M2-M3 loop show dual conformations, with the energy landscape made of two wells in the presence of the ligand (protons).

### Critical residues at the ECD-TMD interface

Phe195 (F195A shows loss of function), Leu246 (L246A shows loss of function, interacts with ECD via hydrophobic cleft), and Asp32-Arg192 salt bridge (D32N shifts pH50, D32N-R192Q double mutant shows loss of function) play key roles in gating.

### Barbiturate binding in the ion channel pore

The first X-ray structures of barbiturates bound to a pLGIC were determined using GLIC K33C-L246C (locally-closed mutant). Bromobarbital (3.3 A, PDB 5L4H), selenocyanobarbital (2.99 A, PDB 5L47), and thiopental (3.5 A, PDB 5L4E) all bind within the central ion channel pore between residues 2' and 9' of the M2 helix. Hydrogen bonds between barbiturate carbonyl groups and 6' serines are the primary interactions, with van der Waals interactions involving 9' isoleucines. Thiopental adopts an inverted orientation due to its branched C5 tail. Docking calculations across closed, open, and desensitized states predict barbiturates preferentially stabilize the closed conformation, explaining their inhibitory mechanism on cationic pLGICs. The same pore site also binds xenon and bromoform.

### Structural fluctuations prefigure the gating transition

Principal component analysis of the 20 monomers in the pH 7 asymmetric unit reveals that the first PC of fluctuations has an overlap of 0.88 with the quaternary transition and 0.75 with the tertiary transition between pH 7 and pH 4 forms. This demonstrates that intrinsic fluctuations of the unperturbed system prefigure the response to ligand binding, consistent with linear response theory.

### Sequential model for pLGIC activation

The gating pathway starts at the extracellular tip with orthosteric site contraction and beta sheet movements, propagates through the ECD-TMD interface involving the beta1-beta2 loop and M2-M3 loop, and results in M2 helix tilting and pore opening. This is consistent with experimental data from nicotinic receptor studies.

### E35 is the key proton sensor for GLIC gating

Using finite difference Poisson-Boltzmann/Debye-Huckel (FD/DH) electrostatics calculations and FTIR spectroscopy combined with site-directed mutagenesis, E35 was identified as the key proton sensor with a measured individual pKa of 5.8, close to the electrophysiological pH50 of 5.1. E35 is located in front of loop F, far from the canonical orthosteric site. It establishes a polar interaction with T158 from loop F, connecting to a water-mediated hydrogen bond network reaching Q193 in the pre-M1 region and further to the ECD-TMD interface.

### Two networks connect E35 to the transmembrane domain

The gating signal from E35 propagates through two distinct networks. Network 1 (hydrophilic): E35 → water network → Q193 (pre-M1) → R192-D122-D32 electrostatic triad → Y197 → K248 → E243 → N239 → H235, reaching the middle of the M2 helix in the adjacent subunit. Network 2 (hydrophobic): Y197-P120-Y119 interactions → L246 (M2-M3 loop) → P247 and T251, encircling the ECD-TMD interface. Q193M/L mutations trap the channel in a nonconductive LC1 conformation. The two networks converge at H235 and the pre-M1 region, showing loop F acts as an allosteric site instead of the classic orthosteric site for gating in GLIC.

### DHA binding site and desensitized state of GLIC

Docosahexaenoic acid (DHA), an omega-3 polyunsaturated fatty acid abundant in synaptic membranes, enhances agonist-induced desensitization in GLIC. The 3.25 A crystal structure (PDB: 5J0Z) reveals DHA bound at the channel periphery near the M4 helix, interacting with Arg118 in the Cys-loop (beta6-beta7 loop). Mutation R118A reduces the DHA effect, validating the binding site. The GLIC-DHA complex adopts a potentially desensitized conformation distinct from previously observed pLGIC states: the extracellular half of M2 is splayed open (reminiscent of open state), while the intracellular half is constricted at Ile9' with loss of both water and permeant ions. DEER spectroscopy in nanodiscs shows M4 undergoes an outward tilt (up to 4 A) during desensitization, with increased lipid exposure of the TMD-facing side. CW-EPR reveals Pro300 acts as a hinge for M4 motion. The DHA effect is absent in the non-desensitizing I9'A/H11'F mutant, confirming the state is agonist-induced and not an uncoupled conformation.

### General anesthetic binding site in GLIC revealed by propofol and desflurane structures

X-ray structures of GLIC complexed with propofol (3.3 A) and desflurane (3.2 A) reveal a common general-anesthetic binding site pre-existing in the apo-structure in the upper part of the transmembrane domain of each protomer. Both molecules bind within an intra-subunit cavity and establish van der Waals interactions with residues from M1 (I201, I202, M205, L206), M2 (V242), M3 (Y254, T255, I258, I259), M4 (N307, F303), and the beta6-beta7 loop (Y119). Propofol binds at the entrance of the cavity while the smaller desflurane binds deeper inside. Mutation of residues within this site (I202Y, V242M, T255A) alters both the intrinsic ionic response of GLIC and its general-anesthetic pharmacology. The binding site is located on the backside of the pore-lining M2 helices at the level of the gate, close to the TMD-ECD interface, suggesting the mechanism involves reorganization of the binding site during gating through M2 and M3 helix tilting. Nearby ordered lipids are displaced upon propofol binding, suggesting general anaesthetics may compete with endogenous lipid modulators.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/">Pentameric Ligand-Gated Ion Channel (pLGIC)</a> — GLIC is a prokaryotic member of the pLGIC superfamily
- <a href="/xray-mp-wiki/reagents/ligands/ketamine/">Ketamine</a> — Ketamine binds to intersubunit cavity in ECD, inhibits GLIC
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia ligand-gated Ion Channel)</a> — Direct structural comparison between closed (ELIC) and open (GLIC) states
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary purification and crystallization detergent
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer component in SEC buffer (10 mM Tris pH 7.5)
- <a href="/xray-mp-wiki/methods/expression-systems/xenopus-oocytes/">Xenopus Oocytes Expression System</a> — GLIC and mutants expressed in Xenopus oocytes for electrophysiology
- <a href="/xray-mp-wiki/reagents/additives/peg-4000/">PEG 4000</a> — Crystallization precipitant
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> — Crystallization buffer at pH 4
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/stelic/">sTeLIC (Tevnia jerichonana Endosymbiont pLGIC)</a> — Homologous prokaryotic pLGIC; sTeLIC shows an even more open pore conformation than GLIC
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/barbiturate-binding-mechanism/">Barbiturate Binding Mechanism in pLGICs</a> — First X-ray structures of barbiturates bound to GLIC revealed the pore binding site
- <a href="/xray-mp-wiki/reagents/ligands/bromobarbital/">Bromobarbital</a> — Barbiturate co-crystallized with GLIC-LC (PDB 5L4H)
- <a href="/xray-mp-wiki/reagents/ligands/thiopental/">Thiopental</a> — Clinically used barbiturate co-crystallized with GLIC-LC (PDB 5L4E)
- <a href="/xray-mp-wiki/reagents/ligands/selenocyanobarbital/">Selenocyanobarbital</a> — Synthetic barbiturate co-crystallized with GLIC-LC (PDB 5L47)
