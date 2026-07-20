---
title: "Human Histamine H3 Receptor (H3R)"
created: 2026-06-08
updated: 2026-07-13
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-33880-y]
verified: agent
uniprot_id: ['P0ABE7', 'Q9Y5N1']
---

# Human Histamine H3 Receptor (H3R)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ABE7">UniProt: P0ABE7</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9Y5N1">UniProt: Q9Y5N1</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human histamine H3 receptor (H3R) is a [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) belonging to the aminergic [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) subfamily. It is expressed mainly in the central nervous system, where it acts as an auto- or hetero-receptor to regulate histamine release and modulate the release of various neurotransmitters including [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/), GABA, and [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/). H3R is associated with physiological processes such as sleep-wake cycles, learning, memory, feeding, and cerebral ischemia, making it a potential drug target for neurological and psychiatric disorders including sleep disorders, Parkinson's disease, schizophrenia, and Alzheimer's disease. The crystal structure of H3R in complex with the non-[Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) antagonist PF-03654746 reveals the molecular basis for ligand recognition and allosteric [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding.


## Publications

### doi/10.1038##s41467-022-33880-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7f61">7F61</a></td>
      <td>2.6</td>
      <td>not specified</td>
      <td>Human H3R (residues 27-432), with N-terminal truncation (1-26), ICL3 truncation (242-346), C-terminal truncation (433-445), S121K mutation, and N-terminal BRIL fusion (M7W, H102I, R106L)</td>
      <td>PF-03654746</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda ([Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)) insect cells
- **Construct**: Codon-optimized human H3R gene cloned into modified pFastBacI vector with N-terminal HA signal sequence, FLAG tag, 10x His tag, and TEV protease cleavage site
- **Notes**: [Bac-to-Bac](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) Expression System; infected at 2-3 x 10^6 cells/ml, harvested 48h post-infection

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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>not specified</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM KCl (hypotonic); 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 1.0 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM KCl (high-osmotic) + not specified</td>
      <td>Cells washed with hypotonic buffer then high-osmotic buffer; purified membranes resuspended with 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilized for 3h at 4 C; centrifuged at 58,000xg for 1h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin (TaKaRa)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash I); 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash II); 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution) + <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Incubated overnight at 4 C; eluted in 3 column volumes</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>H3R-PF-03654746 complex in 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals formed within 1 week; collected with 50 um micro-loops and flash-frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f61">7F61</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">RGFSAAWTAVL</span><span class="topo-membrane">AALMALLIVATVLGNALVMLAFVA</span><span class="topo-outside">DSSLRTQNNF</span><span class="topo-membrane">FLLNLAISDFLVGAFCIPLYV</span><span class="topo-inside">PYVLTGRWTFGRGLCK</span><span class="topo-membrane">LWLVVDYLLCTSKAFNIVLI</span><span class="topo-outside">SYDRFLSVTRAVSYRAQQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GDTRRAV</span><span class="topo-membrane">RKMLLVWVLAFLLYGPAILSW</span><span class="topo-inside">EYLSGGSSIPEGHCYAEFFYN</span><span class="topo-membrane">WYFLITASTLEFFTPFLSVT</span><span class="topo-outside">FFNLSIYLNIQRRTRLRLDGAREAAG</span><span class="topo-unknown">PEPPPEAQPSPPPPPGCWGCWQKGH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">GEAMPLHRYGVGEAAVGAEAGEATLGGGGGGGSVASPTSSSGSSSRGTERPRSLKRGSKPSASSASLEKRMKMVSQSFTQ</span><span class="topo-outside">RFRLSRDRKVAKSLA</span><span class="topo-membrane">VIVSIFGLCWAPYTLLMIIRAACH</span><span class="topo-inside">G</span></span>
<span class="topo-ruler">       370       380       390       400       </span>
<span class="topo-line"><span class="topo-inside">HCVPDY</span><span class="topo-membrane">WYETSFWLLWANSAVNPVLYPL</span><span class="topo-outside">CHHSFRRAFTKLLCPQKL</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>11</td>
      <td>27</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>35</td>
      <td>38</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>45</td>
      <td>62</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>66</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>82</td>
      <td>93</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>102</td>
      <td>109</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>127</td>
      <td>129</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>148</td>
      <td>154</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>175</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>189</td>
      <td>196</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>215</td>
      <td>216</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>320</td>
      <td>242</td>
      <td>346</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>321</td>
      <td>335</td>
      <td>347</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>359</td>
      <td>362</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>366</td>
      <td>386</td>
      <td>392</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>388</td>
      <td>393</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>406</td>
      <td>415</td>
      <td>432</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>407</td>
      <td>433</td>
      <td>433</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7f61">7F61</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDKHHHHHHHHHHENLYFQG</span><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLA</span></span>
<span class="topo-ruler">       130       140       </span>
<span class="topo-line"><span class="topo-inside">NEGKVKEAQAAAEQLKTTRNAYIQKYL</span></span>
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
      <td>41</td>
      <td>-40</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>147</td>
      <td>1</td>
      <td>106</td>
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

### Extended binding pocket (EBP) in H3R

The H3R structure reveals an extended binding pocket (EBP) around TMs2/7 and ECL2 compared to other aminergic receptors. This EBP accommodates the aromatic moieties of H3R antagonists through pi-pi stacking and OH/pi hydrogen bonds with aromatic residues including Y91 and Y189. Functional assays showed Y91A and Y189A mutations significantly decreased inhibition of several antagonists, confirming the EBP's importance for ligand binding and efficacy.

### Allosteric cholesterol binding

A [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecule was observed binding at the extrahelical pocket between TM1 and TM7 of H3R, forming extensive hydrophobic interactions with F29, L37, M41, L40, L44, T396, Y393, and W399. The beta-3-hydroxy head group of [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) forms a hydrogen bond with E395, which also participates in polar interactions with PF-03654746. Molecular dynamics simulations showed [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) stabilizes the TM1-TM7-N-term contacts, potentially affecting antagonist binding through an allosteric mechanism.

### Inactive state conformation

Compared to inactive H1R, H3R shows inward movement of TM6 and TM7 extracellular tips by 2.3 and 3.5 A, respectively, and an outward movement of TM6 by 2.8 A at the intracellular side (vs 12 A in active H1R). The D131-R132 salt bridge (instead of D-R-Y motif) is a key feature of the inactive state. ECL2 shifts 11 A toward TM3, creating space for the antagonist.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/g-protein/">G Protein</a> — Related entity
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">Gpcr</a> — Related entity
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Related entity
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Bac To Bac</a> — Related entity
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression</a> — Related entity
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> — Related entity
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Related entity
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized Metal Affinity Chromatography</a> — Related entity
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Related entity
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Related entity
