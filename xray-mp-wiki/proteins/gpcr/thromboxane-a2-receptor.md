---
title: "Human Thromboxane A2 Receptor (TP)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0170-9]
verified: regex
uniprot_id: P21731
---

# Human Thromboxane A2 Receptor (TP)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P21731">UniProt: P21731</a>

## Overview

The human thromboxane A2 receptor (TP) is a class A G-protein-coupled receptor that mediates the physiological actions of thromboxane A2 (TXA2), an endogenous arachidonic acid metabolite. TP plays a pivotal role in cardiovascular homeostasis and is considered an important drug target for cardiovascular disease. Two splice variants have been identified (TPα and TPβ) that share the same N-terminal 328 residues but differ in their C-terminal tails. Crystal structures of TP bound to the nonprostanoid antagonists ramatroban (2.5 A, PDB 6IIU) and daltroban (3.0 A, PDB 6IIV) revealed a ligand-binding pocket capped by two layers of extracellular loops stabilized by two disulfide bonds (C11-C102 and C105-C183), limiting ligand access from the extracellular milieu. The structures provide a detailed picture of ligand recognition, with the carboxylic acid group of antagonists forming salt bridges with H89(2.65) and R295(7.40) and a hydrogen bond with S181. The benzenesulfonamide moiety occupies a subpocket shaped by helices II, III, VI and VII, with hydrogen bonds to T81(2.57) and Q301(7.46). Molecular docking of prostanoid-like ligands SQ-29548 and U46619, combined with mutagenesis and functional assays, suggests a shared prostanoid binding mode across prostanoid receptors.

## Publications

### doi/10.1038##s41589-018-0170-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6iiu">6IIU</a></td>
      <td>2.5 A</td>
      <td>P 1 2 1</td>
      <td>TPα with bRIL fused at N terminus and rubredoxin fused in ICL3; C-terminal truncation (S324-Q343); L247(6.37) mutation; expressed in Sf9 insect cells via baculovirus</td>
      <td>Ramatroban</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6iiv">6IIV</a></td>
      <td>3.0 A</td>
      <td>P 1 2 1</td>
      <td>TPα with bRIL fused at N terminus and rubredoxin fused in ICL3; C-terminal truncation (S324-Q343); L247(6.37) mutation; expressed in Sf9 insect cells via baculovirus</td>
      <td>Daltroban</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells via Bac-to-Bac baculovirus expression system
- **Construct**: Codon-optimized human TPα with N-terminal HA signal sequence and Flag tag, C-terminal PreScission site and 10xHis tag; bRIL fusion at N terminus; rubredoxin fusion in ICL3; C-terminal truncation of 20 residues (S324-Q343); L247(6.37) point mutation

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
      <td>Hypotonic lysis and centrifugation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors</td>
      <td>Washed with high-salt buffer (1 M NaCl) to remove membrane-associated proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Incubated 3 h at 4°C with 100 uM ramatroban or daltroban</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>20 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 30 mM imidazole</td>
      <td>Washed with 30 column volumes; eluted with 200-300 mM imidazole</td>
    </tr>
    <tr>
      <td>Final purification</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Peak fractions pooled and concentrated</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TP-ramatroban complex at ~25 mg/mL</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20\u00B0C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>PEG 400 as cryoprotectant (by LCP method)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> with monoolein (9.5 A/0.9 A); data collected from 16 crystals for ramatroban, 49 crystals for daltroban</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6iiu">6IIU</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAP</span><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLPCFR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PTNITLEERRLIAS</span><span class="topo-membrane">PWFAASFCVVGLASNLLALSVLA</span><span class="topo-outside">GA</span><span class="topo-unknown">RQGGSH</span><span class="topo-outside">TRSS</span><span class="topo-membrane">FLTFLCGLVLTDFLGLLVTGTIVVSQHA</span><span class="topo-inside">ALFEWHAVDPGCRL</span><span class="topo-membrane">CRFMGVVMIFFGLSPLLLGAAMASERYL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ITRPFSRPAVASQ</span><span class="topo-membrane">RRAWATVGLVWAAALALGLLPLL</span><span class="topo-inside">GVGRYTVQYPGSWCFLTLGAESGDV</span><span class="topo-membrane">AFGLLFSMLGGLSVGLSFLLNTVSVA</span><span class="topo-outside">TLCHVYHGMKKYTCTVCGYIYNPEDGDPDNGVN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">PGTDFKDIPDDWVCPLCGVGKDQFEEVEERDSEVEM</span><span class="topo-membrane">MAQALGIMVVASVCWLPLLVFIAQ</span><span class="topo-inside">TVLRNPPAMSPAGQLSRTTEKE</span><span class="topo-membrane">LLIYLRVATWNQILDPWVYILF</span><span class="topo-outside">R</span><span class="topo-unknown">RAVLRRLQ</span><span class="topo-outside">PRL</span><span class="topo-unknown">EFLE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">VLFQ</span></span>
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
      <td>11</td>
      <td>134</td>
      <td>1001</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>157</td>
      <td>28</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>159</td>
      <td>51</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>169</td>
      <td>59</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>197</td>
      <td>63</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>211</td>
      <td>91</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>239</td>
      <td>105</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>253</td>
      <td>133</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>276</td>
      <td>147</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>301</td>
      <td>170</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>327</td>
      <td>195</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>396</td>
      <td>221</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>420</td>
      <td>244</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>442</td>
      <td>268</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>464</td>
      <td>290</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>465</td>
      <td>312</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>473</td>
      <td>313</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>474</td>
      <td>476</td>
      <td>321</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6iiv">6IIV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGA</span><span class="topo-outside">PADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLPCFR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PTNITLEERRLIASP</span><span class="topo-membrane">WFAASFCVVGLASNLLALSVL</span><span class="topo-inside">AGAR</span><span class="topo-unknown">QGGSHT</span><span class="topo-inside">RSSFLT</span><span class="topo-membrane">FLCGLVLTDFLGLLVTGTIVV</span><span class="topo-outside">SQHAALFEWHAVDPGCRLCR</span><span class="topo-membrane">FMGVVMIFFGLSPLLLGAAMAS</span><span class="topo-inside">ERYLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ITRPFSRPAVASQRRAW</span><span class="topo-membrane">ATVGLVWAAALALGLLPLLGVG</span><span class="topo-outside">RYTVQYPGSWCFLTLGAESG</span><span class="topo-membrane">DVAFGLLFSMLGGLSVGLSFLLNT</span><span class="topo-inside">VSVATLCHVYHGMKKYTCTVCGYIYNPEDGDPDNGVN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PGTDFKDIPDDWVCPLCGVGKDQFEEVEERDSEVEMMAQ</span><span class="topo-membrane">ALGIMVVASVCWLPLLVFIAQ</span><span class="topo-outside">TVLRNPPAMSPAGQLSRTTEKEL</span><span class="topo-membrane">LIYLRVATWNQILDPWVYILF</span><span class="topo-inside">R</span><span class="topo-unknown">RAVLRR</span><span class="topo-inside">LQPRL</span><span class="topo-unknown">EFLE</span></span>
