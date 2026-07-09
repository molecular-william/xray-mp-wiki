---
title: "Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1217042110]
verified: regex
uniprot_id: Q9NRK6
---

# Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9NRK6">UniProt: Q9NRK6</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

ABCB10 is a human [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) transporter found in the inner mitochondrial membrane. It is a homodimeric half transporter essential for erythropoiesis and protection against mitochondrial oxidative stress. ABCB10 adopts an exporter fold with six transmembrane helices per monomer and a C-terminal nucleotide-binding domain (NBD). Its crystal structures in apo- and nucleotide-bound states reveal an unexpected open-inwards conformation with bound [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogs, suggesting that nucleotide binding can occur before transport substrate binding.


## Publications

### doi/10.1073##pnas.1217042110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a></td>
      <td>2.90</td>
      <td></td>
      <td>ABCB10 with N-terminal mitochondrial targeting presequence removed (N-terminal 151 residues or residues 6-126 deleted)</td>
      <td>[AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a></td>
      <td>3.30</td>
      <td></td>
      <td>ABCB10 with N-terminal mTP removed</td>
      <td>AMPPNP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a></td>
      <td></td>
      <td></td>
      <td>ABCB10 apo</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus); ABCB10 expressed with both N- and C-terminal His-tags, with mitochondrial targeting presequence removed (deletion of N-terminal 151 residues or residues 6-126)


**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: ABCB10 with mTP removed, N- and C-terminal His-tags
- **Tag info**: N- and C-terminal His-tags

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
      <td>Extraction</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (dodecyl maltoside)</td>
      <td>Purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with addition of either <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> (cholesteryl-hemisuccinate) or CDL (cardiolipin)</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Cobalt affinity</td>
      <td>Cobalt affinity resin</td>
      <td></td>
      <td>Standard immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Final polishing step in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> or CDL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ABCB10 purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> or <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + CDL</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Plate-form crystals grown with AMPPNP; rod-form crystals grown with [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/) from protein purified with CDL. Diffraction data collected at Diamond Light Source beamline I24.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ayt">4AYT</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAG</span><span class="topo-inside">LPEARKLLGLA</span><span class="topo-membrane">YPERRRLAAAVGFLTMSSVISMSAP</span><span class="topo-outside">FFLGKIIDVIYTNPTVDYSDNLTRLCLGL</span><span class="topo-membrane">SAVFLCGAAANAIRVYLMQTSGQ</span><span class="topo-inside">RIVNRLRTSLFSSILRQEVAFFDKTRTGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LINRLSSDTALLG</span><span class="topo-membrane">RSVTENLSDGLRAGAQASVGISMMF</span><span class="topo-outside">FVSPNLA</span><span class="topo-membrane">TFVLSVVPPVSIIAVIYGRYLRKLT</span><span class="topo-inside">KVTQDSLAQATQLAEERIGNVRTVRAFGKEMTEIEKYASKVDHVMQLA</span><span class="topo-membrane">RK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EAFARAGFFGATGLSGNLIVLSV</span><span class="topo-outside">LYKGGLLMGSAHMTVGELSSF</span><span class="topo-membrane">LMYAFWVGISIGGLSSFYSELMK</span><span class="topo-inside">GLGAGGRLWELLEREPKLPFNEGVILNEKSFQGALEFKNVHFAYPARPEVPIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">QDFSLSIPSGSVTALVGPSGSGKSTVLSLLLRLYDPASGTISLDGHDIRQLNPVWLRSKIGTVSQEPILFSCSIAENIAYGADDPSSVTAEEIQRVAEVANAVAFIRNFPQGFNTVVGEK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590     </span>
<span class="topo-line"><span class="topo-inside">GVLLSGGQKQRIAIARALLKNPKILLLDEATSALDAENEYLVQEALDRLMDGRTVLVIAHRLSTIKNANMVAVLDQGKITEYGKHEE</span><span class="topo-unknown">LLSKPNGIYRKLMNKQSFISAAENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>151</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>14</td>
      <td>154</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>39</td>
      <td>165</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>190</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>219</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>133</td>
      <td>242</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>158</td>
      <td>284</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>309</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>316</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>238</td>
      <td>341</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>263</td>
      <td>389</td>
      <td>413</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>414</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>307</td>
      <td>435</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>567</td>
      <td>458</td>
      <td>717</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>595</td>
      <td>718</td>
      <td>745</td>
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

### Open-inwards conformation with bound nucleotide

Unlike other ABC transporters that adopt open-outwards conformations when bound to [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogs, ABCB10 remains in an open-inwards conformation with separated NBDs. Four structures (apo, AMPPNP-bound, two [AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate)](/xray-mp-wiki/reagents/amppcp/)-bound) all show inward-facing states with varying degrees of NBD separation. Refinement confirms 80-100% nucleotide occupancy in both nucleotide binding sites, demonstrating that [ATP](/xray-mp-wiki/reagents/ligands/atp/) can bind to both NBDs without triggering the conformational change to open-outwards state.

### Portal between TMH1 and TMH2 for substrate entry

The ABCB10 structures reveal a portal between transmembrane helices TMH1 and TMH2 that connects the central cavity to the membrane environment. This portal is occupied by [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) in rod-form crystals and is partially open or closed depending on crystal form. The portal may serve as an entry route for amphipathic transport substrates into the substrate-binding cavity.

### Implications for ABC transporter mechanism

The ABCB10 structures support an adaptation of the [ATP](/xray-mp-wiki/reagents/ligands/atp/) switch model where either nucleotide or transport substrate can bind first to the open-inwards conformation. Binding of transport substrate likely promotes NBD closure and transition to the open-outwards conformation, explaining the stimulation of ATPase activity by substrates. The basal ATPase activity of ABCB10 (Km_app ~0.2 mM) is consistent with nucleotide binding occurring in the absence of transport substrate.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/">Mouse P-glycoprotein (Pgp, ABCB1)</a> — Homologous ABC exporter with similar fold; comparison of open-inwards vs open-outwards conformations
- <a href="/xray-mp-wiki/proteins/abc-transporters/sav1866/">Sav1866 Multidrug ABC Transporter</a> — Bacterial ABC exporter in open-outwards conformation; key structural comparator
- <a href="/xray-mp-wiki/proteins/abc-transporters/tm287-288/">TM287/288 (ABC Exporter from Thermotoga maritima)</a> — ABC exporter with intermediate open-inwards and AMPPNP-bound conformations
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/">Mouse P-glycoprotein</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/sav1866/">Sav1866 Multidrug ABC Transporter</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/tm287-288/">TM287/288 Heterodimeric ABC Exporter from Thermotoga maritima</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Lipid additive for stabilization
