---
title: "GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, gpcr, membrane-protein]
sources: [doi/10.1126##scisignal.ado8741]
verified: agent
uniprot_id: ['P46095', 'P59768', 'P62873', 'P63092']
---

# GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P46095">UniProt: P46095</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P59768">UniProt: P59768</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P62873">UniProt: P62873</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63092">UniProt: P63092</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

GPR6 is an orphan class A G protein-coupled receptor belonging to the MECA cluster
(Melanocortin/EDG/Cannabinoid/Adenosine) that exhibits one of the highest levels of
constitutive activity among GPCRs. It is primarily expressed in the CNS, highly
selectively enriched in [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) D2 receptor-expressing medium spiny neurons (MSNs)
in the striatum, and implicated in Parkinson's disease (PD). Multiple structures were
determined: a pseudo-apo state (2.1 Å, PDB 8TF5) showing a lipid-like density in the
orthosteric pocket stabilizing an active-like conformation; two inverse agonist-bound
inactive structures (GPR6-3h at 2.6 Å, PDB 8T1V; GPR6-CVN424 at 3.5 Å, PDB 8T1W);
and a cryo-EM structure of the fully active GPR6-Gs signaling complex (3.3 Å, PDB 8TYW,
EMDB EMD-41729). The GPR6-selective inverse agonist CVN424 improved motor symptoms in
PD patients in a recent phase II clinical trial (NCT04191577). The structures reveal
that constitutive activity may be driven by an endogenous lipid-like ligand rather than
intrinsic conformational preference of the protein itself.


## Publications

### doi/10.1126##scisignal.ado8741

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8tf5">8TF5</a></td>
      <td>2.10</td>
      <td>Orthorhombic</td>
      <td>GPR6-CC pseudo-apo (no ligand added)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8t1v">8T1V</a></td>
      <td>2.60</td>
      <td>—</td>
      <td>GPR6-CC in complex with IAG 3h</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8t1w">8T1W</a></td>
      <td>3.50</td>
      <td>—</td>
      <td>GPR6-CC in complex with CVN424 (clinical inverse agonist)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8tyw">8TYW</a></td>
      <td>3.30</td>
      <td>—</td>
      <td>Wild-type GPR6 in complex with Gs heterotrimer and <a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a> <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus system); HEK293 mammalian cells for select constructs
- **Construct**: Human GPR6 (UniProt P46095) N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) Δ1-47, ICL3 replaced with bRIL, 6 point mutations (C123L, A173P, G279R, S291C, Y320L, C345D) for crystallization
- **Notes**: For [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/), wild-type GPR6 co-expressed with dominant-negative Gαs and Gβ1γ2

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: GPR6-CC (crystallization construct with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion and 6 point mutations)

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
      <td>Hypotonic lysis and high osmotic washes (1.0 M NaCl)</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 2.5 h at 4°C</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> IMAC resin, gradient <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> elution</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GPR6-CC at 30-40 mg/mL in complex with IAG ligands or apo</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-7 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP mix: 40% receptor solution, 54% <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>, 6% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a>. Crystals harvested using 100 µm dual thickness micromounts. Data collected at APS GM/CA beamline at 1.0332 Å wavelength.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8tf5">8TF5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAGGANGSLELSSQLSAGPPGLLL</span><span class="topo-outside">PAVNP</span><span class="topo-membrane">WDVLLCVSGTVIAGENALVVALIAS</span><span class="topo-inside">TPALRTPMFV</span><span class="topo-membrane">LVGSLATADLLAGLGLILHFVFQYLV</span><span class="topo-outside">PSET</span><span class="topo-membrane">VSLLTVGFLVAS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FAASVSSLLAITV</span><span class="topo-inside">DRYLSLYNPLTYYSRRTLLGV</span><span class="topo-membrane">HLLLAATWTVSLGLGLLPVLGWN</span><span class="topo-outside">CLAERAACS</span><span class="topo-membrane">VVRPLARSHVALLSAAFFMVFGIMLHLYV</span><span class="topo-inside">RICQVVWRHAADLEDNWETLNDNLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VIEKADNAAQVKDALTKMRAAALDAQKATPPKLE</span><span class="topo-unknown">DKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYL</span><span class="topo-unknown">A</span><span class="topo-inside">HLAATRKGVR</span><span class="topo-membrane">TLAVVLGTFGACWLPFAI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430      </span>
