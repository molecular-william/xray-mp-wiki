---
title: "Mep2 Ammonium Transceptor (S. cerevisiae and C. albicans)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11337]
verified: agent
uniprot_id: ['P41948', 'Q59UP8']
---

# Mep2 Ammonium Transceptor (S. cerevisiae and C. albicans)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41948">UniProt: P41948</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q59UP8">UniProt: Q59UP8</a>

<span class="expr-badge">Candida ALBICANS</span>

## Overview

Mep2 (methylammonium permease) proteins are fungal ammonium transceptors that function both as transporters for ammonium uptake and as sensors/receptors for nitrogen-dependent filamentous growth. Mep2 belongs to the Amt/Mep/Rh family of ammonium transporters present in all kingdoms of life. Unlike bacterial Amt proteins, which are regulated by [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) binding, fungal Mep2 is regulated by phosphorylation of a C-terminal region (CTR) residue Ser457 (ScMep2) / Ser453 (CaMep2) by the Npr1 kinase. X-ray crystal structures of Mep2 from Saccharomyces cerevisiae and Candida albicans reveal closed, non-phosphorylated conformations with a two-tier channel block on the cytoplasmic side: ICL1 (via Tyr-His hydrogen bond with the twin-His motif) and ICL3. Structure of phosphorylation-mimicking mutants (S453D, R452D/S453D) and a [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant (442Δ) show conformational changes in the CTR that suggest a mechanism for phosphorylation-dependent channel opening.

## Publications

### doi/10.1038##ncomms11337

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aex">5AEX</a></td>
      <td>2.65</td>
      <td>Not specified</td>
      <td>ScMep2 (S. cerevisiae, residues 2-485, N4Q mutant)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aez">5AEZ</a></td>
      <td>\'2.4\'</td>
      <td>R3</td>
      <td>CaMep2 (C. albicans, residues 2-480, N4Q mutant)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5af1">5AF1</a></td>
      <td>Not specified</td>
      <td>P3</td>
      <td>CaMep2 (C. albicans, residues 2-480, N4Q mutant)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aid">5AID</a></td>
      <td>\'3.4\'</td>
      <td>Not specified</td>
      <td>CaMep2 442Δ <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> mutant (lacking AI region residues 443-480)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ah3">5AH3</a></td>
      <td>\'2.4\'</td>
      <td>Not specified</td>
      <td>CaMep2 R452D/S453D (DD mutant, phosphorylation-mimicking)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5fuf">5FUF</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>CaMep2 S453D (single D mutant, phosphorylation-mimicking)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae W303 pep4Δ strain (galactose-inducible expression)
- **Construct**: ScMep2 (residues 2-485, N4Q to prevent glycosylation) or CaMep2 (residues 2-480, N4Q), C-terminal His tag

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
      <td>Bead beating or cell disruptor at 35,000 psi</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 300 mM NaCl</td>
      <td>S. cerevisiae cells grown in synthetic minimal medium lacking histidine with 1% <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a>, then switched to YP medium with 1.5% galactose for 16-20 h induction. OD600 typically 18-20.</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 300 mM NaCl</td>
      <td>Membranes collected at 200,000g for 90 min. Membrane protein extraction in 1:1 (w/w) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> mixture, 1% total detergent, stirring overnight at 4 C.</td>
    </tr>
    <tr>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IMAC</td>
      <td>Chelating Sepharose (GE Healthcare)</td>
      <td>20 mM Tris pH 8.0, 300 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 15 CV buffer containing 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in 3 CV.</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.0-7.5, 100 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Second gel filtration step for detergent exchange. CaMep2 required 0.05% decyl-<a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>) for diffracting crystals.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ScMep2 or CaMep2 in detergent-containing buffer</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>ScMep2 crystallized in presence of 0.2 M ammonium ions. CaMep2: R3 and P3 crystal forms obtained. <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> mutant 442Δ crystallized from a similar condition. DD mutant and S453D mutant crystallized at 2.4 A resolution. Data collected at Newcastle University Structural Biology Laboratory (beamline not specified). Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using archaeal AfAmt-1 (PDB 2B2H) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aex">5AEX</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SYNFTGTPTGEGTGGNSLTTDLNTQFDLANMGWIG</span><span class="topo-membrane">VASAGVWIMVPGIGLLYS</span><span class="topo-outside">GLSRKKHALSL</span><span class="topo-membrane">LWASMMASAVCIFQWFFWGYSLA</span><span class="topo-inside">FSHNTRGNGFIGTLEFFGFRNVLGAPSSVSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PDILFA</span><span class="topo-membrane">VYQGMFAAVTGALMLGGAC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">FPMMVFLFLWMTIVYCPIACWV</span><span class="topo-inside">WNAEGWLVKLGSLD</span><span class="topo-membrane">YAGGLCVHLTSGHGGLVYALI</span><span class="topo-outside">LGKRNDPVTRKGMPKYKPHSVT</span><span class="topo-membrane">SVVLGTVFLWF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GWMFFNGGS</span><span class="topo-inside">AGNATIRAWYS</span><span class="topo-membrane">IMSTNLAAACGGLTWMVIDY</span><span class="topo-outside">FRCGRKWTTV</span><span class="topo-membrane">GLCSGIIAGLVGITPAA</span><span class="topo-inside">GFVPI</span><span class="topo-membrane">WSAVVIGVVTGAGCNLAVDL</span><span class="topo-outside">KSLLRIDDG</span><span class="topo-membrane">LDCYSIHGVGGCIGSVLTG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">IF</span><span class="topo-inside">AA</span><span class="topo-unknown">DYVNATA</span><span class="topo-inside">GSYISPIDGGWINHHYKQVGYQ</span><span class="topo-membrane">LAGICAALAWTVTVTSILLLTMNAI</span><span class="topo-outside">PFLKLRLSADEEELGTDAAQIGEFTYEESTAYIPEPIRS</span><span class="topo-unknown">KTSAQMPPPHENIDDKIVGNTDA</span></span>
