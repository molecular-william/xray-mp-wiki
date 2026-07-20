---
title: "hGLUT3 (Human Glucose Transporter 3)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14655, doi/10.1073##pnas.2017749118]
verified: agent
uniprot_id: P11169
---

# hGLUT3 (Human Glucose Transporter 3)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P11169">UniProt: P11169</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 3 (hGLUT3, encoded by SLC2A3) is a member of the GLUT/SLC2
family of facilitative [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporters. hGLUT3 shares ~80% sequence similarity
with [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) and is highly expressed in neurons and other tissues with high [Glucose](/xray-mp-wiki/reagents/additives/glucose/) demand.
The high-resolution structure of human GLUT3 in complex with D-glucose was determined at 1.5 Å resolution in an outward-occluded conformation, allowing discrimination of both α- and β-anomers of D-glucose. Two additional structures of GLUT3 bound to the exofacial inhibitor maltose were obtained at 2.6 Å in the outward-open and 2.4 Å in the outward-occluded states. Comparison of the outward-facing GLUT3 structures with the inward-open GLUT1 provides insights into the alternating access cycle for GLUTs, whereby the C-terminal domain provides the primary substrate-binding site and the N-terminal domain undergoes rigid-body rotation with respect to the C-terminal domain.
In the context of antimalarial drug design, the crystal structure of hGLUT3 in complex with the [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) inhibitor [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) was determined at 2.3 Å resolution to study whether the
allosteric pocket found in [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) is conserved in human GLUT transporters. The structure
(outward-occluded conformation) revealed that [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) binds differently in hGLUT3 compared
to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/): the tail of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) occupies the monoolein-binding pocket at the TM2–TM11
interface in hGLUT3, whereas it projects into the central cavity in [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). These
structural differences confirmed the unique inhibitor-binding-induced pocket specific
to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/), providing the basis for selective inhibitor design.


## Publications

### doi/10.1038##nature14655

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zw9">4ZW9</a></td>
      <td>1.5</td>
      <td>P2₁</td>
      <td>Human GLUT3(N43T) in complex with D-glucose, outward-occluded conformation</td>
      <td>D-Glucose (α- and β-anomers), monoolein</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zw9">4ZW9</a></td>
      <td>2.6</td>
      <td>P2₁</td>
      <td>Human GLUT3(N43T) in complex with maltose, outward-open conformation</td>
      <td>Maltose</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zw9">4ZW9</a></td>
      <td>2.4</td>
      <td>P2₁</td>
      <td>Human GLUT3(N43T) in complex with maltose, outward-occluded conformation</td>
      <td>Maltose</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells (baculovirus)
- **Construct**: Human GLUT3(N43T) with N-terminal 10×His tag; N43T mutation eliminates N-glycosylation site

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
      <td>Cell lysis and membrane preparation</td>
      <td>Dounce homogenization (80 cycles on ice)</td>
      <td>--</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl, protease inhibitors (aprotinin 0.8 μM, pepstatin 2 μM, leupeptin 5 μg ml⁻¹) + --</td>
      <td>Sf-9 cells collected 72 h after infection; membrane pellets collected after centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl, 50 mM D-glucose or maltose + 2% (w/v) n-dodecyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized at 4°C for 2 h; insoluble fraction removed by ultracentrifugation (150,000g, 30 min)</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (Qiagen)</td>
      <td>25 mM MES pH 6.0, 500 mM NaCl, 30 mM imidazole + 0.06% (w/v) 6-cyclohexyl-1-hexyl-β-D-maltoside (CYMAL-6)</td>
      <td>Incubated 30 min at 4°C; rinsed 3 times; eluted with 300 mM imidazole; concentrated to 10 mg ml⁻¹; 50 mM D-glucose or maltose present throughout</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> 10/300 GL</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl + 0.06% (w/v) CYMAL-6</td>
      <td>Pre-equilibrated with same buffer; peak fractions collected for transport assay or crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GLUT3(N43T) concentrated to 30-40 mg ml⁻¹, mixed with monoolein in 1:1.5 protein:lipid ratio (w/w) using syringe lipid mixer</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 week (glucose-bound); overnight (maltose-bound)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in LCP using glass sandwich plates. Glucose-bound crystals diffracted to 1.5 Å at SSRF BL17U. Maltose-bound crystals: outward-occluded form appeared with 38-40% PEG400, 100 mM Mg(CHO₂)₂, 50 mM maltose; outward-open form in similar conditions. Two molecules per asymmetric unit in outward-open form (P2₁), one in outward-occluded form. Solved by molecular replacement.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zw9">4ZW9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHSGDEVDAGSGH</span><span class="topo-inside">MGTQKVTPALIF</span><span class="topo-membrane">AITVATIGSFQFGYNTGVINA</span><span class="topo-outside">P</span><span class="topo-unknown">EKIIKEFITKTLTD</span><span class="topo-outside">KGNAPPSEVLLTSLWS</span><span class="topo-membrane">LSVAIFSVGGMIGSFSVGLFV</span><span class="topo-inside">NRFGRR</span><span class="topo-membrane">NSMLIVN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAVTGGCFMGL</span><span class="topo-outside">CKVAKSVE</span><span class="topo-membrane">MLILGRLVIGLFCGLCTGFVPM</span><span class="topo-inside">YIGEISPTALRGA</span><span class="topo-membrane">FGTLNQLGIVVGILVAQIFGL</span><span class="topo-outside">EFILGSEELWP</span><span class="topo-membrane">LLLGFTILPAILQSAALP</span><span class="topo-inside">FCPESPRFLLINRKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">EENAKQILQRLWGTQDVSQDIQEMKDESARMSQEKQVTVLELFRVSSYRQPI</span><span class="topo-membrane">IISIVLQLSQQLSGINAVFYYS</span><span class="topo-outside">TGIFKDAGVQEPIY</span><span class="topo-membrane">ATIGAGVVNTIFTVVSLFLV</span><span class="topo-inside">ERAGR</span><span class="topo-membrane">RTLHMIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGGMAFCSTLMTVS</span><span class="topo-outside">LLLKDNYNGMSF</span><span class="topo-membrane">VCIGAILVFVAFFEIGPGPIPWFIV</span><span class="topo-inside">AELFSQGPRPA</span><span class="topo-membrane">AMAVAGCSNWTSNFLVGLLFPSAA</span><span class="topo-outside">HYLGA</span><span class="topo-membrane">YVFIIFTGFLITFLAFTFF</span><span class="topo-inside">KVPETRGRTF</span></span>
