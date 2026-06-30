---
title: "Human Endothelin ETB Receptor Bound to Endothelin-1"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19319]
verified: false
---

# Human Endothelin ETB Receptor Bound to Endothelin-1

## Overview

The human endothelin ETB receptor is a class A GPCR that binds the endogenous
  21-amino-acid peptide hormone endothelin-1 (ET-1) with sub-nanomolar affinity in
a virtually irreversible manner. Crystal structures of the thermostabilized ETB
receptor in the ligand-free form (PDB 5GLI) and in complex with ET-1 (PDB 5GLH,
  2.8 Å resolution) reveal the mechanism of isopeptide selectivity and
agonist-induced activation. ET-1 binds with an ~1,500 Å2 interaction surface -
the largest among peptide-activated GPCRs - with TM1, TM2, TM6, and TM7 enveloping
the entire peptide.


## Publications

### doi/10.1038##nature19319

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5glh">5GLH</a></td>
      <td>2.8 Å</td>
      <td>Not specified</td>
      <td>ETB-Y5-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (thermostabilized with R124Y, D154A, K270A, S342A, I381A mutations; <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> inserted in ICL3; C396A/C400A/C405A; Flag-Nt-TEV site; C-terminus truncated after Ser407)</td>
      <td>Endothelin-1 (ET-1)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5gli">5GLI</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>ETB-Y5-mT4L (thermostabilized; mT4L in ICL3; C-terminal GFP-His10 tag)</td>
      <td>None (ligand-free form)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells using Bac-to-Bac baculovirus expression system
- **Construct**: HA signal peptide-Flag tag-9aa linker-ETB-Y5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) or -mT4L; TEV protease site between Gly57 and Leu66; C-terminus truncated after Ser407

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
      <td>Cell disruption and membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/french-press/">High-pressure homogenizer</a></td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a> + --</td>
      <td>Emulsiflex-C5 homogenization; membranes collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitors</a> + 1% n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 2 h at 4°C; ET-1 added during purification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Bound for 30 min; washed with 10 CV; eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>TEV protease cleavage and tag removal</td>
      <td>TEV cleavage and reverse <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + --</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> (1:20 w/w) overnight; cleaved <a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a>-<a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His10</a> tag removed by <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Peak fractions concentrated to 40 mg/ml for crystallization</td>
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
      <td>ETB-ET1 complex at 40 mg/ml in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> 8:9:1)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled for data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>ET-1-bound structure determined at 2.8 Å resolution. Ligand-free structure from <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">mT4L</a> construct.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5glh">5GLH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGGLAPAEVPKGDRTAGSPPRTISP</span><span class="topo-outside">PPCQGPIEIKETF</span><span class="topo-membrane">KYINTVVSCLVFVLGIIGNSTLLYIIY</span><span class="topo-inside">KN</span><span class="topo-unknown">KCMRN</span><span class="topo-inside">GPNI</span><span class="topo-membrane">LIASLALGDLLHIVIAIPINVYKL</span><span class="topo-outside">LAEDWPFGA</span><span class="topo-membrane">EMCKLVPFIQK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ASVGITVLSLCALSI</span><span class="topo-inside">DRYRAVASW</span><span class="topo-unknown">SRIKGIGVPK</span><span class="topo-inside">WTA</span><span class="topo-membrane">VEIVLIWVVSVVLAVPEAIGF</span><span class="topo-outside">DIITMDYKGSYLRICLLHPVQKT</span><span class="topo-membrane">AFMQFYATAKDWWLFSFYFCLPLAITAFFYT</span><span class="topo-inside">LMTCEMLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLNDHLKQRREVAKT</span><span class="topo-membrane">VFCLVLVFALCWLPLHLARILKLT</span><span class="topo-outside">LYNQNDPNRCELLSFL</span><span class="topo-membrane">LVLDYIGINMASLNSCANPIALYLV</span></span>
<span class="topo-ruler">       490        </span>
<span class="topo-line"><span class="topo-inside">SKRFKNAFKSAL</span><span class="topo-unknown">CCWAQS</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>25</td>
      <td>63</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>38</td>
      <td>88</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>65</td>
      <td>101</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>67</td>
      <td>128</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>72</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>73</td>
      <td>76</td>
      <td>135</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>100</td>
      <td>139</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>163</td>
      <td>171</td>
      <td>Outside</td>
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
      <td>144</td>
      <td>198</td>
      <td>206</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>154</td>
      <td>207</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>155</td>
      <td>157</td>
      <td>217</td>
      <td>219</td>
      <td>Inside</td>
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
      <td>401</td>
      <td>1002</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>402</td>
      <td>415</td>
      <td>311</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>439</td>
      <td>325</td>
      <td>348</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>440</td>
      <td>455</td>
      <td>349</td>
      <td>364</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>480</td>
      <td>365</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>481</td>
      <td>492</td>
      <td>390</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>498</td>
      <td>402</td>
      <td>407</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5glh">5GLH</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20 </span>