<span class="topo-ruler">       490       500     </span>
<span class="topo-line"><span class="topo-unknown">EKNSTPSDASSTKNTDHIVHHHHHH</span></span>
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
      <td>2</td>
      <td>36</td>
      <td>2</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>37</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>65</td>
      <td>55</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>88</td>
      <td>66</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>126</td>
      <td>89</td>
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
      <td>150</td>
      <td>146</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>186</td>
      <td>173</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>207</td>
      <td>187</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>229</td>
      <td>208</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>249</td>
      <td>230</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>250</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>280</td>
      <td>261</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>307</td>
      <td>291</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>312</td>
      <td>308</td>
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
      <td>341</td>
      <td>333</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>362</td>
      <td>342</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>364</td>
      <td>363</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>365</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>372</td>
      <td>393</td>
      <td>372</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>394</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>457</td>
      <td>419</td>
      <td>457</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aex">5AEX</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SYNFTGTPTGEGTGGNSLTTDLNTQFDLANMGWIG</span><span class="topo-membrane">VASAGVWIMVPGIGLLYS</span><span class="topo-outside">GLSRKKHALSL</span><span class="topo-membrane">LWASMMASAVCIFQWFFWGYSLA</span><span class="topo-inside">FSHNTRGNGFIGTLEFFGFRNVLGAPSSVSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PDILFA</span><span class="topo-membrane">VYQGMFAAVTGALMLGGAC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">FPMMVFLFLWMTIVYCPIACWV</span><span class="topo-inside">WNAEGWLVKLGSLD</span><span class="topo-membrane">YAGGLCVHLTSGHGGLVYALI</span><span class="topo-outside">LGKRNDPVTRKGMPKYKPHSVT</span><span class="topo-membrane">SVVLGTVFLWF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GWMFFNGGS</span><span class="topo-inside">AGNATIRAWYS</span><span class="topo-membrane">IMSTNLAAACGGLTWMVIDY</span><span class="topo-outside">FRCGRKWTTV</span><span class="topo-membrane">GLCSGIIAGLVGITPAA</span><span class="topo-inside">GFVPI</span><span class="topo-membrane">WSAVVIGVVTGAGCNLAVDL</span><span class="topo-outside">KSLLRIDDG</span><span class="topo-membrane">LDCYSIHGVGGCIGSVLTG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">IF</span><span class="topo-inside">AA</span><span class="topo-unknown">DYVNATA</span><span class="topo-inside">GSYISPIDGGWINHHYKQVGYQ</span><span class="topo-membrane">LAGICAALAWTVTVTSILLLTMNAI</span><span class="topo-outside">PFLKLRLSADEEELGTDAAQIGEFTYEESTAYIPEPIRS</span><span class="topo-unknown">KTSAQMPPPHENIDDKIVGNTDA</span></span>
