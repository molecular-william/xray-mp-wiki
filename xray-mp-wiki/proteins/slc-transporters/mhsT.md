---
title: "MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NSMB.2894, doi/10.15252##embj.2020105164]
verified: agent
uniprot_id: Q9KDT3
---

# MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans

<div class="expr-badges"><span class="expr-badge expr-l-lactis">L. lactis</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KDT3">UniProt: Q9KDT3</a>

<span class="expr-badge">Bacillus halodurans</span>

## Overview

MhsT is a multi-hydrophobic amino acid transporter from Bacillus halodurans belonging to the [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/). It mediates the Na+-coupled uptake of hydrophobic amino acids including L-tryptophan, L-tyrosine, [L-Phenylalanine](/xray-mp-wiki/reagents/ligands/l-phenylalanine/), and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/). Initial crystal structures of MhsT in occluded inward-facing states with bound Na+ ions and L-tryptophan revealed a novel mechanism involving TM5 unwinding at a conserved GlyX9Pro motif, providing a solvent pathway for intracellular Na+ release from the Na2 site. Subsequent structures with six different substrates (L-Tyr, L-4-F-Phe, L-Phe, L-Ile, L-Leu, L-Val) revealed how a Gly-Met-Gly (GMG) motif in the unwound region of TM6 tailors the binding site volume to accommodate substrates of different sizes. The GMG loop shifts inward by ~2 A for small aliphatic substrates, reducing binding pocket volume from ~230 A^3 to ~144 A^3. A conserved Glu66 residue maintains interaction with the GMG loop through water-mediated hydrogen bonds in all states.


## Publications