<span class="topo-ruler">       490       500       510        </span>
<span class="topo-line"><span class="topo-inside">EDITRAFEGQAH</span><span class="topo-unknown">GADRSGKDGVMEMNSIEPAKETTTNV</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>13</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>35</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>49</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>65</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>113</td>
      <td>86</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>132</td>
      <td>92</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>140</td>
      <td>111</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>119</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>175</td>
      <td>141</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>196</td>
      <td>154</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>175</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>186</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>292</td>
      <td>204</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>314</td>
      <td>271</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>328</td>
      <td>293</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>348</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>353</td>
      <td>327</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>374</td>
      <td>332</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>386</td>
      <td>353</td>
      <td>364</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>411</td>
      <td>365</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>422</td>
      <td>390</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>446</td>
      <td>401</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>447</td>
      <td>451</td>
      <td>425</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>430</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>492</td>
      <td>449</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zwb">4ZWB</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHSGDEVDAGSGHMG</span><span class="topo-inside">TQKVTPALI</span><span class="topo-membrane">FAITVATIGSFQFGYNTGVINA</span><span class="topo-outside">P</span><span class="topo-unknown">EKIIKEFITKTLTD</span><span class="topo-outside">KGNAPPSEVLLTSLWS</span><span class="topo-membrane">LSVAIFSVGGMIGSFSVGLFV</span><span class="topo-inside">NRFGRR</span><span class="topo-membrane">NSMLIVN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAVTGGCFMGLC</span><span class="topo-outside">KVAKSVE</span><span class="topo-membrane">MLILGRLVIGLFCGLCTGFVPMYI</span><span class="topo-inside">GEISPTALRGA</span><span class="topo-membrane">FGTLNQLGIVVGILVAQIFGL</span><span class="topo-outside">EFILGSEELWP</span><span class="topo-membrane">LLLGFTILPAILQSAALP</span><span class="topo-inside">FCPESPRFLLINRKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">EENAKQILQRLWGTQDVSQDIQEMKDESARMSQEKQVT</span><span class="topo-unknown">VLELFR</span><span class="topo-inside">VSSYRQPI</span><span class="topo-membrane">IISIVLQLSQQLSGINAVFYYS</span><span class="topo-outside">TGIFKDAGVQEPIY</span><span class="topo-membrane">ATIGAGVVNTIFTVVSLFLV</span><span class="topo-inside">ERAGR</span><span class="topo-membrane">RTLHMIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGGMAFCSTLMTVS</span><span class="topo-outside">LLLKDNYNGMSF</span><span class="topo-membrane">VCIGAILVFVAFFEIGPGPIPWFIV</span><span class="topo-inside">AELFSQGPRPA</span><span class="topo-membrane">AMAVAGCSNWTSNFLVGLLFPSAA</span><span class="topo-outside">HYLGA</span><span class="topo-membrane">YVFIIFTGFLITFLAFTFF</span><span class="topo-inside">KVPETRGRTF</span></span>