<span class="topo-ruler">    </span>
<span class="topo-line"><span class="topo-unknown">VLFQ</span></span>
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
      <td>10</td>
      <td>135</td>
      <td>1000</td>
      <td>28</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>156</td>
      <td>29</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>160</td>
      <td>50</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>172</td>
      <td>60</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>193</td>
      <td>66</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>213</td>
      <td>87</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>235</td>
      <td>107</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>129</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>299</td>
      <td>173</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>323</td>
      <td>193</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>399</td>
      <td>217</td>
      <td>246</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>420</td>
      <td>247</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>443</td>
      <td>268</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>464</td>
      <td>291</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>465</td>
      <td>312</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>466</td>
      <td>471</td>
      <td>313</td>
      <td>318</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>472</td>
      <td>476</td>
      <td>319</td>
      <td>323</td>
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

### Two-layer extracellular cap with unique disulfide bonds

The TP structures reveal a unique double-layer extracellular lid formed by two disulfide bonds: the conserved C105(3.25)-C183 bridge between helix III and ECL2, and a novel C11-C102(3.22) bond connecting the N terminus and the extracellular tip of helix III. This two-layer cover constrains ligand access from the extracellular milieu, suggesting ligands enter through the lipid bilayer via a gap between helices I and VII.

### Conserved prostanoid carboxylate-binding motif

The carboxylic acid group of both ramatroban and daltroban forms critical polar interactions with residues H89(2.65), S181 (ECL2), and R295(7.40). This binding mode is conserved across prostanoid receptors, explaining previous mutagenesis data showing that mutations at R(7.40) abolish ligand binding. The residue S181 is conserved across the prostanoid receptor subfamily (except DP2).

### Prostanoid binding mode revealed by docking

Molecular docking of prostanoid-like ligands SQ-29548 and U46619 into the TP structure reveals a V-shaped binding pose. The central ring orients toward helix I, with the alpha-chain (containing the heptenoic acid group) contacting helices II, III, VII and ECL2, and the omega-chain overlapping with the benzenesulfonamide tail of nonprostanoid antagonists. Mutagenesis confirmed the importance of T81(2.57), H89(2.65), S181, R295(7.40), and Q301(7.46) for ligand binding.

### Selectivity determinants across prostanoid receptors

Sequence alignment reveals that residues predicted to interact with the central ring of prostanoids are less conserved between different prostanoid receptors compared to residues forming contacts with the two side tails. This provides new insights into prostanoid receptor selectivity, suggesting the central ring configuration determines receptor specificity as previously proposed from pharmacological classification.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/prostanoid-receptor-family/">Prostanoid Receptor Family</a> — TP is a member of the prostanoid receptor family; structures provide first atomic-level view of TP ligand recognition
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/">GPCR Inactive Conformation</a> — TP-ramatroban and TP-daltroban structures represent antagonist-bound inactive state of a prostanoid receptor
- <a href="/xray-mp-wiki/proteins/gpcr/crth2/">CRTH2 (DP2)</a> — Another prostanoid receptor with distinct ligand-binding mode; comparison highlights diversity in prostanoid receptor ligand recognition
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/disulfide-bond-formation/">Disulfide Bond Formation</a> — Unique C11-C102 disulfide bond in extracellular region stabilizes the two-layer lid over the ligand-binding pocket
