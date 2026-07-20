---
title: "MacB ABC Transporter from Aggregatibacter actinomycetemcomitans"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1712153114]
verified: agent
uniprot_id: Q2EHL8
---

# MacB ABC Transporter from Aggregatibacter actinomycetemcomitans

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q2EHL8">UniProt: Q2EHL8</a>

<span class="expr-badge">Aggregatibacter actinomycetemcomitans</span>

## Overview

MacB is an ABC transporter from Aggregatibacter actinomycetemcomitans that forms a tripartite efflux pump with the MacA adaptor protein and TolC exit duct. It belongs to the type VII ABC transporter superfamily, characterized by a unique four-transmembrane-helix topology, a periplasmic domain between TM1 and TM2, and a [Mechanotransmission](/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/) mechanism that couples cytoplasmic ATP hydrolysis to extracytoplasmic conformational change. Unlike canonical ABC transporters, MacB lacks a central transmembrane cavity and does not transport substrates across the inner membrane; instead, it powers the expulsion of macrolide antibiotics and enterotoxin STII from the periplasm to the extracellular space via a molecular bellows mechanism.


## Publications

### doi/10.1073##pnas.1712153114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a></td>
      <td>3.35</td>
      <td>P21</td>
      <td>Full-length AaMacB (ATP-bound)</td>
      <td>ATP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a></td>
      <td>3.90</td>
      <td>P6522</td>
      <td>Full-length AaMacB (ATP-bound)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5nli">5NLI</a></td>
      <td>Not specified</td>
      <td>—</td>
      <td>MacAB-TolC complex (nucleotide-free)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length AaMacB with N-terminal His-tag
- **Notes**: Expressed in E. coli C43 (DE3) cells

**Purification:**

- **Expression system**: E. coli C43 (DE3)
- **Expression construct**: Full-length AaMacB with N-terminal His-tag

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
      <td>Expressed in E. coli C43 (DE3)</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td>Lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>)</td>
      <td>Purified in lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>) as a stabilizing detergent</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in text</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AaMacB in <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in two distinct crystal forms (P6522 and P21) in the presence of either ATPgammaS or ATP</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNIIEIKQLNRYFGEGENRVHVLKDISLSIERGDFVAIMGQSGSGKSTLMNIIGCLDTATGGSSKIDGKETIELTNDQLSDLRSQKFGFIFQRYNLLSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TAAENVALPAIYAGMPQSQRLERAKQLLEKLGLGDKWQNKPNQLSGGQQQRVSIARALMNGGEIILADQPTGALDSHSGENVMEILRQLHEEGHTIIMVTHDKHIAASANRIIEIKDGEI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ISDTQKRQVKSAVKNPSVF</span><span class="topo-unknown">KGRFGF</span><span class="topo-outside">S</span><span class="topo-unknown">KDQLMEAFRMS</span><span class="topo-membrane">VSAIVAHKMRSLLTMLGIIIGITSVVSVV</span><span class="topo-inside">ALGNGSQQKILENIRGIGTNTMTIF</span><span class="topo-unknown">NGNGFGDRRSRHI</span><span class="topo-inside">QNLKISDANTLSKQSY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">IQSVTPNTSSSGILVVGNKSFTSANLYGIGEQYFDVEGLKLKQGRLLTEDDVDQSNQVVVLDESAKKAIFANENPLGKTVIFNKRPFRVIGVVSDQ</span><span class="topo-unknown">QLGGFPGN</span><span class="topo-inside">SLNLYSPYSTVLNKIT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">GGSRIGSITVKISDDVNSTVAEKSLTELLKSLHGKKDFFIMNSDTIKQTIENTTGTMKLLISS</span><span class="topo-membrane">IAFISLIVGGIGVMNIMLVSVTE</span><span class="topo-outside">RTKEIGVRMAIGARQINI</span><span class="topo-membrane">LQQFLIEAVLICLIGG</span></span>
