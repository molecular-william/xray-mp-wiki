---
title: "MacB ABC Transporter from Acinetobacter baumannii"
created: 2026-06-16
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-01399-2]
verified: agent
uniprot_id: A0A0D8G707
---

# MacB ABC Transporter from Acinetobacter baumannii

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0D8G707">UniProt: A0A0D8G707</a>

<span class="expr-badge">Acinetobacter baumannii</span>

## Overview

MacB from Acinetobacter baumannii is an ATP-binding cassette (ABC) transporter that functions as part of the tripartite MacA-MacB-TolC efflux complex. It actively extrudes macrolide antibiotics, virulence factors, peptides, and cell envelope precursors across both the plasma membrane and outer membrane. The crystal structure at 3.4 Å resolution reveals a homodimer in which each protomer contains a nucleotide-binding domain (NBD) and four transmembrane helices that protrude into the periplasm to form a periplasmic binding domain (PLD) for interaction with the membrane fusion protein MacA. MacB represents a structurally unique ABC transporter with the smallest number of transmembrane helices (four) among characterized ABC exporters.


## Publications

### doi/10.1038##s41467-017-01399-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5gko">5GKO</a></td>
      <td>3.40</td>
      <td>P4₁2₁2</td>
      <td>Full-length A. baumannii MacB (Se-Met derivative)</td>
      <td>Se-Met</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ws4">5WS4</a></td>
      <td>3.40</td>
      <td>P4₁2₁2</td>
      <td>Full-length A. baumannii MacB</td>
      <td>ADPβS</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length A. baumannii MacB with C-terminal [His6-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)
- **Notes**: Expressed in E. coli C43(DE3) cells

**Purification:**

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length A. baumannii MacB with C-terminal His6-tag
- **Tag info**: C-terminal His6-tag

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
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a></td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.0, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a></td>
      <td>Membranes collected after <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a> lysis and low-speed centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.0, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/n-undecyl-beta-d-maltoside/">n-undecyl-β-D-maltoside (UDM)</a></td>
      <td>Solubilized on ice for 1 h with protease inhibitors (Roche)</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td>Chelating Sepharose resin immobilized with Ni2+</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 100 mM NaCl, 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a></td>
      <td>Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> in wash buffer</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex-200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 100 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a></td>
      <td>Flow rate 0.3 ml/min using AKTA explorer 10 <a href="/xray-mp-wiki/reagents/ligands/s-citalopram/">S</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~24 mg/ml MacB in 20 mM Tris pH 7.5, 100 mM NaCl, 10% (v/v) glycerol, 0.05% (w/v) UDM
