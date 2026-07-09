---
title: "MjNhaP1 Sodium/Proton Antiporter"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##ELIFE.03583]
verified: regex
uniprot_id: Q60362
---

# MjNhaP1 Sodium/Proton Antiporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q60362">UniProt: Q60362</a>

<span class="expr-badge">Methanocaldococcus JANNASCHII</span>

## Overview

MjNhaP1 is an electroneutral Na+/H+ antiporter from the archaeon *Methanocaldococcus jannaschii*, belonging to the CPA1 family of cation-proton antiporters. It exchanges one Na+ for one H+ and plays roles in pH, ion, and volume homeostasis. The structure was determined in two complementary states: an inward-open state by X-ray crystallography at pH 8 with sodium (3.5 Å resolution, PDB 4CZB), and an outward-open state by electron crystallography at pH 4 without sodium (6 Å resolution, EMDB-2636). The conformational transition involves a ~7° tilt of a 6-helix bundle and a ~5 Å vertical relocation of the ion binding site, consistent with a rocking bundle mechanism.


## Publications

### doi/10.7554##ELIFE.03583

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4czb">4CZB</a></td>
      <td>3.5</td>
      <td>P21</td>
      <td>Full-length MjNhaP1 (untagged, CPD fusion)</td>
      <td>Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/emd-2636">EMD-2636</a></td>
      <td>6.0</td>
      <td>—</td>
      <td>2D crystals at pH 4, no NaCl</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: MjNhaP1 with C-terminal CPD fusion (untagged after cleavage)
- **Notes**: CPD fusion removed by low pH elution during purification
- **Induction**: ZYM-5052 autoinduction medium, 37°C

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
      <td>Cell harvest and lysis</td>
      <td>Microfluidizer</td>
      <td>—</td>
      <td>50 mM Tris/HCl pH 7.5, 140 mM <a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> chloride, 250 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>100,000×g, 4°C, 1 hr</td>
    </tr>
    <tr>
      <td>Membrane protein extraction</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>150 mM MOPS/KOH pH 7.0, 45% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + ~2.0% <a href="/xray-mp-wiki/reagents/detergents/foscholine-12/">Foscholine-12</a></td>
      <td>2 hr at 4°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IgG affinity (CPD binding)</td>
      <td>—</td>
      <td>500 mM NaCl, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (wash); sodium-free buffer (15 mM Tris/HCl pH 7.5, 200 mM KCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) (wash)</td>
      <td>CPD fusion binds to IgG resin via its pro-domain</td>
    </tr>
    <tr>
      <td>Elution and tag cleavage</td>
      <td>pH elution</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/additives/potassium-acetate/">Potassium acetate</a> pH 4, 100 mM KCl, 5 mM MgCl2 + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Low pH elution also cleaves CPD tag</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified untagged MjNhaP1 in elution buffer
