---
title: "Human MT2 Melatonin Receptor"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1144-0]
verified: pdb-check
uniprot_id: P00268
---

# Human MT2 Melatonin Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P00268">UniProt: P00268</a>

<span class="expr-badge">Clostridium pasteurianum</span>

## Overview

The human MT2 melatonin receptor (type 1B, MTNR1B) is a class A G-protein-coupled receptor (GPCR) that binds the neurohormone melatonin and regulates circadian rhythms, sleep patterns, and has been implicated in type 2 diabetes. X-ray free electron laser (XFEL) structures of MT2 in complex with agonists 2-phenylmelatonin (2-PMT) and ramelteon at 2.8-3.3 Angstrom resolution reveal a conserved orthosteric binding pocket with notable conformational differences from the MT1 subtype despite identical binding site residues. The structures show a membrane-buried lateral ligand entry channel between TM4 and TM5 (more constricted than in MT1) and an additional narrow extracellular loop (ECL) opening towards solvent that is absent in MT1. Kinetic ligand dissociation studies demonstrate the importance of both access routes, with the ECL opening providing a potential path for more polar ligands in MT2. These findings explain melatonin receptor subtype selectivity and enable design of highly selective melatonin tool compounds.


## Publications

### doi/10.1038##s41586-019-1144-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me6">6ME6</a></td>
      <td>2.80</td>
      <td>P2_1</td>
      <td>MT2-CC (<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion, N-term trunc 30 aa, C-term trunc 22 aa, 8 point mutations, rubredoxin in ICL3)</td>
      <td>2-PMT (2-phenylmelatonin)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me7">6ME7</a></td>
      <td>3.20</td>
      <td>P2_1</td>
      <td>MT2-CC(H208A) mutant</td>
      <td>2-PMT (2-phenylmelatonin)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me8">6ME8</a></td>
      <td>3.10</td>
      <td>P2_1</td>
      <td>MT2-CC(N86D) mutant</td>
      <td>2-PMT (2-phenylmelatonin)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6me9">6ME9</a></td>
      <td>3.30</td>
      <td>P2_1</td>
      <td>MT2-CC</td>
      <td>ramelteon</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: MT2-CC (human MT2 with N-terminal 30 aa truncation, C-terminal 22 aa truncation, ICL3 residues 232-240 replaced with rubredoxin fusion; 8 thermostabilizing point mutations: D86N, L108F, F129W, N137D, C140L, W264F, A305P, N312D)
