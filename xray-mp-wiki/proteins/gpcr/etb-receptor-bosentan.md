---
title: "Human Endothelin ETB Receptor Bound to Bosentan"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3450]
verified: agent
uniprot_id: P24530
---

# Human Endothelin ETB Receptor Bound to Bosentan

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P24530">UniProt: P24530</a>

<span class="expr-badge">Enterobacteria phage RB59</span>

## Overview

The human endothelin ETB receptor is a class A G-protein-coupled receptor (GPCR) activated by vasoactive peptide hormones endothelins. This paper reports the crystal structures of the ETB receptor bound to the clinical dual ETA-ETB antagonist bosentan at 3.6-A resolution and to the ETB-selective analog K-8794 at 2.2-A resolution. The ETB receptor plays crucial roles in vascular control as a target for drugs treating pulmonary arterial hypertension and cancer progression. Bosentan is the first oral drug approved to treat PAH, with worldwide sales surpassing $1 billion per year. The structures reveal detailed interactions between the antagonists and the receptor, unexpected similarity between antagonist and agonist binding at the orthosteric site, and how bosentan sterically prevents the inward movement of transmembrane helix 6 (TM6), thereby exerting its antagonistic activity. The K-8794-bound structure at high resolution reveals a detailed water-mediated hydrogen-bonding network at the transmembrane core that accounts for weak negative allosteric modulation of ETB by sodium ions.


## Publications

### doi/10.1038##nsmb.3450

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5x93">5X93</a></td>
      <td>2.2</td>
      <td>C2221</td>
      <td>ETB-Y5-mT4L thermostabilized mutant with mT4L fusion in ICL3, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation">Protein Truncation for Crystallization</a> after Ser407, C396A/C400A/C405A mutations, five thermostabilizing mutations, HA signal peptide, Flag tag, and 9-aa linker</td>
      <td>K-8794 (ETB-selective antagonist, 10 uM throughout purification)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xpr">5XPR</a></td>
      <td>3.6</td>
      <td>P3221</td>
      <td>ETB-Y4-mT4L thermostabilized mutant (reverted Asp154Ala to Asp for bosentan crystallization), same core mutations as Y5 variant</td>
      <td>Bosentan (clinical dual ETA-ETB antagonist, 10 uM throughout purification)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells using Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system) (Invitrogen)
- **Construct**: ETB-Y5-mT4L or ETB-Y4-mT4L in modified pFastBac1 vector with [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) recognition sequence and EGFP-His10 tag. Infected at 4.0 x 10^6 cells/ml in Sf900 II medium, grown 48 h at 27 C.

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
      <td>Sonication and ultracentrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.5, 20% glycerol + --</td>
      <td>Harvested Sf9 cells disrupted by sonication; crude membrane fraction collected by ultracentrifugation at 180,000g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 200 mM NaCl, 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">Iodoacetamide</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilized for 2 h at 4 C; antagonists added to 10 uM final concentration</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON Cobalt Affinity Resin</a> resin (Clontech)</td>
      <td>20 mM Tris-HCl pH 7.5, 500 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (wash); 200 mM imidazole (elution) + <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG (Lauryl Maltose Neopentyl Glycol)</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Incubated with resin for 30 min; eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease digestion and dialysis</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.5, 500 mM NaCl + --</td>
      <td>Eluate treated with <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> and dialyzed to remove imidazole</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 7.5, 500 mM NaCl + --</td>
      <td>Cleaved GFP-His10 tag and <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a> removed with <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) resin</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200 Increase [SEC</a> Resin](/xray-mp-wiki/reagents/additives/superdex-200) 10/300 Increase column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a>-NaOH pH 7.5, 200 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG (Lauryl Maltose Neopentyl Glycol)</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Peak fractions concentrated to 40 mg/ml; antagonists added to 100 uM for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ETB receptor at 40 mg/ml reconstituted into <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> of monoolein with <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> at 8:9:1 ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of ETB-Y5-mT4L-K-8794 in space group C2221 (2.2 A); ETB-Y4-mT4L-bosentan in space group P3221 (3.6 A). Molecular replacement used for structure determination.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5x93">5X93</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGGLAPAEVPKGDRTAGSPPRT</span><span class="topo-inside">ISPPPCQGPIEIKETF</span><span class="topo-membrane">KYINTVVSCLVFVLGIIGNSTLL</span><span class="topo-outside">YIIYKNKCMRNGPNIL</span><span class="topo-membrane">IASLALGDLLHIVIAIPINVYKLL</span><span class="topo-inside">AEDW</span><span class="topo-membrane">PFGAEMCKLVPFIQK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ASVGITVLSLCA</span><span class="topo-outside">LSIDRYRAVASWSRIKGIGVPKWTAVE</span><span class="topo-membrane">IVLIWVVSVVLAVPEAIGFD</span><span class="topo-inside">IITMDYKGSYLRICLLHPVQKTAFM</span><span class="topo-membrane">QFYATAKDWWLFSFYFCLPLAITAF</span><span class="topo-outside">FYTLMTCEMLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-outside">DHLKQRREVAKTV</span><span class="topo-membrane">FCLVLVFALCWLPLHLARILKLTL</span><span class="topo-inside">YNQNDPNRCELLSF</span><span class="topo-membrane">LLVLDYIGINMASLNSCANPIALYL</span><span class="topo-outside">VS</span><span class="topo-unknown">KRFKNAFKSAL</span><span class="topo-outside">CCW</span><span class="topo-unknown">AQSPSSENLYFQ</span></span>
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
      <td>23</td>
      <td>38</td>
      <td>85</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>101</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>77</td>
      <td>124</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>101</td>
      <td>140</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>105</td>
      <td>164</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>132</td>
      <td>168</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>159</td>
      <td>195</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>179</td>
      <td>222</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>242</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>229</td>
      <td>267</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>373</td>
      <td>292</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>397</td>
      <td>326</td>
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
      <td>436</td>
      <td>364</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>438</td>
      <td>389</td>
      <td>390</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>449</td>
      <td>391</td>
      <td>401</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>450</td>
      <td>452</td>
      <td>402</td>
      <td>404</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xpr">5XPR</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGGLAPAEVPKGDRTAGSPPRTISPPP</span><span class="topo-outside">CQGPIEIKETFKY</span><span class="topo-membrane">INTVVSCLVFVLGIIGNSTLLYIIYK</span><span class="topo-inside">NKCMRNGPN</span><span class="topo-membrane">ILIASLALGDLLHIVIDIPINVY</span><span class="topo-outside">KLLAEDWPFGAE</span><span class="topo-membrane">MCKLVPFIQK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ASVGITVLSLCALSID</span><span class="topo-inside">RYRAVASWSRIKGIGVPKWT</span><span class="topo-membrane">AVEIVLIWVVSVVLAVPEAIGF</span><span class="topo-outside">DIITMDYKGSYLRICLLHPVQKT</span><span class="topo-membrane">AFMQFYATAKDWWLFSFYFCLPLAITAFFYT</span><span class="topo-inside">LMTCEMLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KNIFEMLRIDE</span><span class="topo-unknown">GGGSGGDEAEKL</span><span class="topo-inside">FNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-inside">DHLKQRREVAK</span><span class="topo-membrane">TVFCLVLVFALCWLPLHLARILKLTL</span><span class="topo-outside">YNQNDPNRCELLSFLLV</span><span class="topo-membrane">LDYIGINMASLNSCANPIALYLVS</span><span class="topo-inside">KRFKNAFKSALC</span><span class="topo-unknown">CWAQSPSSENLYFQ</span></span>
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
      <td>27</td>
      <td>63</td>
      <td>89</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>28</td>
      <td>40</td>
      <td>90</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>66</td>
      <td>103</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>75</td>
      <td>129</td>
      <td>137</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>98</td>
      <td>138</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>110</td>
      <td>161</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>136</td>
      <td>173</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>156</td>
      <td>199</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>178</td>
      <td>219</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>201</td>
      <td>241</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>232</td>
      <td>264</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>241</td>
      <td>295</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>251</td>
      <td>1002</td>
      <td>1011</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>263</td>
      <td>1012</td>
      <td>1023</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>358</td>
      <td>1024</td>
      <td>1118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>371</td>
      <td>311</td>
      <td>323</td>
      <td>Inside</td>
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
      <td>414</td>
      <td>350</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>438</td>
      <td>367</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>450</td>
      <td>391</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>464</td>
      <td>403</td>
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