### doi/10.1038##NSMB.2894

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4us3">4US3</a></td>
      <td>2.1 A</td>
      <td>not specified</td>
      <td>Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved</td>
      <td>Na+ (2 ions), L-tryptophan</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4us3">4US3</a></td>
      <td>2.6 A</td>
      <td>not specified</td>
      <td>Full-length MhsT from B. halodurans, residues 1-453, His-tag cleaved, LCP crystal form</td>
      <td>Na+ (2 ions), L-tryptophan</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: mhsT gene cloned into plasmid pNZ8048, N-terminal 10x histidine tag with TEV protease cleavage site

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>--</td>
      <td>not specified + not specified</td>
      <td>Expressed in Lactococcus lactis NZ9000, purified as previously described</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm">n-dodecyl-beta-D-maltopyranoside</a>)</td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) affinity resin</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">His-tag</a>ged MhsT captured on <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta)</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV protease</a> digestion</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) affinity resin (<a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)ond column)</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV protease</a> used to remove N-terminal histidine tag, MhsT-containing flow-through collected</td>
    </tr>
    <tr>
      <td>Second affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) affinity resin (Qiagen)</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)ond <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) column to remove cleaved <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">His-tag</a> and <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV protease</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>HiLiDe (hydrophobic interaction-driven crystallization)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MhsT at 7 mg/mL after <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV</a> cleavage and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)ond <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> purification, in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>MhsT crystallized using HiLiDe method, yielding structure at 2.1 A resolution. Crystallographic dimer formed through intracellular half of helix 11 and intracellular loop 5.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MhsT in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>MhsT crystallized using <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> method, yielding structure at 2.6 A resolution. Similar overall structure to HiLiDe form (0.65 A RMSD) but differs at TM5 region.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4us3">4US3</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLGF</span><span class="topo-membrane">ILAAMGSAVGLGNIWRFSYVT</span><span class="topo-inside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVLAEF</span><span class="topo-outside">TIGRRAQSDAVGSFEKLAPGKP</span><span class="topo-membrane">WKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYIT</span><span class="topo-inside">GQLWSAPAEGFGGFFEGFIANP</span><span class="topo-membrane">TLPLFWQALFMIATIWIVAI</span><span class="topo-outside">GVKKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAI</span><span class="topo-inside">YSLTLGGAKEGLAFLFSPDWSALKD</span><span class="topo-membrane">PGVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIMI</span><span class="topo-inside">FPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFD</span><span class="topo-inside">SIRLGP</span><span class="topo-membrane">IVGIAFFILLGAAALSSAVSLLEVPVAYF</span><span class="topo-outside">MRKFDWSRK</span><span class="topo-membrane">QAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSSLS</span><span class="topo-inside">FGVLGEVTIIPGL</span><span class="topo-membrane">NIFDSVDFIASSVFLPLGGMIIALF</span><span class="topo-outside">IGWGWK</span><span class="topo-unknown">TSDALA</span><span class="topo-outside">ESDLTDSVWGK</span><span class="topo-membrane">LWILSLRFIAPIAILIVFLSAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>10</td>
      <td>20</td>
      <td>8</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>19</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>68</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>126</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>148</td>
      <td>125</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>147</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>173</td>
      <td>167</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>219</td>
      <td>193</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>218</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>254</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>292</td>
      <td>275</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>291</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>302</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>338</td>
      <td>308</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>347</td>
      <td>337</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>367</td>
      <td>346</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>380</td>
      <td>366</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>405</td>
      <td>379</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>411</td>
      <td>404</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>417</td>
      <td>410</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>418</td>
      <td>428</td>
      <td>416</td>
      <td>426</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>450</td>
      <td>427</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4us3">4US3</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLGF</span><span class="topo-membrane">ILAAMGSAVGLGNIWRFSYVT</span><span class="topo-inside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVLAEF</span><span class="topo-outside">TIGRRAQSDAVGSFEKLAPGKP</span><span class="topo-membrane">WKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYIT</span><span class="topo-inside">GQLWSAPAEGFGGFFEGFIANP</span><span class="topo-membrane">TLPLFWQALFMIATIWIVAI</span><span class="topo-outside">GVKKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAI</span><span class="topo-inside">YSLTLGGAKEGLAFLFSPDWSALKD</span><span class="topo-membrane">PGVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIMI</span><span class="topo-inside">FPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFD</span><span class="topo-inside">SIRLGP</span><span class="topo-membrane">IVGIAFFILLGAAALSSAVSLLEVPVAYF</span><span class="topo-outside">MRKFDWSRK</span><span class="topo-membrane">QAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSSLS</span><span class="topo-inside">FGVLGEVTIIPGL</span><span class="topo-membrane">NIFDSVDFIASSVFLPLGGMIIALF</span><span class="topo-outside">IGWGWK</span><span class="topo-unknown">TSDALA</span><span class="topo-outside">ESDLTDSVWGK</span><span class="topo-membrane">LWILSLRFIAPIAILIVFLSAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>10</td>
      <td>20</td>
      <td>8</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>19</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>68</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>126</td>
      <td>90</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>148</td>
      <td>125</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>147</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>173</td>
      <td>167</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>219</td>
      <td>193</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>218</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>254</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>292</td>
      <td>275</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>291</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>302</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>338</td>
      <td>308</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>347</td>
      <td>337</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>367</td>
      <td>346</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>380</td>
      <td>366</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>405</td>
      <td>379</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>411</td>
      <td>404</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>417</td>
      <td>410</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>418</td>
      <td>428</td>
      <td>416</td>
      <td>426</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>450</td>
      <td>427</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.15252##embj.2020105164

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu7">6YU7</a></td>
      <td>2.3 A</td>
      <td>P2</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a>, crystallized in OG/NG</td>
      <td>Na+, L-Tyrosine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu4">6YU4</a></td>
      <td>2.26 A</td>
      <td>P2</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a></td>
      <td>Na+, L-4-Fluoro-Phenylalanine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu3">6YU3</a></td>
      <td>2.25 A</td>
      <td>P2</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a></td>
      <td>Na+, <a href="/xray-mp-wiki/reagents/ligands/l-phenylalanine/">L-Phenylalanine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu2">6YU2</a></td>
      <td>2.3 A</td>
      <td>P2_1</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a></td>
      <td>Na+, L-Isoleucine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu6">6YU6</a></td>
      <td>2.1 A</td>
      <td>P2_1</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a></td>
      <td>Na+, <a href="/xray-mp-wiki/reagents/ligands/l-leucine/">L-Leucine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yu5">6YU5</a></td>
      <td>2.1 A</td>
      <td>P2_1</td>
      <td>Full-length MhsT, religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a></td>
      <td>Na+, L-Valine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Lactococcus lactis NZ9000
