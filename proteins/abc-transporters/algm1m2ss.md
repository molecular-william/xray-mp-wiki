---
title: "AlgM1M2SS Alginate ABC Transporter"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2015.06.021]
verified: false
---

# AlgM1M2SS Alginate ABC Transporter

## Overview

AlgM1M2SS is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) importer from the [Alginate](/xray-mp-wiki/reagents/ligands/alginate/)-assimilating bacterium Sphingomonas sp. A1, responsible for the import of the acidic polysaccharide [Alginate](/xray-mp-wiki/reagents/ligands/alginate/) across the cytoplasmic membrane. The transporter comprises two transmembrane subunits (AlgM1 and AlgM2) forming a heterodimer and two nucleotide-binding domains (homodimer of AlgS). It belongs to the type I ABC importer family. The crystal structure of the AlgM1M2SS/AlgQ2 complex reveals an inward-facing conformation with a tunnel-like structure at the interface between the periplasmic binding protein AlgQ2 and the transmembrane domains, facilitating [Alginate](/xray-mp-wiki/reagents/ligands/alginate/) translocation.

## Publications

### doi/10.1016##j.str.2015.06.021

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a></td>
      <td>3.2</td>
      <td>P212121</td>
      <td>AlgM1(d24)M2(H10)SS(E160Q) in complex with AlgQ2; 24-residue deletion in AlgM1, 10-His tag at C-terminus of AlgM2, E160Q mutation in AlgS</td>
      <td>AlgQ2 (periplasmic binding protein), Delta-MMM (unsaturated <a href="/xray-mp-wiki/reagents/ligands/alginate/">Alginate</a> trisaccharide)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21-Gold(DE3)/pLysS
