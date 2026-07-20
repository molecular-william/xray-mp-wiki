---
title: "mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2350, doi/10.1038##nature13984]
verified: none
uniprot_id: C7Z7K1
---

# mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/C7Z7K1">UniProt: C7Z7K1</a>

<span class="expr-badge">Nectria haematococca</span>

## Overview

mTMEM16A is the murine ortholog of TMEM16A (Ano1), the long sought-after Ca2+-activated chloride channel (CaCC). TMEM16A is a member of the TMEM16 (anoctamin) protein family, which includes both Ca2+-activated chloride channels and lipid scramblases. TMEM16A is activated from the intracellular side at sub-micromolar Ca2+ concentrations with a voltage-dependent EC50. It contributes to diverse physiological processes including epithelial chloride secretion, electrical signaling in smooth muscles, and potentially nociception. The calcium binding site in mTMEM16A is structurally equivalent to that in [nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)](/xray-mp-wiki/proteins/miscellaneous/nhtmem16/), and mutations of residues involved in Ca2+ coordination affect ion conduction in mTMEM16A, demonstrating a common activation mechanism across the TMEM16 family.


## Publications

### doi/10.1038##nsmb.2350

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3jfq">3JFQ</a></td>
      <td>3.7</td>
      <td>TBD</td>
      <td>Full-length mTMEM16A (isoform a) from Mus musculus</td>
      <td>TBD</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (human embryonic kidney)
- **Construct**: mTMEM16A (isoform ac) expressed with C-terminal HRV 3C cleavage site, Myc tag, and SBP tag (scrambling assay construct); mTMEM16A (isoform ac) fused to Venus-YFP with Myc and SBP tags (electrophysiology construct)

### doi/10.1038##nature13984

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4wis">4WIS</a></td>
      <td>TBD</td>
      <td>TBD</td>
      <td>Full-length mTMEM16A (isoform ac) from Mus musculus, expressed in HEK293T cells</td>
      <td>TBD</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293T cells (human embryonic kidney)
- **Construct**: mTMEM16A (isoform ac) expressed with C-terminal HRV 3C cleavage site, Myc tag, and SBP tag (scrambling assay construct); mTMEM16A (isoform ac) fused to Venus-YFP with Myc and SBP tags (electrophysiology construct)

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
      <td>Cell transfection</td>
      <td>Transfection of HEK293T cells with plasmid DNA</td>
      <td>--</td>
      <td>Transfection buffer with 2.8 mM Na2HPO4 + --</td>
      <td>mTMEM16A-YFP expressed in HEK293T cells for electrophysiology</td>
    </tr>
    <tr>
      <td>Electrophysiology</td>
      <td>Patch-clamp recordings</td>
      <td>--</td>
      <td>Standard external solution (140 mM NaCl, 4 mM KCl, 2 mM CaCl2, 1 mM MgCl2, 10 mM <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a>, 10 mM HEPES pH 7.4) + --</td>
      <td>mTMEM16A-YFP currents recorded in excised inside-out patches at 80 mV</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wis">4WIS</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSNLKDFSQPGSGQESNF</span><span class="topo-inside">GVDFVIHYKVPAAERDEAEAGFVQLIRALTTVGLATEVRHGENESLLVFVKVASPDLFAKQVYRARLGDWLHGVRVSAPHNDIAQALQDEPVVEAERLRLIY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LMITKPHNE</span><span class="topo-unknown">GGAGVTPTNAK</span><span class="topo-inside">WKHVESIFPLHSHSFNKEWIKKWSSKYTLEQTDIDNIRDKFGESVAFYFAFLRSY</span><span class="topo-membrane">FRFLVIPSAFGFGAWLLLGQ</span><span class="topo-outside">F</span><span class="topo-membrane">SYLYALLCGLWSVVFFE</span><span class="topo-inside">YWKKQEV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DLAVQWGVRGVSSIQQSRPEFEWEHEAEDPITGEPVKVYPPMKRVK</span><span class="topo-membrane">TQLLQIPFALACVVALGALIVTCNSLEVFINE</span><span class="topo-outside">VYSGPG</span><span class="topo-membrane">KQYLGFLPTIFLVIGTPTISGVLMGAAEKL</span><span class="topo-inside">NAMENY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ATVDAHDAAL</span><span class="topo-membrane">IQKQFVLNFMTSYMALFFTAFVYIPFG</span><span class="topo-unknown">HILHPFLNFWRATAQTLT</span><span class="topo-outside">FSEKELPTREFQIN</span><span class="topo-membrane">PARISNQMFYFTVTAQIVNFATEVVV</span><span class="topo-unknown">PYIKQQAF</span><span class="topo-inside">Q</span><span class="topo-unknown">KAKQLKSGSKVQEDHE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">EE</span><span class="topo-inside">AEFLQRVREECTLEEYDVSGDY</span><span class="topo-membrane">REMVMQFGYVAMFSVAW</span><span class="topo-outside">P</span><span class="topo-membrane">LAACCFLVNNWVE</span><span class="topo-inside">LRSDALKIAISSRRPIPWRTDSIGPW</span><span class="topo-membrane">LTALSFLSWLGSITSSAIVYLCSN</span><span class="topo-unknown">SKNGTQGE</span><span class="topo-outside">ASP</span><span class="topo-membrane">LKAW</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">GLLLSILFAEHFYLVVQLAVR</span><span class="topo-inside">FVLSKLDSPGLQKERKERFQTKKRLLQENLGQDAA</span><span class="topo-unknown">EEA</span><span class="topo-inside">AAPGIEHSEKITREALEEEARQASI</span><span class="topo-unknown">RGHGTPE</span><span class="topo-inside">EMFWQRQRGMQETIEIGRRMIEQQLAAG</span><span class="topo-unknown">K</span></span>
