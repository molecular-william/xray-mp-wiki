---
title: "Human M4 Muscarinic Acetylcholine Receptor"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17188]
verified: regex
uniprot_id: P08173
---

# Human M4 Muscarinic Acetylcholine Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P08173">UniProt: P08173</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human M4 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (M4 mAChR) is a class A G protein-coupled receptor that mediates inhibitory cholinergic neurotransmission in the central nervous system. It couples to Gi/Go family G proteins and is highly expressed in the striatum, where it plays a critical role in motor control and cognitive function. The M4 receptor has emerged as an attractive drug target for schizophrenia, as selective M4 positive allosteric modulators (PAMs) have demonstrated preclinical efficacy. The first crystal structure of the M4 receptor was solved in complex with the inverse agonist [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) at 2.6 A resolution, revealing the orthosteric binding site and a network of residues linking the orthosteric and allosteric sites.


## Publications

### doi/10.1038##nature17188

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5dsg">5DSG</a></td>
      <td>2.6 A</td>
      <td>P 1 21 1</td>
      <td>Human M4 muscarinic receptor, N-terminal FLAG epitope tag, N-terminus truncated (residues 1-21 removed), residues 226-389 of ICL3 replaced by minimal T4 lysozyme (mT4L), C-terminal 8x histidine tag
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Human M4 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor with N-terminal FLAG epitope tag, N-terminus truncated (residues 1-21 removed by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) cleavage at engineered HRV 3C site), residues 226-389 of ICL3 replaced by minimal Cys-free T4 lysozyme fusion (mT4L), and C-terminal deca-histidine tag. Expressed using the Bac-to-Bac Baculovirus Expression System (Invitrogen) in Sf9 cells.


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
      <td>Sf9 cell expression</td>
      <td>Baculovirus expression in <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9 insect cells</a></td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells infected at density of 4.0-5.0 x 10^6 cells/mL, treated with 10 uM <a href="/xray-mp-wiki/reagents/ligands/atropine/">Atropine</a>, harvested at 60 hours</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization in presence of <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a></td>
      <td>--</td>
      <td>-- + --</td>
      <td>Receptor solubilized and purified in presence of <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> as previously described for M3 receptor</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>-- + --</td>
      <td>First purification step via C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His tag</a></td>
    </tr>
    <tr>
      <td>FLAG <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity resin</td>
      <td>-- + --</td>
      <td>Second purification step via N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> epitope tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Size exclusion column</td>
      <td>-- + --</td>
      <td>N-terminus cleaved with <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> (2% w/w) during concentration prior to SEC (~2hr at 4 degrees C). Purified receptor concentrated to 85 AU (~50 mg/mL) and flash frozen in small aliquots using <a href="/xray-mp-wiki/concepts/methods-techniques/cryocooling/">liquid nitrogen</a>.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase (LCP) crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M4-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a> bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a>, reconstituted by mixing protein solution into 10:1 (w/w) <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> in 1:1.5 parts w/w protein:lipid ratio using the two-syringe method. Sample volume 20-40 nL.
</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Initial crystals formed after 24 hours</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested using mesh grid loops and stored in <a href="/xray-mp-wiki/concepts/methods-techniques/cryocooling/">liquid nitrogen</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>M4-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a> crystallized in space group P 1 21 1. Data processed using XDS. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using inactive M2 structure (PDB: 3UON) and inactive M3-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a> (PDB: 4U15) as search models for receptor and <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a> fusion domains respectively. Refinement carried out in Phenix with manual building in Coot. 64 crystals used. Final Rwork/Rfree: 22.7%/24.0%.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5dsg">5DSG</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">GPSSHNRYETVEMV</span><span class="topo-membrane">FIATVTGSLSLVTVVGNILVMLSIK</span><span class="topo-inside">VNRQLQTVNN</span><span class="topo-membrane">YFLFSLACADLIIGAFSMNLYTVYI</span><span class="topo-outside">IKGYWPLGAV</span><span class="topo-membrane">VCDLWLALDYVVSNASVMNLLIISF</span><span class="topo-inside">DRYFCVTKPLT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">YPARRTTKMA</span><span class="topo-membrane">GLMIAAAWVLSFVLWAPAILFWQFVV</span><span class="topo-outside">GKRTVPDNQCFIQFL</span><span class="topo-membrane">SNPAVTFGTAIAAFYLPVVIMTVLYI</span><span class="topo-inside">HISLASRSRVNIFEMLRIDE</span><span class="topo-unknown">GGGSGGD</span><span class="topo-inside">EAEKLFNQDVDAAVRG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span><span class="topo-unknown">QMAARE</span><span class="topo-inside">RKVTR</span><span class="topo-membrane">TIFAILLAFILTWTPYNVMVLVNTF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420  </span>
<span class="topo-line"><span class="topo-membrane">CQ</span><span class="topo-outside">SCIPDT</span><span class="topo-membrane">VWSIGYWLCYVNSTINPACYALCN</span><span class="topo-inside">ATFKKTFRHLLLC</span><span class="topo-unknown">QYRNIGTARHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>20</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>34</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>49</td>
      <td>59</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>74</td>
      <td>69</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>84</td>
      <td>94</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>109</td>
      <td>104</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>130</td>
      <td>129</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>156</td>
      <td>150</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>171</td>
      <td>176</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>197</td>
      <td>191</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>207</td>
      <td>217</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>217</td>
      <td>1002</td>
      <td>1011</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>324</td>
      <td>1019</td>
      <td>1118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>335</td>
      <td>396</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>362</td>
      <td>401</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>368</td>
      <td>428</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>392</td>
      <td>434</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>405</td>
      <td>458</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>422</td>
      <td>471</td>
      <td>487</td>
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

