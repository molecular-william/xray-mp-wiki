---
title: "Human Endothelin ETB Receptor in Complex with IRL2500"
created: 2026-06-08
updated: 2026-07-13
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s42003-019-0482-7]
verified: agent
uniprot_id: P24530
---

# Human Endothelin ETB Receptor in Complex with IRL2500

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P24530">UniProt: P24530</a>

<span class="expr-badge">Enterobacteria phage RB59</span>

## Overview

The human endothelin ETB receptor (ETB) is a class A GPCR that binds the endogenous
peptide hormone endothelin-1 (ET-1). [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is a peptide-mimetic of the C-terminal
tripeptide of ET-1 that functions as a potent ETB-selective inverse agonist. The
crystal structure of the thermostabilized ETB receptor (ETB-Y4-mT4L) in complex
with [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) was determined at 2.7 Å resolution. The structure reveals that the
biphenyl group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the transmembrane core proximal to
D[2.50], stabilizing the inactive conformation. [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) functions as an inverse
agonist, as demonstrated using a constitutively active ETB mutant (L192[3.43]Q).


## Publications

### doi/10.1038##s42003-019-0482-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6k1q">6K1Q</a></td>
      <td>2.7</td>
      <td>I422</td>
      <td>ETB-Y4-mT4L (thermostabilized ETB receptor with R124Y[1.55], K270A[5.35], S342A[6.54], I381A[7.48] mutations; mT4L inserted in ICL3 between K303[5.68] and L311[6.23]; C396A/C400A/C405A; N-terminal deletion G57-L66; C-terminus truncated after S407; C-terminal TEV-GFP-His10 tag)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system (Invitrogen)
- **Construct**: ETB-Y4-mT4L subcloned into modified pFastBac vector with C-terminal TEV cleavage site followed by GFP-His10 tag

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
      <td>Baculovirus infection of <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells</td>
      <td>—</td>
      <td>Sf900 II medium</td>
      <td>Infected at cell density of 4.0 x 10^6 cells per ml, grown for 48 h at 27°C</td>
    </tr>
    <tr>
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Crude membrane fraction collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 180,000 g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM <a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a>, 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
      <td>Solubilized for 1 h at 4°C; supernatant clarified by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 180,000 g for 20 min</td>
    </tr>
    <tr>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin (Clontech)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM <a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a>, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution)</td>
      <td>Incubated with <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin for 30 min; washed with 10 column volumes; eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>TEV protease cleavage and tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> cleavage and dialysis</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 μM <a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> treatment during dialysis; cleaved <a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a>-<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His10</a> tag removed with Co2+-NTA resin</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex200</a> 10/300 Increase column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 μM <a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a></td>
      <td>Peak fractions pooled and concentrated to 40 mg/ml using centrifugal filter device (Millipore 50 kDa MW cutoff); <a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a> added to 100 μM final concentration during concentration</td>
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
      <td>Purified ETB-Y4-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a>-<a href="/xray-mp-wiki/reagents/ligands/irl2500/">IRL2500</a> complex at 40 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> and <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (10:1 by mass)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-laden mesophase dispensed into 96-well glass plates in 30 nl drops overlaid with 800 nl precipitant solution by Gryphon <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> robot. Crystals harvested directly from <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> using micromounts or LithoLoops, frozen in <a href="/xray-mp-wiki/concepts/methods-techniques/cryocooling/">liquid nitrogen</a> without extra cryoprotectant.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6k1q">6K1Q</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGGLAPAEVPKGDRTAGSPPRTISPPPC</span><span class="topo-inside">QGPIEIKETFKY</span><span class="topo-membrane">INTVVSCLVFVLGIIGNSTLLYIIY</span><span class="topo-outside">KNKCMRNGP</span><span class="topo-membrane">NILIASLALGDLLHIVIDIPINVYKL</span><span class="topo-inside">LAEDWPFGA</span><span class="topo-membrane">EMCKLVPFIQK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ASVGITVLSLCALSI</span><span class="topo-outside">DRYRAVASWS</span><span class="topo-unknown">RIKGIG</span><span class="topo-outside">VPKWTA</span><span class="topo-membrane">VEIVLIWVVSVVLAVPEAIGF</span><span class="topo-inside">DIITMDYKGSYLRICLLHPVQKTAFMQFY</span><span class="topo-membrane">ATAKDWWLFSFYFCLPLAITAFFYT</span><span class="topo-outside">LMTCEMLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KNIFEMLRIDEG</span><span class="topo-unknown">GGSGGDE</span><span class="topo-outside">AEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-outside">DHLKQRREVAK</span><span class="topo-membrane">TVFCLVLVFALCWLPLHLARILKLTL</span><span class="topo-inside">YNQNDPNRCELLSF</span><span class="topo-membrane">LLVLDYIGINMASLNSCANPIALYLVS</span><span class="topo-outside">KRFKNAFKSALCC</span><span class="topo-unknown">WAQSPSSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>28</td>
      <td>63</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>40</td>
      <td>91</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>65</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>74</td>
      <td>128</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>100</td>
      <td>137</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>163</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>135</td>
      <td>172</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>145</td>
      <td>198</td>
      <td>207</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>151</td>
      <td>208</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>214</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>220</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>207</td>
      <td>241</td>
      <td>269</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>232</td>
      <td>270</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>241</td>
      <td>295</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>252</td>
      <td>1002</td>
      <td>1012</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>358</td>
      <td>1013</td>
      <td>1111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>371</td>
      <td>311</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>397</td>
      <td>324</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>411</td>
      <td>350</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>438</td>
      <td>364</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>451</td>
      <td>391</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>464</td>
      <td>404</td>
      <td>416</td>
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