- **Construct**: mhsT gene cloned into plasmid pNZ8048, N-terminal 10x histidine tag with TEV protease cleavage site

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">hanging-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MhsT religipidated in <a href="/xray-mp-wiki/reagents/lipids/dopc/">DOPC</a> at 9 mg/mL, 4CMC <a href="/xray-mp-wiki/reagents/detergents/og">OG</a> or NG detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14-24% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.3-0.5 M NaCl, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> or HEPES-NaOH pH 7.0, 5-10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5% TMANO</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized by <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a> in hanging drops using immersion oil as sealing agent. Substrates included Tyr, 4F-Phe, Phe, Ile, Leu, Val. Diffraction data collected at Diamond Light Source (I24, I04) and Swiss Light Source (PXI).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu7">6YU7</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLG</span><span class="topo-membrane">FILAAMGSAVGLGNIWRFSYVT</span><span class="topo-inside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVLAEF</span><span class="topo-outside">TIGRRAQSDAVGSFEKLAPGKP</span><span class="topo-membrane">WKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYITG</span><span class="topo-inside">QLWSAPAEGFGGFFEGFIANP</span><span class="topo-membrane">TLPLFWQALFMIATIWIVAI</span><span class="topo-outside">GVKKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAI</span><span class="topo-inside">YSLTLGGAKEGLAFLFSPDWSALKD</span><span class="topo-membrane">PGVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIMI</span><span class="topo-inside">FPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFD</span><span class="topo-inside">SIRLGP</span><span class="topo-membrane">IVGIAFFILLGAAALSSAVSLLEVPVAYF</span><span class="topo-outside">MRKFDWSRK</span><span class="topo-membrane">QAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSSLSF</span><span class="topo-inside">GVLGEVTIIPGL</span><span class="topo-membrane">NIFDSVDFIASSVFLPLGGMIIALFIGW</span><span class="topo-outside">GWK</span><span class="topo-unknown">TSDALAE</span><span class="topo-outside">SDLTDSV</span><span class="topo-membrane">WGKLWILSLRFIAPIAILIVFLSAFQ</span><span class="topo-unknown">IFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>10</td>
      <td>19</td>
      <td>8</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>41</td>
      <td>18</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>68</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>127</td>
      <td>90</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>148</td>
      <td>126</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>147</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>173</td>
      <td>167</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>219</td>
      <td>193</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>218</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>276</td>
      <td>254</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>292</td>
      <td>275</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>291</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>302</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>338</td>
      <td>308</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>347</td>
      <td>337</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>368</td>
      <td>346</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>380</td>
      <td>367</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>408</td>
      <td>379</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>411</td>
      <td>407</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>418</td>
      <td>410</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>419</td>
      <td>425</td>
      <td>417</td>
      <td>423</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>451</td>
      <td>424</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu4">6YU4</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLGFI</span><span class="topo-membrane">LAAMGSAVGLGNIWRFSYVT</span><span class="topo-inside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVL</span><span class="topo-outside">AEFTIGRRAQSDAVGSFEKLAPGKPWKV</span><span class="topo-membrane">AGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LF</span><span class="topo-inside">NYITGQLWSAPAE</span><span class="topo-unknown">GFGGFFEGFIA</span><span class="topo-inside">NPTLP</span><span class="topo-membrane">LFWQALFMIATIWIVAIG</span><span class="topo-outside">VKKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAI</span><span class="topo-inside">YSLTLGGAKEGLAFLFSPDWSAL</span><span class="topo-membrane">KDPGVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLPGA</span><span class="topo-membrane">AVSVAGLDTAFAIIAGIM</span><span class="topo-inside">IFPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFD</span><span class="topo-inside">SIRLGPI</span><span class="topo-membrane">VGIAFFILLGAAALSSAVSLLEVPVAYF</span><span class="topo-outside">MRKFDWSR</span><span class="topo-membrane">KQAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSS</span><span class="topo-inside">LSFGVLGEVTIIPGLNI</span><span class="topo-membrane">FDSVDFIASSVFLPLGGMIIAL</span><span class="topo-outside">FIGWGWKTSDALAESDLTDS</span><span class="topo-unknown">VWGKLWIL</span><span class="topo-membrane">SLRFIAPIAILIVFLSAFQ</span><span class="topo-unknown">IFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>10</td>
      <td>21</td>
      <td>8</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>41</td>
      <td>20</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>66</td>
      <td>45</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>94</td>
      <td>65</td>
      <td>92</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>122</td>
      <td>93</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>135</td>
      <td>121</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>146</td>
      <td>134</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>151</td>
      <td>145</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>150</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>173</td>
      <td>168</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>193</td>
      <td>215</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>244</td>
      <td>216</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>257</td>
      <td>243</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>275</td>
      <td>256</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>274</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>291</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>310</td>
      <td>302</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>338</td>
      <td>309</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>346</td>
      <td>337</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>365</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>364</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>404</td>
      <td>381</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>424</td>
      <td>403</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>432</td>
      <td>423</td>
      <td>430</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>433</td>
      <td>451</td>
      <td>431</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu3">6YU3</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLGFI</span><span class="topo-membrane">LAAMGSAVGLGNIWRFSYVT</span><span class="topo-inside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVLAEF</span><span class="topo-outside">TIGRRAQSDAVGSFEKLAPGKP</span><span class="topo-membrane">WKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LF</span><span class="topo-inside">NYITGQLWSAPAE</span><span class="topo-unknown">GFGGFFEGFIA</span><span class="topo-inside">NPTLP</span><span class="topo-membrane">LFWQALFMIATIWIVAIGV</span><span class="topo-outside">KKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAIY</span><span class="topo-inside">SLTLGGAKEGLAFLFSPDWSALKDP</span><span class="topo-membrane">GVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLPG</span><span class="topo-membrane">AAVSVAGLDTAFAIIAGIMI</span><span class="topo-inside">FPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFDS</span><span class="topo-inside">IRLGP</span><span class="topo-membrane">IVGIAFFILLGAAALSSAVSLLEVPVAYFM</span><span class="topo-outside">RKFDWSR</span><span class="topo-membrane">KQAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSS</span><span class="topo-inside">LSFGVLGEVTIIPGLNI</span><span class="topo-membrane">FDSVDFIASSVFLPLGGMIIALF</span><span class="topo-outside">IGWGWK</span><span class="topo-unknown">TSDALAE</span><span class="topo-outside">SDLTDSVWGKL</span><span class="topo-membrane">WILSLRFIAPIAILIVFLSAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>10</td>
      <td>21</td>
      <td>8</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>41</td>
      <td>20</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>68</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>122</td>
      <td>90</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>135</td>
      <td>121</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>146</td>
      <td>134</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>151</td>
      <td>145</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>170</td>
      <td>150</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>173</td>
      <td>169</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>195</td>
      <td>172</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>220</td>
      <td>194</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>219</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>256</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>276</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>292</td>
      <td>275</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>304</td>
      <td>291</td>
      <td>302</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>309</td>
      <td>303</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>339</td>
      <td>308</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>346</td>
      <td>338</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>365</td>
      <td>345</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>364</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>405</td>
      <td>381</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>411</td>
      <td>404</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>418</td>
      <td>410</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>419</td>
      <td>429</td>
      <td>417</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>450</td>
      <td>428</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu2">6YU2</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-inside">GREQWASRLGFI</span><span class="topo-membrane">LAAMGSAVGLGNIWRFS</span><span class="topo-outside">YVTGENGGAAFL</span><span class="topo-membrane">LVYLGFIALIGIPIVLAEF</span><span class="topo-inside">TIGRRAQSDAVGSFEKLAPGK</span><span class="topo-membrane">PWKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYITG</span><span class="topo-outside">QLWSAPAE</span><span class="topo-unknown">GFGGFFEGFI</span><span class="topo-outside">ANPT</span><span class="topo-membrane">LPLFWQALFMIATIWIVA</span><span class="topo-inside">IGVKKGIERS</span><span class="topo-membrane">NKILMPLLGVLLIALAIY</span><span class="topo-outside">SLTLGG</span><span class="topo-unknown">AKEGLAFLF</span><span class="topo-outside">SPDWSALKDPGVY</span><span class="topo-membrane">LAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-inside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIM</span><span class="topo-outside">IFPAVFALGLSPSGGPGL</span><span class="topo-unknown">VFVVLPDIF</span><span class="topo-outside">DSIRL</span><span class="topo-membrane">GPIVGIAFFILLGAAALSSAVSLLEVPV</span><span class="topo-inside">AYFMRKFDWSRKQA</span><span class="topo-membrane">AITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSS</span><span class="topo-outside">LSFGVLGEVTIIPGLNIFDS</span><span class="topo-membrane">VDFIASSVFLPLGGMIIALFIGWG</span><span class="topo-inside">WK</span><span class="topo-unknown">TSDALAE</span><span class="topo-inside">SDLTDSV</span><span class="topo-membrane">WGKLWILSLRFIAPIAILIVFL</span><span class="topo-outside">SAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>10</td>
      <td>21</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>38</td>
      <td>20</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>37</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>49</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>90</td>
      <td>68</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>127</td>
      <td>89</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>135</td>
      <td>126</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>145</td>
      <td>134</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>146</td>
      <td>149</td>
      <td>144</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>167</td>
      <td>148</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>166</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>195</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>201</td>
      <td>194</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>210</td>
      <td>200</td>
      <td>208</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>223</td>
      <td>209</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>244</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>254</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>293</td>
      <td>274</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>302</td>
      <td>292</td>
      <td>300</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>303</td>
      <td>307</td>
      <td>301</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>335</td>
      <td>306</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>349</td>
      <td>334</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>365</td>
      <td>348</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>385</td>
      <td>364</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>409</td>
      <td>384</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>408</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>418</td>
      <td>410</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>419</td>
      <td>425</td>
      <td>417</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>447</td>
      <td>424</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>450</td>
      <td>446</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu2">6YU2</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-inside">GREQWASRLGFI</span><span class="topo-membrane">LAAMGSAVGLGNIWRFS</span><span class="topo-outside">YVTGENGGAAFL</span><span class="topo-membrane">LVYLGFIALIGIPIVLAEF</span><span class="topo-inside">TIGRRAQSDAVGSFEKLAPGK</span><span class="topo-membrane">PWKVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYITG</span><span class="topo-outside">QLWSAPAE</span><span class="topo-unknown">GFGGFFEGFIA</span><span class="topo-outside">NPT</span><span class="topo-membrane">LPLFWQALFMIATIWIVA</span><span class="topo-inside">IGVKKGIERS</span><span class="topo-membrane">NKILMPLLGVLLIALAIY</span><span class="topo-outside">SLTLGG</span><span class="topo-unknown">AKEGLAFLF</span><span class="topo-outside">SPDWSALKDPGVY</span><span class="topo-membrane">LAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-inside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIM</span><span class="topo-outside">IFPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFDS</span><span class="topo-outside">IRL</span><span class="topo-membrane">GPIVGIAFFILLGAAALSSAVSLLEVPV</span><span class="topo-inside">AYFMRKFDWSRKQA</span><span class="topo-membrane">AITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSS</span><span class="topo-outside">LSFGVLGEVTIIPGLNIFDS</span><span class="topo-membrane">VDFIASSVFLPLGGMIIALFIGWG</span><span class="topo-inside">WK</span><span class="topo-unknown">TSDALA</span><span class="topo-inside">ESDLTDSV</span><span class="topo-membrane">WGKLWILSLRFIAPIAILIVFL</span><span class="topo-outside">SAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>10</td>
      <td>21</td>
      <td>8</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>38</td>
      <td>20</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>37</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>49</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>90</td>
      <td>68</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>127</td>
      <td>89</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>135</td>
      <td>126</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>146</td>
      <td>134</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>149</td>
      <td>145</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>167</td>
      <td>148</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>166</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>195</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>201</td>
      <td>194</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>210</td>
      <td>200</td>
      <td>208</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>223</td>
      <td>209</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>244</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>254</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>274</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>304</td>
      <td>291</td>
      <td>302</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>307</td>
      <td>303</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>335</td>
      <td>306</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>349</td>
      <td>334</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>365</td>
      <td>348</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>385</td>
      <td>364</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>409</td>
      <td>384</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>411</td>
      <td>408</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>417</td>
      <td>410</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>418</td>
      <td>425</td>
      <td>416</td>
      <td>423</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>447</td>
      <td>424</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>450</td>
      <td>446</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu6">6YU6</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-outside">GREQWASRLGFIL</span><span class="topo-membrane">AAMGSAVGLGNIWRFS</span><span class="topo-inside">YVTGENGGA</span><span class="topo-membrane">AFLLVYLGFIALIGIPIV</span><span class="topo-outside">LAEFTIGRRAQSDAVGSFEKLAPGKP</span><span class="topo-membrane">WKVAGLMGVAAGFLILSFYGVIAG</span><span class="topo-unknown">WILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">LFNYI</span><span class="topo-inside">TGQLWSAPAEGFGGFFEGFIANPTLPLF</span><span class="topo-membrane">WQALFMIATIWIVAIG</span><span class="topo-outside">VKKGIER</span><span class="topo-membrane">SNKILMPLLGVLLIALAIY</span><span class="topo-inside">SLTLGGAKEGLAFLFSPDWSALKDP</span><span class="topo-membrane">GVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-outside">GSYVSKDSRLPGAA</span><span class="topo-membrane">VSVAGLDTAFAIIAGIM</span><span class="topo-inside">IFPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFDS</span><span class="topo-inside">IRLGPI</span><span class="topo-membrane">VGIAFFILLGAAALSSAVSLLEVPVAYFM</span><span class="topo-outside">RKFDW</span><span class="topo-membrane">SRKQAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GI</span><span class="topo-inside">PSSLSFGVLGEVTIIPGLNIFDS</span><span class="topo-membrane">VDFIASSVFLPLGGMIIAL</span><span class="topo-outside">FIGWGWKTSDALAESDLTDSVWGKLWILS</span><span class="topo-membrane">LRFIAPIAILIVFLSAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>10</td>
      <td>22</td>
      <td>8</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>38</td>
      <td>21</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>47</td>
      <td>37</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>91</td>
      <td>64</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>115</td>
      <td>90</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>125</td>
      <td>114</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>126</td>
      <td>153</td>
      <td>124</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>169</td>
      <td>152</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>176</td>
      <td>168</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>195</td>
      <td>175</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>220</td>
      <td>194</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>219</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>243</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>257</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>274</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>304</td>
      <td>291</td>
      <td>302</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>310</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>339</td>
      <td>309</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>344</td>
      <td>338</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>362</td>
      <td>343</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>385</td>
      <td>361</td>
      <td>383</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>404</td>
      <td>384</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>433</td>
      <td>403</td>
      <td>431</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>450</td>
      <td>432</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yu5">6YU5</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SMASLKQQT</span><span class="topo-inside">GREQWASRLGF</span><span class="topo-membrane">ILAAMGSAVGLGNIWRFSYVT</span><span class="topo-outside">GENGG</span><span class="topo-membrane">AAFLLVYLGFIALIGIPIVLAEF</span><span class="topo-inside">TIGRRAQSDAVGSFEKLAPGKPW</span><span class="topo-membrane">KVAGLMGVAAGFLILSFYGVIAGWILFY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LFNYIT</span><span class="topo-outside">GQLWSAPAEGFGGFFEGFIANPT</span><span class="topo-membrane">LPLFWQALFMIATIWIVAI</span><span class="topo-inside">GVKKG</span><span class="topo-membrane">IERSNKILMPLLGVLLIALAI</span><span class="topo-outside">YSLTLGGAKEGLAFLFSPDWSAL</span><span class="topo-membrane">KDPGVYLAAISQAFFTLSLGMGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LITY</span><span class="topo-inside">GSYVSKDSRLP</span><span class="topo-membrane">GAAVSVAGLDTAFAIIAGIM</span><span class="topo-outside">IFPAVFALGLSPSGGPG</span><span class="topo-unknown">LVFVVLPDIFD</span><span class="topo-outside">SIRLGPI</span><span class="topo-membrane">VGIAFFILLGAAALSSAVSLLEVPVAYF</span><span class="topo-inside">MRKFDWSRK</span><span class="topo-membrane">QAAITLGVIITLL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">GIPSSL</span><span class="topo-outside">SFGVLGEVTIIPGL</span><span class="topo-membrane">NIFDSVDFIASSVFLPLGGMIIALF</span><span class="topo-inside">IGWGWK</span><span class="topo-unknown">TSDALAE</span><span class="topo-inside">SDLTDSVWGKL</span><span class="topo-membrane">WILSLRFIAPIAILIVFLSAF</span><span class="topo-unknown">QIFFN</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>10</td>
      <td>20</td>
      <td>8</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>41</td>
      <td>19</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>46</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>45</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>92</td>
      <td>68</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>126</td>
      <td>91</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>149</td>
      <td>125</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>168</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>173</td>
      <td>167</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>172</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>193</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>244</td>
      <td>216</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>255</td>
      <td>243</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>275</td>
      <td>254</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>292</td>
      <td>274</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>303</td>
      <td>291</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>310</td>
      <td>302</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>338</td>
      <td>309</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>347</td>
      <td>337</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>366</td>
      <td>346</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>380</td>
      <td>365</td>
      <td>378</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>405</td>
      <td>379</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>411</td>
      <td>404</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>418</td>
      <td>410</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>419</td>
      <td>429</td>
      <td>417</td>
      <td>427</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>450</td>
      <td>428</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Occluded inward-facing state with bound Na+ and substrate