<span class="topo-line"><span class="topo-membrane">YCVVGS</span><span class="topo-outside">HEDPA</span><span class="topo-membrane">VYTYATLLPATLNSMINPIIYAFR</span><span class="topo-inside">NQEIQRALWLLLDGC</span><span class="topo-unknown">FQSKVPFRSRSPSEVEFHHHHHHHHH</span></span>
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
      <td>38</td>
      <td>32</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>43</td>
      <td>70</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>78</td>
      <td>100</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>104</td>
      <td>110</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>108</td>
      <td>136</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>140</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>165</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>177</td>
      <td>186</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>186</td>
      <td>209</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>215</td>
      <td>218</td>
      <td>246</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>225</td>
      <td>247</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>274</td>
      <td>1001</td>
      <td>1049</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>282</td>
      <td>1050</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>283</td>
      <td>331</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>342</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>366</td>
      <td>280</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>371</td>
      <td>304</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>395</td>
      <td>309</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>410</td>
      <td>333</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>436</td>
      <td>348</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8t1v">8T1V</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAGRAGGANGSLELSSQLSAGPPGL</span><span class="topo-outside">LLPAVN</span><span class="topo-membrane">PWDVLLCVSGTVIAGENALVVALIAS</span><span class="topo-inside">TPALRTP</span><span class="topo-membrane">MFVLVGSLATADLLAGLGLILHFVF</span><span class="topo-outside">QYLVPSETV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SLLTVGFLVASFAASVSSLLAITVD</span><span class="topo-inside">RYLSLYNPLTYYSRRTLL</span><span class="topo-membrane">GVHLLLAATWTVSLGLGLLPVLGW</span><span class="topo-outside">NCLAERAACSVVRPL</span><span class="topo-membrane">ARSHVALLSAAFFMVFGIMLHLYVR</span><span class="topo-inside">ICQVVWRHAADLE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATP</span><span class="topo-unknown">PKLEDKSPDSPEMKDFRHGF</span><span class="topo-inside">DILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYL</span><span class="topo-unknown">A</span><span class="topo-inside">HLAATRKGVR</span><span class="topo-membrane">TLAVVLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">TFGACWLPFAIYCVVG</span><span class="topo-outside">SHEDPAV</span><span class="topo-membrane">YTYATLLPATLNSMINPIIYAFR</span><span class="topo-inside">NQEIQRALWLLLDG</span><span class="topo-unknown">CFQSKVPFRSRSPSEVEFLEVLFQGPHHHHHHHHH</span></span>
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
      <td>47</td>
      <td>21</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>68</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>79</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>86</td>
      <td>100</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>111</td>
      <td>107</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>120</td>
      <td>132</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>145</td>
      <td>141</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>163</td>
      <td>166</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>187</td>
      <td>184</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>202</td>
      <td>208</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>227</td>
      <td>223</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>236</td>
      <td>248</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>281</td>
      <td>1001</td>
      <td>1045</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>301</td>
      <td>1046</td>
      <td>1065</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>342</td>
      <td>1066</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>353</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>376</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>383</td>
      <td>303</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>406</td>
      <td>310</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>420</td>
      <td>333</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>455</td>
      <td>347</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8t1w">8T1W</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAGRAGGANGSLELSSQLSAGPPGLL</span><span class="topo-outside">LPAVNPW</span><span class="topo-membrane">DVLLCVSGTVIAGENALVVALIAST</span><span class="topo-inside">PALRTP</span><span class="topo-membrane">MFVLVGSLATADLLAGLGLILHFV</span><span class="topo-outside">FQYLVPSETV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SLL</span><span class="topo-membrane">TVGFLVASFAASVSSLLAITVDRY</span><span class="topo-inside">LSLYNPLTYYSRRTL</span><span class="topo-membrane">LGVHLLLAATWTVSLGLGLLPVL</span><span class="topo-outside">GWNCLAERAACSVVRPLARS</span><span class="topo-membrane">HVALLSAAFFMVFGIMLHLYVRI</span><span class="topo-inside">CQVVWRHAADLE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPP</span><span class="topo-unknown">KLEDKSPDSPEMKDFR</span><span class="topo-inside">HGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYL</span><span class="topo-unknown">A</span><span class="topo-inside">HLAATRKGV</span><span class="topo-membrane">RTLAVVLG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-membrane">TFGACWLPFAIYCVV</span><span class="topo-outside">GSHEDPAVY</span><span class="topo-membrane">TYATLLPATLNSMINPIIYAFRN</span><span class="topo-inside">QEIQRALWLLLDGC</span><span class="topo-unknown">FQSKVPFRSRSPSEVEFLEVLFQGPHHHHHHHHH</span></span>
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
      <td>48</td>
      <td>21</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>49</td>
      <td>55</td>
      <td>69</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>80</td>
      <td>76</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>101</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>110</td>
      <td>107</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>123</td>
      <td>131</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>147</td>
      <td>144</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>162</td>
      <td>168</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>183</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>205</td>
      <td>206</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>228</td>
      <td>226</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>236</td>
      <td>249</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>282</td>
      <td>1001</td>
      <td>1046</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>298</td>
      <td>1047</td>
      <td>1062</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>299</td>
      <td>342</td>
      <td>1063</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>352</td>
      <td>270</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>375</td>
      <td>279</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>384</td>
      <td>302</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>407</td>
      <td>311</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>421</td>
      <td>334</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>455</td>
      <td>348</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8tyw">8TYW</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNASAASLNDSQVVVVAAEGAAAAATAAGGPDTGEWGPPAAAALGAGGGANGSLELSSQLSAGPPGLLLPA</span><span class="topo-inside">VNP</span><span class="topo-membrane">WDVLLCVSGTVIAGENALVVALIAS</span><span class="topo-outside">TPALRTPMF</span><span class="topo-membrane">VLVGSLATADLL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AGCGLILHFVFQ</span><span class="topo-inside">YLVPSET</span><span class="topo-membrane">VSLLTVGFLVASFAASVSSLLAITV</span><span class="topo-outside">DRYLSLYNALTYYSRRTLLGV</span><span class="topo-membrane">HLLLAATWTVSLGLGLLPVLGWNC</span><span class="topo-inside">LAERAAC</span><span class="topo-membrane">SVVRPLARSHVALLSAAFFMVFGI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">MLHLY</span><span class="topo-outside">VRICQVVWRHAHQIALQQH</span><span class="topo-unknown">CLAPPHLAA</span><span class="topo-outside">TRKGV</span><span class="topo-membrane">GTLAVVLGTFGASWLPFAIYCVVGS</span><span class="topo-inside">HEDPA</span><span class="topo-membrane">VYTYATLLPATYNSMINPIIYAFR</span><span class="topo-outside">NQEIQRALWLLL</span><span class="topo-unknown">CGCFQSKVPFRSRSPS</span></span>
