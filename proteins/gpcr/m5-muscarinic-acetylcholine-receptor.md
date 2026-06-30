---
title: "Human M5 Muscarinic Acetylcholine Receptor"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1914446116]
verified: false
---

# Human M5 Muscarinic Acetylcholine Receptor

## Overview

The human M5 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (M5 mAChR) is a class A G protein-coupled receptor that preferentially couples to Gq/11 proteins. It represents less than 2% of total muscarinic receptor expression in the brain but is found predominantly in the central nervous system, where it has recently emerged as an exciting therapeutic target for treating disorders including drug addiction. The first high-resolution crystal structure of the M5 mAChR was determined bound to the clinically used inverse agonist [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) at 3.4 A resolution, using a T4 lysozyme ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion construct with the thermostabilizing S117(3.39)R mutation. This structure enabled complete structural comparison across all five mAChR family members (M1-M5), revealing differences in extracellular loop (ECL) regions that mediate orthosteric and allosteric ligand selectivity. A ternary complex structure with the bis-ammonium alkane modulator 4B-C7/3-phth was also determined at 2.55 A. Chimeric swaps between M2 and M5 ECL regions provided structural insight into kinetic selectivity, where ligands show differential residency times between related family members.


## Publications

### doi/10.1073##pnas.1914446116

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ol9">6OL9</a></td>
      <td>3.4 A</td>
      <td>Not specified</td>
      <td>Human M5 muscarinic receptor with T4 lysozyme fusion (residues 225-430 of ICL3 replaced by <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>), S117(3.39)R thermostabilizing mutation, N-terminal 20 amino acids cleaved by TEV protease site, bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a>
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ol9">6OL9</a></td>
      <td>2.55 A</td>
      <td>Not specified</td>
      <td>Human M5 muscarinic receptor with T4 lysozyme fusion, S117(3.39)R mutation, ternary complex with <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> and bis-ammonium alkane modulator 4B-C7/3-phth
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a>, 4B-C7/3-phth</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in source paper (standard baculovirus/Sf9 insect cell system as previously described for M3-M4 receptors)
- **Construct**: M5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with S117(3.39)R mutation. ICL3 residues 225-430 removed and replaced with T4 lysozyme fusion. N-terminal TEV protease site for removal of first 20 amino acids.


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
      <td>Receptor expression and purification</td>
      <td>M5-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> with S117(3.39)R purified similarly to previous methods for M3 receptor</td>
      <td>Not specified</td>
      <td>Not specified + Not specified</td>
      <td>S117(3.39)R mutation increased receptor yields during purification and resulted in crystals diffracting to 3.4 A.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M5-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> S117(3.39)R bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a>, reconstituted into 10:1 (wt/wt) <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> in 1:1.5 wt/wt protein:lipid ratio