- **Construct**: AlgM1M2SS with 10-His tag at C-terminus of AlgM2, expressed from pET21b vector; AlgM1(d24) variant with 24-residue N-terminal deletion; AlgS(E160Q) mutant for trapping inward-facing conformation

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
      <td>Overexpression</td>
      <td>E. coli BL21-Gold(DE3)/pLysS transformed with pET21b vector; C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> on AlgM2 produced protein, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> on AlgM1 did not</td>
      <td>--</td>
      <td>LB medium + --</td>
      <td>pET21b vector most suitable for AlgM1M2SS overexpression; C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> on AlgM2 successful, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> on AlgM1 failed</td>
    </tr>
    <tr>
      <td>Solubilization and purification</td>
      <td>Membrane protein solubilized in mixture of <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, <a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a>, and <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a>; purified by <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> and functional reconstitution in liposomes</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 8.0) + <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, <a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a>, <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
      <td>Purified to homogeneity and functionally reconstituted in liposomes for ATPase and transport assays</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>7 mg/ml AlgM1(d24)M2(H10)SS(E160Q), 3 mg/ml AlgQ2, 1 mM Delta-MMM, 3.6 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 16 mM <a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18% <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a>, 0.15 M NaCl, 0.1 M N-(2-acetamido)iminodiacetic acid (pH 6.6)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a> derivative crystallized separately with <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> instead of <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>; binding-protein-free form also crystallized at 4.5 A resolution (P1 space group)</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> (<a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a> derivative)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>7 mg/ml <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a>-AlgM1(d24)M2(H10)SS(WT), 3 mg/ml AlgQ2, 1 mM Delta-MMM, 1.2 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a>, 16 mM <a href="/xray-mp-wiki/reagents/detergents/chapso/">CHAPSO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>18% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>4000, 0.15 M sodium potassium tartrate, 0.1 M N-(2-acetamido)iminodiacetic acid (pH 6.6)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a> derivative used for phasing; structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a>, <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a>, <a href="/xray-mp-wiki/proteins/abc-transporters/malK/">MalK (Escherichia coli Maltose Transporter ATPase Subunit)</a> subunits from PDB 2R6G</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a> — Chain M (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">ERLWKDIKRDWLLY</span><span class="topo-membrane">AMLLPTIIWFLIFLYKPMIGLQM</span><span class="topo-outside">AF</span><span class="topo-unknown">KQYSAWKGIAGS</span><span class="topo-outside">PWIGFDHFVTLFQSEQFIRAI</span><span class="topo-membrane">KNTLTLSGLSLLFGFPMPILLALMI</span><span class="topo-inside">NEVYSKG</span><span class="topo-membrane">YRKAVQTIVYLPHFI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SIVIVA</span><span class="topo-outside">GLVVTFLSPSTGVVNNMLSWIGLDRVYFLTQPEWFR</span><span class="topo-membrane">PIYISSNIWKEAGFDSIVYL</span><span class="topo-inside">AAIMSINPALYESAQVDGATRWQMITRITLPCIVPTI</span><span class="topo-membrane">AVLLVIRLGHILEVGFEY</span><span class="topo-outside">IIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300 </span>
<span class="topo-line"><span class="topo-outside">LYQPTTYETADVISTYIYRLGLQGARYDIAT</span><span class="topo-membrane">AAGIFNAVVALVIVLFANHMS</span><span class="topo-inside">RRITK</span><span class="topo-unknown">TGVF</span></span>
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
      <td>2</td>
      <td>15</td>
      <td>25</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>38</td>
      <td>39</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>40</td>
      <td>62</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>52</td>
      <td>64</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>53</td>
      <td>73</td>
      <td>76</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>98</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>105</td>
      <td>122</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>126</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>162</td>
      <td>150</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>186</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>219</td>
      <td>206</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>237</td>
      <td>243</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>271</td>
      <td>261</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>292</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>297</td>
      <td>316</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>301</td>
      <td>321</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a> — Chain N (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">LATPFYSRSDRIFGI</span><span class="topo-membrane">VNAVLLGIFALCALYPIIYIFS</span><span class="topo-outside">MSISSGAAVTQGRVFLLPVDIDFSAYGRVLHDKLFWTSY</span><span class="topo-membrane">ANTIFYTVFGVVTSLIFIVPGA</span><span class="topo-inside">YALSKPRIRGRRV</span><span class="topo-membrane">FGFIIAFT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MWFNAGMIPFF</span><span class="topo-outside">LNMRDLGLLDN</span><span class="topo-membrane">RFGILIGFACNAFNIILM</span><span class="topo-inside">RNYFESISASFEEAARMDGANDLQILWKVYIPLAKPA</span><span class="topo-membrane">LATITLLCAISRWNGYFWA</span><span class="topo-outside">MVLLRAEEKIPLQVYLKKTIVDLN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300     </span>
<span class="topo-line"><span class="topo-outside">VNEEFAGALLTNSYSMETVVGAII</span><span class="topo-membrane">VMSIIPVIIVYPVVQKYFT</span><span class="topo-unknown">KGVMLGGVKELEHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>2</td>
      <td>16</td>
      <td>2</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>38</td>
      <td>17</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>77</td>
      <td>39</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>99</td>
      <td>78</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>112</td>
      <td>100</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>131</td>
      <td>113</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>142</td>
      <td>132</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>197</td>
      <td>161</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>216</td>
      <td>198</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>264</td>
      <td>217</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>283</td>
      <td>265</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a> — Chain S (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVASVSIQNVVKRYDKTTVVHGVSLDIEPGEFVVLVGPSGCGKSTTLRMVAGLEEISGGTIRIDGRVINDLAPKDRDVAMVFQNYALYPHLNVRDNISFGLRLKRTKKSVIDAAVKTAAD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ILGLQPLLERKPSDLSGGQRQRVAMGRAIVRDPKVFLFDQPLSNLDAKLRTQMRAEIKRLHQRLGTTVIYVTHDQVEAMTLADRIVVMRDGLIEQIGKPMDLFLHPANTFVASFIGSPPM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NLMPARIAVDSTQHVELNGGNRISLLPRAGTHLAPGQEVVFGIRPEDVTLDGVEGSERAQIKATVDIVEPLGSESILHATVGDHSLVVKVGGLNEVHPGDPVTLHVDLTRVHLFDAQSQA</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">SIY</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>363</td>
      <td>1</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a> — Chain Q (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKKMMLSVAAVATLMAFAAPVATA</span><span class="topo-outside">KEATWVTDKPLTLKIHMHFRDKWVWDENWPVAKESFRLTNVKLQSVANKAATNSQEQFNLMMASGDLPDVVGGDNLKDKFIQYGQEGAFVPLNKLI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DQYAPHIKAFFKSHPEVERAIKAPDGNIYFIPYVPDGVVARGYFIREDWLKKLNLKPPQNIDELYTVLKAFKEKDPNGNGKADEVPFIDRHPDEVFRLVNFWGARSSGSDNYMDFYIDNG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RVKHPWAETAFRDGMKHVAQWYKEGLIDKEIFTRKARAREQMFGGNLGGFTHDWFASTMTFNEGLAKTVPGFKLIPIAPPTNSKGQRWEEDSRQKVRPDGWAITVKNKNPVETIKFFDFY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">FSRPGRDISNFGVPGVTYDIKNGKAVFKDSVLKSPQPVNNQLYDMGAQIPIGFWQDYDYERQWTTPEAQAGIDMYVKGKYVMPGFEGVNMTREERAIYDKYWADVRTYMYEMGQAWVMGT</span></span>
<span class="topo-ruler">       490       500       510      </span>
<span class="topo-line"><span class="topo-outside">KDVDKTWDEYQRQLKLRGLYQVLQMMQQAYDRQYKN</span></span>
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
      <td>24</td>
      <td>-23</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>516</td>
      <td>1</td>
      <td>492</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tqu">4TQU</a> — Chain T (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVASVSIQNVVKRYDKTTVVHGVSLDIEPGEFVVLVGPSGCGKSTTLRMVAGLEEISGGTIRIDGRVINDLAPKDRDVAMVFQNYALYPHLNVRDNISFGLRLKRTKKSVIDAAVKTAAD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ILGLQPLLERKPSDLSGGQRQRVAMGRAIVRDPKVFLFDQPLSNLDAKLRTQMRAEIKRLHQRLGTTVIYVTHDQVEAMTLADRIVVMRDGLIEQIGKPMDLFLHPANTFVASFIGSPPM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NLMPARIAVDSTQHVELNGGNRISLLPRAGTHLAPGQEVVFGIRPEDVTLDGVEGSERAQIKATVDIVEPLGSESILHATVGDHSLVVKVGGLNEVHPGDPVTLHVDLTRVHLFDAQSQA</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-inside">SIY</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>363</td>
      <td>1</td>
      <td>363</td>
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

### Inward-facing conformation of AlgM1M2SS

The crystal structure of AlgM1M2SS in complex with AlgQ2 adopts an inward-facing conformation, with AlgM1 and AlgM2 open to the cytoplasm and the [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding sites of the AlgS dimer widely separated. This conformation is similar to the resting state of the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter MalFGK2 without its binding protein MalE. Unlike the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter which undergoes conformational changes upon solute-binding protein interaction, AlgM1M2SS binds AlgQ2 without conformational change, suggesting the ABC transporter in the resting state conformation can bind solute-binding protein directly.

### Tunnel-like alginate translocation route

The interaction between AlgQ2 and AlgM1M2SS induces the formation of an [Alginate](/xray-mp-wiki/reagents/ligands/alginate/)-binding tunnel-like structure accessible to the solvent. The uncovered part of the [Alginate](/xray-mp-wiki/reagents/ligands/alginate/)-binding cleft of AlgQ2 resembles the entrance of a tunnel that continues inside AlgQ2. AlgQ2 accommodates oligoalginate at the back of the tunnel, with a length of approximately 30 A corresponding to [Alginate](/xray-mp-wiki/reagents/ligands/alginate/) heptasaccharides. The tunnel accommodates the non-reducing terminal residue of [Alginate](/xray-mp-wiki/reagents/ligands/alginate/) while other residues extend outward.

### Charged inner cavity for acidic saccharide import

The translocation route inside the transmembrane domains contains charged residues suitable for the import of acidic saccharides. Charged residues in the cavity include AlgM1 Lys195, Glu196, Asp200, Arg249, Glu259, and AlgM2 Arg209. Histidine residues AlgM1 His141 and His252 are also present. Mutagenesis of H141A and E196A decreased both ATPase and transport activities to less than 50%, while E259A, R209A, and E196A/E259A mutants showed transport activities below 40%. This contrasts with the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter, which lacks charged residues in its inner cavity.

### Substrate specificity and transport range

AlgM1M2SS specifically transports oligoalginate trisaccharides to heptasaccharides. ATPase activity is enhanced by poly- and oligoalginate, with the strongest response to tetrasaccharides and longer chains. Transport assays show that oligoalginate up to heptasaccharides can be transported, but polysaccharides longer than heptasaccharides (8-20M and 8-20G) are not transported in the in vitro system. This suggests additional factors such as the [Alginate](/xray-mp-wiki/reagents/ligands/alginate/) concentrator pit on the cell surface may be required for macromolecular transport.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB Multidrug Efflux Pump</a> — AcrB is a related ABC transporter from E. coli, providing comparative framework for ABC transporter structure-function analysis
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM tested for AlgM1M2SS solubilization in ATPase activity assays
- <a href="/xray-mp-wiki/reagents/detergents/chapso/">3-[(3-Cholamidopropyl)dimethylammonio]-1-propanesulfonate (CHAPSO)</a> — CHAPSO used in crystallization sample solution for AlgM1M2SS/AlgQ2 complex
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-Hydroxymethyl-Aminomethane)</a> — Tris-HCl buffer (pH 8.0) used in purification and functional assays
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — ABC transporters operate via alternating-access mechanism between inward and outward facing conformations
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Related protein mentioned in the study