<span class="topo-ruler">       490       500       510        </span>
<span class="topo-line"><span class="topo-inside">EDITRAFEGQAH</span><span class="topo-unknown">GADRSGKDGVMEMNSIEPAKETTTNV</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>25</td>
      <td>33</td>
      <td>3</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>55</td>
      <td>12</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>35</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>49</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>107</td>
      <td>65</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>113</td>
      <td>86</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>133</td>
      <td>92</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>112</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>164</td>
      <td>119</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>175</td>
      <td>143</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>196</td>
      <td>154</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>175</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>186</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>278</td>
      <td>204</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>284</td>
      <td>257</td>
      <td>262</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>292</td>
      <td>263</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>314</td>
      <td>271</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>328</td>
      <td>293</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>348</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>353</td>
      <td>327</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>374</td>
      <td>332</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>386</td>
      <td>353</td>
      <td>364</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>411</td>
      <td>365</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>422</td>
      <td>390</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>446</td>
      <td>401</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>447</td>
      <td>451</td>
      <td>425</td>
      <td>429</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>470</td>
      <td>430</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>492</td>
      <td>449</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zwc">4ZWC</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHSGDEVDAGSGHMG</span><span class="topo-outside">TQKVTPALIFAI</span><span class="topo-membrane">TVATIGSFQFGYNTGVIN</span><span class="topo-inside">AP</span><span class="topo-unknown">EKIIKEFITKTLTD</span><span class="topo-inside">KGNAPPSEVLLTSLWS</span><span class="topo-membrane">LSVAIFSVGGMIGSFSVGL</span><span class="topo-outside">FVNRFGRRNS</span><span class="topo-membrane">MLIVN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAVTGGCFMGLC</span><span class="topo-inside">KVAKSVE</span><span class="topo-membrane">MLILGRLVIGLFCGLCTGFVP</span><span class="topo-outside">MYIGEISPTALRGA</span><span class="topo-membrane">FGTLNQLGIVVGILVAQIFG</span><span class="topo-inside">LEFILGSEELW</span><span class="topo-membrane">PLLLGFTILPAILQSAAL</span><span class="topo-outside">PFCPESPRFLLINRKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EENAKQILQRLWGTQDVSQDIQEMKDESARMSQEKQVT</span><span class="topo-unknown">VLELFR</span><span class="topo-outside">VSSYRQPI</span><span class="topo-membrane">IISIVLQLSQQLSGINAVFY</span><span class="topo-inside">YSTGIFKDAGVQEPIYA</span><span class="topo-membrane">TIGAGVVNTIFTVVSLFLV</span><span class="topo-outside">ERAGR</span><span class="topo-membrane">RTLHMIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGGMAFCSTLMT</span><span class="topo-inside">VSLLLKDNYNGMSFVC</span><span class="topo-membrane">IGAILVFVAFFEIGPGPIPWFIV</span><span class="topo-outside">AELFSQGPRPAAM</span><span class="topo-membrane">AVAGCSNWTSNFLVGLLF</span><span class="topo-inside">PSAAHYLGAY</span><span class="topo-membrane">VFIIFTGFLITFLAFTFFKV</span><span class="topo-outside">PETRGRTF</span></span>
<span class="topo-ruler">       490       500       510        </span>
<span class="topo-line"><span class="topo-outside">EDITRAFEGQAH</span><span class="topo-unknown">GADRSGKDGVMEMNSIEPAKETTTNV</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>25</td>
      <td>36</td>
      <td>3</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>56</td>
      <td>33</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>35</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>49</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>105</td>
      <td>65</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>133</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>119</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>175</td>
      <td>140</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>195</td>
      <td>154</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>206</td>
      <td>174</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>224</td>
      <td>185</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>278</td>
      <td>203</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>284</td>
      <td>257</td>
      <td>262</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>292</td>
      <td>263</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>312</td>
      <td>271</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>329</td>
      <td>291</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>348</td>
      <td>308</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>353</td>
      <td>327</td>
      <td>331</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>372</td>
      <td>332</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>388</td>
      <td>351</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>411</td>
      <td>367</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>424</td>
      <td>390</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>442</td>
      <td>403</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>452</td>
      <td>421</td>
      <td>430</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>472</td>
      <td>431</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>492</td>
      <td>451</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.2017749118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7crz">7CRZ</a></td>
      <td>2.3</td>
      <td></td>
      <td>hGLUT3</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf-9 insect cells (baculovirus)
