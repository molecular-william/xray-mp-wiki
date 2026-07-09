---
title: "Human Delta-Opioid Receptor (DOP)"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11111, doi/10.1038##nsmb.2965, doi/10.1126##sciadv.aax9115]
verified: regex
uniprot_id: ['P32300', 'P41143']
---

# Human Delta-Opioid Receptor (DOP)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P32300">UniProt: P32300</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41143">UniProt: P41143</a>

<span class="expr-badge">Mus musculus</span>

## Overview

The δ-opioid receptor (DOP) is a class A G protein-coupled receptor (GPCR) that mediates the effects of endogenous enkephalin peptides. DOP is an attractive target for chronic pain treatment due to its anxiolytic and antidepressant-like effects with reduced adverse effects compared to μ-opioid receptor (MOP) agonists. The first crystal structure of the mouse δ-OR was determined at 3.4 Å resolution bound to the subtype-selective antagonist [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) via a T4 lysozyme fusion construct (Granier et al., 2012), revealing the structural basis for the message–address model of opioid pharmacology. This was followed by the first activated-state structures of human DOP bound to the peptide agonist KGCHM07 (2.8 Å resolution) and the small-molecule agonist DPI-287 (3.3 Å resolution), revealing key determinants for agonist recognition, receptor activation, and DOP selectivity. A subsequent XFEL structure of human δ-OR bound to the bifunctional δ-antagonist/μ-agonist tetrapeptide DIPP-NH₂ was determined at 2.73 Å resolution by serial femtosecond crystallography (Fenalti et al., 2015), revealing a cis-peptide bond between H-Dmt and Tic and new molecular determinants of peptide recognition at δ-OR.


## Publications

### doi/10.1038##nature11111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ej4">4EJ4</a></td>
      <td>3.4</td>
      <td></td>
      <td>Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a></td>
    </tr>
  </tbody>
</table>
 - R-work %, R-free %; Data collection: Merged from 20 crystals; GM/CA-CAT beamline 23ID-B, Advanced Photon Source

**Expression:**

- **Expression system**: Baculovirus expression system in Sf9 insect cells using pFastBac vector

- **Construct**: Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag


**Purification:**