**Yield**: Not specified
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MacB at ~24 mg/ml with 10 mM ADPβS and 2 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.2-1.3 M <a href="/xray-mp-wiki/reagents/buffers/citrate/">sodium citrate</a>, 100 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.2</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (protein:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> gradually increased to 30% (v/v) by soaking in several steps</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting-drop vapor diffusion</a> technique. For Se-Met labeling, M9 minimal medium with seleno-<a href="/xray-mp-wiki/reagents/ligands/l-methionine/">L-methionine</a>; 2 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> added instead of ADPβS before crystallization.</td>
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
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.2</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>25 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Citrate: 1.2-1.3 M [buffer]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5gko">5GKO</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHMT</span><span class="topo-inside">KQALLEVSNLVREFPAGESTIQILKGIDLTIYEGELVAIVGQSGSGKSTLMNILGCLDRPTSGSYKVNGQETGKLEPDQLAQLRREYFGFIFQRYHLLGDLSAEGNVEVPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VYAGVTPADRKQRATALLTELGLGTKTQNRPSQLSGGQQQRVSIARALMNGGDVILADEPTGALDSHSGVEVMRILRELNAAGHTIILVTHDMQVAKNATRIIEISDGEIISDRPNVPDQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLEEVKSDPDAAPA</span><span class="topo-unknown">LQNKQKKGKSIS</span><span class="topo-inside">AWR</span><span class="topo-unknown">STLDRLSEAFQMALLSMNA</span><span class="topo-inside">H</span><span class="topo-membrane">RMRTFLTMLGIIIGIASVVTVVAL</span><span class="topo-outside">GNGSQQQILSNISSLGTNTITVFQGRGFGDNSKTANFKTLVPADADA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LMTQPYVSAVSPMVSTSKTMRYQQNEANATINGVSNDYFDVKGLVFKDGQTFDQRSVRDRSQDVVIDTNTQKQFFSDGTNPIGQVVLLGSVPARIIGIVEPQTSGMGSDDTLNVYMPYTT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VMSRMLGQAHVRNIVVRINDKYSTSAAENAIVNLLTQRHGAQDIFTMNSDSIRQTIEKTTSTMTL</span><span class="topo-membrane">LVSAIAVISLVVGGIGVMNIMLV</span><span class="topo-inside">SVTERTQEIGVRMAVGARQSDIL</span><span class="topo-membrane">QQFLIEAIL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670 </span>
<span class="topo-line"><span class="topo-membrane">VCLIGGVLGVLLSLGLGQLI</span><span class="topo-outside">NKFAGGNFAVA</span><span class="topo-membrane">YSTTSIVAAFVCSTLIGVVFGFLPAK</span><span class="topo-inside">NAAKLDPVAALSRE</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>254</td>
      <td>3</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>269</td>
      <td>260</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>288</td>
      <td>263</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>289</td>
      <td>282</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>313</td>
      <td>283</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>545</td>
      <td>307</td>
      <td>538</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>568</td>
      <td>539</td>
      <td>561</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>569</td>
      <td>591</td>
      <td>562</td>
      <td>584</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>592</td>
      <td>620</td>
      <td>585</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>621</td>
      <td>631</td>
      <td>614</td>
      <td>624</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>632</td>
      <td>657</td>
      <td>625</td>
      <td>650</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>658</td>
      <td>671</td>
      <td>651</td>
      <td>664</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5gko">5GKO</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHMT</span><span class="topo-inside">KQALLEVSNLVREFPAGESTIQILKGIDLTIYEGELVAIVGQSGSGKSTLMNILGCLDRPTSGSYKVNGQETGKLEPDQLAQLRREYFGFIFQRYHLLGDLSAEGNVEVPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VYAGVTPADRKQRATALLTELGLGTKTQNRPSQLSGGQQQRVSIARALMNGGDVILADEPTGALDSHSGVEVMRILRELNAAGHTIILVTHDMQVAKNATRIIEISDGEIISDRPNVPDQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLEEVKSDPDAAPA</span><span class="topo-unknown">LQNKQKKGKSIS</span><span class="topo-inside">AWRS</span><span class="topo-unknown">TLDRLSEAFQMALLSMNA</span><span class="topo-inside">HR</span><span class="topo-membrane">MRTFLTMLGIIIGIASVVTVVAL</span><span class="topo-outside">GNGSQQQILSNISSLGTNTITVFQGRGFGDNSKTANFKTLVPADADA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LMTQPYVSAVSPMVSTSKTMRYQQNEANATINGVSNDYFDVKGLVFKDGQTFDQRSVRDRSQDVVIDTNTQKQFFSDGTNPIGQVVLLGSVPARIIGIVEPQTSGMGSDDTLNVYMPYTT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VMSRMLGQAHVRNIVVRINDKYSTSAAENAIVNLLTQRHGAQDIFTMNSDSIRQTIEKTTSTMTL</span><span class="topo-membrane">LVSAIAVISLVVGGIGVMNIMLV</span><span class="topo-inside">SVTERTQEIGVRMAVGARQSDILQQF</span><span class="topo-membrane">LIEAIL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670 </span>
<span class="topo-line"><span class="topo-membrane">VCLIGGVLGVLLSLGLGQLI</span><span class="topo-outside">NKFAGGNFAVA</span><span class="topo-membrane">YSTTSIVAAFVCSTLIGVVFGFLPAK</span><span class="topo-inside">NAAKLDPVAALSRE</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>254</td>
      <td>3</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>270</td>
      <td>260</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>288</td>
      <td>264</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>290</td>
      <td>282</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>313</td>
      <td>284</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>545</td>
      <td>307</td>
      <td>538</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>568</td>
      <td>539</td>
      <td>561</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>569</td>
      <td>594</td>
      <td>562</td>
      <td>587</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>595</td>
      <td>620</td>
      <td>588</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>621</td>
      <td>631</td>
      <td>614</td>
      <td>624</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>632</td>
      <td>657</td>
      <td>625</td>
      <td>650</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>658</td>
      <td>671</td>
      <td>651</td>
      <td>664</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ws4">5WS4</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHMT</span><span class="topo-inside">KQALLEVSNLVREFPAGESTIQILKGIDLTIYEGELVAIVGQSGSGKSTLMNILGCLDRPTSGSYKVNGQETGKLEPDQLAQLRREYFGFIFQRYHLLGDLSAEGNVEVPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VYAGVTPADRKQRATALLTELGLGTKTQNRPSQLSGGQQQRVSIARALMNGGDVILADEPTGALDSHSGVEVMRILRELNAAGHTIILVTHDMQVAKNATRIIEISDGEIISDRPNVPDQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLEEVKSDPDAAPA</span><span class="topo-unknown">LQNKQKKGKSIS</span><span class="topo-inside">AWR</span><span class="topo-unknown">STLDRLSEAFQMALLSMNA</span><span class="topo-inside">HR</span><span class="topo-membrane">MRTFLTMLGIIIGIASVVTVVAL</span><span class="topo-outside">GNGSQQQILSNISSLGTNTITVFQGRGFGDNSKTANFKTLVPADADA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LMTQPYVSAVSPMVSTSKTMRYQQNEANATINGVSNDYFDVKGLVFKDGQTFDQRSVRDRSQDVVIDTNTQKQFFSDGTNPIGQVVLLGSVPARIIGIVEPQTSGMGSDDTLNVYMPYTT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VMSRMLGQAHVRNIVVRINDKYSTSAAENAIVNLLTQRHGAQDIFTMNSDSIRQTIEKTTSTMT</span><span class="topo-membrane">LLVSAIAVISLVVGGIGVMNIM</span><span class="topo-inside">LVSVTERTQEIGVRMAVGARQSDILQQFL</span><span class="topo-membrane">IEAIL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670 </span>
<span class="topo-line"><span class="topo-membrane">VCLIGGVLGVLLSLGLGQLINKF</span><span class="topo-outside">AGGNFAV</span><span class="topo-membrane">AYSTTSIVAAFVCSTLIGVVFGFLP</span><span class="topo-inside">AKNAAKLDPVAALSRE</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>254</td>
      <td>3</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>269</td>
      <td>260</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>288</td>
      <td>263</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>290</td>
      <td>282</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>313</td>
      <td>284</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>544</td>
      <td>307</td>
      <td>537</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>545</td>
      <td>566</td>
      <td>538</td>
      <td>559</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>595</td>
      <td>560</td>
      <td>588</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>596</td>
      <td>623</td>
      <td>589</td>
      <td>616</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>624</td>
      <td>630</td>
      <td>617</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>631</td>
      <td>655</td>
      <td>624</td>
      <td>648</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>656</td>
      <td>671</td>
      <td>649</td>
      <td>664</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ws4">5WS4</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHMT</span><span class="topo-inside">KQALLEVSNLVREFPAGESTIQILKGIDLTIYEGELVAIVGQSGSGKSTLMNILGCLDRPTSGSYKVNGQETGKLEPDQLAQLRREYFGFIFQRYHLLGDLSAEGNVEVPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VYAGVTPADRKQRATALLTELGLGTKTQNRPSQLSGGQQQRVSIARALMNGGDVILADEPTGALDSHSGVEVMRILRELNAAGHTIILVTHDMQVAKNATRIIEISDGEIISDRPNVPDQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SLEEVKSDPDAAPA</span><span class="topo-unknown">LQNKQKKGKSIS</span><span class="topo-inside">AWRS</span><span class="topo-unknown">TLDRLSEAFQMALLSMNA</span><span class="topo-inside">HR</span><span class="topo-membrane">MRTFLTMLGIIIGIASVVTVVAL</span><span class="topo-outside">GNGSQQQILSNISSLGTNTITVFQGRGFGDNSKTANFKTLVPADADA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LMTQPYVSAVSPMVSTSKTMRYQQNEANATINGVSNDYFDVKGLVFKDGQTFDQRSVRDRSQDVVIDTNTQKQFFSDGTNPIGQVVLLGSVPARIIGIVEPQTSGMGSDDTLNVYMPYTT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VMSRMLGQAHVRNIVVRINDKYSTSAAENAIVNLLTQRHGAQDIFTMNSDSIRQTIEKTTSTMT</span><span class="topo-membrane">LLVSAIAVISLVVGGIGVMNIM</span><span class="topo-inside">LVSVTERTQEIGVRMAVGARQSDILQQFL</span><span class="topo-membrane">IEAIL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670 </span>
<span class="topo-line"><span class="topo-membrane">VCLIGGVLGVLLSLGLGQLINK</span><span class="topo-outside">FAGGNFAV</span><span class="topo-membrane">AYSTTSIVAAFVCSTLIGVVFGFLP</span><span class="topo-inside">AKNAAKLDPVAALSRE</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>254</td>
      <td>3</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>270</td>
      <td>260</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>288</td>
      <td>264</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>290</td>
      <td>282</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>313</td>
      <td>284</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>544</td>
      <td>307</td>
      <td>537</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>545</td>
      <td>566</td>
      <td>538</td>
      <td>559</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>595</td>
      <td>560</td>
      <td>588</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>596</td>
      <td>622</td>
      <td>589</td>
      <td>615</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>623</td>
      <td>630</td>
      <td>616</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>631</td>
      <td>655</td>
      <td>624</td>
      <td>648</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>656</td>
      <td>671</td>
      <td>649</td>
      <td>664</td>
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

### Unique four-TM architecture of MacB

MacB has only four transmembrane helices per monomer, the smallest number among characterized ABC exporters. The TMs are not swapped between half-transporters, and the structure lacks helical extensions into intracellular domains found in most type-I ABC exporters. Despite having only one cytoplasmic loop, MacB preserves two coupling helices (CH1 and CH2). CH1 is in the intracellular loop between TM2 and TM3, while CH2 is located at the carboxy terminus. Both CHs contact only one NBD within the same monomer, unlike Sav1866 and MsbA where CHs contact opposite monomers.

### MacB defines a unique ABC transporter structural class

Comparison with other ABC transporters shows MacB is structurally distinct from both type-I and type-II ABC exporters and importers. The NBD arrangement in the MacB dimer is most similar to the ADP-bound outward-occluded state of the lipid-linked oligosaccharide flippase PglK. The periplasmic domain fold and the arrangement of TMs are unique among bacterial ABC exporters.

### Coupling helix function and importance

Removal of CH2 by truncation of the carboxy terminus of MacB leads to inactivation of drug export, demonstrating the functional importance of the coupling helices. The positions of the CHs and their interactions with the NBDs are similar to other ABC exporters, but the connecting TMs are completely different, and the order of the CHs is opposite due to topological differences.

### Tripartite complex function

MacB functions as part of the MacA-MacB-TolC tripartite complex that spans both the plasma membrane and outer membrane of Gram-negative bacteria. The complex confers resistance to macrolide antibiotics including erythromycin, clarithromycin, azithromycin, roxithromycin, and spiramycin, as confirmed by MIC measurements in drug-sensitive E. coli ΔacrAB ΔmacAB cells expressing A. baumannii MacAB-TolC.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/macb/">MacB ABC Transporter from Aggregatibacter actinomycetemcomitans</a> — Orthologous MacB from related bacterial species with structural comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — MacB is a member of the ABC transporter superfamily with unique structural features
- <a href="/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/">Mechanotransmission</a> — Related biological concept for MacB-type ABC transporters
- <a href="/xray-mp-wiki/reagents/detergents/udm/">n-Undecyl-β-D-Maltoside (UDM)</a> — Detergent used for MacB purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used in purification buffers
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in crystallization reservoir
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Method used for crystallization of MacB
- <a href="/xray-mp-wiki/methods/structure-determination/semet-sad-phasing/">Selenomethionine SAD Phasing</a> — Phase determination method used for MacB structure
