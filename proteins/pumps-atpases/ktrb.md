---
title: "KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12055]
verified: false
---

# KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)

## Overview

KtrB is a membrane protein component of the KtrAB potassium transporter from the bacterium Bacillus subtilis. It assembles as a homodimer and belongs to the Trk/Ktr/HKT superfamily of ion transporters. Each KtrB monomer contains four repeat domains (D1-D4), each with a TM-P loop-TM structural motif that assembles to form an ion pore with a funnel-shaped selectivity filter. KtrB is essential for K+ uptake and plays a key role in osmotic stress resistance and high salinity tolerance. The long C-terminus of KtrB snakes into the cytoplasmic pore of the neighbouring subunit and is involved in gating regulation.


## Publications

### doi/10.1038##nature12055

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j7c">4J7C</a></td>
      <td>3.5</td>
      <td>Not specified</td>
      <td>KtrB homodimer (residues 1-445) in complex with octameric KtrA-ATP ring</td>
      <td>ATP, K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: N-terminal His-tagged KtrB, tag cleaved with thrombin before complex assembly
- **Notes**: Overexpressed in LB media at 37°C for 2.5 h after [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: N-terminal His-tagged KtrB, tag cleaved with thrombin

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>LB media</td>
      <td>37°C for 2.5 h after <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> induction</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 120 mM NaCl, 30 mM KCl + 40 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltoside)</td>
      <td>Overnight extraction at 4°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> metal affinity resin (Clontech)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 120 mM NaCl, 30 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with Buffer B, eluted with 150 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease cleavage</td>
      <td>--</td>
      <td></td>
      <td>Incubated overnight at 4°C with thrombin for tag removal</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~2.5 mg/ml in Buffer B supplemented with [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KtrAB complex (KtrB homodimer + <a href="/xray-mp-wiki/proteins/pumps-atpases/ktra/">KTRA</a> octamer) in Buffer E supplemented with 1 mM ATP, concentrated to ~10 mg/ml, detergent exchanged to <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/aces/">ADA</a> (N-(2-acetamido)-iminodiacetic acid) pH 6.5, 20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 200 mM ammonium sulphate</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-frozen in liquid nitrogen after addition of mother liquor with 45% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j7c">4J7C</a> — Chain I (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMTLQKDKVIKWVRF</span><span class="topo-outside">TPPQVL</span><span class="topo-membrane">AIGFFLTIIIGAVLLML</span><span class="topo-inside">PISTTKPLSWI</span><span class="topo-unknown">DALFTAASATTVTGLA</span><span class="topo-inside">VVDTGTQFTV</span><span class="topo-membrane">FGQTVIMGLIQIGGLGFM</span><span class="topo-outside">TFAVLIVM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IL</span><span class="topo-unknown">GK</span><span class="topo-outside">KIGLKERMLVQEALNQPTIGGVIGLVKVLF</span><span class="topo-membrane">LFSISIELIAALILSIRLVP</span><span class="topo-inside">QYGWSSG</span><span class="topo-unknown">LFASLFHAISAFNNAGFSL</span><span class="topo-inside">WPDNLMSYVG</span><span class="topo-membrane">DPTVNLVITFLFITGGI</span><span class="topo-outside">GFTVLFDVMKNRR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">FKTFSLHTKLMLTG</span><span class="topo-membrane">TLMLNAIAMLTVFILE</span><span class="topo-inside">YSNPGTLGHLHI</span><span class="topo-unknown">VDKLWASYFQAVTPRTAGFNS</span><span class="topo-inside">LDFGSMRE</span><span class="topo-membrane">GTIVFTLLLMFIGAGS</span><span class="topo-outside">ASTASGIKLTTFIVILTSVIAYLRGKKETVIFR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460     </span>
<span class="topo-line"><span class="topo-outside">RSIKYPIIIKALAV</span><span class="topo-membrane">SVTSLFIVFLGIFALTIT</span><span class="topo-inside">EQAPFLQI</span><span class="topo-unknown">VFETFSAFGTVGLT</span><span class="topo-inside">MGLTPELTTA</span><span class="topo-membrane">GKCIIIVIMFIGRIGPLTFV</span><span class="topo-outside">FSFAKTEQSNIRYPDGEVFTG</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>34</td>
      <td>-19</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>40</td>
      <td>15</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>57</td>
      <td>21</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>68</td>
      <td>38</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>84</td>
      <td>49</td>
      <td>64</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>94</td>
      <td>65</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>112</td>
      <td>75</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>122</td>
      <td>93</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>124</td>
      <td>103</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>154</td>
      <td>105</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>174</td>
      <td>135</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>181</td>
      <td>155</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>200</td>
      <td>162</td>
      <td>180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>201</td>
      <td>210</td>
      <td>181</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>227</td>
      <td>191</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>254</td>
      <td>208</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>270</td>
      <td>235</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>282</td>
      <td>251</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>303</td>
      <td>263</td>
      <td>283</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>311</td>
      <td>284</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>327</td>
      <td>292</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>374</td>
      <td>308</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>355</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>373</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>414</td>
      <td>381</td>
      <td>394</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>415</td>
      <td>424</td>
      <td>395</td>
      <td>404</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>444</td>
      <td>405</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>465</td>
      <td>425</td>
      <td>445</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4j7c">4J7C</a> — Chain J (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMTLQKDKVIKWVRF</span><span class="topo-outside">TPPQVLA</span><span class="topo-membrane">IGFFLTIIIGAVLLML</span><span class="topo-inside">PISTTKPLSW</span><span class="topo-unknown">IDALFTAASATTVTGLA</span><span class="topo-inside">VVDTGTQFTV</span><span class="topo-membrane">FGQTVIMGLIQIGGLGF</span><span class="topo-outside">MTFAVLIVM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IL</span><span class="topo-unknown">GK</span><span class="topo-outside">KIGLKERMLVQEALNQPTIGGVIGLVKVLF</span><span class="topo-membrane">LFSISIELIAALILSIRLV</span><span class="topo-inside">PQYGWSSG</span><span class="topo-unknown">LFASLFHAISAFNNAGFSL</span><span class="topo-inside">WPDNLMSYVGD</span><span class="topo-membrane">PTVNLVITFLFITGGIG</span><span class="topo-outside">FTVLFDVMKNRR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">FKTFSLHTKLM</span><span class="topo-membrane">LTGTLMLNAIAMLTVFIL</span><span class="topo-inside">EYSNPGTLGHLHIVDKL</span><span class="topo-unknown">WASYFQAVTPRTAGFNS</span><span class="topo-inside">LDFGSMREG</span><span class="topo-membrane">TIVFTLLLMFIGAGS</span><span class="topo-outside">ASTASGIKLTTFIVILTSVIAYLRGKKETVIFR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460     </span>
<span class="topo-line"><span class="topo-outside">RSIKYPIIIKALAV</span><span class="topo-membrane">SVTSLFIVFLGIFALTIT</span><span class="topo-inside">EQAPFL</span><span class="topo-unknown">QIVFETFSAFGTVGLT</span><span class="topo-inside">MGLTPELTTA</span><span class="topo-membrane">GKCIIIVIMFIGRIGP</span><span class="topo-outside">LTFVFSFAKTEQSNIRYPDGEVFTG</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>34</td>
      <td>-19</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>15</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>22</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>67</td>
      <td>38</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>84</td>
      <td>48</td>
      <td>64</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>94</td>
      <td>65</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>75</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>122</td>
      <td>92</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>124</td>
      <td>103</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>125</td>
      <td>154</td>
      <td>105</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>173</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>181</td>
      <td>154</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>200</td>
      <td>162</td>
      <td>180</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>201</td>
      <td>211</td>
      <td>181</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>228</td>
      <td>192</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>251</td>
      <td>209</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>269</td>
      <td>232</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>286</td>
      <td>250</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>303</td>
      <td>267</td>
      <td>283</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>304</td>
      <td>312</td>
      <td>284</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>327</td>
      <td>293</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>374</td>
      <td>308</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>355</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>398</td>
      <td>373</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>414</td>
      <td>379</td>
      <td>394</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>415</td>
      <td>424</td>
      <td>395</td>
      <td>404</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>440</td>
      <td>405</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>465</td>
      <td>421</td>
      <td>445</td>
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

### KtrB homodimer architecture

KtrB assembles as a homodimer in the bacterial membrane. Each monomer contains four repeat domains (D1-D4), each with the TM-P loop-TM structural motif. The four subunits (two per monomer) assemble to form an ion pore with a funnel-shaped selectivity filter whose wider mouth (11-13 A across) faces the extracellular side and a single ion-binding site at the narrow end. The overall architecture closely resembles that of potassium channel pores.

### Intramembrane loop and gating

An intramembrane loop (connecting helices M2a to M2b in repeat D3), composed almost exclusively of glycines, alanines and serines, together with a highly conserved arginine (R417), forms a structure that blocks access between the selectivity filter and the cytoplasmic pore. This region has been proposed to function as a transporter gate; mutations or truncations in this region increase ion flux. An open pathway from the R417/intramembrane loop to the cytoplasmic face is ~4 A wide at its narrowest point.

### C-terminal domain interaction

The long C-terminus of KtrB runs from one subunit, forms a lateral contact, and snakes into the cytoplasmic pore of the neighbouring KtrB subunit, finishing just below the intramembrane loop. The last seven residues line the wall of the cytoplasmic pore of the neighbouring subunit. The highly conserved C-terminal [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G445) has its carboxylate interacting with a lysine (K315 in KtrB) that is part of the intramembrane loop and conserved in both Ktr and Trk transporters. Sequential [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of up to three C-terminal residues has no effect or only minor effects on K+ transport activity.

### Comparison with TrkH

The monomer and homodimer structures of KtrB and the related [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) (a Trk membrane protein) are very similar. A major difference is in the C terminus: [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) has a much shorter C terminus that does not establish contacts. In [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/), the side-chain carboxylate of a conserved glutamate (E470) occupies the same volume as the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) carboxylate in KtrB and also interacts with the conserved lysine. Additionally, in [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) the helices M2a and M2b in repeat D1 are continuous, whereas in KtrB they are separated by an ordered amino acid stretch in the D1-D2 loop.

### Ligand binding and activation

KtrB alone allows K+ into cells but less efficiently than the full KtrAB complex. The 86Rb+ flux difference between KtrAB-ATP and KtrB (~2-fold at 30 min) is smaller than expected from K+ uptake measurements in cells (~10-fold difference in Vmax), suggesting that additional activating factors beyond ATP may be required for full transporter activity. Ktr proteins transport K+ but are also permeable to Na+, and K+ transport is ATP and Na+ dependent.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/ktra/">KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)</a> — KtrA forms the cytosolic octameric ring that associates with KtrB homodimer to form the KtrAB transporter complex
- <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> — ATP is the activating ligand that binds to KtrA and induces conformational changes in the octameric ring
- <a href="/xray-mp-wiki/reagents/ligands/adp/">Adenosine Diphosphate (ADP)</a> — ADP binds to KtrA and induces a different conformation from ATP (diamond vs square)
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM used for KtrB membrane protein extraction and solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> — Cymal-6 detergent used for KtrAB complex crystallization after detergent exchange
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Tris-HCl buffer used throughout KtrB purification (pH 8.0)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/">RCK Domain Activation Mechanism</a> — KtrA contains RCK domains that form an octameric gating ring; KtrAB activation mechanism differs from MthK and BK channels
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Ion Channel Selectivity Filter</a> — KtrB selectivity filter is funnel-shaped and shares architectural similarity with potassium channel pores
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