- **Notes**: Bac-to-bac baculovirus expression system; D86N mutation critical for expression and stability

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: MT2-CC
- **Tag info**: N-terminal HA signal + [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) tag; C-terminal PreScission site + 10x His tag

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
      <td>Dounce homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail</td>
      <td>Washed in hypotonic buffer then high-osmotic buffer (1.0 M NaCl) to remove soluble/membrane-associated proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 50 uM ligand (2-PMT or ramelteon) + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> / 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>3 h incubation at 4C</td>
    </tr>
    <tr>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td>Talon resin</td>
      <td>—</td>
      <td></td>
      <td>Overnight binding at 4C; washed with 800 mM NaCl, 10% glycerol, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10-20 mM imidazole</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>)</td>
      <td>—</td>
      <td></td>
      <td>Buffer with 100 mM NaCl, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, ligand</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (lipid cubic phase)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~30 mg/mL MT2-CC in 50 mM HEPES pH 7.5, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> with P2_1 space group; XFEL data collected at LCLS; synchrotron data also used</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me6">6ME6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGK</span><span class="topo-unknown">VKEAQA</span><span class="topo-inside">AAEQLKTTRNAYIQKYLGDGARPSW</span><span class="topo-membrane">VAPALS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AVLIVTTAVDVVGNLLVIL</span><span class="topo-outside">SVLRNRKLRNAGNLF</span><span class="topo-membrane">LVSLALANLVVAFYPYPLILVAI</span><span class="topo-inside">FYDGWAFGEE</span><span class="topo-membrane">HCKASAFVMGLSVIGSVWNITAIAI</span><span class="topo-outside">DRYLYICHSMAYHRIYRRWHTP</span><span class="topo-membrane">LHICLI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">WLLTVVALLPNFFVG</span><span class="topo-inside">SLEYDPRIYSCTFIQTAS</span><span class="topo-membrane">TQYTAAVVVIHFLLPIAVVSFC</span><span class="topo-outside">YLRIWVLVLQARMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-outside">CLKPSDLRSFLTM</span><span class="topo-membrane">FVVFVIFAICFAPLNCIGLAVAIN</span><span class="topo-inside">PQEMAPQIPEG</span><span class="topo-membrane">LFVTSYLLAYFNSCLNPIVYGL</span><span class="topo-outside">LD</span><span class="topo-unknown">QNFRREYKRILLALW</span><span class="topo-outside">N</span><span class="topo-unknown">PRHCIQDASKGS</span></span>
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
      <td>83</td>
      <td>2001</td>
      <td>2083</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>2084</td>
      <td>2089</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>114</td>
      <td>2090</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>139</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>154</td>
      <td>64</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>177</td>
      <td>79</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>187</td>
      <td>102</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>212</td>
      <td>112</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>234</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>255</td>
      <td>159</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>273</td>
      <td>180</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>295</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>373</td>
      <td>220</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>397</td>
      <td>254</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>408</td>
      <td>278</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>430</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>432</td>
      <td>311</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>447</td>
      <td>313</td>
      <td>327</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>448</td>
      <td>448</td>
      <td>328</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me7">6ME7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGK</span><span class="topo-unknown">VKEAQAAAEQLKTTRNA</span><span class="topo-inside">YIQKYLGDGARPSW</span><span class="topo-membrane">VAPALS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AVLIVTTAVDVVGNLLVIL</span><span class="topo-outside">SVLRN</span><span class="topo-unknown">RKLRNAG</span><span class="topo-outside">NL</span><span class="topo-membrane">FLVSLALANLVVAFYPYPLILVAIF</span><span class="topo-inside">YDGWAFGE</span><span class="topo-membrane">EHCKASAFVMGLSVIGSVWNITAIAI</span><span class="topo-outside">DRYLYICHSMAYHRIYRRWHT</span><span class="topo-membrane">PLHICLI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">WLLTVVALLPNFFVG</span><span class="topo-inside">SLEYDPRIYSCTFIQTAS</span><span class="topo-membrane">TQYTAAVVVIAFLLPIAVVSFCYLR</span><span class="topo-outside">IWVLVLQARMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-outside">CLKPSDLRSFL</span><span class="topo-membrane">TMFVVFVIFAICFAPLNCIGLAVAIN</span><span class="topo-inside">PQEMAPQIPEG</span><span class="topo-membrane">LFVTSYLLAYFNSCLNPIVYGLL</span><span class="topo-outside">D</span><span class="topo-unknown">QNFRREYKRILLAL</span><span class="topo-outside">WN</span><span class="topo-unknown">PRHCIQDASKGS</span></span>
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
      <td>83</td>
      <td>2001</td>
      <td>2083</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>2084</td>
      <td>2100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>114</td>
      <td>2101</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>139</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>144</td>
      <td>64</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>151</td>
      <td>69</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>153</td>
      <td>76</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>178</td>
      <td>78</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>186</td>
      <td>103</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>212</td>
      <td>111</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>233</td>
      <td>137</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>255</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>273</td>
      <td>180</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>298</td>
      <td>198</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>371</td>
      <td>223</td>
      <td>251</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>397</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>408</td>
      <td>278</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>431</td>
      <td>289</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>432</td>
      <td>312</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>446</td>
      <td>313</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>447</td>
      <td>448</td>
      <td>327</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me8">6ME8</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGK</span><span class="topo-unknown">VKEAQAAAEQLKTTRNA</span><span class="topo-inside">YIQKYLGDGARPSW</span><span class="topo-membrane">VAPALS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AVLIVTTAVDVVGNLLVIL</span><span class="topo-outside">SVLRNRKLRNAGNLF</span><span class="topo-membrane">LVSLALADLVVAFYPYPLILVAIF</span><span class="topo-inside">YDGWAFGEE</span><span class="topo-membrane">HCKASAFVMGLSVIGSVWNITAIAI</span><span class="topo-outside">DRYLYICHSMAYHRIYRRWHTP</span><span class="topo-membrane">LHICLI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">WLLTVVALLPNFFVG</span><span class="topo-inside">SLEYDPRIYSCTFIQTAS</span><span class="topo-membrane">TQYTAAVVVIHFLLPIAVVSFCYL</span><span class="topo-outside">RIWVLVLQARMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-outside">CLKPSDLRSFLT</span><span class="topo-membrane">MFVVFVIFAICFAPLNCIGLAVAI</span><span class="topo-inside">NPQEMAPQIPEG</span><span class="topo-membrane">LFVTSYLLAYFNSCLNPIVYGLL</span><span class="topo-outside">D</span><span class="topo-unknown">QNFRREYKRILLALW</span><span class="topo-outside">NP</span><span class="topo-unknown">RHCIQDASKGS</span></span>
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
      <td>83</td>
      <td>2001</td>
      <td>2083</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>100</td>
      <td>2084</td>
      <td>2100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>101</td>
      <td>114</td>
      <td>2101</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>139</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>154</td>
      <td>64</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>178</td>
      <td>79</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>187</td>
      <td>103</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>212</td>
      <td>112</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>234</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>255</td>
      <td>159</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>273</td>
      <td>180</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>297</td>
      <td>198</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>372</td>
      <td>222</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>396</td>
      <td>253</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>408</td>
      <td>277</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>431</td>
      <td>289</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>432</td>
      <td>312</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>447</td>
      <td>313</td>
      <td>327</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>448</td>
      <td>449</td>
      <td>328</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6me9">6ME9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGDGARPSW</span><span class="topo-membrane">VAPALS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AVLIVTTAVDVVGNLLVIL</span><span class="topo-outside">SVLRNRKLRNAGNLF</span><span class="topo-membrane">LVSLALANLVVAFYPYPLILV</span><span class="topo-inside">AIFYDGWAFGEE</span><span class="topo-membrane">HCKASAFVMGLSVIGSVWNITAIAI</span><span class="topo-outside">DRYLYICHSMAYHRIYRRWHTP</span><span class="topo-membrane">LHICLI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">WLLTVVALLPNFFV</span><span class="topo-inside">GSLEYDPRIYSCTFIQTAS</span><span class="topo-membrane">TQYTAAVVVIHFLLPIAVVSFC</span><span class="topo-outside">YLRIWVLVLQARMKKYTCTVCGYIYNPEDGDPDNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-outside">CLKPSDLRSFLTM</span><span class="topo-membrane">FVVFVIFAICFAPLNCIGLAVAI</span><span class="topo-inside">NPQEMAPQIPEG</span><span class="topo-membrane">LFVTSYLLAYFNSCLNPIVYGL</span><span class="topo-outside">LD</span><span class="topo-unknown">QNFRREYKRILLALW</span><span class="topo-outside">N</span><span class="topo-unknown">PRHCIQDASKGS</span></span>
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
      <td>1</td>
      <td>114</td>
      <td>2001</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>139</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>154</td>
      <td>64</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>175</td>
      <td>79</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>187</td>
      <td>100</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>212</td>
      <td>112</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>234</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>254</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>273</td>
      <td>179</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>295</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>373</td>
      <td>220</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>396</td>
      <td>254</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>408</td>
      <td>277</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>430</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>432</td>
      <td>311</td>
      <td>312</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>447</td>
      <td>313</td>
      <td>327</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>448</td>
      <td>448</td>
      <td>328</td>
      <td>328</td>
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