<span class="topo-ruler">       370  </span>
<span class="topo-line"><span class="topo-unknown">EVHHHHHHHHHH</span></span>
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
      <td>71</td>
      <td>1</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>74</td>
      <td>72</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>99</td>
      <td>75</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>108</td>
      <td>100</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>132</td>
      <td>109</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>139</td>
      <td>133</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>164</td>
      <td>140</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>185</td>
      <td>165</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>209</td>
      <td>186</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>216</td>
      <td>210</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>245</td>
      <td>217</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>264</td>
      <td>246</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>273</td>
      <td>265</td>
      <td>273</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>274</td>
      <td>278</td>
      <td>274</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>303</td>
      <td>279</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>308</td>
      <td>304</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>332</td>
      <td>309</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>344</td>
      <td>333</td>
      <td>344</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>372</td>
      <td>345</td>
      <td>372</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8tyw">8TYW</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHGSSG</span><span class="topo-outside">SELDQLRQEAEQLKNQIRDARKACADATLSQITNNIDPVGRIQMRTRRTLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YVACGGLDNICSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALWDIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDIN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350</span>
<span class="topo-line"><span class="topo-outside">AICFFPNGNAFATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGYDDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
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
      <td>11</td>
      <td>-9</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>350</td>
      <td>2</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8tyw">8TYW</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGCLGNS</span><span class="topo-outside">KTEDQRNEEKAQREANKKIEKQLQKDKQVYRATHRLLLLG</span><span class="topo-unknown">AGE</span><span class="topo-outside">SGKNTIVKQMRIL</span><span class="topo-unknown">LVNGFNGEGGEEDPQAARSNSDGEKATKVQDIKNNLKEAIETIVAAMSNLVPPVELA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">NPENQFRVDYILSVMNVPDFDFPPEFYEHAKALWEDEGVRACYERSNEYQLIDCAQYFLDKIDVIKQADYVPSDQDLLRCRVLH</span><span class="topo-outside">TSGIFETKFQVDKVNFHMFDVGAQRDERRKWIQCFN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DVTAIIFVVASSSY</span><span class="topo-unknown">NMVIREDN</span><span class="topo-outside">QTNRLQAALKLFDSIWNNKWLRDTSVILFLNKQDLLAEKVLAGKSKIEDYFPEFARYTTPEDATPEPGEDPRVTRAKYFIRDEFLRISTASGDGRHYC</span></span>