<span class="topo-ruler">       610       620       630       640       650       660    </span>
<span class="topo-line"><span class="topo-membrane">VAGILLSVLIGVL</span><span class="topo-inside">FNSFITDFSMDFST</span><span class="topo-membrane">ASIVTAVLFSTLIGVLFGYMPAKK</span><span class="topo-outside">AAELNPITALA</span><span class="topo-unknown">QE</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>21</td>
      <td>259</td>
      <td>1</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>266</td>
      <td>246</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>277</td>
      <td>247</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>278</td>
      <td>306</td>
      <td>258</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>331</td>
      <td>287</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>456</td>
      <td>325</td>
      <td>436</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>465</td>
      <td>543</td>
      <td>445</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>544</td>
      <td>566</td>
      <td>524</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>584</td>
      <td>547</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>613</td>
      <td>565</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>614</td>
      <td>627</td>
      <td>594</td>
      <td>607</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>651</td>
      <td>608</td>
      <td>631</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>652</td>
      <td>662</td>
      <td>632</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNIIEIKQLNRYFGEGENRVHVLKDISLSIERGDFVAIMGQSGSGKSTLMNIIGCLDTATGGSSKIDGKETIELTNDQLSDLRSQKFGFIFQRYNLLSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TAAENVALPAIYAGMPQSQRLERAKQLLEKLGLGDKWQNKPNQLSGGQQQRVSIARALMNGGEIILADQPTGALDSHSGENVMEILRQLHEEGHTIIMVTHDKHIAASANRIIEIKDGEI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ISDTQKRQVKSAVKNPSVFKG</span><span class="topo-unknown">RFGFS</span><span class="topo-outside">K</span><span class="topo-unknown">DQLMEAFRMS</span><span class="topo-membrane">VSAIVAHKMRSLLTMLGIIIGITSVVSVV</span><span class="topo-inside">ALGNGSQQKILENIRGIGTNTMTI</span><span class="topo-unknown">FNGNGFGDRRSRHIQ</span><span class="topo-inside">NLKISDANTLSKQSY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">IQSVTPNTSSSGILVVGNKSFTSANLYGIGEQYFDVEGLKLKQGRLLTEDDVDQSNQVVVLDESAKKAIFANENPLGKTVIFNKRPFRVIGVVSDQ</span><span class="topo-unknown">QLGGFPGNS</span><span class="topo-inside">LNLYSPYSTVLNKIT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">GGSRIGSITVKISDDVNSTVAEKSLTELLKS</span><span class="topo-unknown">LHGKKDFFI</span><span class="topo-inside">MNSDTIKQTIENTTGTMKLLISS</span><span class="topo-membrane">IAFISLIVGGIGVMNIMLVSVTE</span><span class="topo-outside">RTKEIGVRMAIGARQINIL</span><span class="topo-membrane">QQFLIEAVLICLIGG</span></span>