<span class="topo-ruler">       490       500     </span>
<span class="topo-line"><span class="topo-unknown">EKNSTPSDASSTKNTDHIVHHHHHH</span></span>
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
      <td>2</td>
      <td>36</td>
      <td>2</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>37</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>65</td>
      <td>55</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>88</td>
      <td>66</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>126</td>
      <td>89</td>
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
      <td>150</td>
      <td>146</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>186</td>
      <td>173</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>207</td>
      <td>187</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>229</td>
      <td>208</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>249</td>
      <td>230</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>250</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>280</td>
      <td>261</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>307</td>
      <td>291</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>312</td>
      <td>308</td>
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
      <td>341</td>
      <td>333</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>362</td>
      <td>342</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>364</td>
      <td>363</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>365</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>372</td>
      <td>393</td>
      <td>372</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>394</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>457</td>
      <td>419</td>
      <td>457</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aex">5AEX</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">SYNFTGTPTGEGTGGNSLTTDLNTQFDLANMGWIG</span><span class="topo-membrane">VASAGVWIMVPGIGLLYS</span><span class="topo-outside">GLSRKKHALSL</span><span class="topo-membrane">LWASMMASAVCIFQWFFWGYSLA</span><span class="topo-inside">FSHNTRGNGFIGTLEFFGFRNVLGAPSSVSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PDILFA</span><span class="topo-membrane">VYQGMFAAVTGALMLGGAC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">FPMMVFLFLWMTIVYCPIACWV</span><span class="topo-inside">WNAEGWLVKLGSLD</span><span class="topo-membrane">YAGGLCVHLTSGHGGLVYALI</span><span class="topo-outside">LGKRNDPVTRKGMPKYKPHSVT</span><span class="topo-membrane">SVVLGTVFLWF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GWMFFNGGS</span><span class="topo-inside">AGNATIRAWYS</span><span class="topo-membrane">IMSTNLAAACGGLTWMVIDY</span><span class="topo-outside">FRCGRKWTTV</span><span class="topo-membrane">GLCSGIIAGLVGITPAA</span><span class="topo-inside">GFVPI</span><span class="topo-membrane">WSAVVIGVVTGAGCNLAVDL</span><span class="topo-outside">KSLLRIDDG</span><span class="topo-membrane">LDCYSIHGVGGCIGSVLTG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">IF</span><span class="topo-inside">AA</span><span class="topo-unknown">DYVNATA</span><span class="topo-inside">GSYISPIDGGWINHHYKQVGYQ</span><span class="topo-membrane">LAGICAALAWTVTVTSILLLTMNAI</span><span class="topo-outside">PFLKLRLSADEEELGTDAAQIGEFTYEESTAYIPEPIRS</span><span class="topo-unknown">KTSAQMPPPHENIDDKIVGNTDA</span></span>