- **Construct**: Human GLUT3(N43T) with N-terminal 10×His tag; N43T mutation eliminates N-glycosylation site

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td>The hGLUT3-<a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> complex structure was determined at 2.30 A resolution. The overall structure adopts a similar conformation to the glucose-bound form (PDB 4ZW9). The sugar moiety of <a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> is coordinated nearly identically to D-<a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> by conserved residues. The tail of <a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> occupies the monoolein-binding pocket at the TM2-TM11 interface, distinct from its binding mode in <a href="/xray-mp-wiki/proteins/mfs-transporters/pfht1/">PfHT1 (Plasmodium falciparum Hexose Transporter 1)</a>.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7crz">7CRZ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHHHHSGDEVDAGSGHMG</span><span class="topo-inside">TQKVTPALIFAIT</span><span class="topo-membrane">VATIGSFQFGYNTGVINA</span><span class="topo-outside">P</span><span class="topo-unknown">EKIIKEFITKTLTD</span><span class="topo-outside">KGNAPPSEVLLTSLWS</span><span class="topo-membrane">LSVAIFSVGGMIGSFSVGLF</span><span class="topo-inside">VNRFGRRNS</span><span class="topo-membrane">MLIVN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAVTGGCFMGLC</span><span class="topo-outside">KVAKSVE</span><span class="topo-membrane">MLILGRLVIGLFCGLCTGFVP</span><span class="topo-inside">MYIGEISPTALRGAFG</span><span class="topo-membrane">TLNQLGIVVGILVAQIFGL</span><span class="topo-outside">EFILGSEEL</span><span class="topo-membrane">WPLLLGFTILPAILQSAAL</span><span class="topo-inside">PFCPESPRFLLINRKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">EENAKQILQRLWGTQDVSQDIQEMKDESARMSQEKQVTVLELFRVSSYRQPI</span><span class="topo-membrane">IISIVLQLSQQLSGINAVFYYS</span><span class="topo-outside">TGIFKDAGVQEPIY</span><span class="topo-membrane">ATIGAGVVNTIFTVVSLFLV</span><span class="topo-inside">ERAGR</span><span class="topo-membrane">RTLHMIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LGGMAFCSTLMTV</span><span class="topo-outside">SLLLKDNYNGMSFV</span><span class="topo-membrane">CIGAILVFVAFFEIGPGPIPWFIV</span><span class="topo-inside">AELFSQGPRPAA</span><span class="topo-membrane">MAVAGCSNWTSNFLVGLLF</span><span class="topo-outside">PSAAHYLGAY</span><span class="topo-membrane">VFIIFTGFLITFLAFTFFKV</span><span class="topo-inside">PETRGRTF</span></span>
<span class="topo-ruler">       490       500       510        </span>
<span class="topo-line"><span class="topo-inside">EDITRAFEGQAHG</span><span class="topo-unknown">ADRSGKDGVMEMNSIEPAKETTTNV</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>25</td>
      <td>37</td>
      <td>3</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>55</td>
      <td>16</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>35</td>
      <td>48</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>49</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>106</td>
      <td>65</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>115</td>
      <td>85</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>133</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>140</td>
      <td>112</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>119</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>177</td>
      <td>140</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>196</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>205</td>
      <td>175</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>224</td>
      <td>184</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>292</td>
      <td>203</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>314</td>
      <td>271</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>328</td>
      <td>293</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>348</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>353</td>
      <td>327</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>373</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>387</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>411</td>
      <td>366</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>423</td>
      <td>390</td>
      <td>401</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>442</td>
      <td>402</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>452</td>
      <td>421</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>453</td>
      <td>472</td>
      <td>431</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>493</td>
      <td>451</td>
      <td>471</td>
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

### Recognition of α- and β-anomers of D-glucose

The 1.5 Å resolution structure of glucose-bound GLUT3 enabled discrimination of both α- and β-D-glucose anomers. Despite the prevailing presence of β-D-glucose in aqueous solution, the α-anomer exhibits dominant occupancy of approximately 69% in the refined structure. D-glucose is bound asymmetrically within the central cavity, coordinated predominantly by polar residues from the C-terminal domain. Key coordinating residues include Gln280 and Gln281 on TM7b, Asn315 on TM8, and Glu378 on TM10a. The high-resolution structure resolves the long-standing question of whether GLUTs require anomerization for transport — both anomers are recognized, so anomerization may not be required for D-glucose transport.

### Conformational transition from outward-open to outward-occluded

