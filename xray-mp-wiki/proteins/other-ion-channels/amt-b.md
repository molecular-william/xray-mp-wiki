---
title: "Ammonium Transporter AmtB (E. coli)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1101952, doi/10.1073##pnas.0609796104, doi/10.1073##pnas.1719813115, doi/10.1038##nature13419, doi/10.1074##jbc.M608325200, doi/10.1073##pnas.0406475101]
verified: agent
uniprot_id: ['P0AC55', 'P69681']
---

# Ammonium Transporter AmtB (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AC55">UniProt: P0AC55</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P69681">UniProt: P69681</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

AmtB (ammonium transporter B) is a trimeric ammonium channel from
Escherichia coli that mediates ammonium uptake across the cytoplasmic
membrane. Each subunit contains 11 transmembrane helices (TMH). The
first atomic-resolution structure of AmtB at 1.35 Å revealed it as a
channel rather than a transporter, conducting uncharged NH3 through a
20 Å hydrophobic channel. AmtB was shown to be highly selective for
[Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG) among phospholipids, with PG binding inducing
distinct conformational changes that reposition key residues to interact
with the lipid bilayer. The twin-His motif (His-168 and His-318) within
the channel pore was demonstrated by comprehensive mutagenesis to 14
polar and non-polar residues to be absolutely essential for optimum
substrate conductance. Crystal structures of variants confirmed that
substitutions do not affect overall structure. Pore hydration analysis
revealed a correlation between transport activity and the presence of
ordered water/ammonia molecules in the central pore.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1101952 (2 structures, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1u7g">1U7G</a></td>
      <td>1.35</td>
      <td>—</td>
      <td>AmtB_Ecoli (residues 23-428, signal peptide removed)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1u7g">1U7G</a></td>
      <td>1.35</td>
      <td>—</td>
      <td>AmtB_Ecoli with ammonia bound</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: AmtB_Ecoli (native, signal peptide removed)

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
      <td>Recombinant expression in E. coli</td>
      <td>—</td>
      <td></td>
      <td>20 amino acids excised from N terminus; signal sequence identified by MALDI-MS and neural network prediction</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25 mM AmSO4, pH 6.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of AmtB_Ecoli grown in presence of 25 mM AmSO4 at pH 6.5 diffract to 1.35 A. Also crystallized with 100 mM MASO4 at pH 6.5 for methylammonium complex.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1u7g">1U7G</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFYG</span><span class="topo-inside">GLIRGKNVLSM</span><span class="topo-membrane">LTQVTVTFALVCILWVVYG</span><span class="topo-outside">YSLASGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRF</span><span class="topo-membrane">PAVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALDFA</span><span class="topo-membrane">GGTVVHINAAIAGLVGAY</span><span class="topo-inside">LIGKRVGFGKEAFKPHNLP</span><span class="topo-membrane">MVFTGTAILYIGWFGFN</span><span class="topo-outside">AGSAGTANEIAALAF</span><span class="topo-membrane">VNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWA</span><span class="topo-inside">LRGLPSL</span><span class="topo-membrane">LGACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGVTML</span><span class="topo-inside">KRLLRVDDP</span><span class="topo-membrane">CDVFGVHGVCGIVGCIMT</span><span class="topo-outside">GIFAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380     </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-inside">GLRV</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>15</td>
      <td>3</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>44</td>
      <td>34</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>63</td>
      <td>45</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>102</td>
      <td>64</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>120</td>
      <td>103</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>162</td>
      <td>145</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>180</td>
      <td>163</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>181</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>200</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>231</td>
      <td>217</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>251</td>
      <td>232</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>258</td>
      <td>252</td>
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
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>302</td>
      <td>282</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>311</td>
      <td>303</td>
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
      <td>355</td>
      <td>330</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>381</td>
      <td>356</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>385</td>
      <td>382</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1u7g">1U7G</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFYG</span><span class="topo-inside">GLIRGKNVLSM</span><span class="topo-membrane">LTQVTVTFALVCILWVVYG</span><span class="topo-outside">YSLASGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRF</span><span class="topo-membrane">PAVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALDFA</span><span class="topo-membrane">GGTVVHINAAIAGLVGAY</span><span class="topo-inside">LIGKRVGFGKEAFKPHNLP</span><span class="topo-membrane">MVFTGTAILYIGWFGFN</span><span class="topo-outside">AGSAGTANEIAALAF</span><span class="topo-membrane">VNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWA</span><span class="topo-inside">LRGLPSL</span><span class="topo-membrane">LGACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGVTML</span><span class="topo-inside">KRLLRVDDP</span><span class="topo-membrane">CDVFGVHGVCGIVGCIMT</span><span class="topo-outside">GIFAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380     </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-inside">GLRV</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>15</td>
      <td>3</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>44</td>
      <td>34</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>63</td>
      <td>45</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>102</td>
      <td>64</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>120</td>
      <td>103</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>162</td>
      <td>145</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>180</td>
      <td>163</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>181</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>200</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>231</td>
      <td>217</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>251</td>
      <td>232</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>258</td>
      <td>252</td>
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
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>302</td>
      <td>282</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>311</td>
      <td>303</td>
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
      <td>355</td>
      <td>330</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>381</td>
      <td>356</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>385</td>
      <td>382</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1u7g">1U7G</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFYG</span><span class="topo-inside">GLIRGKNVLSM</span><span class="topo-membrane">LTQVTVTFALVCILWVVYG</span><span class="topo-outside">YSLASGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRF</span><span class="topo-membrane">PAVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALDFA</span><span class="topo-membrane">GGTVVHINAAIAGLVGAY</span><span class="topo-inside">LIGKRVGFGKEAFKPHNLP</span><span class="topo-membrane">MVFTGTAILYIGWFGFN</span><span class="topo-outside">AGSAGTANEIAALAF</span><span class="topo-membrane">VNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWA</span><span class="topo-inside">LRGLPSL</span><span class="topo-membrane">LGACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGVTML</span><span class="topo-inside">KRLLRVDDP</span><span class="topo-membrane">CDVFGVHGVCGIVGCIMT</span><span class="topo-outside">GIFAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380     </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-inside">GLRV</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>15</td>
      <td>3</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>33</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>44</td>
      <td>34</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>63</td>
      <td>45</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>102</td>
      <td>64</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>120</td>
      <td>103</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>162</td>
      <td>145</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>180</td>
      <td>163</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>199</td>
      <td>181</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>200</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>231</td>
      <td>217</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>251</td>
      <td>232</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>258</td>
      <td>252</td>
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
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>302</td>
      <td>282</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>311</td>
      <td>303</td>
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
      <td>355</td>
      <td>330</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>381</td>
      <td>356</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>385</td>
      <td>382</td>
      <td>385</td>
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
<summary><strong>doi/10.1073##pnas.0609796104 (1 structure, 6 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a></td>
      <td>1.96</td>
      <td>P6(3)22</td>
      <td>AmtB (full-length) in complex with <a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">GlnK PII Signal Transduction Protein (E. coli)</a> Y51F mutant</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AmtB-<a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">GlnK PII Signal Transduction Protein (E. coli)</a> Y51F complex at 10 mg/ml in 40 mM <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 25 mM AmSO4, 2 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 200 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 4000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using AmtB structure (1U7G) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-inside">AVADKADNAFM</span><span class="topo-membrane">MICTALVLFMTIPGIALFYGGL</span><span class="topo-outside">IRGKNVL</span><span class="topo-membrane">SMLTQVTVTFALVCILWVVYGYSLAF</span><span class="topo-inside">GEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ERI</span><span class="topo-membrane">RFSAVLIFVVVWLTLSYIPIAHMVW</span><span class="topo-inside">GGGLLASHGA</span><span class="topo-membrane">LDFAGGTVVHINAAIAGLVGAYL</span><span class="topo-outside">IGKRVGFGKEAFKPHNL</span><span class="topo-membrane">PMVFTGTAILYIGWFGFNAGS</span><span class="topo-inside">AGTANEIAAL</span><span class="topo-membrane">AFVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWAL</span><span class="topo-outside">RGKP</span><span class="topo-membrane">SLLGACSGAIAGLVGVTPACG</span><span class="topo-inside">YI</span><span class="topo-membrane">GVGGALIIGVVAGLAGLWGVTMLK</span><span class="topo-outside">RLLRVDD</span><span class="topo-membrane">PCDVFGVHGVCGIVGCIMTGIF</span><span class="topo-inside">AASSLGGVGFAEGVTMGHQ</span><span class="topo-membrane">LLVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410  </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-outside">GLRVPEEQEREG</span><span class="topo-unknown">LDVNSH</span><span class="topo-outside">GENAYNA</span><span class="topo-unknown">GTLVPR</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>13</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>35</td>
      <td>14</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>36</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>68</td>
      <td>43</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>101</td>
      <td>69</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>123</td>
      <td>121</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>124</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>181</td>
      <td>159</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>182</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>219</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>229</td>
      <td>220</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>252</td>
      <td>230</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>256</td>
      <td>253</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>277</td>
      <td>257</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>279</td>
      <td>278</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>280</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>310</td>
      <td>304</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>351</td>
      <td>333</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>381</td>
      <td>352</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>393</td>
      <td>382</td>
      <td>393</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>399</td>
      <td>394</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>412</td>
      <td>407</td>
      <td>412</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110      </span>
<span class="topo-line"><span class="topo-unknown">GPG</span><span class="topo-outside">SMKLVTVIIKPFKLEDVREALSSIGIQGLTVTEVKGFGRQKGHAELYRGAEFSVNFLPKVKIDVAIADDQLDEVIDIVSKAAYTGKIGDGKIFVAELQRVIRIRTGEADEAAL</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>3</td>
      <td>-3</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>116</td>
      <td>0</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-inside">AVADKADNAFM</span><span class="topo-membrane">MICTALVLFMTIPGIALFYGGL</span><span class="topo-outside">IRGKNVL</span><span class="topo-membrane">SMLTQVTVTFALVCILWVVYGYSLAF</span><span class="topo-inside">GEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ERI</span><span class="topo-membrane">RFSAVLIFVVVWLTLSYIPIAHMVW</span><span class="topo-inside">GGGLLASHGA</span><span class="topo-membrane">LDFAGGTVVHINAAIAGLVGAYL</span><span class="topo-outside">IGKRVGFGKEAFKPHNL</span><span class="topo-membrane">PMVFTGTAILYIGWFGFNAGS</span><span class="topo-inside">AGTANEIAAL</span><span class="topo-membrane">AFVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWAL</span><span class="topo-outside">RGKP</span><span class="topo-membrane">SLLGACSGAIAGLVGVTPACG</span><span class="topo-inside">YI</span><span class="topo-membrane">GVGGALIIGVVAGLAGLWGVTMLK</span><span class="topo-outside">RLLRVDD</span><span class="topo-membrane">PCDVFGVHGVCGIVGCIMTGIF</span><span class="topo-inside">AASSLGGVGFAEGVTMGHQ</span><span class="topo-membrane">LLVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410  </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-outside">GLRVPEEQEREG</span><span class="topo-unknown">LDVNSH</span><span class="topo-outside">GENAYNA</span><span class="topo-unknown">GTLVPR</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>13</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>35</td>
      <td>14</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>36</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>68</td>
      <td>43</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>101</td>
      <td>69</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>123</td>
      <td>121</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>124</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>181</td>
      <td>159</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>182</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>219</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>229</td>
      <td>220</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>252</td>
      <td>230</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>256</td>
      <td>253</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>277</td>
      <td>257</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>279</td>
      <td>278</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>280</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>310</td>
      <td>304</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>351</td>
      <td>333</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>381</td>
      <td>352</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>393</td>
      <td>382</td>
      <td>393</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>399</td>
      <td>394</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>412</td>
      <td>407</td>
      <td>412</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110      </span>
<span class="topo-line"><span class="topo-unknown">GPG</span><span class="topo-outside">SMKLVTVIIKPFKLEDVREALSSIGIQGLTVTEVKGFGRQKGHAELYRGAEFSVNFLPKVKIDVAIADDQLDEVIDIVSKAAYTGKIGDGKIFVAELQRVIRIRTGEADEAAL</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>3</td>
      <td>-3</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>116</td>
      <td>0</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain E (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-inside">AVADKADNAFM</span><span class="topo-membrane">MICTALVLFMTIPGIALFYGGL</span><span class="topo-outside">IRGKNVL</span><span class="topo-membrane">SMLTQVTVTFALVCILWVVYGYSLAF</span><span class="topo-inside">GEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ERI</span><span class="topo-membrane">RFSAVLIFVVVWLTLSYIPIAHMVW</span><span class="topo-inside">GGGLLASHGA</span><span class="topo-membrane">LDFAGGTVVHINAAIAGLVGAYL</span><span class="topo-outside">IGKRVGFGKEAFKPHNL</span><span class="topo-membrane">PMVFTGTAILYIGWFGFNAGS</span><span class="topo-inside">AGTANEIAAL</span><span class="topo-membrane">AFVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFGEWAL</span><span class="topo-outside">RGKP</span><span class="topo-membrane">SLLGACSGAIAGLVGVTPACG</span><span class="topo-inside">YI</span><span class="topo-membrane">GVGGALIIGVVAGLAGLWGVTMLK</span><span class="topo-outside">RLLRVDD</span><span class="topo-membrane">PCDVFGVHGVCGIVGCIMTGIF</span><span class="topo-inside">AASSLGGVGFAEGVTMGHQ</span><span class="topo-membrane">LLVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410  </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLADLTV</span><span class="topo-outside">GLRVPEEQEREG</span><span class="topo-unknown">LDVNSH</span><span class="topo-outside">GENAYNA</span><span class="topo-unknown">GTLVPR</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>13</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>35</td>
      <td>14</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>36</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>68</td>
      <td>43</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>101</td>
      <td>69</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>120</td>
      <td>102</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>123</td>
      <td>121</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>124</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>181</td>
      <td>159</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>182</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>219</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>229</td>
      <td>220</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>252</td>
      <td>230</td>
      <td>252</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>256</td>
      <td>253</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>277</td>
      <td>257</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>279</td>
      <td>278</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>303</td>
      <td>280</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>310</td>
      <td>304</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>351</td>
      <td>333</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>381</td>
      <td>352</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>393</td>
      <td>382</td>
      <td>393</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>399</td>
      <td>394</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>400</td>
      <td>406</td>
      <td>400</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>412</td>
      <td>407</td>
      <td>412</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ns1">2NS1</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110      </span>
<span class="topo-line"><span class="topo-unknown">GPG</span><span class="topo-outside">SMKLVTVIIKPFKLEDVREALSSIGIQGLTVTEVKGFGRQKGHAELYRGAEFSVNFLPKVKIDVAIADDQLDEVIDIVSKAAYTGKIGDGKIFVAELQRVIRIRTGEADEAAL</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>3</td>
      <td>-3</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>116</td>
      <td>0</td>
      <td>112</td>
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
<summary><strong>doi/10.1073##pnas.1719813115 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b21">6B21</a></td>
      <td>2.45</td>
      <td>H32</td>
      <td>AmtB E. coli (residues 1-428)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AmtB at 10 mg/mL (79 uM) mixed with 1:1.5:3 molar excess of <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)</a> and TFCDL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 0.3 M magnesium nitrate, 22% (wt/vol) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 8000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified (room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>No cryoprotection needed; mounted with CrystalCap HT Cryoloops and flash-frozen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Best diffracting crystals grew at 1:1 sample to reservoir ratio. Diffraction data collected at APS beamline 24-ID-E at 2.45 A resolution. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using apo AmtB structure (PDB 1U76). Space group H32.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b21">6B21</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALF</span><span class="topo-inside">YGGLIRGKNVLSMLTQ</span><span class="topo-membrane">VTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVG</span><span class="topo-inside">ALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFSAV</span><span class="topo-membrane">LIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLV</span><span class="topo-inside">GAYLIG</span><span class="topo-unknown">KRVGFGKEAF</span><span class="topo-inside">KPHNLPMVF</span><span class="topo-membrane">TGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLGA</span><span class="topo-membrane">CSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWG</span><span class="topo-inside">VTMLKR</span><span class="topo-unknown">LLRVDD</span><span class="topo-inside">PCDV</span><span class="topo-membrane">FGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>48</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>117</td>
      <td>102</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>128</td>
      <td>118</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>147</td>
      <td>129</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>161</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>183</td>
      <td>178</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>202</td>
      <td>194</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>203</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>261</td>
      <td>249</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>276</td>
      <td>262</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>304</td>
      <td>299</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>314</td>
      <td>311</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>332</td>
      <td>315</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b21">6B21</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALF</span><span class="topo-inside">YGGLIRGKNVLSMLTQ</span><span class="topo-membrane">VTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVG</span><span class="topo-inside">ALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFSAV</span><span class="topo-membrane">LIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLV</span><span class="topo-inside">GAYLIG</span><span class="topo-unknown">KRVGFGKEAF</span><span class="topo-inside">KPHNLPMVF</span><span class="topo-membrane">TGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLGA</span><span class="topo-membrane">CSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWG</span><span class="topo-inside">VTMLKR</span><span class="topo-unknown">LLRVDD</span><span class="topo-inside">PCDV</span><span class="topo-membrane">FGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>48</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>117</td>
      <td>102</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>128</td>
      <td>118</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>147</td>
      <td>129</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>161</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>183</td>
      <td>178</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>202</td>
      <td>194</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>203</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>261</td>
      <td>249</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>276</td>
      <td>262</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>304</td>
      <td>299</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>314</td>
      <td>311</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>332</td>
      <td>315</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b21">6B21</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALF</span><span class="topo-inside">YGGLIRGKNVLSMLTQ</span><span class="topo-membrane">VTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVG</span><span class="topo-inside">ALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFSAV</span><span class="topo-membrane">LIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLV</span><span class="topo-inside">GAYLIG</span><span class="topo-unknown">KRVGFGKEAF</span><span class="topo-inside">KPHNLPMVF</span><span class="topo-membrane">TGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLGA</span><span class="topo-membrane">CSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWG</span><span class="topo-inside">VTMLKR</span><span class="topo-unknown">LLRVDD</span><span class="topo-inside">PCDV</span><span class="topo-membrane">FGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>48</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>117</td>
      <td>102</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>128</td>
      <td>118</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>147</td>
      <td>129</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>161</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>183</td>
      <td>178</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>202</td>
      <td>194</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>203</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>261</td>
      <td>249</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>276</td>
      <td>262</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>298</td>
      <td>282</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>304</td>
      <td>299</td>
      <td>304</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>314</td>
      <td>311</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>332</td>
      <td>315</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
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
<summary><strong>doi/10.1038##nature13419 (1 structure, 6 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a></td>
      <td>2.3</td>
      <td>C2221</td>
      <td>AmtB (residues 26-428), MBP fusion construct</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

**Purification:**

- **Expression system**: E. coli BL21(DE3) Gold
- **Expression construct**: MBP-AmtB fusion (residues 26-428) with pelB signal peptide and 10x His-tag
- **Tag info**: MBP fusion + 10x His-tag, TEV cleaved

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
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>—</td>
      <td>100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM 2-mercaptoethanol, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.4 + 200 mM n-octyl beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Extracted from purified membranes overnight at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>5 mL HisTrap-HP column (GE Healthcare)</td>
      <td>200 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.4 + 0.025% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Washed with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>-free buffer + 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>; eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage</td>
      <td>—</td>
      <td>150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.4 + 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Tag-removed protein collected as flow-through after second HisTrap-HP pass</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentration</td>
      <td>—</td>
      <td>150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.4 + 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>100 kDa MWCO concentrator; stored at -80 C</td>
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
      <td>AmtB at 15 mg/mL in 0.5% <a href="/xray-mp-wiki/reagents/detergents/c8e4/">C8E4</a>, 130 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.4</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>15% <a href="/xray-mp-wiki/reagents/additives/peg-4000/">PEG 4000 (Polyethylene Glycol 4000)</a>, 0.8 M Potassium Formate, 0.1 M Sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a> pH 4.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>One month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen with CrystalCap HT Cryoloops</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Ten-fold molar excess of PG added prior to crystallization. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using PHASER with PDB 1U7G.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLI</span><span class="topo-unknown">GKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDDP</span><span class="topo-inside">CD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>145</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>182</td>
      <td>179</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>194</td>
      <td>183</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>311</td>
      <td>302</td>
      <td>311</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>312</td>
      <td>313</td>
      <td>312</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLIGK</span><span class="topo-unknown">RVGFGKEAFKP</span><span class="topo-inside">HNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TML</span><span class="topo-unknown">KRLLRVD</span><span class="topo-inside">DPCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>145</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>184</td>
      <td>179</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>195</td>
      <td>185</td>
      <td>195</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>201</td>
      <td>196</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>302</td>
      <td>300</td>
      <td>302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>309</td>
      <td>303</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>313</td>
      <td>310</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLIG</span><span class="topo-unknown">KRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TML</span><span class="topo-unknown">KRLLRV</span><span class="topo-inside">DDPCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>145</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>183</td>
      <td>179</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>194</td>
      <td>184</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>302</td>
      <td>300</td>
      <td>302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>308</td>
      <td>303</td>
      <td>308</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>309</td>
      <td>313</td>
      <td>309</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain D (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAH</span><span class="topo-outside">MVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLI</span><span class="topo-unknown">GKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TML</span><span class="topo-unknown">KRLLRVD</span><span class="topo-inside">DPCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>127</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>160</td>
      <td>146</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>182</td>
      <td>179</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>194</td>
      <td>183</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>302</td>
      <td>300</td>
      <td>302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>309</td>
      <td>303</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>313</td>
      <td>310</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain E (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLIGKRV</span><span class="topo-unknown">GFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TMLK</span><span class="topo-unknown">RLLRVD</span><span class="topo-inside">DPCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>145</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>186</td>
      <td>179</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>194</td>
      <td>187</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>303</td>
      <td>300</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>304</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>310</td>
      <td>313</td>
      <td>310</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nh2">4NH2</a> — Chain F (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GASVADKADNAFMMI</span><span class="topo-membrane">CTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVA</span><span class="topo-membrane">FQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIA</span><span class="topo-outside">HMVWGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYLI</span><span class="topo-unknown">GKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNA</span><span class="topo-outside">GSAGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TML</span><span class="topo-unknown">KRLLRVDDP</span><span class="topo-inside">CD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGI</span><span class="topo-outside">FAASSLGGVGFAEGVTMGHQLLVQ</span><span class="topo-membrane">LESIA</span></span>
<span class="topo-ruler">       370       380       390       400      </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRV</span><span class="topo-unknown">PEEQEREGLDVNSHGENAYNA</span></span>
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
      <td>1</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>102</td>
      <td>65</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>144</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>145</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>182</td>
      <td>179</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>194</td>
      <td>183</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>217</td>
      <td>202</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>218</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>302</td>
      <td>300</td>
      <td>302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>311</td>
      <td>303</td>
      <td>311</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>312</td>
      <td>313</td>
      <td>312</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>331</td>
      <td>314</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>355</td>
      <td>332</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>377</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>385</td>
      <td>378</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>406</td>
      <td>386</td>
      <td>406</td>
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
<summary><strong>doi/10.1074##jbc.M608325200 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2nmr">2NMR</a></td>
      <td>2.0 (best)</td>
      <td>—</td>
      <td>AmtB variants: H168A, H168E, H168F, H318A, H318F, H168A/H318A</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (hexagonal form)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AmtB variants</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Five variants (H168A, H168E, H168F, H318A, H318F) and double mutant H168A/H318A crystallized in hexagonal form. Data collected at Swiss Light Source. Structures refined to 2.0-2.2 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2nmr">2NMR</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">PAVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGAL</span><span class="topo-inside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PC</span><span class="topo-membrane">DVFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>2</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>119</td>
      <td>102</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>126</td>
      <td>120</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>332</td>
      <td>313</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>424</td>
      <td>387</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2nmr">2NMR</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">PAVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGAL</span><span class="topo-inside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PC</span><span class="topo-membrane">DVFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>2</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>119</td>
      <td>102</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>126</td>
      <td>120</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>332</td>
      <td>313</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>424</td>
      <td>387</td>
      <td>424</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2nmr">2NMR</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">PAVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGAL</span><span class="topo-inside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PC</span><span class="topo-membrane">DVFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>2</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>119</td>
      <td>102</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>126</td>
      <td>120</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>312</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>332</td>
      <td>313</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>424</td>
      <td>387</td>
      <td>424</td>
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
<summary><strong>doi/10.1073##pnas.0406475101 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1xqf">1XQF</a></td>
      <td>1.8 A</td>
      <td>P6$_3$</td>
      <td>Wild-type full-length E. coli AmtB</td>
      <td>None (apo structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) Gold (Agilent) transformed with MBP-AmtB plasmid
- **Construct**: MBP-AmtB fusion (residues 26-428); secreted with pelB signal peptide and 10x His-tag

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xqf">1XQF</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLE</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>14</td>
      <td>3</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>313</td>
      <td>311</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>332</td>
      <td>314</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>418</td>
      <td>387</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xqf">1XQF</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLE</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>14</td>
      <td>3</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>313</td>
      <td>311</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>332</td>
      <td>314</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>418</td>
      <td>387</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1xqf">1XQF</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AP</span><span class="topo-outside">AVADKADNAFMM</span><span class="topo-membrane">ICTALVLFMTIPGIALFY</span><span class="topo-inside">GGLIRGKNVLSML</span><span class="topo-membrane">TQVTVTFALVCILWVVYGY</span><span class="topo-outside">SLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHV</span><span class="topo-membrane">AFQGSFACITVGLIVGA</span><span class="topo-inside">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERIRFS</span><span class="topo-membrane">AVLIFVVVWLTLSYIPIAHMV</span><span class="topo-outside">WGGGLLASHGALD</span><span class="topo-membrane">FAGGTVVHINAAIAGLVG</span><span class="topo-inside">AYL</span><span class="topo-unknown">IGKRVGFGKEAFK</span><span class="topo-inside">PHNLPMV</span><span class="topo-membrane">FTGTAILYIGWFGFNAGS</span><span class="topo-outside">AGTANEIAALA</span><span class="topo-membrane">FVNTVVATAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AILGWIFG</span><span class="topo-inside">EWALRGKPSLLG</span><span class="topo-membrane">ACSGAIAGLVGVTPAC</span><span class="topo-outside">GYIGV</span><span class="topo-membrane">GGALIIGVVAGLAGLWGV</span><span class="topo-inside">TM</span><span class="topo-unknown">LKRLLRVDD</span><span class="topo-inside">PCD</span><span class="topo-membrane">VFGVHGVCGIVGCIMTGIF</span><span class="topo-outside">AASSLGGVGFAEGVTMGHQL</span><span class="topo-membrane">LVQLESIA</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-membrane">ITIVWSGVVAFIGYKLA</span><span class="topo-inside">DLTVGLRVP</span><span class="topo-unknown">EEQEREGLDVNSHGENAYNADQAQQPAQADLE</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>14</td>
      <td>3</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>45</td>
      <td>33</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>64</td>
      <td>46</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>101</td>
      <td>65</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>102</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>126</td>
      <td>119</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>160</td>
      <td>148</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>178</td>
      <td>161</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>181</td>
      <td>179</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>248</td>
      <td>231</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>249</td>
      <td>260</td>
      <td>249</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>261</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>281</td>
      <td>277</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>301</td>
      <td>300</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>310</td>
      <td>302</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>313</td>
      <td>311</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>332</td>
      <td>314</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>377</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>386</td>
      <td>378</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>418</td>
      <td>387</td>
      <td>418</td>
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


## Biological / Functional Insights

### First structure of an ammonia channel from Amt/MEP/Rh superfamily

The 1.35 A structure of AmtB revealed it as an 11-transmembrane helix channel with a quasi-twofold axis in the plane of the membrane. The structure shows a vestibule that recruits NH4+/NH3, a binding site for NH4+ using pi-cation interactions with Trp148 and Phe107, and a 20 A hydrophobic channel that lowers the NH4+ pKa to below 6 and conducts NH3. Two conserved histidines (His168 and His318) at the center of the channel provide C-H hydrogen bond donors for NH3 passage. Reconstitution into vesicles confirmed AmtB conducts uncharged NH3.

### Mechanism of NH3 conductance

The mechanism involves vestibular recruitment of total Am (NH3 + NH4+), a site that can bind NH4+ via pi-cation interactions, and a hydrophobic channel for NH3 that lowers its pKa to <6. NH4+ becomes deprotonated at the Am2/Am3 site, and uncharged NH3 passes through. This mechanism reconciles seemingly inconsistent proposals about Amt/MEP family function, showing bidirectional NH3 conductance. The narrow hydrophobic channel excludes water and ions while selectively conducting NH3.

### GlnK-mediated channel blockade by R47 insertion

The 1.96 A structure of the AmtB-[GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) complex reveals that the T-loop of [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) becomes highly ordered upon complex formation, inserting R47 deeply into the cytoplasmic vestibule of AmtB. The guanidinium cation of R47 makes five donor hydrogen bonds inside the channel, completely occluding any NH3 or water from passage through the cytosolic portal.

### Specific phosphatidylglycerol binding site

Eight PG molecules resolved on the periplasmic side of AmtB. A distinct conformational change in residues 70-81 forms a specific lipid-binding site. PG forms hydrogen bonds to N72 and E70. Mutation of N72 and N79 to alanine abolishes PG-induced gas-phase stability.

### Allosteric modulation of lipid binding to AmtB

Native MS analysis of AmtB binding to heterogeneous lipid pairs revealed that different lipid combinations display a range of allosteric modulation. The TFCDL (TopFluor cardiolipin) and [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) pair exhibited the strongest positive allosteric modulation, where binding of [POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)](/xray-mp-wiki/reagents/lipids/pope/) enhanced TFCDL binding. Principal component analysis of coupling factors grouped six lipid pairs into four distinct allosteric patterns. The H156A mutation in AmtB completely abolished this positive allostery. Crystal structure of AmtB bound to TFCDL (PDB 6B21, 2.45 A) revealed H156 forms a hydrogen bond with the TFCDL headgroup, and E357 rotates ~150 degrees relative to the PG-bound state to interact with H156. This H156-E357 interaction is unique among all 21 previously determined AmtB structures and provides a mechanism for allosteric communication between lipid binding sites.

### Twin-His motif is essential for optimum substrate conductance

Mutagenesis of His-168 and His-318 to 14 different polar and non-polar residues demonstrated both are absolutely required for optimum methylammonium transport activity in E. coli AmtB. Crystal structures of six variants (H168A, H168E, H168F, H318A, H318F, H168A/H318A) confirmed no structural perturbation beyond the mutated residue. The H168E variant retains partial activity (~30% of WT), and its structure suggests the glutamate side chain can make similar hydrogen-bonding interactions to histidine, explaining the natural Glu substitution found in some fungal Amt proteins. Pore hydration analysis revealed that inactive variants show no electron density at the central pore site S4, while wild-type and H168E show strong peaks, correlating pore hydration with transport activity. Rh30 proteins (RhD, RhCE) lack the twin-His motif entirely and likely do not function as ammonium channels.


## Cross-References

- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">Glycerol Facilitator (GlpF)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/">Rh/Amt/MEP Protein Family</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">E. coli AmtB (ammonia channel)</a> — Alternative protein entry for the same protein; twin-His mutagenesis study
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/concepts/ammonia-channel-mechanism/">Ammonia Channel Mechanism</a> — AmtB is the prototype ammonia channel; this paper established the mechanistic basis for NH3 transport through the Amt/Mep/Rh family
- <a href="/xray-mp-wiki/concepts/ammonium-transport/">Ammonium Transport</a> — AmtB is an ammonium transport protein from the Mep/Amt/Rh family
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Referenced in context related to LDAO
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">Glnk</a> — Referenced in context related to Glnk
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in context related to Imidazole