<span class="topo-ruler">       730     </span>
<span class="topo-line"><span class="topo-unknown">NGKKSAPAVPSEKAS</span></span>
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
      <td>19</td>
      <td>129</td>
      <td>19</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>195</td>
      <td>141</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>215</td>
      <td>196</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>286</td>
      <td>234</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>318</td>
      <td>287</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>354</td>
      <td>325</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>397</td>
      <td>371</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>415</td>
      <td>398</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>416</td>
      <td>429</td>
      <td>416</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>455</td>
      <td>430</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>463</td>
      <td>456</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>504</td>
      <td>483</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>521</td>
      <td>505</td>
      <td>521</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>535</td>
      <td>523</td>
      <td>535</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>561</td>
      <td>536</td>
      <td>561</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>585</td>
      <td>562</td>
      <td>585</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>594</td>
      <td>596</td>
      <td>594</td>
      <td>596</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>597</td>
      <td>621</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>622</td>
      <td>656</td>
      <td>622</td>
      <td>656</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>660</td>
      <td>684</td>
      <td>660</td>
      <td>684</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>692</td>
      <td>719</td>
      <td>692</td>
      <td>719</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4wis">4WIS</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSNLKDFSQPGSGQESNF</span><span class="topo-inside">GVDFVIHYKVPAAERDEAEAGFVQLIRALTTVGLATEVRHGENESLLVFVKVASPDLFAKQVYRARLGDWLHGVRVSAPHNDIAQALQDEPVVEAERLRLIY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LMITKPHNE</span><span class="topo-unknown">GGAGVTPTNAK</span><span class="topo-inside">WKHVESIFPLHSHSFNKEWIKKWSSKYTLEQTDIDNIRDKFGESVAFYFAFLRSY</span><span class="topo-membrane">FRFLVIPSAFGFGAWLLLGQ</span><span class="topo-outside">F</span><span class="topo-membrane">SYLYALLCGLWSVVFFE</span><span class="topo-inside">YWKKQEV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DLAVQWGVRGVSSIQQSRPEFEWEHEAEDPITGEPVKVYPPMKRVK</span><span class="topo-membrane">TQLLQIPFALACVVALGALIVTCNSLEVFINE</span><span class="topo-outside">VYSGPG</span><span class="topo-membrane">KQYLGFLPTIFLVIGTPTISGVLMGAAEKL</span><span class="topo-inside">NAMENY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ATVDAHDAAL</span><span class="topo-membrane">IQKQFVLNFMTSYMALFFTAFVYIPFG</span><span class="topo-unknown">HILHPFLNFWRATAQTLT</span><span class="topo-outside">FSEKELPTREFQIN</span><span class="topo-membrane">PARISNQMFYFTVTAQIVNFATEVVV</span><span class="topo-unknown">PYIKQQAF</span><span class="topo-inside">Q</span><span class="topo-unknown">KAKQLKSGSKVQEDHE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">EE</span><span class="topo-inside">AEFLQRVREECTLEEYDVSGDYR</span><span class="topo-membrane">EMVMQFGYVAMFSVAW</span><span class="topo-outside">P</span><span class="topo-membrane">LAACCFLVNNWVE</span><span class="topo-inside">LRSDALKIAISSRRPIPWRTDSIGPW</span><span class="topo-membrane">LTALSFLSWLGSITSSAIVYLCSN</span><span class="topo-unknown">SKNGTQGE</span><span class="topo-outside">ASP</span><span class="topo-membrane">LKAW</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">GLLLSILFAEHFYLVVQLAVR</span><span class="topo-inside">FVLSKLDSPGLQKERKERFQTKKRLLQENLGQDAA</span><span class="topo-unknown">EEA</span><span class="topo-inside">AAPGIEHSEKITREALEEEARQASI</span><span class="topo-unknown">RGHGTPE</span><span class="topo-inside">EMFWQRQRGMQETIEIGRRMIEQQLAAG</span><span class="topo-unknown">K</span></span>
