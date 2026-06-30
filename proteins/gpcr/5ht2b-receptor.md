---
title: "Human 5-HT2B Receptor"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2016.12.033, doi/10.1126##science.1244142]
verified: false
---

# Human 5-HT2B Receptor

## Overview

The human serotonin 2B (5-HT2B) receptor is a class A GPCR that signals primarily through Gq/11 and [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin) pathways. It is a target of several drugs and is the molecular target of the hallucinogen LSD. Multiple crystal structures have been determined revealing structural determinants of receptor activation and biased agonism, including complexes with ergotamine, LSD, methylergonovine, methysergide, lisuride, and LY266097.

## Publications

### doi/10.1016##j.cell.2016.12.033

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tvn">5TVN</a></td>
      <td>2.9 A</td>
      <td>C2221</td>
      <td>Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by BRIL fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG Tag</a>, C-terminal PreScission site and 10xHis tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/lsd">LSD</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells)
- **Construct**: Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag), C-terminal PreScission site and 10xHis tag

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
      <td>Cell culture and membrane preparation</td>
      <td>Baculovirus expression in <a href="/xray-mp-wiki/methods/expression-systems/sf9-insect-cells">Sf9 Cells</a></td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, 150 mM NaCl + --</td>
      <td>High-titer recombinant <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus</a> used to infect Sf9 cells. Cells harvested 48 hr post-infection, washed in PBS, flash-frozen at -80C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/lsd/">LSD</a> (50 uM) pre-incubated with membranes before solubilization. <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">Iodoacetamide</a> treatment for 30 min prior to solubilization</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a> resin</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His Tag</a> on <a href="/xray-mp-wiki/concepts/c-terminus/">C-terminus</a> used for affinity capture via <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final purification step to obtain monodisperse 5-HT2B-R-<a href="/xray-mp-wiki/reagents/ligands/lsd/">LSD</a>-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT2B-R-<a href="/xray-mp-wiki/reagents/ligands/lsd/">LSD</a>-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> complex at ~15 mg/ml</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> method with <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>. Crystals diffracted to 2.9 A (space group C2221). Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using 5-HT2B-R/<a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> (PDB: 4IB4) and <a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> (PDB: 1M6T) as search models</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5tvn">5TVN</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">EEMKQIVEEQGNK</span><span class="topo-membrane">LHWAALLILMVIIPTIGGNTLVI</span><span class="topo-inside">LAVSLEKKLQYATNYF</span><span class="topo-membrane">LMSLAVADLLVGLFVMPIALLTIMF</span><span class="topo-outside">EAMW</span><span class="topo-membrane">PLPLVLCPAWLFLDVLFSTASIWHLCAISV</span><span class="topo-inside">DRYIAIKKP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IQANQYNSRATAFI</span><span class="topo-membrane">KITVVWLISIGIAIPVPIKGI</span><span class="topo-outside">ET</span><span class="topo-unknown">DVD</span><span class="topo-outside">NPNNITCVLTKER</span><span class="topo-membrane">FGDFMLFGSLAAFFTPLAIMIVTYFL</span><span class="topo-inside">TIHALQKKAADLEDNWETLNDNLKVIEKADNAAQVKDALTK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">MRAAALDAQKATPPKLE</span><span class="topo-unknown">DKSPDS</span><span class="topo-inside">PEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLVQTISNEQRASKV</span><span class="topo-membrane">LGIVFFLFLLMWCPFFITNITLVLC</span><span class="topo-outside">DSCNQTTL</span></span>
<span class="topo-ruler">       370       380       390       400  </span>
<span class="topo-line"><span class="topo-membrane">QMLLEIFVWIGYVSSGVNPLVYT</span><span class="topo-inside">LFNKTFRDAFGRYITCNYR</span></span>
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
      <td>13</td>
      <td>41</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>36</td>
      <td>54</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>77</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>77</td>
      <td>93</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>81</td>
      <td>118</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>111</td>
      <td>122</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>134</td>
      <td>152</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>155</td>
      <td>175</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>157</td>
      <td>196</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>160</td>
      <td>198</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>161</td>
      <td>173</td>
      <td>201</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>199</td>
      <td>214</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>208</td>
      <td>240</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>257</td>
      <td>1001</td>
      <td>1049</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>263</td>
      <td>1050</td>
      <td>1055</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>314</td>
      <td>1056</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>315</td>
      <td>327</td>
      <td>313</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>352</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>360</td>
      <td>351</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>383</td>
      <td>359</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>402</td>
      <td>382</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.1244142

**Expression:**

- **Expression system**: [Sf9 Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells)
- **Construct**: Human 5-HT2B receptor, N-terminal residues 1-35 truncated, C-terminal residues 406-481 truncated, thermostabilizing M144W mutation, ICL3 replaced by [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion (A1-L106 of apocytochrome b562 RIL), N-terminal HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag), C-terminal PreScission site and 10xHis tag

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography">LCP-SFX</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-HT2B-R-<a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ergotamine</a>-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> complex in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> at ~3 mg/ml (300 ug total)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40:60 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>21 C (room temperature)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>-grown microcrystals (5x5x5 um) delivered via <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> injector at LCLS CXI. Co-axial He/N2 gas stabilization at 20-30 bar. 4,217,508 diffraction patterns collected in 10 hours at 120 Hz, 50 fs pulses, 9.5 keV. 152,651 crystal hits (3.6%), 32,819 indexed (21.5%). Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> at 2.8 A resolution. Rwork/Rfree = 22.7/27.0%. Space group C2221. First room-temperature <a href="/xray-mp-wiki/concepts/gpcr/">GPCR</a> structure obtained by SFX.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unexpected shallow binding mode of LSD