### Lateral Ligand Entry Channel

MT2 has a membrane-buried lateral channel between TM4 and TM5 connecting the orthosteric binding site to the lipid bilayer, similar to MT1 but more constricted (~2.6 A diameter). This channel provides the primary access route for lipophilic ligands like melatonin. Mutation of channel-lining residue Y200^5.38A widened the channel and reduced ligand residence time 30-fold, while constricting mutation A171M^4.56 markedly increased residence time to ~20 h.

### Extracellular Loop Opening in MT2

In contrast to MT1, MT2 structures reveal a narrow opening towards solvent in the extracellular part of the receptor, bounded by residues T191^ECL2, Q194^ECL2, and Y294^7.39. The ECL opening provides a potential secondary ligand entry path. Mutations widening this opening (T191A, Q194A, Y294A) reduced ligand residence time 10-22 fold in MT2, while equivalent MT1 mutations had minimal effect.

### Subtype Selectivity Determinants

Despite identical orthosteric binding site residues between MT1 and MT2 (68% sequence identity overall), the binding pocket in MT2 is ~50 A3 (7%) larger, with differences concentrated around the alkylamide tail region and a hydrophobic subpocket. R1 substituents on the melatonin scaffold confer MT1 selectivity, while R2 and R3 substituents confer MT2 selectivity. Docking of selective ligands reveals that the membrane channel in MT1 better accommodates extended R1 alkyl chains, while MT2 selectivity is achieved through interactions in the expanded hydrophobic subpocket.

### Ligand Access Routes and Residence Time

Kinetic [3H]melatonin dissociation studies show substantially longer residence time in wild-type MT2 (koff^-1 >> MT1), consistent with the narrower membrane entry channel. Mutation studies systematically probing both the lateral membrane channel and ECL opening demonstrate functional relevance of both access routes, with the ECL opening playing a more prominent role in MT2 than MT1.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-mt1-melatonin-receptor/">Human MT1 Melatonin Receptor</a> — Sister subtype; companion paper (10.1038/s41586-019-1141-3) describes MT1 structures used for comparison
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — MT2 structures represent inactive 'low agonist affinity' state
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/">GPCR Inactive Conformation</a> — MT2 structures stabilized in inactive state by crystallization construct mutations
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> — Lipid additive used with detergent for membrane protein stabilization
- <a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL (Thermostabilized Apocytochrome b562RIL)</a> — Fusion protein used for crystallization
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG Tag</a> — Affinity tag used for purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> — Purification method used in protein preparation