### IRL2500 binds in a distinct mode from ET-1 and bosentan

[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is designed to mimic the F14, I19, I20, and W21 residues of ET-1.
While the electrostatic interactions between the carboxylates and positively
charged residues are conserved between [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) and ET-1 binding, the biphenyl
group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the receptor core in an opposite manner to
the F14 and I20 of ET-1. The tryptophan of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) superimposes with I20
of ET-1 rather than W21, while the dimethylbenzoyl group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/)
superimposes with W21 of ET-1.

### IRL2500 as an inverse agonist stabilizing the inactive conformation

[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) functions as an inverse agonist for the ETB receptor. The biphenyl
group of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) penetrates into the transmembrane core proximal to D147[2.50],
stabilizing the inactive conformation. This is analogous to other class A GPCR
inverse agonists such as ritanserin-bound 5-HT2CR and BIIL260-bound [Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human](/xray-mp-wiki/proteins/gpcr/blt1/),
which also interact near the sodium binding site.

### ETB-selectivity mechanism of IRL2500

ETB-selectivity of [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) is attributed to residues Y129[2.53] and F161[3.28]
in the ETA receptor, which specifically clash with [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/). The H150Y and V177F
mutations in ETA (corresponding to ETB residues) selectively reduce [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/)
potency without affecting bosentan potency. The S376T mutation in ETB increases
[IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) potency by 4-fold.

### Constitutively active ETB mutant L192[3.43]Q

The L192[3.43]Q mutation in ETB confers constitutive activity, as measured by
AP-TGFα shedding assay. Using this mutant, [IRL2500](/xray-mp-wiki/reagents/ligands/irl2500/) was shown to reduce basal
signaling, confirming its inverse agonist activity. Bosentan, K-8794, and BQ-788
also showed inverse agonist activity in this assay.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-endothelin-etb-receptor-et1/">Human Endothelin ETB Receptor Bound to Endothelin-1</a> — Same ETB receptor bound to agonist ET-1 for comparison of binding modes
- <a href="/xray-mp-wiki/proteins/gpcr/etb-receptor-bosentan/">Human Endothelin ETB Receptor Bound to Bosentan</a> — Same ETB receptor bound to clinical antagonist for comparison
- <a href="/xray-mp-wiki/proteins/gpcr/etb-s6b-complex/">Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b</a> — Related ETB receptor structure with snake toxin agonist
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent for membrane solubilization
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in IMAC wash and SEC buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L) fusion</a> — mT4L insertion in ICL3 enabled crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for ETB receptor crystallization
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — IRL2500 stabilizes the inactive conformation, relevant to GPCR activation mechanism
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/gpcr/blt1/">Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human</a> — Related protein structure