<span class="topo-ruler">       610       620       630       640       650       660    </span>
<span class="topo-line"><span class="topo-membrane">VAGILLSVLIGVL</span><span class="topo-inside">FNSFITDFSMDFST</span><span class="topo-membrane">ASIVTAVLFSTLIGVLFGYMPAKK</span><span class="topo-outside">AAELNPITALA</span><span class="topo-unknown">QE</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>21</td>
      <td>261</td>
      <td>1</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>247</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>248</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>278</td>
      <td>306</td>
      <td>258</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>330</td>
      <td>287</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>456</td>
      <td>326</td>
      <td>436</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>511</td>
      <td>446</td>
      <td>491</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>543</td>
      <td>501</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>544</td>
      <td>566</td>
      <td>524</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>585</td>
      <td>547</td>
      <td>565</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>613</td>
      <td>566</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>614</td>
      <td>627</td>
      <td>594</td>
      <td>607</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>651</td>
      <td>608</td>
      <td>631</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>652</td>
      <td>662</td>
      <td>632</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNIIEIKQLNRYFGEGENRVHVLKDISLSIERGDFVAIMGQSGSGKSTLMNIIGCLDTATGGSSKIDGKETIELTNDQLSDLRSQKFGFIFQRYNLLSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TAAENVALPAIYAGMPQSQRLERAKQLLEKLGLGDKWQNKPNQLSGGQQQRVSIARALMNGGEIILADQPTGALDSHSGENVMEILRQLHEEGHTIIMVTHDKHIAASANRIIEIKDGEI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ISDTQKRQVKSAVKNPSVF</span><span class="topo-unknown">KGRFGF</span><span class="topo-outside">S</span><span class="topo-unknown">KDQLMEAFRMS</span><span class="topo-membrane">VSAIVAHKMRSLLTMLGIIIGITSVVSVV</span><span class="topo-inside">ALGNGSQQKILENIRGIGTNTMTIF</span><span class="topo-unknown">NGNGFGDRRSRHI</span><span class="topo-inside">QNLKISDANTLSKQSY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">IQSVTPNTSSSGILVVGNKSFTSANLYGIGEQYFDVEGLKLKQGRLLTEDDVDQSNQVVVLDESAKKAIFANENPLGKTVIFNKRPFRVIGVVSDQ</span><span class="topo-unknown">QLGGFPGN</span><span class="topo-inside">SLNLYSPYSTVLNKIT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">GGSRIGSITVKISDDVNSTVAEKSLTELLKSLHGKKDFFIMNSDTIKQTIENTTGTMKLLISS</span><span class="topo-membrane">IAFISLIVGGIGVMNIMLVSVTE</span><span class="topo-outside">RTKEIGVRMAIGARQINI</span><span class="topo-membrane">LQQFLIEAVLICLIGG</span></span>
<span class="topo-ruler">       610       620       630       640       650       660    </span>
<span class="topo-line"><span class="topo-membrane">VAGILLSVLIGVL</span><span class="topo-inside">FNSFITDFSMDFST</span><span class="topo-membrane">ASIVTAVLFSTLIGVLFGYMPAKK</span><span class="topo-outside">AAELNPITALA</span><span class="topo-unknown">QE</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>21</td>
      <td>259</td>
      <td>1</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>266</td>
      <td>246</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>277</td>
      <td>247</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>278</td>
      <td>306</td>
      <td>258</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>331</td>
      <td>287</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>456</td>
      <td>325</td>
      <td>436</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>465</td>
      <td>543</td>
      <td>445</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>544</td>
      <td>566</td>
      <td>524</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>584</td>
      <td>547</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>613</td>
      <td>565</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>614</td>
      <td>627</td>
      <td>594</td>
      <td>607</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>651</td>
      <td>608</td>
      <td>631</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>652</td>
      <td>662</td>
      <td>632</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5lil">5LIL</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNIIEIKQLNRYFGEGENRVHVLKDISLSIERGDFVAIMGQSGSGKSTLMNIIGCLDTATGGSSKIDGKETIELTNDQLSDLRSQKFGFIFQRYNLLSSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TAAENVALPAIYAGMPQSQRLERAKQLLEKLGLGDKWQNKPNQLSGGQQQRVSIARALMNGGEIILADQPTGALDSHSGENVMEILRQLHEEGHTIIMVTHDKHIAASANRIIEIKDGEI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ISDTQKRQVKSAVKNPSVFKG</span><span class="topo-unknown">RFGFS</span><span class="topo-outside">K</span><span class="topo-unknown">DQLMEAFRMS</span><span class="topo-membrane">VSAIVAHKMRSLLTMLGIIIGITSVVSVV</span><span class="topo-inside">ALGNGSQQKILENIRGIGTNTMTI</span><span class="topo-unknown">FNGNGFGDRRSRHIQ</span><span class="topo-inside">NLKISDANTLSKQSY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">IQSVTPNTSSSGILVVGNKSFTSANLYGIGEQYFDVEGLKLKQGRLLTEDDVDQSNQVVVLDESAKKAIFANENPLGKTVIFNKRPFRVIGVVSDQ</span><span class="topo-unknown">QLGGFPGNS</span><span class="topo-inside">LNLYSPYSTVLNKIT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">GGSRIGSITVKISDDVNSTVAEKSLTELLKS</span><span class="topo-unknown">LHGKKDFFI</span><span class="topo-inside">MNSDTIKQTIENTTGTMKLLISS</span><span class="topo-membrane">IAFISLIVGGIGVMNIMLVSVTE</span><span class="topo-outside">RTKEIGVRMAIGARQINIL</span><span class="topo-membrane">QQFLIEAVLICLIGG</span></span>