<span class="topo-ruler">       490       500     </span>
<span class="topo-line"><span class="topo-unknown">EKNSTPSDASSTKNTDHIVHHHHHH</span></span>
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
      <td>2</td>
      <td>36</td>
      <td>2</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>37</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>65</td>
      <td>55</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>88</td>
      <td>66</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>126</td>
      <td>89</td>
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
      <td>150</td>
      <td>146</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>186</td>
      <td>173</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>207</td>
      <td>187</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>229</td>
      <td>208</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>249</td>
      <td>230</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>250</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>280</td>
      <td>261</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>290</td>
      <td>281</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>307</td>
      <td>291</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>312</td>
      <td>308</td>
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
      <td>341</td>
      <td>333</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>362</td>
      <td>342</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>364</td>
      <td>363</td>
      <td>364</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>371</td>
      <td>365</td>
      <td>371</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>372</td>
      <td>393</td>
      <td>372</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>394</td>
      <td>418</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>457</td>
      <td>419</td>
      <td>457</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aez">5AEZ</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSGQFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLL</span><span class="topo-outside">YSGISRKKHALSLM</span><span class="topo-membrane">WAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGA</span><span class="topo-outside">GCERARLGPM</span><span class="topo-membrane">MVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSSIV</span><span class="topo-membrane">MGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVGL</span><span class="topo-membrane">CMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFA</span><span class="topo-outside">VDLKDLLQIDDGMD</span><span class="topo-membrane">VWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRSTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>48</td>
      <td>33</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>62</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>84</td>
      <td>63</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>147</td>
      <td>138</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>226</td>
      <td>199</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>243</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>273</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>301</td>
      <td>287</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>324</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>356</td>
      <td>338</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>455</td>
      <td>407</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aez">5AEZ</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSGQFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLL</span><span class="topo-outside">YSGISRKKHALSLM</span><span class="topo-membrane">WAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGA</span><span class="topo-outside">GCERARLGPM</span><span class="topo-membrane">MVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSSIV</span><span class="topo-membrane">MGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVGL</span><span class="topo-membrane">CMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFA</span><span class="topo-outside">VDLKDLLQIDDGMD</span><span class="topo-membrane">VWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRSTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>48</td>
      <td>33</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>62</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>84</td>
      <td>63</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>147</td>
      <td>138</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>226</td>
      <td>199</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>243</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>273</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>301</td>
      <td>287</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>324</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>356</td>
      <td>338</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>455</td>
      <td>407</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aez">5AEZ</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSGQFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLL</span><span class="topo-outside">YSGISRKKHALSLM</span><span class="topo-membrane">WAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGA</span><span class="topo-outside">GCERARLGPM</span><span class="topo-membrane">MVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSSIV</span><span class="topo-membrane">MGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVGL</span><span class="topo-membrane">CMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFA</span><span class="topo-outside">VDLKDLLQIDDGMD</span><span class="topo-membrane">VWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRSTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>48</td>
      <td>33</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>62</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>84</td>
      <td>63</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>147</td>
      <td>138</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>226</td>
      <td>199</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>243</td>
      <td>227</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>286</td>
      <td>273</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>301</td>
      <td>287</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>337</td>
      <td>324</td>
      <td>337</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>356</td>
      <td>338</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>455</td>
      <td>407</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5af1">5AF1</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYSGI</span><span class="topo-inside">SRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span><span class="topo-membrane">LY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFNGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADYVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450 </span>
<span class="topo-line"><span class="topo-outside">MIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRS</span></span>
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
      <td>2</td>
      <td>31</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>59</td>
      <td>53</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>82</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>118</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>137</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>142</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>164</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>178</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>199</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>202</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>252</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>273</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>281</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>304</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>324</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>333</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>354</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>379</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>407</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>451</td>
      <td>410</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5af1">5AF1</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYSGI</span><span class="topo-inside">SRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span><span class="topo-membrane">LY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFNGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADYVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450 </span>
<span class="topo-line"><span class="topo-outside">MIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRS</span></span>
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
      <td>2</td>
      <td>31</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>59</td>
      <td>53</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>82</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>118</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>137</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>142</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>164</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>178</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>199</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>202</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>252</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>273</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>281</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>304</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>324</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>333</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>354</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>379</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>407</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>451</td>
      <td>410</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5af1">5AF1</a> — Chain D (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYSGI</span><span class="topo-inside">SRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span><span class="topo-membrane">LY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">QGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFNGG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADYVA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450 </span>