- **Expression system**: Sf9 insect cells (Baculovirus)
- **Expression construct**: Mouse δ-OR-T4L fusion (ΔC-term P342, T4L ICL3 insertion)
- **Tag info**: N-terminal Flag tag, C-terminal octa-histidine tag

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
      <td>Cell culture and expression</td>
      <td>Baculovirus infection in Sf9 cells</td>
      <td>—</td>
      <td></td>
      <td>Cells grown to 4×10^6 cells/mL, infected with δ-OR-T4L baculovirus, shaken at 27°C for 48 h, harvested and stored at -80°C. 10 μM naloxone present during expression.</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Osmotic shock</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a>, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> added to block reactive cysteines</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 0.5 M NaCl, 30% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a> + 1.0% lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (MNG), 0.3% sodium cholate, 0.03% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> hemisuccinate (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
      <td>Membranes homogenized with glass dounce homogenizer, mixed at 4°C for 1 h, centrifuged at high speed</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td>0.1% MNG, 0.03% sodium cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 0.5 M NaCl, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a></td>
      <td>Resin washed 3x in batch, eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in washing buffer</td>
    </tr>
    <tr>
      <td>Anti-Flag M1 affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> antibody <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td>0.1% MNG, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a>; salt gradient from 0.5 M to 0.1 M NaCl</td>
      <td>Eluted with 0.2 mg/mL <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide and 2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> in 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 0.1 M NaCl, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a></td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease added at 1:3 <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a>:δ-OR-T4L ratio by weight to remove flexible N and C termini</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic mesophase (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Mouse δ-OR-T4L purified in 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 0.1 M NaCl, 1 μM <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized using the lipidic mesophase technique. Diffraction data collected from 20 crystals and merged for structure solution. Structure solved by molecular replacement at 3.4 Å resolution.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ej4">4EJ4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSPGA</span><span class="topo-inside">RSASSLALAIA</span><span class="topo-membrane">ITALYSAVCAVGLLGNVLVMFGIVR</span><span class="topo-outside">YTKLKTATN</span><span class="topo-membrane">IYIFNLALADALATSTLPFQSA</span><span class="topo-inside">KYLMETWPFG</span><span class="topo-membrane">ELLCKAVLSIDYYNMFTSIFTLTMMSV</span><span class="topo-outside">DRYIAVCHPVK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ALDFRTPAKAK</span><span class="topo-membrane">LINICIWVLASGVGVPIMVMAV</span><span class="topo-inside">TQPRDGAVVC</span><span class="topo-membrane">MLQFPSPSWYWDTVTKICVFLFAFVVPILIITVCYG</span><span class="topo-outside">LMLLRLRSVRNIFEMLRIDEGLRLKIYKNTEGYYTIGIGHL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460 </span>
<span class="topo-line"><span class="topo-outside">FRTGTWDAYEKDRSLRRITR</span><span class="topo-membrane">MVLVVVGAFVVCWAPIHIFVIVWTLV</span><span class="topo-inside">DINRRDPLVVA</span><span class="topo-membrane">ALHLCIALGYANSSLNPVLYAFLD</span><span class="topo-outside">ENFKRC</span><span class="topo-unknown">FRQLCRTPCGRQEP</span></span>
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
      <td>5</td>
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16</td>
      <td>41</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>41</td>
      <td>52</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>50</td>
      <td>77</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>82</td>
      <td>108</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>109</td>
      <td>118</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>131</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>163</td>
      <td>189</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>199</td>
      <td>199</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>209</td>
      <td>235</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>369</td>
      <td>1002</td>
      <td>1161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>380</td>
      <td>251</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>406</td>
      <td>262</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>417</td>
      <td>288</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>441</td>
      <td>299</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>447</td>
      <td>323</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>461</td>
      <td>329</td>
      <td>342</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.2965

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rwd">4RWD</a></td>
      <td>2.73</td>
      <td>P2₁</td>
      <td>BRIL-Δ₃₈δ-OR fusion: residues 1-38 of δ-OR replaced with thermostabilized apocytochrome b562 (<a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a>), C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> of residues 339-372</td>
      <td>DIPP-NH₂ (H-Dmt-Tic-Phe-Phe-NH₂)</td>
    </tr>
  </tbody>
</table>
 - R-work 20.2%, R-free 22.9%; Data collection: Serial femtosecond crystallography (XFEL) at LCLS CXI beamline; 36,083 indexed patterns from 4.6 h collection; CC₁/₂ = 0.538 in highest-resolution shell

**Expression:**

- **Expression system**: Baculovirus expression system in Sf9 insect cells using pFastBac vector

- **Construct**: Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP) for serial femtosecond crystallography (XFEL)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-Δ₃₈δ-OR purified in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1 mM DIPP-NH₂</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (protein:lipid)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> crystals were used for serial femtosecond crystallography at the LCLS CXI beamline. Crystals were injected using an <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> injector. 4.6 h collection yielded 36,083 indexed patterns. Structure determined by molecular replacement using naltindole-bound δ-OR as search model. Two structures determined: XFEL structure at 2.73 Å and synchrotron structure at 3.0 Å; both highly similar (rmsd 0.5 Å).
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rwd">4RWD</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTM</span><span class="topo-outside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGARSASSL</span><span class="topo-membrane">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAIAITALYSAVCAVGLLGNVLVMF</span><span class="topo-inside">GIVRYTKMKTAT</span><span class="topo-membrane">NIYIFNLALADALATSTLPFQSAKYL</span><span class="topo-outside">METWP</span><span class="topo-membrane">FGELLCKAVLSIDYYNMFTSIFTLTMMSVDRY</span><span class="topo-inside">IAVCH</span><span class="topo-unknown">PVKALDF</span><span class="topo-inside">RTPA</span><span class="topo-membrane">KAKL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">INICIWVLASGVGVPIMV</span><span class="topo-outside">MAVTRPRDGAVVCMLQFPSPSWYWDTV</span><span class="topo-membrane">TKICVFLFAFVVPILIITVCYGL</span><span class="topo-inside">MLLRLRSVRLLSGSKEKDRSLRRITRM</span><span class="topo-membrane">VLVVVGAFVVCWAPIHIFVIVW</span><span class="topo-outside">TLV</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-outside">DIDRRDPL</span><span class="topo-membrane">VVAALHLCIALGYANSSLNPVLY</span><span class="topo-inside">AFLD</span><span class="topo-unknown">ENFKRCFRQL</span><span class="topo-inside">C</span><span class="topo-unknown">RKPCG</span></span>
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
      <td>6</td>
      <td>119</td>
      <td>1001</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>145</td>
      <td>47</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>157</td>
      <td>73</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>183</td>
      <td>85</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>188</td>
      <td>111</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>220</td>
      <td>116</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>225</td>
      <td>148</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>232</td>
      <td>153</td>
      <td>159</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>236</td>
      <td>160</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>258</td>
      <td>164</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>285</td>
      <td>186</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>308</td>
      <td>213</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>335</td>
      <td>236</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>357</td>
      <td>263</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>368</td>
      <td>285</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>391</td>
      <td>296</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>395</td>
      <td>319</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>405</td>
      <td>323</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>406</td>
      <td>406</td>
      <td>333</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rwd">4RWD</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTM</span><span class="topo-outside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGARSASSLA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LAI</span><span class="topo-membrane">AITALYSAVCAVGLLGNVLVMFGIVRY</span><span class="topo-inside">TKM</span><span class="topo-membrane">KTATNIYIFNLALADALATSTLPFQS</span><span class="topo-outside">AKYLMETWPFGELLCKA</span><span class="topo-membrane">VLSIDYYNMFTSIFTLTMMSVDRYIA</span><span class="topo-inside">VCH</span><span class="topo-unknown">PVKALD</span><span class="topo-membrane">FRTPAKAKL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">INICIWVLASGVGV</span><span class="topo-outside">PIMVMAVTRPRDGAVVCMLQFPSPSWYWDTVTK</span><span class="topo-membrane">ICVFLFAFVVPILIITVCYGLML</span><span class="topo-inside">LRLRSVRLLSGSKEKDRSLRRI</span><span class="topo-membrane">TRMVLVVVGAFVVCWAPIHIFVI</span><span class="topo-outside">VWTLV</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-outside">DIDRRDPLVVA</span><span class="topo-membrane">ALHLCIALGYANSSLNPVLYAFLD</span><span class="topo-unknown">ENFKRCFRQ</span><span class="topo-inside">L</span><span class="topo-unknown">CRKPCG</span></span>
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
      <td>6</td>
      <td>123</td>
      <td>1001</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>150</td>
      <td>51</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>153</td>
      <td>78</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>179</td>
      <td>81</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>196</td>
      <td>107</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>222</td>
      <td>124</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>225</td>
      <td>150</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>231</td>
      <td>153</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>254</td>
      <td>159</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>287</td>
      <td>182</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>238</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>355</td>
      <td>260</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>283</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>395</td>
      <td>299</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>404</td>
      <td>323</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>405</td>
      <td>332</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.aax9115

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6pt2">6PT2</a></td>
      <td>2.8</td>
      <td></td>
      <td>BRIL-DOP fusion: residues 1-40 of DOP replaced with thermostabilized apocytochrome b562 (<a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a>), C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> of residues 339-372, with sodium pocket mutations N90S, D95G, N131S</td>
      <td>KGCHM07</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6pt2">6PT2</a></td>
      <td>3.3</td>
      <td></td>
      <td>BRIL-DOP fusion: residues 1-40 of DOP replaced with thermostabilized apocytochrome b562 (<a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a>), C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> of residues 339-372, with sodium pocket mutations N90S, D95G, N131S</td>
      <td>DPI-287</td>
    </tr>
  </tbody>
</table>
 - R-work %, R-free %; Data collection: 
 - R-work %, R-free %; Data collection: 

**Expression:**

- **Expression system**: Baculovirus expression system in Sf9 insect cells using pFastBac vector

- **Construct**: Mouse δ-OR-T4L fusion: TEV site after residue 35, C-term [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) after P342, T4L residues 2-161 inserted in ICL3 between residues 244 and 251, N-terminal Flag tag, C-terminal octa-histidine tag


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-DOP bound to KGCHM07 or DPI-287 in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM NaCl, 2% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein with 10% (w/w) cholesterol</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (protein:lipid)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-DOP-KGCHM07: 27-32% <a href="/xray-mp-wiki/reagents/additives/peg-400/">Peg 400</a>, 100-120 mM potassium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0, crystals ~70 μm. <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-DOP-DPI-287: 32-35% <a href="/xray-mp-wiki/reagents/additives/peg-400/">Peg 400</a>, 100-110 mM potassium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0, crystals 100-140 μm. Both crystallized at 20°C. Crystals appeared overnight, full size in ~10 days. 20 μM BMS986187 (PAM) added during DPI-287 purification but no electron density observed.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6pt2">6PT2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAKLQTMHHHHHHHHHHENLYFQGGT</span><span class="topo-outside">TMADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLRSASSLALAIA</span><span class="topo-membrane">ITALYSAVCAVGLLGNVLVMFVIVRYTKM</span><span class="topo-inside">KTAT</span><span class="topo-membrane">NIYIFSLALAGALATSTLPFQS</span><span class="topo-outside">ADYLMETWPFGEL</span><span class="topo-membrane">LCKAV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LSIDYYSMFTSIFTLTMMCVD</span><span class="topo-inside">RYIAVCHPVKALDFRTPAKA</span><span class="topo-membrane">KLINICIWVLASGVGVPIMVMA</span><span class="topo-outside">VTRPRDGAVVCMLQFPSPSWY</span><span class="topo-membrane">WDTVTKICVFLFAFVVPILIITVCYG</span><span class="topo-inside">LMLLRLRSVR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450    </span>
<span class="topo-line"><span class="topo-inside">LLSGSKEKDRSLRRIT</span><span class="topo-membrane">RMVLVVVVAFVVCWAPIHIFVIVWTL</span><span class="topo-outside">VDIDRRDPLVVA</span><span class="topo-membrane">ALHLCIALGYINSSLNPVLYAFLD</span><span class="topo-unknown">KNFKRC</span><span class="topo-inside">F</span><span class="topo-unknown">RQLCRKPCG</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>49</td>
      <td>167</td>
      <td>999</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>196</td>
      <td>52</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>200</td>
      <td>81</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>222</td>
      <td>85</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>235</td>
      <td>107</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>261</td>
      <td>120</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>281</td>
      <td>146</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>303</td>
      <td>166</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>324</td>
      <td>188</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>350</td>
      <td>209</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>376</td>
      <td>235</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>402</td>
      <td>261</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>414</td>
      <td>287</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>438</td>
      <td>299</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>444</td>
      <td>323</td>
      <td>328</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>445</td>
      <td>445</td>
      <td>329</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6pt2">6PT2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAKLQTMHHHHHHHHHHENLYFQGGT</span><span class="topo-outside">TMADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">QIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLRSASSLALAIA</span><span class="topo-membrane">ITALYSAVCAVGLLGNVLVMFVIVRYTKM</span><span class="topo-inside">KTAT</span><span class="topo-membrane">NIYIFSLALAGALATSTLPFQS</span><span class="topo-outside">ADYLMETWPFGEL</span><span class="topo-membrane">LCKAV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LSIDYYSMFTSIFTLTMMCVD</span><span class="topo-inside">RYIAVCHPVKALDFRTPAKA</span><span class="topo-membrane">KLINICIWVLASGVGVPIMVMA</span><span class="topo-outside">VTRPRDGAVVCMLQFPSPSWY</span><span class="topo-membrane">WDTVTKICVFLFAFVVPILIITVCYG</span><span class="topo-inside">LMLLRLRSVR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450    </span>
<span class="topo-line"><span class="topo-inside">LLSGSKEKDRSLRRIT</span><span class="topo-membrane">RMVLVVVVAFVVCWAPIHIFVIVWTL</span><span class="topo-outside">VDIDRRDPLVVA</span><span class="topo-membrane">ALHLCIALGYINSSLNPVLYAFLD</span><span class="topo-unknown">KNFKRC</span><span class="topo-inside">F</span><span class="topo-unknown">RQLCRKPCG</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>49</td>
      <td>167</td>
      <td>999</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>196</td>
      <td>52</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>200</td>
      <td>81</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>222</td>
      <td>85</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>235</td>
      <td>107</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>261</td>
      <td>120</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>281</td>
      <td>146</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>303</td>
      <td>166</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>324</td>
      <td>188</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>350</td>
      <td>209</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>376</td>
      <td>235</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>402</td>
      <td>261</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>414</td>
      <td>287</td>
      <td>298</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>438</td>
      <td>299</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>444</td>
      <td>323</td>
      <td>328</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>445</td>
      <td>445</td>
      <td>329</td>
      <td>329</td>
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

### Message–Address Model of Opioid Pharmacology Validated Structurally

The δ-OR structure validates the message–address concept of opioid pharmacology, where the ligand contains distinct 'message' (efficacy) and 'address' (selectivity) determinants. The lower part of the binding pocket is highly conserved among opioid receptors and interacts with the morphinan core (message). The upper part contains divergent residues that confer subtype selectivity (address). Comparison with μ-OR and κ-OR structures reveals that residue 7.35 is a key selectivity determinant: L300^7.35 in δ-OR accommodates naltrindole's indole group, while W318^7.35 in μ-OR and Y312^7.35 in κ-OR are sterically incompatible. This structural organization of distinct message and address regions may extend to other GPCR families, analogous to the allosteric site in muscarinic receptors.

### Naltrindole Binding and Selectivity

[Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) binds in a deep but solvent-exposed binding pocket in the δ-OR. The ligand forms key interactions including a salt bridge with D128^3.32 and contacts with H278^6.52, W274^6.48, W284^6.58, and L300^7.35. The high δ-OR selectivity of [Naltrindole](/xray-mp-wiki/reagents/ligands/naltrindole/) is primarily determined by L300^7.35, which accommodates the indole group while the larger W318 in μ-OR and Y312 in κ-OR create steric incompatibility. ECL2 contains a conserved β-hairpin across all opioid receptors despite low sequence identity.

### Activation-related conformational changes

Agonist-bound DOP displays large outward movements of intracellular parts of helices V (4.5 Å) and VI (9.4-11.2 Å) and a 3.9 Å inward movement of helix VII. The P-I-F motif (P225^5.50, I136^3.40, F270^6.44) shows characteristic rearrangements with F270 rotating ~3.5 Å toward helix V. Collapse of the sodium-binding pocket is observed with N314^7.49 shifting ~3.5 Å inward. The DRY motif was the only microswitch not predicted to be fully active by the GAUGE machine learning tool.

### Sodium pocket mutations enable thermostabilization

Three mutations in the sodium-binding pocket (N90^2.45S, D95^2.50G, N131^3.35S) facilitate sodium expulsion and pocket collapse, stabilizing the active-like state. The crystal construct shows constitutive G protein signaling activity. Reversing D95^2.50G (G95^2.50D) restores both cAMP and β-arrestin2 signaling.

### Common denominator for opioid receptor activation

A basic, protonated nitrogen forming a salt bridge to D128^3.32 is a hallmark of opioid receptor activation. Agonists extend deeper into the binding pocket compared to structurally similar antagonists, with rearrangements in the polar network around D128^3.32 serving as common denominators for opioid receptor activation.

### DOP agonist selectivity determinants

For the peptide KGCHM07, a 125° rotation of W284^6.58 opens a hydrophobic pocket harboring the bistrifluoromethylated benzyl moiety. R291^ECL3 becomes accessible during activation, likely playing a role in DOP-selective peptide binding. For small-molecule DPI-287 (~10-fold DOP-selective over MOP), the N,N-diethylbenzamide moiety interacts with nonconserved extracellular ends of helices VI and VII, providing structural basis for DOP selectivity.

### Bifunctional Peptide Recognition at δ-OR

The DIPP-NH₂ tetrapeptide (H-Dmt-Tic-Phe-Phe-NH₂) binds δ-OR with a cis-peptide bond between H-Dmt and Tic, revealing peptide-specific recognition determinants distinct from morphinan or peptidomimetic ligands. The Dmt residue reaches deep into the receptor core, while Phe4 sits at the extracellular entrance interacting with ECL2. DIPP-NH₂ binding induces expansion of the orthosteric site through outward movements of TM helices II and VI (1.1 Å increase) and ECL2 (~2 Å). The Phe3 side chain shields the salt bridge between the N-terminal amine and D128^3.32 from solvent. The Tic scaffold is critical for the bifunctional δ-antagonist/μ-agonist profile, and superimposition with μ-OR reveals a clash between Tic and μ-OR Trp318, explaining subtype selectivity.

### XFEL structure determination at δ-OR

The δ-OR-DIPP-NH₂ structure was determined by serial femtosecond crystallography (SFX) using an X-ray free-electron laser (XFEL) at LCLS. Crystals grown in LCP were injected as a microjet using an LCP injector. 36,083 indexed patterns were collected in 4.6 hours, yielding a 2.73 Å structure (CC₁/₂ = 0.538 in highest-resolution shell). This was one of the first GPCR structures solved by SFX, demonstrating the viability of room-temperature serial crystallography for membrane protein structure determination with minimal radiation damage.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/naltrindole/">Naltrindole</a> — Subtype-selective antagonist co-crystallized with mouse δ-OR in the first δ-OR structure
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme</a> — T4L fusion inserted in ICL3 enabled crystallization of mouse δ-OR
- <a href="/xray-mp-wiki/proteins/gpcr/mu-opioid-receptor/">Murine Mu-Opioid Receptor</a> — Classical opioid receptor family member; message-address model comparison
- <a href="/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/">Kappa Opioid Receptor</a> — Classical opioid receptor family member; message-address model comparison
- <a href="/xray-mp-wiki/reagents/ligands/beta-fna/">beta-FNA</a> — Covalent morphinan ligand bound to μ-OR used for structural comparison
- <a href="/xray-mp-wiki/reagents/ligands/jdtc/">JDTic</a> — KOR-selective antagonist used for structural comparison across opioid subtypes
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL Fusion Protein</a> — Alternative fusion partner used in later human DOP active-state structures; also used in the DIPP-NH₂ XFEL structure
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — In meso crystallization method used for δ-OR structure determination including the XFEL DIPP-NH₂ structure
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Truncation</a> — Referenced in context related to Truncation
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in context related to Tris Hcl
