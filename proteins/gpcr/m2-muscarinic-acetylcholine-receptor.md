---
title: "Human M2 Muscarinic Acetylcholine Receptor"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10753, doi/10.1038##nature12735]
verified: false
---

# Human M2 Muscarinic Acetylcholine Receptor

## Overview

The human M2 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor (M2 mAChR) is a class A G protein-coupled receptor that mediates parasympathetic neurotransmission in the central and peripheral nervous systems. It couples to Gi/Go family G proteins to activate G-protein-coupled inwardly rectifying potassium channels, playing an essential role in cardiovascular function. The M2 receptor was the first human [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor to be characterized structurally. The crystal structure reveals a deeply buried orthosteric binding pocket for antagonists within the transmembrane domain, an aromatic cage of tyrosine residues that forms a lid over bound ligands, and a long aqueous channel extending from the extracellular surface through approximately two-thirds of the membrane. The structure also maps an allosteric binding site at the entrance to the orthosteric pocket, explaining the M2 receptor's exceptional propensity for allosteric regulation.


## Publications

### doi/10.1038##nature10753

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4qdt">4QDT</a></td>
      <td>2.8 A</td>
      <td>P 21 21 2</td>
      <td>M2-T4L fusion (N-linked glycosylation sites Asn 2, 3, 6, 9 mutated to Asp; cysteine-less T4L residues 2-161 inserted into ICL3 replacing M2 residues 218-376; C-terminal truncation after residue 466)</td>
      <td>3-quinuclidinyl-benzilate (QNB)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Wild-type human M2 muscarinic acetylcholine receptor. Expressed using baculovirus in Sf9 insect cells. Purified to homogeneity by nickel affinity chromatography, followed by Flag affinity and size exclusion chromatography.


### doi/10.1038##nature12735

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mqs">4MQS</a></td>
      <td>3.5 A</td>
      <td>P212121</td>
      <td>M2 receptor (wild-type) in complex with active-state-stabilizing nanobody Nb9-8, bound to agonist iperoxo</td>
      <td>iperoxo, Nb9-8 nanobody</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mqs">4MQS</a></td>
      <td>3.7 A</td>
      <td>P212121</td>
      <td>M2 receptor (wild-type) in complex with Nb9-8 nanobody, bound to agonist iperoxo and positive allosteric modulator LY2119620</td>
      <td>iperoxo, LY2119620, Nb9-8 nanobody</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Wild-type human M2 muscarinic acetylcholine receptor. Expressed using baculovirus in Sf9 insect cells. Purified to homogeneity by nickel affinity chromatography, followed by Flag affinity and size exclusion chromatography.


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
      <td>Cell culture and infection</td>
      <td>Baculovirus expression in Sf9 insect cells</td>
      <td>--</td>
      <td>-- + --</td>
      <td>M2 receptor expressed in Sf9 insect cells</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>-- + --</td>
      <td>M2 receptor purified in the presence of 10 uM <a href="/xray-mp-wiki/reagents/ligands/iperoxo">Iperoxo</a></td>
    </tr>
    <tr>
      <td>Nickel affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>-- + --</td>
      <td>Initial purification step</td>
    </tr>
    <tr>
      <td>Flag affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">flag</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">flag</a> affinity resin</td>
      <td>-- + --</td>
      <td>Secondary purification step</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>Size exclusion chromatography</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Final purification step for homogeneity</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic mesophase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/iperoxo">Iperoxo</a>-bound M2 receptor complex with <a href="/xray-mp-wiki/reagents/antibodies/nb9-8">Nb9-8 Nanobody</a> <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">Nanobody</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized by lipidic mesophase crystallography at Advanced Photon Source beamline 23ID-D. Data collected by X-ray microdiffraction. 17 crystals used for the <a href="/xray-mp-wiki/reagents/ligands/iperoxo">Iperoxo</a>-<a href="/xray-mp-wiki/reagents/antibodies/nb9-8">Nb9-8 Nanobody</a> structure (3.5 A). Supplementing crystallization conditions with <a href="/xray-mp-wiki/reagents/ligands/ly2119620">LY2119620</a> yielded crystals of the ternary complex (3.7 A, 18 crystals). Both structures solved in P212121 space group.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mqs">4MQS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDENLYFQGLEMDDSTDSSDNSLALTSPYLE</span><span class="topo-inside">KTF</span><span class="topo-membrane">EVVFIVLVAGSLSLVTIIGNILVMV</span><span class="topo-outside">SIKVNRHLQTVNNY</span><span class="topo-membrane">FLFSLACADLIIGVFSMNLYTLYTV</span><span class="topo-inside">IGYWPLGPVV</span><span class="topo-membrane">CDLWLALD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YVVSNASVMNLLIISF</span><span class="topo-outside">DRYFCVTKPLTYPVKRTTKMA</span><span class="topo-membrane">GMMIAAAWVLSFILWAPAILF</span><span class="topo-inside">WQFIVGVRTVEDGECYIQFFSNA</span><span class="topo-membrane">AVTFGTAIAAFYLPVIIMTVLYW</span><span class="topo-outside">HISRASKS</span><span class="topo-unknown">RIKKDKKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350 </span>
<span class="topo-line"><span class="topo-unknown">PVANQDPVSTRKK</span><span class="topo-outside">PPPSREKKVTRTI</span><span class="topo-membrane">LAILLAFIITWAPYNVMVLIN</span><span class="topo-inside">TFCAPCIPNT</span><span class="topo-membrane">VWTIGYWLCYINSTINPACYA</span><span class="topo-outside">LCN</span><span class="topo-unknown">ATFKKTFK</span><span class="topo-outside">HLLM</span><span class="topo-unknown">CHYKNIGATRHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>35</td>
      <td>-16</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>19</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>22</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>47</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>112</td>
      <td>86</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>136</td>
      <td>96</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>120</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>201</td>
      <td>162</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>224</td>
      <td>185</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>232</td>
      <td>208</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>253</td>
      <td>216</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>254</td>
      <td>266</td>
      <td>377</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>297</td>
      <td>411</td>
      <td>420</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>421</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>321</td>
      <td>442</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>329</td>
      <td>445</td>
      <td>452</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>330</td>
      <td>333</td>
      <td>453</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>351</td>
      <td>457</td>
      <td>474</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mqs">4MQS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDENLYFQGLEMDDSTDSSDNSLALTSPYLE</span><span class="topo-inside">KTF</span><span class="topo-membrane">EVVFIVLVAGSLSLVTIIGNILVMV</span><span class="topo-outside">SIKVNRHLQTVNNY</span><span class="topo-membrane">FLFSLACADLIIGVFSMNLYTLYTV</span><span class="topo-inside">IGYWPLGPVV</span><span class="topo-membrane">CDLWLALD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YVVSNASVMNLLIISF</span><span class="topo-outside">DRYFCVTKPLTYPVKRTTKMA</span><span class="topo-membrane">GMMIAAAWVLSFILWAPAILF</span><span class="topo-inside">WQFIVGVRTVEDGECYIQFFSNA</span><span class="topo-membrane">AVTFGTAIAAFYLPVIIMTVLYW</span><span class="topo-outside">HISRASKS</span><span class="topo-unknown">RIKKDKKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350 </span>
<span class="topo-line"><span class="topo-unknown">PVANQDPVSTRKK</span><span class="topo-outside">PPPSREKKVTRTI</span><span class="topo-membrane">LAILLAFIITWAPYNVMVLIN</span><span class="topo-inside">TFCAPCIPNT</span><span class="topo-membrane">VWTIGYWLCYINSTINPACYA</span><span class="topo-outside">LCN</span><span class="topo-unknown">ATFKKTFK</span><span class="topo-outside">HLLM</span><span class="topo-unknown">CHYKNIGATRHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>35</td>
      <td>-16</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>19</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>22</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>47</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>112</td>
      <td>86</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>136</td>
      <td>96</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>120</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>201</td>
      <td>162</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>224</td>
      <td>185</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>232</td>
      <td>208</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>253</td>
      <td>216</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>254</td>
      <td>266</td>
      <td>377</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>297</td>
      <td>411</td>
      <td>420</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>421</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>321</td>
      <td>442</td>
      <td>444</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>329</td>
      <td>445</td>
      <td>452</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>330</td>
      <td>333</td>
      <td>453</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>351</td>
      <td>457</td>
      <td>474</td>
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

### Active-state conformational changes

The active-state M2 receptor shows key conformational changes consistent with
GPCR activation: an outward displacement of TM6 at the intracellular side,
smaller outward movement of TM5, and rearrangement of TM7 around the NPXXY
motif. The DRY motif rearranges with Arg 121 (3.50) adopting an extended
conformation and Asp 120 (3.49) forming a hydrogen bond with Asn 58 (2.39).
The active-state M2 receptor shows larger conformational changes in the
extracellular region and orthosteric binding site than observed in the active
states of the beta2 AR and rhodopsin.

### Orthosteric binding pocket closure on activation

The activated M2 receptor shows a small orthosteric binding site that
completely occludes the agonist [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo) from solvent. Transmembrane helices
5, 6 and 7 move inward toward the agonist in the active conformation. TM3
undergoes a slight rotation about its axis. The largest differences involve
TM6, where an inward movement of 2 A at Asn 404 (6.52) allows formation of
a hydrogen bond between its side chain and [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo). The agonist [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo)
adopts a bent conformation within the active orthosteric binding pocket.

### Extracellular vestibule contraction

The M2 receptor possesses a large extracellular vestibule above the
orthosteric site that shows substantial contraction upon activation due to
TM6 rotation. This motion of TM6 provides a structural link among three
receptor regions: the extracellular vestibule, the orthosteric binding
pocket, and the intracellular surface. The structural coupling accounts for
the fact that allosteric modulators can affect the affinity and efficacy of
orthosteric ligands and can also directly activate G proteins as allosteric
agonists.

### Allosteric modulator binding site

The positive allosteric modulator [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620) binds at a site directly
superficial to the orthosteric site in the extracellular vestibule. Its
aromatic rings are situated between Tyr 177 (ECL2) and Trp 422 (7.35),
forming a three-layered aromatic stack. Polar interactions include hydrogen
bonds from Tyr 80 (2.61), Asn 410 (6.58) and Asn 419 (ECL3), and a
charge-charge interaction with Glu 172 (ECL2). [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620) binds at a site
separated from the orthosteric site only by the tyrosine lid, with Tyr 426
(7.39) interacting with both ligands.

### Asn 58 (2.39) in active-state stabilization

Asn 58 (2.39) stabilizes the active conformation through a hydrogen bond
with Asp 120 (3.49). Mutation of Asn 58 to alanine (N58A) resulted in a
mutant with normal ligand-binding properties but impaired ability to
activate G protein. This residue likely either directly stabilizes the
active conformation or engages in direct interactions with G protein.

### TM6 pivot mechanism

Activation involves a pivot of TM6 that moves inward in the orthosteric
binding site (forming a hydrogen bond with [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo) via Asn 404) and
outward at the intracellular side (creating the G-protein binding cavity).
This dual motion of TM6 structurally couples the orthosteric site,
extracellular vestibule, and intracellular G-protein binding surface.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/tx24/">Tx24</a> — Engineered allosteric toxin targeting M2AChR, derived from MT7 via in vitro evolution
- <a href="/xray-mp-wiki/concepts/signaling-receptors/three-finger-toxin-gpcr-modulation/">Three-Finger Toxin Scaffold for GPCR Modulation</a> — M2AChR is target of engineered 3FT Tx24 demonstrating scaffold retargetability
- <a href="/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/">M1 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; orthosteric binding pocket residues identical between M1 and M2
- <a href="/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/">M3 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; orthosteric binding pocket residues identical between M3 and M2
- <a href="/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/">Human M4 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; M4 structure solved in same study as M1 (Thal et al., 2016)
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/acetylcholine-binding-protein/">Acetylcholine-Binding Protein (AChBP)</a> — Structural homologue showing convergent evolution of acetylcholine binding sites
- <a href="/xray-mp-wiki/reagents/ligands/acetylcholine/">Acetylcholine</a> — Endogenous orthosteric ligand of the M2 receptor
- <a href="/xray-mp-wiki/reagents/ligands/3-quinuclidinyl-benzilate/">3-Quinuclidinyl-benzilate (QNB)</a> — Antagonist co-crystallized with inactive M2 receptor (PDB 4QDT)
- <a href="/xray-mp-wiki/reagents/ligands/iperoxo/">Iperoxo</a> — High-affinity agonist co-crystallized with active-state M2 receptor
- <a href="/xray-mp-wiki/reagents/ligands/ly2119620/">LY2119620</a> — Positive allosteric modulator co-crystallized with active-state M2 receptor
- <a href="/xray-mp-wiki/reagents/antibodies/nb9-8/">Nb9-8 Nanobody</a> — Active-state-stabilizing nanobody used for crystallization of active M2 receptor
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Nanobody fusion used for crystallization