Both MhsT crystal structures represent an occluded, inward-facing state with two bound Na+ ions and one L-tryptophan molecule. The extracellular side is sealed by a tight hydrophobic cluster of TMs 1b, 2, 6a, and 7, collapsing the extracellular vestibule. At the intracellular side, a water-access pathway reaches the Na2 site while the substrate and Na1 site remain inaccessible. This state is distinct from the inward-open apo conformation of [LEUT](/xray-mp-wiki/proteins/enzymes/leut/).

### TM5 unwinding via GlyX9Pro motif

The intracellular part of transmembrane helix 5 (TM5i) unwinds at a conserved GlyX9Pro motif, creating a solvent pathway from the cytoplasm to the Na2 site. This unwinding results from strain between the movement of the extracellular part of TM5 (TM5e) together with TM6a during closure of the extracellular vestibule around Trp33, while TM5i maintains coiled-coil interaction with TM1a through coordination with Na+ at the Na2 site. The GlyX9Pro motif is conserved across the NSS family and is predicted to promote unraveling of TM5i.

### Na2 site solvation and Na+ release mechanism

TM5 unwinding provides a cytoplasmic water molecule access to the Na2 site as a sixth ligand, completing octahedral coordination. TM8 is displaced relative to TM1, and the Ser323 side chain shifts to provide space. This solvation primes the Na2 site for intracellular Na+ release in the low-Na+ cytoplasmic environment. Release of Na+ from Na2 triggers TM1a to swing out, opening a wide intracellular pathway for substrate and Na1 release.