<span class="topo-line"><span class="topo-outside">MIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRLHEDEEMLGTDLAQIGEYAYYADDDPETNPYVLEPIRS</span></span>
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
      <td>2</td>
      <td>31</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>59</td>
      <td>53</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>82</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>118</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>137</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>142</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>164</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>178</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>199</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>202</td>
      <td>223</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>240</td>
      <td>224</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>252</td>
      <td>243</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>273</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>281</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>299</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>304</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>324</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>333</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>354</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>379</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>407</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>451</td>
      <td>410</td>
      <td>453</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aid">5AID</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYS</span><span class="topo-inside">GISRK</span><span class="topo-unknown">K</span><span class="topo-inside">HALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LG</span><span class="topo-unknown">KRHDPVAKGKVPKY</span><span class="topo-inside">KPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-outside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRL</span><span class="topo-unknown">HEDEEMLGTDLAQIGEYAYYADDDPEHHHHHH</span></span>
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
      <td>4</td>
      <td>33</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>55</td>
      <td>51</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>61</td>
      <td>57</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>218</td>
      <td>223</td>
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>326</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>335</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>416</td>
      <td>410</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aid">5AID</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYS</span><span class="topo-inside">GISRK</span><span class="topo-unknown">K</span><span class="topo-inside">HALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LG</span><span class="topo-unknown">KRHDPVAKGKVPKY</span><span class="topo-inside">KPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-outside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRL</span><span class="topo-unknown">HEDEEMLGTDLAQIGEYAYYADDDPEHHHHHH</span></span>
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
      <td>4</td>
      <td>33</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>55</td>
      <td>51</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>61</td>
      <td>57</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>218</td>
      <td>223</td>
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>326</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>335</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>416</td>
      <td>410</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aid">5AID</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-outside">QFTGTGTGGDVFKVDLNEQFDRADMVWIGT</span><span class="topo-membrane">ASVLVWIMIPGVGLLYS</span><span class="topo-inside">GISRK</span><span class="topo-unknown">K</span><span class="topo-inside">HALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-outside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-inside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-outside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-inside">LG</span><span class="topo-unknown">KRHDPVAKGKVPKY</span><span class="topo-inside">KPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-outside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-inside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-outside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAVDL</span><span class="topo-inside">KDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-outside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440        </span>