<span class="topo-ruler">       610       620       630       640       650       660    </span>
<span class="topo-line"><span class="topo-membrane">VAGILLSVLIGVL</span><span class="topo-inside">FNSFITDFSMDFST</span><span class="topo-membrane">ASIVTAVLFSTLIGVLFGYMPAKK</span><span class="topo-outside">AAELNPITALA</span><span class="topo-unknown">QE</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>21</td>
      <td>261</td>
      <td>1</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>267</td>
      <td>247</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>277</td>
      <td>248</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>278</td>
      <td>306</td>
      <td>258</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>330</td>
      <td>287</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>456</td>
      <td>326</td>
      <td>436</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>511</td>
      <td>446</td>
      <td>491</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>543</td>
      <td>501</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>544</td>
      <td>566</td>
      <td>524</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>567</td>
      <td>585</td>
      <td>547</td>
      <td>565</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>613</td>
      <td>566</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>614</td>
      <td>627</td>
      <td>594</td>
      <td>607</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>628</td>
      <td>651</td>
      <td>608</td>
      <td>631</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>652</td>
      <td>662</td>
      <td>632</td>
      <td>642</td>
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

### Mechanotransmission mechanism of MacB

MacB defines a noncanonical ABC transporter (type VII) with a unique four-transmembrane-helix topology and a periplasmic domain. The structure of ATP-bound MacB reveals no central pore for substrate passage. Instead, reversible dimerization of the NBDs drives opening and closing of the periplasmic domains via concerted movements of TM2 and the major coupling helix — a process termed [Mechanotransmission](/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/). This contrasts with the alternating-access mechanism used by other ABC transporters.

### MacB is the type specimen for type VII ABC transporter superfamily

MacB's novel topology, dimerization interface, and transmembrane fold define it as the type VII ABC transporter superfamily. Homologs sharing these features include LolCDE (lipoprotein trafficking), FtsEX (cell division signaling), PvdT, and AatP. The LolC periplasmic domain was solved at 1.88 A and confirmed a MacB-like fold.

### Molecular bellows mechanism for MacAB-TolC efflux

The assembled MacAB-TolC complex acts as a molecular bellows. Substrates enter the interior cavity through openings between parted periplasmic domains. ATP binding causes closure of the periplasmic domain via [Mechanotransmission](/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/), reducing cavity volume and forcing contents through the MacA gate ring. ATP hydrolysis resets the system.

### MacB confers resistance to cyclic peptides

In addition to the known macrolide [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/), MacB confers resistance to cyclic peptides including bacitracin and colistin, expanding the known substrate range of MacB. Structure-guided mutagenesis identified a periplasmic hotspot (Tyr376, Phe444, Trp505, Thr349) essential for [Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin/) tolerance.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for MacB purification and crystallization
- <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> — ATP bound in the MacB NBD dimer interface; ATPgammaS used for crystallization
- <a href="/xray-mp-wiki/reagents/ligands/erythromycin/">Erythromycin</a> — MacB confers resistance to erythromycin; used in functional assays
- <a href="/xray-mp-wiki/concepts/miscellaneous/mechanotransmission/">Mechanotransmission</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Additive used in purification or crystallization buffers