**Purity**: Monodisperse on SEC

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MjNhaP1 (heat-treated 85°C, 15 min; centrifuged 125,000×g, 1 hr; filtered)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris/Cl pH 8.2, 24% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10-14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct vitrification in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>3D crystals for X-ray; maximal size 350 µm</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4czb">4CZB</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MELM</span><span class="topo-membrane">MAIGYLGLALVLGSLVAKIA</span><span class="topo-inside">EKLKI</span><span class="topo-membrane">PDIPLLLLLGLIIGPFL</span><span class="topo-outside">QIIP</span><span class="topo-unknown">SDSAMEI</span><span class="topo-membrane">FEYAGPIGLIFILLGGA</span><span class="topo-inside">FTMRISLLKRVIKTV</span><span class="topo-membrane">VRLDTITFLITLLISGFIF</span><span class="topo-outside">NMVLNLPYTSPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">YLFGAITAATDPAT</span><span class="topo-inside">LIPVFSRVRTNPEVAITLEA</span><span class="topo-membrane">ESIFNDPLGIVSTSV</span><span class="topo-outside">ILGLFGLFSSSNPL</span><span class="topo-membrane">IDLITLAGGAIVVGLLLAKIY</span><span class="topo-inside">EKIIIHCDFHEY</span><span class="topo-membrane">VAPLVLGGAMLLLYVGD</span><span class="topo-outside">DLLPSI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">CGYG</span><span class="topo-membrane">FSGYMAVAIMGLYL</span><span class="topo-inside">GDALFRADDIDYKYIVSF</span><span class="topo-membrane">CDDLSLLARVFIFVFLGACI</span><span class="topo-outside">K</span><span class="topo-unknown">LSMLENYF</span><span class="topo-membrane">IPGLLVALGSIFLARPLGVFLGLIG</span><span class="topo-inside">SKHSFKEKLYF</span><span class="topo-membrane">ALEGPRGVVPAALAVT</span><span class="topo-outside">VGI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420      </span>
<span class="topo-line"><span class="topo-outside">EILKNADKIPASITKYITPTDIAGTI</span><span class="topo-membrane">IIGTFMTILLSVILEAS</span><span class="topo-inside">WAGMLALKLLGE</span><span class="topo-unknown">YKPKYKEESHH</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>24</td>
      <td>5</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>50</td>
      <td>47</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>51</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>89</td>
      <td>75</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>108</td>
      <td>90</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>121</td>
      <td>109</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>135</td>
      <td>122</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>136</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>170</td>
      <td>156</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>184</td>
      <td>171</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>205</td>
      <td>185</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>217</td>
      <td>206</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>244</td>
      <td>235</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>245</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>259</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>296</td>
      <td>277</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>297</td>
      <td>297</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>305</td>
      <td>298</td>
      <td>305</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>306</td>
      <td>330</td>
      <td>306</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>341</td>
      <td>331</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>357</td>
      <td>342</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>386</td>
      <td>358</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>403</td>
      <td>387</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>415</td>
      <td>404</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4czb">4CZB</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEL</span><span class="topo-membrane">MMAIGYLGLALVLGSLVAKIA</span><span class="topo-inside">EKLKI</span><span class="topo-membrane">PDIPLLLLLGLIIGPFL</span><span class="topo-outside">QIIP</span><span class="topo-unknown">SDSAMEI</span><span class="topo-membrane">FEYAGPIGLIFILLGGA</span><span class="topo-inside">FTMRISLLKRVIKTV</span><span class="topo-membrane">VRLDTITFLITLLISGFIF</span><span class="topo-outside">NMVLNLPYTSPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">YLFGAITAATDPAT</span><span class="topo-inside">LIPVFSRVRTNPEVAITLEA</span><span class="topo-membrane">ESIFNDPLGIVSTSVI</span><span class="topo-outside">LGLFGLFSSSNP</span><span class="topo-membrane">LIDLITLAGGAIVVGLLLAKIYE</span><span class="topo-inside">KIIIHCDFHEY</span><span class="topo-membrane">VAPLVLGGAMLLLYVGD</span><span class="topo-outside">DLLPSI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">CGYG</span><span class="topo-membrane">FSGYMAVAIMGLYL</span><span class="topo-inside">GDALFRADDIDYKYIVSF</span><span class="topo-membrane">CDDLSLLARVFIFVFLGACI</span><span class="topo-outside">K</span><span class="topo-unknown">LSMLEN</span><span class="topo-outside">YF</span><span class="topo-membrane">IPGLLVALGSIFLARPLGVFLGLIG</span><span class="topo-inside">SKHSFKEKLYF</span><span class="topo-membrane">ALEGPRGVVPAALAVTV</span><span class="topo-outside">GI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420      </span>
<span class="topo-line"><span class="topo-outside">EILKNADKIPASITKYITPTDIAGTI</span><span class="topo-membrane">IIGTFMTILLSVILEAS</span><span class="topo-inside">WAGMLALKLLGEYKPK</span><span class="topo-unknown">YKEESHH</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>50</td>
      <td>47</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>57</td>
      <td>51</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>89</td>
      <td>75</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>108</td>
      <td>90</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>121</td>
      <td>109</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>135</td>
      <td>122</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>136</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>171</td>
      <td>156</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>183</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>206</td>
      <td>184</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>217</td>
      <td>207</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>244</td>
      <td>235</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>258</td>
      <td>245</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>276</td>
      <td>259</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>296</td>
      <td>277</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>297</td>
      <td>297</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>303</td>
      <td>298</td>
      <td>303</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>305</td>
      <td>304</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>330</td>
      <td>306</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>331</td>
      <td>341</td>
      <td>331</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>358</td>
      <td>342</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>386</td>
      <td>359</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>403</td>
      <td>387</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>404</td>
      <td>419</td>
      <td>404</td>
      <td>419</td>
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

### Two-state conformational cycle

MjNhaP1 adopts inward-open (pH 8 + Na+) and outward-open (pH 4, no Na+) states. The 6-helix bundle (H3, H4, H5, H6, H12, H13) tilts by ~7° as a rigid body, closing the extracellular cavity while opening the cytoplasmic funnel. The ion binding site (coordinated by Asp132, Thr131 backbone, Ser157, Asp161) moves vertically by ~5 Å during the transition.

### Transport mechanism

The transport cycle involves four steps: (i) a proton from the cell replaces bound Na+, releasing Na+ to the cytoplasm; (ii) upon protonation of Asp161, the antiporter switches to the outward-open state; (iii) extracellular Na+ displaces the proton at Asp161; (iv) deprotonation and Na+ binding trigger the switch back to the inward-open state. This is consistent with a rocking bundle alternating-access mechanism.

### Electroneutral vs electrogenic transport

MjNhaP1 is electroneutral (1 Na+:1 H+), characteristic of CPA1 antiporters. The ND motif (Asn160-Asp161) in H6 is essential for function. Replacing N160 with alanine abolishes activity; N160D retains reduced activity but is not electrogenic. CPA2 antiporters (EcNhaA, TtNapA) use a DD motif and exchange 2 H+:1 Na+. Despite different stoichiometries, the overall fold and conformational changes are similar across [CPA](/xray-mp-wiki/reagents/ligands/cyclopiazonic-acid/) families.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/potassium-acetate/">Potassium acetate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/foscholine-12/">Foscholine-12</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/ligands/cyclopiazonic-acid/">CPA</a> — Related ligand or cofactor