<span class="topo-line"><span class="topo-outside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-inside">PFLRIRL</span><span class="topo-unknown">HEDEEMLGTDLAQIGEYAYYADDDPEHHHHHH</span></span>
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
      <td>4</td>
      <td>33</td>
      <td>4</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>34</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>55</td>
      <td>51</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>61</td>
      <td>57</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>203</td>
      <td>202</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>218</td>
      <td>223</td>
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>326</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>335</td>
      <td>327</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>416</td>
      <td>410</td>
      <td>416</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ah3">5AH3</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLYS</span><span class="topo-outside">GISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-outside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-inside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-outside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-outside">PFLRIRLHED</span><span class="topo-unknown">EEML</span><span class="topo-outside">GTDLAQIGEYAYYADDDPETNPYVLEPIDDT</span><span class="topo-unknown">TISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>61</td>
      <td>51</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
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
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>419</td>
      <td>410</td>
      <td>419</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>454</td>
      <td>424</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ah3">5AH3</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLYS</span><span class="topo-outside">GISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-outside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-inside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-outside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-outside">PFLRIRLHED</span><span class="topo-unknown">EEML</span><span class="topo-outside">GTDLAQIGEYAYYADDDPETNPYVLEPIDDT</span><span class="topo-unknown">TISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>61</td>
      <td>51</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
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
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>419</td>
      <td>410</td>
      <td>419</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>454</td>
      <td>424</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ah3">5AH3</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLYS</span><span class="topo-outside">GISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAGC</span><span class="topo-outside">ERARL</span><span class="topo-membrane">GPMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAYSLW</span><span class="topo-outside">LGKRHDPVAKGKVPKYKPHSVS</span><span class="topo-membrane">SIVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GG</span><span class="topo-inside">STGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLVDWF</span><span class="topo-outside">RTGGKWST</span><span class="topo-membrane">VGLCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AADY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VAMIDGTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAMDRI</span><span class="topo-outside">PFLRIRLHED</span><span class="topo-unknown">EEML</span><span class="topo-outside">GTDLAQIGEYAYYADDDPETNPYVLEPIDDT</span><span class="topo-unknown">TISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>61</td>
      <td>51</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>140</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
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
      <td>275</td>
      <td>255</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>276</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>284</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>381</td>
      <td>357</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>409</td>
      <td>382</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>419</td>
      <td>410</td>
      <td>419</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>454</td>
      <td>424</td>
      <td>454</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5fuf">5FUF</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLY</span><span class="topo-outside">SGISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAG</span><span class="topo-outside">CERARLG</span><span class="topo-membrane">PMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSS</span><span class="topo-membrane">IVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVG</span><span class="topo-membrane">LCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDL</span><span class="topo-unknown">AQI</span><span class="topo-outside">GEYAYYADDDPETNPYVLEPIRDTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>61</td>
      <td>50</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>145</td>
      <td>139</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>146</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>224</td>
      <td>199</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>273</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>301</td>
      <td>286</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>455</td>
      <td>431</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5fuf">5FUF</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLY</span><span class="topo-outside">SGISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAG</span><span class="topo-outside">CERARLG</span><span class="topo-membrane">PMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSS</span><span class="topo-membrane">IVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVG</span><span class="topo-membrane">LCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDL</span><span class="topo-unknown">AQI</span><span class="topo-outside">GEYAYYADDDPETNPYVLEPIRDTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>61</td>
      <td>50</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>145</td>
      <td>139</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>146</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>224</td>
      <td>199</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>273</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>301</td>
      <td>286</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>455</td>
      <td>431</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5fuf">5FUF</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSG</span><span class="topo-inside">QFTGTGTGGDVFKVDLNEQFDRADMVWIG</span><span class="topo-membrane">TASVLVWIMIPGVGLLY</span><span class="topo-outside">SGISRKKHALSL</span><span class="topo-membrane">MWAALMAACVAAFQWFWWGYSLV</span><span class="topo-inside">FAHNGSVFLGTLQNFCLKDVLGAPSIVKTVPDILFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LYQGMFAAVTAILMAGAG</span><span class="topo-outside">CERARLG</span><span class="topo-membrane">PMMVFLFIWLTVVYCPIAYWT</span><span class="topo-inside">WGGNGWLVSLGALD</span><span class="topo-membrane">FAGGGPVHENSGFAALAY</span><span class="topo-outside">SLWLGKRHDPVAKGKVPKYKPHSVSS</span><span class="topo-membrane">IVMGTIFLWFGWYGFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GGS</span><span class="topo-inside">TGNSSMRSWYA</span><span class="topo-membrane">CVNTNLAAATGGLTWMLV</span><span class="topo-outside">DWFRTGGKWSTVG</span><span class="topo-membrane">LCMGAIAGLVGITPAA</span><span class="topo-inside">GYVPV</span><span class="topo-membrane">YTSVIFGIVPAIICNFAV</span><span class="topo-outside">DLKDLLQIDDG</span><span class="topo-membrane">MDVWALHGVGGFVGNFMTGLF</span><span class="topo-inside">AA</span><span class="topo-unknown">DY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">VAMID</span><span class="topo-inside">GTEIDGGWMNHHWKQL</span><span class="topo-membrane">GYQLAGSCAVAAWSFTVTSIILLAM</span><span class="topo-outside">DRIPFLRIRLHEDEEMLGTDL</span><span class="topo-unknown">AQI</span><span class="topo-outside">GEYAYYADDDPETNPYVLEPIRDTT</span><span class="topo-unknown">ISQPLPHIDGVADGSSNNDSGEAKN</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">HHHHHH</span></span>
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
      <td>4</td>
      <td>32</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>61</td>
      <td>50</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>84</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>120</td>
      <td>85</td>
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
      <td>145</td>
      <td>139</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>146</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>167</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>224</td>
      <td>199</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>243</td>
      <td>225</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>254</td>
      <td>244</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>273</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>301</td>
      <td>286</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>306</td>
      <td>302</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>335</td>
      <td>325</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>356</td>
      <td>336</td>
      <td>356</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>358</td>
      <td>357</td>
      <td>358</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>365</td>
      <td>359</td>
      <td>365</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>406</td>
      <td>382</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>455</td>
      <td>431</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Two-tier cytoplasmic channel block in non-phosphorylated Mep2

