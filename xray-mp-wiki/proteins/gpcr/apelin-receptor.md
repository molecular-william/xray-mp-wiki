---
title: "Human Apelin Receptor (APJR)"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.04.008]
verified: agent
uniprot_id: P35414
---

# Human Apelin Receptor (APJR)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P35414">UniProt: P35414</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human apelin receptor (APJR), also known as angiotensin receptor-like 1 (AGTRL1) or [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type J receptor, is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) that plays a key role in cardiovascular regulation. APJR is activated by two endogenous peptide ligands, apelin and elabela/toddler, and is involved in angiogenesis, vasoconstriction, heart muscle contractility, energy metabolism regulation, and fluid homeostasis. Polymorphisms in the APJR gene have been associated with increased risks of hypertension and coronary artery disease.


## Publications

### doi/10.1016##j.str.2017.04.008

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vbl">5VBL</a></td>
      <td>2.6</td>
      <td>P 21 21 21</td>
      <td>Residues 19-330 with ICL3 (residues 230-242) replaced by rubredoxin (M1-E54). Mutations: C325L, C326M (palmitoylation site removal), T177N (glycosylation site removal), V117A, W261K.</td>
      <td>AMG3054</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: N-terminal HA signal sequence + Flag tag; C-terminal ppase site + 10x His tag. Residues 1-6 deleted, residues 331-380 truncated. ICL3 replaced with rubredoxin (M1-E54). Mutations: C325L, C326M, T177N, V117A, W261K.

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
      <td>Cell harvest</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cell culture infected with <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">baculovirus</a> at MOI 5; harvested after 48 h</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Hypotonic lysis (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail), centrifugation, high salt wash</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (N-Dodecyl-B-D-Maltoside, Anatrace D310) with <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (Cholesteryl hemisuccinate, Sigma C6512)</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin (Clontech 635507) for <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a> capture</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) buffer</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentrated for co-crystallization with AMG3054</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (Sigma M7765)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vbl">5VBL</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10       </span>
<span class="topo-line"><span class="topo-outside">KFRRQRP??EHKK??P</span><span class="topo-unknown">?</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vbl">5VBL</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDKFDNYYGADNQSE</span><span class="topo-outside">CEYTDWKSSGALIP</span><span class="topo-membrane">AIYMLVFLLGTTGNGLVLW</span><span class="topo-inside">TVFRSSREKRRSADIF</span><span class="topo-membrane">IASLAVADLTFVVTLPLW</span><span class="topo-outside">ATYTYRDYDWPFGTFFC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KLSSYLIFVNMYASAFCLT</span><span class="topo-inside">GLSFDRYLAIVRPVANARLRLRVSGAVA</span><span class="topo-membrane">TAVLWVLAALLAMPVMVL</span><span class="topo-outside">RTTGDLENTNKVQCYMDYSMVATVSSEWAWE</span><span class="topo-membrane">VGLGVSSTTVGFVVPFTIML</span><span class="topo-inside">TCYF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">FIAQTIAMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVEERRRLLSII</span><span class="topo-membrane">VVLVVTFALCKMPYHLVKTL</span><span class="topo-outside">YMLGSLLHWPCDFDLFLMNIFP</span><span class="topo-membrane">YCTCISYVN</span></span>
<span class="topo-ruler">       370       380       390       400       </span>
<span class="topo-line"><span class="topo-membrane">SCLNPFLYAF</span><span class="topo-inside">FDPRFRQACTSMLLMGQSR</span><span class="topo-unknown">LEVLFQGPHHHHHHHHHH</span></span>
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
      <td>36</td>
      <td>-17</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>50</td>
      <td>19</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>69</td>
      <td>33</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>85</td>
      <td>52</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>103</td>
      <td>68</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>120</td>
      <td>86</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>103</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>167</td>
      <td>122</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>150</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>216</td>
      <td>168</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>236</td>
      <td>199</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>309</td>
      <td>219</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>329</td>
      <td>251</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>330</td>
      <td>351</td>
      <td>271</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>352</td>
      <td>370</td>
      <td>293</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>312</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>407</td>
      <td>331</td>
      <td>348</td>
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

### Two-Site Peptide Binding Mode

The crystal structure of APJR in complex with [AMG3054](/xray-mp-wiki/reagents/ligands/amg3054/) revealed a novel two-site
peptide ligand binding mode, where the C-terminal end of the peptide binds deeply
into the canonical orthosteric pocket (site 1) and the N-terminal half extends to
a surface groove (site 2). This binding mode has not been observed in any other
solved class A [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) structure.
Key binding residues at site 1 include Y35 (1.39), W85 (2.60), and R168 (ECL2),
whose mutation to alanine completely abolished apelin binding. Y264 (6.51) and
K268 (6.55) mutations reduced binding affinity but did not eliminate it. At site 2,
D23 (N-terminus) and D284 (7.28) are critical for peptide recognition.
The structure provides a mechanistic framework for understanding how endogenous
peptide ligands with high conformational flexibility may bind and modulate class A
peptide GPCRs through a similar two-site mechanism.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/amg3054/">AMG3054</a> — Designed 17-mer apelin mimetic peptide agonist used in structure determination (PDB 5VBL)
- <a href="/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/">Kappa Opioid Receptor</a> — Class A GPCR with endogenous peptide ligand; two-site binding model proposed via MD
- <a href="/xray-mp-wiki/reagents/ligands/apelin-13/">Apelin-13</a> — Endogenous peptide agonist of APJR; binding analyzed by mutation and MD simulation
- <a href="/xray-mp-wiki/reagents/ligands/apelin-17/">Apelin-17</a> — Endogenous peptide ligand; AMG3054 is a constrained analog of apelin-17
- <a href="/xray-mp-wiki/concepts/signaling-receptors/two-site-binding-mode/">Two-Site Binding Mode</a> — Novel binding mechanism revealed by APJR-AMG3054 crystal structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in apelin-receptor
- <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a> — Referenced in apelin-receptor
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Referenced in apelin-receptor
- <a href="/xray-mp-wiki/reagents/additives/chloride/">Chloride Ion</a> — Referenced in apelin-receptor
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Referenced in apelin-receptor