<span class="topo-line"><span class="topo-unknown">C</span><span class="topo-outside">SCSSLMDKECVYFCHL</span><span class="topo-unknown">DIIW</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>17</td>
      <td>2</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>21</td>
      <td>18</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5gli">5GLI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGGLAPAEVPKGDRTAGSPPRT</span><span class="topo-inside">ISPPPCQGPIEIKET</span><span class="topo-membrane">FKYINTVVSCLVFVLGIIGNSTLLY</span><span class="topo-outside">IIYKNKCMRNGPNIL</span><span class="topo-membrane">IASLALGDLLHIVIAIPINVYKLL</span><span class="topo-inside">AEDWPFGAE</span><span class="topo-membrane">MCKLVPFIQK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ASVGITVLSLCAL</span><span class="topo-outside">SIDRYRAVASWSRIKGIGVPKWTA</span><span class="topo-membrane">VEIVLIWVVSVVLAVPEAIGF</span><span class="topo-inside">DIITMDYKGSYLRICLLHPVQKTAF</span><span class="topo-membrane">MQFYATAKDWWLFSFYFCLPLAITAF</span><span class="topo-outside">FYTLMTCEMLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-outside">DHLKQRREVAKTVF</span><span class="topo-membrane">CLVLVFALCWLPLHLARILKLTL</span><span class="topo-inside">YNQNDPNRCELLSF</span><span class="topo-membrane">LLVLDYIGINMASLNSCANPIAL</span><span class="topo-outside">YLVS</span><span class="topo-unknown">KRFKNAFKSALC</span><span class="topo-outside">C</span><span class="topo-unknown">WAQSPSSENLYFQ</span></span>
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
      <td>37</td>
      <td>85</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>100</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>77</td>
      <td>125</td>
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
      <td>110</td>
      <td>164</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>133</td>
      <td>173</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>157</td>
      <td>196</td>
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
      <td>203</td>
      <td>241</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>229</td>
      <td>266</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>374</td>
      <td>292</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>397</td>
      <td>327</td>
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
      <td>434</td>
      <td>364</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>438</td>
      <td>387</td>
      <td>390</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>450</td>
      <td>391</td>
      <td>402</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>451</td>
      <td>451</td>
      <td>403</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### ET-1 binds with the largest interaction surface among peptide-activated GPCRs

Endothelin-1 binds to the ETB receptor with an ~1,500 Å2 interaction surface,
the largest observed among peptide-activated GPCRs. The 21-amino-acid bicyclic
peptide is completely enveloped by TM1, TM2, TM6, and TM7. The C-terminal
tripeptide (Ile19-Ile20-Trp21) penetrates deeply into the orthosteric pocket
in a manner similar to small-molecule drug agonists, explaining the virtually
irreversible binding (Kd in the sub-nanomolar range).

### Isopeptide selectivity between ET-1 and ET-3

Structural comparison and mutation analysis reveal the mechanism for isopeptide
selectivity between ET-1 and ET-3. The N-terminal region of the endothelin
peptides modulates interactions at the alpha-helical and C-terminal binding
interfaces. The ET-1-bound structure provides a foundation for understanding
the distinct pharmacological profiles of the three endothelin isopeptides.

### Conformational changes propagate to the G-protein coupling interface

ET-1 binding induces dramatic rearrangements: TM2, TM6, and TM7 move inward
by 2.6, 4.1, and 4.9 Å respectively, while TM1 moves outward by 4.4 Å.
The orthosteric pocket contracts into a compact closed configuration. The
N-terminal tail and ECL2 form a lid-like architecture. These changes propagate
to the receptor core, with TM7 transmitting signals to the cytoplasmic side,
while TM6 appears primed for G-protein engagement.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/etb-receptor-bosentan/">Human Endothelin ETB Receptor Bound to Bosentan</a> — Same ETB receptor bound to clinical antagonist for comparison
- <a href="/xray-mp-wiki/proteins/gpcr/etb-s6b-complex/">Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b</a> — Related ETB receptor structure with snake toxin agonist
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary solubilization detergent
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent for IMAC wash and SEC buffers
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hemisuccinate (CHS)</a> — Additive in purification buffers for receptor stability
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L) fusion</a> — T4L insertion in ICL3 enabled crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used for ETB receptor crystallization
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Receptor expressed in Sf9 insect cells via Bac-to-Bac system
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — ET-1 binding induces conformational changes characteristic of GPCR activation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