</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 24 hours and grew to full size in 1-2 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Whole drops harvested using mesh grid loops and flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>For allosteric modulator cocrystallization, 2.5 mM modulator was added to purified protein and incubated on ice for 3 hours before <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) reconstitution. The ternary complex with 4B-C7/3-phth yielded crystals that grew to much larger size and diffracted to 2.55 A. Data collected at SPring-8 beamline BL32XU and Australian Synchrotron MX2 beamline. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using M5-mTAL (PDB 4U15) as search model for receptor and <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> ensemble for T4 lysozyme. Refinement performed with Phenix.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ol9">6OL9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAPLERH</span><span class="topo-outside">RLWE</span><span class="topo-membrane">VITIAAVTAVVSLITIVGNVLVMISFKV</span><span class="topo-inside">NSQLKTVN</span><span class="topo-membrane">NYYLLSLACADLIIGIFSMNLYTTYI</span><span class="topo-outside">LMGRWALGSLA</span><span class="topo-membrane">CDLWLALDYVASNARVMNLLVISFD</span><span class="topo-inside">RYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RAKRTP</span><span class="topo-membrane">KRAGIMIGLAWLISFILWAPAILCW</span><span class="topo-outside">QYLVGKRTVPLDECQIQF</span><span class="topo-membrane">LSEPTITFGTAIAAFYIPVSVMTILYC</span><span class="topo-inside">RIYRETEKRTNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHL</span><span class="topo-unknown">LTK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SPSLNAAKSELDKAIGRNCNGVI</span><span class="topo-inside">TKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GTWDAYRVVLVKERKAAQT</span><span class="topo-membrane">LSAILLAFIITWTPYNIMVLVSTFC</span><span class="topo-outside">DKCV</span><span class="topo-membrane">PVTLWHLGYWLCYVNSTVNPICYALC</span><span class="topo-inside">NRTFRKTFKMLLLCR</span><span class="topo-unknown">WKKKKVEEKLYWQGNSKLPSSHHHHHHHHHH</span></span>
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
      <td>7</td>
      <td>19</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>39</td>
      <td>30</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>47</td>
      <td>58</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>73</td>
      <td>66</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>92</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>109</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>126</td>
      <td>128</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>151</td>
      <td>145</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>170</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>196</td>
      <td>188</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>206</td>
      <td>215</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>237</td>
      <td>1001</td>
      <td>1031</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>263</td>
      <td>1032</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>366</td>
      <td>1058</td>
      <td>1160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>379</td>
      <td>431</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>404</td>
      <td>444</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>408</td>
      <td>469</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>434</td>
      <td>473</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>449</td>
      <td>499</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>480</td>
      <td>514</td>
      <td>544</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ol9">6OL9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GAPLERH</span><span class="topo-outside">RLWE</span><span class="topo-membrane">VITIAAVTAVVSLITIVGNVLVMISFKV</span><span class="topo-inside">NSQLKTVN</span><span class="topo-membrane">NYYLLSLACADLIIGIFSMNLYTTYI</span><span class="topo-outside">LMGRWALGSLA</span><span class="topo-membrane">CDLWLALDYVASNARVMNLLVISFD</span><span class="topo-inside">RYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RAKRTP</span><span class="topo-membrane">KRAGIMIGLAWLISFILWAPAILCW</span><span class="topo-outside">QYLVGKRTVPLDECQIQF</span><span class="topo-membrane">LSEPTITFGTAIAAFYIPVSVMTILYC</span><span class="topo-inside">RIYRETEKRTNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHL</span><span class="topo-unknown">LTK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SPSLNAAKSELDKAIGRNCNGVI</span><span class="topo-inside">TKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">GTWDAYRVVLVKERKAAQT</span><span class="topo-membrane">LSAILLAFIITWTPYNIMVLVSTFC</span><span class="topo-outside">DKCV</span><span class="topo-membrane">PVTLWHLGYWLCYVNSTVNPICYALC</span><span class="topo-inside">NRTFRKTFKMLLLCR</span><span class="topo-unknown">WKKKKVEEKLYWQGNSKLPSSHHHHHHHHHH</span></span>
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
      <td>7</td>
      <td>19</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>26</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>39</td>
      <td>30</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>47</td>
      <td>58</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>73</td>
      <td>66</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>92</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>109</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>126</td>
      <td>128</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>151</td>
      <td>145</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>170</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>196</td>
      <td>188</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>206</td>
      <td>215</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>237</td>
      <td>1001</td>
      <td>1031</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>263</td>
      <td>1032</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>366</td>
      <td>1058</td>
      <td>1160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>379</td>
      <td>431</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>404</td>
      <td>444</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>408</td>
      <td>469</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>434</td>
      <td>473</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>449</td>
      <td>499</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>480</td>
      <td>514</td>
      <td>544</td>
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

### Complete structural comparison of all five mAChR subtypes

The M5 structure completed the structural coverage of all five muscarinic receptor subtypes (M1-M5). The orthosteric binding pocket residues are absolutely conserved across all five subtypes. However, subtle differences in the extracellular loops (ECL2 and ECL3) are observed, with ECL2 showing a 1.8 A difference beginning at the first nonconserved residue. The ECL2 3-10 helix motif moves inward by 2.8 A in M5 compared to M1, and the conserved ECL3 disulphide bond is displaced inward by 3.1 A for M3 and M5. These ECL differences are the major determinants of subtype selectivity for both orthosteric and allosteric ligands.

### Kinetic selectivity through ECL chimeric swaps

The M2 receptor has a shorter half-life for [3H][NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) dissociation than M5. Chimeric swaps of ECL1, ECL2, and ECL3 between M2 and M5 receptors revealed that ECL1 has the largest effect on dissociation kinetics. R95(ECL1) in M5 is a conserved Tyr in M1-M4 subtypes and can form an ionic bond with M5 ECL2 residue D181(-2), potentially tethering ECL1 and ECL2 and limiting dynamics to reduce orthosteric ligand dissociation rates. The bis-ammonium alkane allosteric modulators (ML375, 4P-C7/3-phth) showed differential effects on [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine/) dissociation across the chimeras.

### Extracellular vestibule differences between M2 and M5

Comparison of the M2 and M5 extracellular vestibules (ECV) revealed major differences in nonconserved residues lining the top of TM6 starting from S465(6.58) across ECL3 and down to H478(7.36) in TM7. In the M5 receptor, these residues are bulkier and point more inwardly, constricting the overall size of the ECV. The allosteric modulator binding site at the ECV shows subtype-specific features that can be exploited for selective drug design.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/">M1 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; compared in M5 structural study
- <a href="/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/">Human M2 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; used for ECL chimeric swaps and kinetic selectivity studies
- <a href="/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/">M3 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; M5 structure solved using M3-mTAL (PDB 4U15) as molecular replacement search model
- <a href="/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/">Human M4 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; compared in M5 structural study
- <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> — Inverse agonist co-crystallized with M5 receptor (PDB 6OL9)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method for M5 structure determination
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-tartrate/">Ammonium Tartrate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/acetylcholine/">Acetylcholine</a> — Related ligand or cofactor