### Substrate recognition by the GMG motif

Six new substrate-bound structures (L-Tyr, L-4-F-Phe, L-Phe, L-Ile, L-Leu, L-Val) reveal a bimodal binding site that distinguishes between aliphatic and aromatic amino acids. The unwound region of TM6 containing a Gly-Met-Gly (GMG) motif shifts inward by ~2 A for small aliphatic substrates, reducing the binding pocket volume from ~230 A^3 (aromatic) to ~144 A^3 (valine). This is an induced-fit mechanism where the GMG loop compensates for smaller substrate side chains. Met236 undergoes rotamer changes to fine-tune the chemical environment for different substrates.

### Conserved Glu66 fulcrum

Glu66 on TM2 forms a conserved interaction with the unwound TM6 region through water-mediated hydrogen bonds. With aliphatic substrates, an additional ordered water molecule is recruited compared to aromatic substrates. This interaction is maintained throughout the transport cycle (as confirmed by comparison with various [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) structures) and is critical for conformational transitions. Mutation of the equivalent glutamate in [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/), DAT, NET, and GAT1 diminishes transport activity without affecting substrate binding.

### M236F mutation alters substrate specificity

The M236F substitution (mimicking the AFG motif of human SLC6A18/SLC6A19) completely abolishes transport of aromatic amino acids (L-Trp, L-Phe, L-Tyr) while maintaining aliphatic amino acid (L-Leu, L-Val, L-Ile) transport. The Vmax for Leu is unchanged (3.23 vs 3.33 nmol/min/mg for WT vs M236F), while Trp uptake is undetectable. This explains why human SLC6A18/SLC6A19 (with AFG motif) preferentially transport aliphatic amino acids, despite sharing ~50% binding site conservation with MhsT.