LSD adopts a shallow binding mode in the 5-HT2B receptor orthosteric pocket, positioned higher and closer to EL2 compared to the deeper-binding [Ergotamine](/xray-mp-wiki/reagents/ligands/ergotamine). The ergoline moiety of LSD forms a hydrogen bond between the basic amine and the conserved D135 residue at position 3.32, while the indole nitrogen hydrogen bonds with G221 at position 5.42 in helix V, rather than T140 at position 3.37 at the bottom of the pocket as seen with ergotamine. The diethylamide substituent does not interact with M218 at position 5.39, allowing this residue to flip upward and create more space for LSD shallower pose.

### Arrestin-biased conformational state

The LSD-bound 5-HT2B receptor adopts a conformation reminiscent of the ERG-bound structure, showing hallmarks of an arrestin-biased state. This includes a partially activated PIF motif, larger activation-related changes in helix VII and the NPxxY motif compared to helices V, VI, and the DRY motif. At 5-HT2B receptors, both LSD and ERG preferentially engage [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)-mediated over Gq-mediated signal transduction.

### EL2 lid and slow LSD dissociation kinetics

Molecular dynamics simulations reveal that extracellular loop 2 (EL2) residues 207-214 form a lid over the binding pocket. The lid residue L209 at EL2 acts as a latch through extensive hydrophobic contacts with LSD and surrounding TM residues. Mutation of L209 to alanine dramatically accelerates LSD off-rate (residence time decreases from 46 min to 4 min at 5-HT2B), selectively dampening [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment while leaving Gq signaling intact. This structural motif explains LSD extremely slow residence time at serotonin receptors, which likely contributes to its prolonged psychoactive effects.

### Room-temperature SFX structure reveals native conformational ensemble

The 5-HT2B-XFEL structure (2.8 A) was the first room-temperature GPCR structure determined by [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography) (SFX). Comparison with the cryo-cooled synchrotron structure (PDB 4IB4, 2.7 A) revealed that the room-temperature structure has a 2.1% larger unit cell volume and a 2.5 degree rotation of the [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion domain. The average B-factor was 21 A^2 higher (88.4 vs 67.2 A^2), consistent with greater thermal motions. A salt bridge between Glu319 and Lys247, well-defined in the room-temperature structure, appeared broken in the cryo structure, suggesting it plays a role in receptor function. Helix II adopted a regular alpha-helix at room temperature vs a water-stabilized kink in the cryo structure. These findings demonstrate that SFX provides a more accurate representation of the native conformational ensemble of GPCRs.

### Diethylamide stereoselectivity

The conformation of LSD diethylamide moiety in the receptor-bound state differs from the free small-molecule crystal structure by approximately 60 degrees rotation. Sterically constrained analogs show that the (S,S)-azetidide (SSAz) conformation, which matches the receptor-bound LSD conformation, retains full potency and efficacy. In contrast, the (R,R)-azetidide (RRAz) analog, which resembles the free LSD conformation, has much reduced potency for [Beta-Arrestin](/xray-mp-wiki/concepts/beta-arrestin)2 recruitment at both 5-HT2B and 5-HT2A receptors.

### Orthosteric binding pocket (OBP) vs extended binding pocket (EBP) mutations in biased agonism

Systematic mutagenesis of the 5-HT2B receptor reveals that the orthosteric binding pocket (OBP) residue T140^3.37 and the extended binding pocket (EBP) residue A225^5.46 play distinct roles in biased agonism. OBP mutation T140A reduces Gq potency more than beta-arrestin2 recruitment, while EBP mutation A225G enhances Gq potency and converts methysergide from antagonist to full agonist. These results demonstrate that ligand-receptor interactions at different depths in the binding pocket contribute differentially to G protein versus arrestin signaling.

### OBP toggle switch residue L362^7.35

The residue L362^7.35 at the bottom of the orthosteric binding pocket acts as a toggle switch for biased signaling. Mutation to smaller residues (L362A, L362N) or aromatic residues (L362F, L362Y) differentially affects LSD-mediated beta-arrestin2 recruitment. The L362F mutation converts lisuride from a balanced agonist to a Gq-biased ligand, suggesting that steric interactions at the base of the binding pocket control signaling bias through the intracellular cavity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/lsd">LSD (Lysergic Acid Diethylamide)</a> — Primary co-crystallized ligand in PDB 5TVN
- <a href="/xray-mp-wiki/reagents/protein-tags/bril">bRIL Fusion Protein</a> — Replaces ICL3 for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization detergent
- <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) lipid matrix for crystallization
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">Cholesterol Hemisucinate (CHS)</a> — Stabilizing lipid additive
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> — Crystallization method used
- <a href="/xray-mp-wiki/proteins/5ht2a-receptor">Human 5-HT2A Receptor</a> — Homology model based on 5-HT2B-R/LSD structure; functional assays performed
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus</a> — Expression system used for protein production
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography">Serial Femtosecond Crystallography</a> — SFX method used to obtain room-temperature 2.8 A structure of 5-HT2B-ergotamine complex