Comparison of the outward-open and outward-occluded GLUT3 structures reveals the molecular basis for the conformational switch. TM7b, consisting of four helical turns, is partly unwound and bent in the middle such that the first two helical turns tilt inwards, undergoing an axial rotation by approximately 60 degrees. This leads to relocation of Tyr290 and the substrate-coordinating residue Asn286 into the transport path. An invariant glycine (Gly284) constitutes the kink preceding TM7b, providing flexibility for the structural shift. The N-terminal domain remains nearly rigid throughout, while the ICH domain exhibits minor intra-domain rearrangements.

### Alternating access mechanism for GLUTs

Comparison of glucose-bound outward-occluded GLUT3 with inward-open GLUT1 (PDB 4PYP) provides the framework for alternating access in GLUTs. The C-terminal domain provides the primary substrate-binding site, while the N-terminal domain undergoes rigid-body rotation with respect to the C-terminal domain. TM7b and TM10b undergo prominent conformational changes during the outward-to-inward transition. The N-terminal domain core is relatively hydrophilic with a continuous strip of hydrogen-bonded water molecules, supporting its rigidity. The C-terminal domain is highly hydrophobic, enabling structural adaptability during conformational change.

### Substrate selectivity and ligand design

The structures provide molecular interpretation for the asymmetry of ligand binding from endo- and exofacial sides of GLUTs. The C-terminal domain provides a partial substrate-binding site composed of polar residues on TM7b, TM8, and TM10a. Arrival of substrate at this primary site induces conformational changes including local shifts of TM7b and TM10b along with relative domain rotation. These insights provide a framework for rational design of ligands targeting GLUTs, particularly relevant for cancer therapy via the Warburg effect.

### Structural comparison confirms PfHT1-specific allosteric site

The hGLUT3-[C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) co-crystal structure at 2.3 A resolution revealed that [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) binds
differently in hGLUT3 compared to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). In hGLUT3, the tail of [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) points toward
the TM2-TM11 interface, occupying the pocket that accommodates [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) in the
glucose-bound structure. In [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/), the tail projects into the central cavity of the
occluded structure. This differential binding confirms that [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) possesses unique
intra-domain flexibility that can be exploited for designing selective inhibitors
targeting the allosteric site without inhibiting human GLUTs.

### SP-A network and kinetic differences from GLUT1

Direct comparison of [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) and [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) under identical experimental conditions
(doi/10.26508##lsa.202000858) revealed that [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) has ~3.7-fold higher apparent
affinity (Km = 2.6 mM vs 9.5 mM for [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/)) but ~2.2-fold lower Vmax. These
differences arise from the SP-A network: the C-domain SP motif contains Arg454 in
[GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) versus Lys456 in [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/). The [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) R454K mutation (mimicking [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/)) decreased
affinity sixfold to Km = 17 mM, while the reciprocal [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) K456R mutation produced
GLUT3-like kinetics (Km = 4.2 mM). This demonstrates that a single residue in the
C-domain SP motif determines the isoform-specific kinetic properties. In the N-domain,
both [SLC2A1](/xray-mp-wiki/proteins/mfs-transporters/glut1/) and [GLUT3](/xray-mp-wiki/proteins/mfs-transporters/human-glut3/) have identical SP-A networks with Glu209/Glu207 interacting
with the A motif to stabilize the outward conformation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/pfht1/">PfHT1 (Plasmodium falciparum Hexose Transporter 1)</a> — Structural comparison between hGLUT3-C3361 and PfHT1-C3361 confirmed the unique allosteric pocket in PfHT1
- <a href="/xray-mp-wiki/proteins/mfs-transporters/hglut1/">hGLUT1 (Human Glucose Transporter 1)</a> — hGLUT3 shares 80% sequence similarity with hGLUT1 and was used as a surrogate for structural studies; comparison of outward-facing GLUT3 with inward-open GLUT1 reveals alternating access mechanism
- <a href="/xray-mp-wiki/reagents/ligands/c3361/">C3361 (PfHT1 Inhibitor)</a> — C3361 bound to hGLUT3 was used to study the structural basis of PfHT1 selectivity
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — GLUT3 structures in outward-open, outward-occluded, and comparison with inward-open GLUT1 provide key structural evidence for alternating access in MFS transporters
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — GLUT3 is a member of the MFS with canonical 12-TM fold; the high-resolution structure reveals details of the MFS alternating access cycle
- <a href="/xray-mp-wiki/concepts/protein-families/sugar-porter-family/">Sugar Porter (SP) Family</a> — hGLUT3 is a member of the Sugar Porter family within MFS; structures provide insights into SP motif function