### Substrate binding and selectivity

MhsT binds L-tryptophan with a Kd of 4.8 +/- 0.6 uM and a molar binding stoichiometry of 1.1 +/- 0.04. The substrate binding site is similar to the L-leucine-occupied S1 site in [LEUT](/xray-mp-wiki/proteins/enzymes/leut/). MhsT shows transport activity for L-tryptophan (Kt 1.7 +/- 0.3 uM), L-tyrosine, [L-Phenylalanine](/xray-mp-wiki/reagents/ligands/l-phenylalanine/), and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/). The catalytic turnover number (kcat 0.8 +/- 0.03 s-1) is about two and three orders of magnitude faster than LeuT-mediated transport of [L-Alanine](/xray-mp-wiki/reagents/substrates/l-alanine/) and [L-Leucine](/xray-mp-wiki/reagents/ligands/l-leucine/), respectively. The bulky side chains of Phe259LeuT and Ile359LeuT (Met236MhsT and Leu328MhsT) cannot accommodate L-tryptophan, explaining substrate selectivity differences.

### Transport mechanism model for NSS family

A general model of NSS function: (1) Na+ and substrate binding in outward-open state initiates occlusion. (2) Occluded outward-facing state exposes hydrophobic vestibule, priming for extracellular closure around Trp33. (3) Transition to inward-facing state with TM5 unwinding providing solvation pathway for Na2 site. (4) Na+ release from Na2 triggers forward reaction. (5) TM1a swings out, TM5i reassociates with TM5e, releasing substrate and Na1 intracellularly. (6) Return to outward-open state through unknown occluded states.