In the closed, non-phosphorylated state, Mep2 exhibits a two-tier block of the cytoplasmic channel exit. First tier: ICL1 has moved inward (~10 A backbone shift) and unwound relative to bacterial Amts. The side chain hydroxyl of Tyr49 (CaMep2) / Tyr53 (ScMep2) forms a strong hydrogen bond with the epsilon-2 nitrogen of His342 (twin-His motif residue), directly closing the channel. Second tier: ICL3 is shifted up to ~10 A and forms an additional barrier. The conserved RxK motif in ICL1 (Arg54, Lys55, Lys56 in CaMep2) undergoes large conformational changes (Arg54 head group moved ~11 A, Lys55 head group moved ~20 A relative to Amt-1). This two-tier block likely ensures minimal ammonium transport under nitrogen-sufficient conditions.

### C-terminal region (CTR) and AI region structure

The CTR in Mep2 is elongated and makes relatively few contacts with the main body of the transporter compared to bacterial Amts. The phosphorylation target Ser457/453 is located in a well-defined electronegative pocket ~30 A away from the channel exit, formed by backbone carbonyl atoms of Asp419, Glu420, and Glu421 (CaMep2). The adjacent AI (autoinhibitory) region bridges the CTR and the main body of Mep2. Deletion of the AI region (442Δ mutant) results in a constitutively active channel.

### Phosphorylation-mimicking mutants show CTR conformational changes

The S453D and R452D/S453D (DD) mutants of CaMep2 show substantial conformational changes in the conserved part of the CTR. A 12-residue alpha-helix forms from Leu427 to Asp438, and the ExxGxD motif (Glu420-Leu423) undergoes rearrangement. In the DD mutant, the AI segment shows only a slight shift relative to wild-type. MD simulations (200 ns) show that the distance between Asp453 and Glu420 acidic oxygens increases from ~7 to >22 A due to electrostatic repulsion, supporting the model that phosphorylation-induced charge repulsion drives CTR conformational changes.

### Tyr-His hydrogen bond is essential for channel closure

The Tyr49-His342 (CaMep2) / Tyr53-His348 (ScMep2) hydrogen bond is the key interaction closing the Mep2 channel. In bacterial Amts, the equivalent Tyr side chain is rotated ~4 A away, leaving the channel open. The Y53A mutant in ScMep2 results in a constitutively active transporter, confirming the functional importance of this hydrogen bond. The Tyr residue is highly conserved in fungal Mep2 orthologues, suggesting this is a general mechanism for Mep2 channel closure.

### Model for phosphorylation-regulated Mep2 gating

A model is proposed where phosphorylation at Ser453 in the CTR introduces steric clashes and electrostatic repulsion that cause conformational changes in the CTR. These changes allow the CTR to interact with ICL3, which moves inward to open the channel. This is opposite to plant AMT transporters, where phosphorylation closes the channel. In Mep2, the phosphorylation site is peripheral (near the AI region), and phosphorylation drives channel opening; in plant AMTs, the phosphorylation site is central (near the ExxGxD motif), and phosphorylation drives channel closure. The model explains how intra-monomeric CTR-ICL1/ICL3 interactions regulate both fungal and plant ammonium transporters: close interactions generate open channels, while lack of interactions leads to inactive states.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/rh-amt-mep-protein-family/">Rh/Amt/MEP Protein Family</a> — Mep2 is a member of the Amt/Mep/Rh ammonium transporter family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/amt-b/">Ammonium Transporter AmtB (E. coli)</a> — Bacterial orthologue used for structural comparison; bacterial Amts show open channel conformation
- <a href="/xray-mp-wiki/proteins/other-ion-channels/a-fulgidus-amt1/">A. fulgidus Amt-1</a> — Archaeal orthologue used as molecular replacement search model and for structural comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/twin-histidine-motif/">Twin-Histidine Motif in Ammonium Channels</a> — The twin-His motif is essential for ammonium transport in Mep2 as in all Amt/Mep/Rh family members
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glnk/">GLNK</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