### M4-specific rotameric change of D112 (3.32)

The M4 receptor exhibits a unique rotameric change of D112 (3.32) compared to M1, M2, and M3 structures. This residue is conserved throughout biogenic amine GPCRs and serves as the counter-ion for positively charged neurotransmitters. In the M4 structure, D112 (3.32) points away from [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) and is accompanied by slight movements of Y439 (7.39) and Y443 (7.43), allowing them to form a network of hydrogen bond interactions between D112 (3.32), S85 (2.57), W108 (3.28), Y439 (7.39), and Y443 (7.43). This hydrogen bond network is distinct from M1, M2, and M3 muscarinic receptor structures.

### Intact ionic lock in M4 receptor

The M4 receptor was crystallized with an intact ionic lock, a feature uncommonly seen in other GPCRs and not present in other muscarinic structures. Chain B of the M4 receptor shows R (3.50) forming hydrogen bonds with T (6.34) and E (6.30). This contrasts with the other muscarinic receptor structures where the ionic lock is disrupted.

### PEG 300 as allosteric modulator

[PEG](/xray-mp-wiki/reagents/additives/peg/) 300, a required precipitant for crystallization, was found to occupy the allosteric binding site of the inactive-state M4 receptor. Surrounding the [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 molecule are residues forming the allosteric site from the top regions of TM2, TM3, and TMs 5-7. [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 sits immediately above the aromatic cage composed of Y113 (3.33), Y416 (6.51), Y439 (7.39), and Y443 (7.43). [PEG](/xray-mp-wiki/reagents/additives/peg/) 300 was confirmed to act as an allosteric modulator through its ability to retard the dissociation of [3H][NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) in a concentration-dependent manner with an apparent affinity of approximately 10 mM for the NMS-occupied M4 receptor.

### Allosteric network linking orthosteric and allosteric sites

A network of residues was identified that links the allosteric and orthosteric sites of the M4 receptor, involving the interface between TMs 2, 3, 6, and 7, and extending along the top of ECL2. This network was mapped through mutagenesis studies examining cooperativity between [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) and the PAM [LY2033298](/xray-mp-wiki/reagents/ligands/ly2033298/). Residues including W435 (7.35), F186 (ECL2), Y113 (3.33), Y416 (6.51), Y439 (7.39), Y89 (2.61), W108 (3.28), L109 (3.29), N423 (6.58), and others were found to significantly affect cooperativity upon mutation. The TM2/3/7 interface may act as a hinge mediating conformational rearrangements in the extracellular vestibule between inactive and active states.

### Comparison with M1-M3 receptor structures

The M4 structure is overall similar to M1, M2, and M3 with RMSD of 0.6-0.9 A (excluding [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusions). The M4 structure reveals differences in the allosteric vestibule that are strikingly divergent between subtypes, while the orthosteric site residues are highly conserved. The M4 structure, together with M1, M2, and M3 structures, provides a near complete view of the inactive state of the muscarinic receptor subfamily.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/">M1 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; co-crystallized with tiotropium in same study
- <a href="/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/">Human M2 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; used as search model for M4 structure determination (PDB 3UON)
- <a href="/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/">M3 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; used as search model for mT4L fusion (PDB 4U15)
- <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> — Inverse agonist co-crystallized with M4 receptor (PDB 5DSG)
- <a href="/xray-mp-wiki/proteins/gpcr/mt4l-lysozyme/">mT4L (Minimal T4 Lysozyme)</a> — Minimal T4 lysozyme fusion used to replace ICL3 for crystallization
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">Flag Epitope Tag (DYKDDDDK)</a> — N-terminal FLAG tag used for purification and as crystallization construct component
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — LCP lipid matrix used for M4 crystallization (10:1 monoolein:cholesterol)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — M4 receptor allosteric site and cooperativity network central to paper findings
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