### Comparison with LeuT functional states

MhsT occluded inward-facing state differs from [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) inward-open apo conformation: the extracellular-closed conformation is not paired with an open intracellular side. Instead, the intracellular configuration resembles outward-facing states with the N-terminal tail sealing the cytoplasmic side and Trp12 plugging a hydrophobic pocket. However, TM5 unwinding creates a solvent pathway to the Na2 site that is absent in outward-facing [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) structures. The MhsT structure shares 33% sequence identity with [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) and 25% with dDAT.

### Conservation of GlyXnPro pattern in LeuT-fold transporters

Structural alignment of MhsT (NSS family) with [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/) (NCS1 family, another LeuT-fold transporter) reveals a recurring GlyXnPro pattern in the intracellular part of TM5, suggesting that TM5 unwinding and cytoplasmic water access to the Na+-binding site may be a general mechanism exploited by other Na+-dependent LeuT-fold transporters. The GlyX9Pro motif is slightly shifted in eukaryotic NSSs relative to bacterial NSSs, potentially fine-tuning the TM5 deformation mechanism to species-specific conditions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — NSS family prototype; MhsT shares 33% sequence identity with LeuT; LeuT structures 5JAE and 5JAF show return state mechanism with Leu25 rotation; compared with MhsT inward-facing state for NSS transport cycle model
- <a href="/xray-mp-wiki/proteins/slc-transporters/d-dopamine-transporter/">Drosophila Dopamine Transporter (dDAT)</a> — Eukaryotic NSS homolog used for structural comparison; MhsT shares 25% sequence identity
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/nss-family/">Neurotransmitter/Sodium Symporter (NSS) Family</a> — MhsT belongs to the NSS family
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/slc6-substrate-recognition-gmg-motif/">SLC6 Substrate Recognition by the GMG Motif</a> — The GMG motif in TM6 mediates MhsT substrate recognition
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for MhsT solubilization, purification, and binding studies
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Used to cleave N-terminal histidine tag from MhsT
- <a href="/xray-mp-wiki/methods/crystallization/hilide-crystallization/">HiLiDe Crystallization</a> — MhsT crystallized using HiLiDe method (2.1 A structure)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — MhsT crystallized using LCP method (2.6 A structure)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Core transport mechanism of NSS family
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
