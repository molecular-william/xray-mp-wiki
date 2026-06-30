---
title: "TmYidC (Thermotoga maritima YidC Insertase)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbamem.2021.183825, doi/10.1096##fj.201700893RR]
verified: false
---

# TmYidC (Thermotoga maritima YidC Insertase)

## Overview

TmYidC is the YidC insertase/chaperone from the thermophilic bacterium Thermotoga maritima. YidC is a member of the evolutionarily conserved YidC/Alb3/Oxa1 membrane protein family that plays essential roles in the insertion and folding of membrane proteins. The crystal structure of TmYidC at 3.4 A resolution (PDB 6Y86) revealed the N-terminal amphipathic helix (N-AH) for the first time, which acts as a membrane recognition helix. The structure shows an active insertase conformation. Molecular dynamics simulations showed that N-AH lies on the periplasmic side of the membrane forming an angle of about 15 deg with the membrane surface. The C1 region exhibits high flexibility, enabling switching between insertase and chaperone conformations.

## Publications

### doi/10.1016##j.bbamem.2021.183825

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6y86">6Y86</a></td>
      <td>3.4</td>
      <td>P 41 21 2</td>
      <td>Full-length TmYidC, residues 1-425</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length TmYidC with C-terminal hexahistidine tag

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
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>n-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>TmYidC expressed in E. coli and purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Final polishing step. TmYidC exists as a monomer in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solution.</td>
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
      <td>Notes</td>
      <td>Crystallized using vapor diffusion method in presence of <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. Structure solved by molecular replacement using P1 domain of TmYidC as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6y86">6Y86</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVLRKVVAILLAILPIFLFAVEPIKVVRSEKEIVVLTRFEEYHFDLEKGILKDFYTLVDGRKHVFTYGNDGFDVLDEGTPLTVIEEPIVTGVGKVSEGFSDEVSIVYNYGYVKKIFTIKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NENYTFFVDIENSKPVDVTVPRVSVDTSTDRYLENYFASFNPKTRTLVLLKHDEGLLFEGTLKVNGQKRFIVFMGPNKRTLIKKAFPEDYDVLIKALVNIPGFNKWYDSVFYGLVWFFWW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LKDLTKNFGWAI</span><span class="topo-membrane">MLFTLIVRLILYPLYHAQT</span><span class="topo-inside">KSLINMRKLQPQIEAIKKKYKDPTKQQEALLKLYREAGVN</span><span class="topo-membrane">PASGCLMLLIQLPIFMLL</span><span class="topo-outside">WSVIRYYVEEFAYSGSFLIWKDLSAGGFSNN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-outside">W</span><span class="topo-membrane">LFLVITIVASYYTTLLTS</span><span class="topo-inside">QDA</span><span class="topo-membrane">RTAWQGIIMSVIFPFLFV</span><span class="topo-outside">GLPSGL</span><span class="topo-membrane">FLYYATNTLIQLAVTYYT</span><span class="topo-inside">Y</span></span>
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
      <td>252</td>
      <td>1</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>271</td>
      <td>253</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>311</td>
      <td>272</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>329</td>
      <td>312</td>
      <td>329</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>361</td>
      <td>330</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>379</td>
      <td>362</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>382</td>
      <td>380</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>400</td>
      <td>383</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>406</td>
      <td>401</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>424</td>
      <td>407</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>425</td>
      <td>425</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1096##fj.201700893RR

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5y82">5Y82</a></td>
      <td>2.5</td>
      <td>P4(1)</td>
      <td>TmPD (Thermotoga maritima YidC periplasmic domain, residues 24-222)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5y83">5Y83</a></td>
      <td>3.8</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length TmYidC, residues 1-445</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length TmYidC with C-terminal hexahistidine tag

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5y83">5Y83</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVLRKVVAILLAILPIFLFAV</span><span class="topo-outside">EPVVVVRSEKEIVVLTRFEEYHFDLEKGILKDFYTLVDGRKHVFTYGNDGFDVLDEGTPLTVIEEPIVTGVGKVSEGFSDEVSIVYNYGYVKKIFTIKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">NENYTFFVDIESSKPVDVTVPRVSVDTSTDRYLENYFASFNPKTRTLVLLKHDEGLLFEGTLKVNGQKRFIVFMGPNKRTLIKKAFPEDYDVLIKALVNIPGFNKWYDSVFYGLVWFFWW</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LKDLTKNFGW</span><span class="topo-membrane">AIMLFTLIVRLILY</span><span class="topo-inside">PLYHAQ</span><span class="topo-unknown">TKSLINMRKLQPQIEAIKKKYKDPTKQQEALLKLYREAGVNPASG</span><span class="topo-inside">CL</span><span class="topo-membrane">MLLIQLPIFMLLW</span><span class="topo-outside">SVIRYYVEEFAYSGSFLIWKDLSAGGF</span><span class="topo-membrane">SNN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450 </span>
<span class="topo-line"><span class="topo-membrane">WLFLVITIVAS</span><span class="topo-inside">YYT</span><span class="topo-unknown">TLLTSQDARTAWQG</span><span class="topo-inside">I</span><span class="topo-membrane">IMSVIFPFLFV</span><span class="topo-outside">GLPSG</span><span class="topo-membrane">LFLYYATNTLIQLA</span><span class="topo-inside">VTY</span><span class="topo-unknown">YTYKRYKIKGLTTRELLGLPKKAHHHHHH</span></span>
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
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>250</td>
      <td>22</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>264</td>
      <td>251</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>270</td>
      <td>265</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>315</td>
      <td>271</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>317</td>
      <td>316</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>330</td>
      <td>318</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>357</td>
      <td>331</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>371</td>
      <td>358</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>374</td>
      <td>372</td>
      <td>374</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>388</td>
      <td>375</td>
      <td>388</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>389</td>
      <td>389</td>
      <td>389</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>400</td>
      <td>390</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>405</td>
      <td>401</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>419</td>
      <td>406</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>420</td>
      <td>422</td>
      <td>420</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>451</td>
      <td>423</td>
      <td>451</td>
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

### N-terminal amphipathic helix as membrane recognition helix

The N-AH (residues 1-19) is tilted on the membrane surface at approximately 15 deg, as confirmed by MD simulations in POPE:POPG (3:1) bilayers. The N-terminus is embedded in the membrane, acting as a recognition helix to localize YidC to the lipid bilayer.

### Dual insertase and chaperone conformations

YidC functions both as an insertase (independent membrane protein insertion) and as a chaperone (in complex with SecYEG translocon). The C1 region (residues 282-308) exhibits high flexibility with deviations up to 2.5 nm from the crystal structure, enabling functional switching between conformations. The EH1 helix (residues 226-244) acts as a mechanical lever coordinating domain movements.

### Species-specific SecY interaction

Complementation assays showed that TmYidC cannot rescue E. coli YidC depletion, but a chimera with EcYidC's N-AH (YidC61) partially rescues growth. Crosslinking experiments identified N-AH as a major contact site with SecY, suggesting species-specific interaction with the Sec translocon.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/yidc-oxa1-alb3-insertase-family/">YidC/Oxa1/Alb3 Insertase Family</a> — YidC is the founding member of this conserved membrane protein family
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for purification of TmYidC
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) IMAC used for purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) used as polishing step
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Structure solved by MR using P1 domain as search model
- <a href="/xray-mp-wiki/reagents/detergents/dm">n-Decyl-beta-D-Maltoside (DM)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> — Immobilized metal affinity chromatography resin