<span class="topo-ruler">       730     </span>
<span class="topo-line"><span class="topo-unknown">NGKKSAPAVPSEKAS</span></span>
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
      <td>19</td>
      <td>129</td>
      <td>19</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>195</td>
      <td>141</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>215</td>
      <td>196</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>233</td>
      <td>217</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>286</td>
      <td>234</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>318</td>
      <td>287</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>324</td>
      <td>319</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>354</td>
      <td>325</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>397</td>
      <td>371</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>415</td>
      <td>398</td>
      <td>415</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>416</td>
      <td>429</td>
      <td>416</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>455</td>
      <td>430</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>463</td>
      <td>456</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>464</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>505</td>
      <td>483</td>
      <td>505</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>506</td>
      <td>521</td>
      <td>506</td>
      <td>521</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>535</td>
      <td>523</td>
      <td>535</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>561</td>
      <td>536</td>
      <td>561</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>585</td>
      <td>562</td>
      <td>585</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>594</td>
      <td>596</td>
      <td>594</td>
      <td>596</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>597</td>
      <td>621</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>622</td>
      <td>656</td>
      <td>622</td>
      <td>656</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>660</td>
      <td>684</td>
      <td>660</td>
      <td>684</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>692</td>
      <td>719</td>
      <td>692</td>
      <td>719</td>
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

### Ca2+ activation from intracellular side at sub-micromolar concentrations

TMEM16A is activated from the intracellular side by Ca2+ at sub-micromolar concentrations. The EC50 is voltage-dependent and decreases upon depolarization. This voltage-dependence is explained by the intramembrane location of the Ca2+ binding site, where the ion must cross a fraction of the transmembrane electric field to reach the binding site.

### Shared Ca2+ binding site with nhTMEM16

Mutations of residues in the Ca2+ binding site of mTMEM16A (equivalent to [nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)](/xray-mp-wiki/proteins/miscellaneous/nhtmem16/)) affect ion conduction, demonstrating that Ca2+ binding by equivalent residues regulates both functional branches of the TMEM16 family (chloride channels and lipid scramblases) by a common mechanism. Strongest effect observed for E654Q mutant, which showed no activation at any Ca2+ concentration.

### Physiological roles in epithelial chloride secretion and nociception

TMEM16A contributes to epithelial chloride secretion, electrical signaling in smooth muscles, and potentially nociception. It is expressed in diverse tissues and is implicated in various pathophysiological conditions including asthma, cancer, and pain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/nhtmem16/">nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca)</a> — Homologous TMEM16 protein; Ca2+ binding site mutations affect both ion conduction and lipid scrambling
- <a href="/xray-mp-wiki/concepts/protein-families/tmem16-family/">TMEM16 Family</a> — mTMEM16A is the prototype of the TMEM16 chloride channel subfamily
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride</a> — Ca2+ is the activating ligand for TMEM16A channel activity
- <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA (Ethylene Glycol Tetraacetic Acid)</a> — Ca2+ chelator used in TMEM16A patch-clamp experiments to control free Ca2+
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