<span class="topo-ruler">       370       380       390     </span>
<span class="topo-line"><span class="topo-outside">YPHFTCAVDTENIRRVFNDCRDIIQRMHLRQYELL</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>47</td>
      <td>8</td>
      <td>47</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>50</td>
      <td>48</td>
      <td>50</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>63</td>
      <td>51</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>254</td>
      <td>204</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>262</td>
      <td>254</td>
      <td>261</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>263</td>
      <td>395</td>
      <td>262</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8tyw">8TYW</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70 </span>
<span class="topo-line"><span class="topo-unknown">MASN</span><span class="topo-outside">NTASIAQARKLVEQLKMEANIDRIKVSKAAADLMAYCEAHAKEDPLLTPVPASENPFR</span><span class="topo-unknown">EKKFFCAIL</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>62</td>
      <td>5</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>71</td>
      <td>63</td>
      <td>71</td>
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

### High constitutive activity driven by endogenous lipid

The pseudo-apo GPR6 structure shows a lipid-like density in the orthosteric
pocket stabilizing an active-like conformation. Extensive experiments including
native mass spectrometry, lipidomics, MD simulations, and docking suggest the
ligand may be a single-chain lipid (tentatively OLA). Markov State Model
simulations of the apo receptor show 83% preference for the inactive state,
suggesting constitutive activity is driven by the bound lipid rather than
intrinsic protein dynamics.

### Phe152 as a conformational switch

Phe152(3.36) acts as a key molecular switch between inactive and active
states. Inverse agonists lock Phe152 in its inactive conformation where it
π-stacks with Trp292(6.48) and Phe234(5.47). The lipid agonist stabilizes
the active conformation of Phe152, releasing TM5 and TM6 for activation
motions. In the absence of ligands, Phe152 oscillates between both
conformations.

### CVN424 clinical inverse agonist

CVN424 is a potent and selective GPR6 inverse agonist that completed a
phase II clinical trial (NCT04191577) showing improvement of motor symptoms
in PD patients. The co-crystal structure reveals CVN424 binds in the
orthosteric pocket with a single hydrogen bond to Thr319(7.43) and
hydrophobic/π-stacking interactions with residues including His128(2.60),
Phe152(3.36), Phe295(6.51), and Leu315(7.39). GPR6 inhibition represents a
non-dopaminergic therapeutic strategy for PD treatment.

### Lipid entry pathway from membrane

The active-like pseudo-apo structure reveals a continuous channel from the
orthosteric pocket to the lipid bilayer through an opening framed by TM3-TM5.
This opening is gated by Phe152(3.36) and allows lipid agonists to enter
directly from the membrane. This transmembrane entry is closed in most other
MECA cluster receptors but open in the active-like GPR6 conformation,
suggesting a unique access mechanism.

### G protein coupling interface

The [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of the GPR6-Gs complex shows a canonical GPCR-Gs
interface. TM6 undergoes 8.2 Å outward movement from the inactive state.
The α5 helix of Gαs inserts into the cytoplasmic cavity, with Arg166(3.50)
forming a π-cation interaction with Tyr391 of Gαs. Additional interactions
involve Arg332(7.56) and Thr280(6.36) with Gαs residues, and ICL1/ICL2
interactions with Gβ and the αN helix of Gαs.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/dopamine/">Dopamine</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo Em</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in gpr6 text
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Referenced in gpr6 text