### Unexpected similarity between antagonist and agonist binding

Despite having little structural similarity to the endogenous agonist endothelin-1, bosentan occupies the bottom of the orthosteric site, corresponding to the binding site for the C-terminal tripeptide of ET-1 (Ile19, Ile20, Trp21). The pharmacophore of bosentan consists of: (1) a negatively charged sulfonamide group that forms ionic interactions with positively charged residues (Lys182, Lys273, Arg343); (2) a hydrophobic 4-t-butylphenyl group; and (3) a 2-methoxyphenoxy group. The 2-pyrimidyl group shows relatively poor interaction, consistent with SAR studies showing less influence on affinity.

### Antagonistic mechanism via steric prevention of TM6 inward movement

Bosentan does not induce the inward movement of TM6 and TM7 that characterizes agonist binding. The critical activation residues Arg343(6.55) and Trp336(6.48) are not repositioned upon bosentan binding. Unlike ET-1 which causes significant conformational changes in TM6 and TM7, bosentan's binding to the orthosteric pocket sterically prevents the conformational transitions required for receptor activation, explaining its antagonistic activity despite occupying the same binding site as the agonist.

### Water-mediated hydrogen-bonding network and Na+ allosteric modulation

The high-resolution K-8794-bound structure reveals a detailed water-mediated hydrogen-bonding network at the transmembrane core. A putative Na+-binding site is identified with conserved residues N1.50, D2.50, S3.35, T3.39, W6.48, N7.45, S7.46, N7.49 matching the canonical GPCR sodium binding motif. Competition binding assays show that ETB receptor is weakly negatively allosterically modulated by Na+ ions, as 2 M [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride) does not 50% inhibit [125I]ET-1 binding.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM (N-Dodecyl-beta-D-maltoside)</a> — Primary solubilization detergent (0.5%) for ETB membrane extraction
- <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG (Lauryl Maltose Neopentyl Glycol)</a> — Used in IMAC wash/elution (0.1-0.01%) and [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) (0.01%) buffers
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">Cholesterol Hemisuccinate (CHS)</a> — Added at 0.1% during solubilization and 0.001% in [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) for receptor stability
- <a href="/xray-mp-wiki/reagents/buffers/tris">Tris Buffer</a> — Primary buffer (20-50 mM pH 7.5) for membrane prep and affinity purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> — Used at 10 mM pH 7.5 in [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) buffer
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">Sodium Chloride</a> — 200-500 mM [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride) in purification buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme">T4 Lysozyme (T4L) fusion</a> — mT4L fusion protein used in ICL3 for crystallization stabilization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> — LCP method used for ETB receptor crystallization with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein)
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
