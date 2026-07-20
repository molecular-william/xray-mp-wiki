---
title: "V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09580]
verified: agent
uniprot_id: P96169
---

# V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P96169">UniProt: P96169</a>

<span class="expr-badge">Vibrio parahaemolyticus</span>

## Overview

V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) is a secondary active transporter from the bacterium Vibrio parahaemolyticus that couples the electrochemical gradient of sodium ions to the active transport of galactose across the cell membrane. vSGLT belongs to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) and shares structural homology with the bacterial amino acid transporter [LEUT](/xray-mp-wiki/proteins/enzymes/leut/). The crystal structures of vSGLT in both inward-occluded and outward-open conformations provided the first direct structural evidence for the alternating-access mechanism in an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter, revealing a sodium-dependent rocker-switch mechanism.


## Publications

### doi/10.1038/NATURE09580

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3dh4">3DH4</a></td>
      <td>2.7</td>
      <td>P212121</td>
      <td>vSGLT residues 1-452 (full-length) without N-terminal His-tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/d-galactose/">D-Galactose</a>, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2xq2">2XQ2</a></td>
      <td>2.7</td>
      <td>P212121</td>
      <td>vSGLT residues 1-452 (full-length) without N-terminal His-tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/d-galactose/">D-Galactose</a>, sodium ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: vSGLT residues 1-452 with N-terminal His-tag; selenomethionine-substituted variant for SAD phasing

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
      <td>Cell lysis</td>
      <td>Detergent solubilization from E. coli membrane fractions</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) (His-tag affinity)</td>
      <td>Buffer containing Tris</td>
      <td>Selenomethionine-substituted protein for <a href="/xray-mp-wiki/methods/structure-determination/single-anomalous-dispersion/">[SAD</a>](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction) phasing</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Selenomethionine-substituted vSGLT construct</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group P212121; <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction">SAD</a> phasing with selenium sites; two structures reported: inward-occluded (3DH4, galactose-bound) and outward-open (3DH5)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3dh4">3DH4</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">UUUUU</span><span class="topo-membrane">UUUUUUUUUUUU</span><span class="topo-outside">AGKSLPWW</span><span class="topo-membrane">AVGASLIAANISAEQFIGM</span><span class="topo-inside">SGSGYSIGLAI</span><span class="topo-membrane">ASYEWMSAITLIIV</span><span class="topo-outside">GKYFLPIFIEKGIYTIPEFVEKRFNKKLKTI</span><span class="topo-membrane">LAVFWISLYIFVNLTSVLYL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">G</span><span class="topo-inside">GLALETILGIPLMYSI</span><span class="topo-membrane">LGLALFALVYSI</span><span class="topo-unknown">YGGLSA</span><span class="topo-outside">V</span><span class="topo-membrane">VWTDVIQVFFLVLGGF</span><span class="topo-inside">MTTYMAVSFIGGTDGWFAGVSKMVDAAPGHFEMILDQSNPQYMNLPGI</span><span class="topo-membrane">AVLIGGLWVANLYYWGFNQ</span><span class="topo-outside">Y</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IIQRTLAAKSVSEAQKG</span><span class="topo-membrane">IVFAAFLKLIVPFLV</span><span class="topo-inside">VLPGIAAYVITSDPQLMASLGDIAATNLPSAANADKAYPWLTQFLPVGVKG</span><span class="topo-membrane">VVFAALAAAIVSSLASMLNSTATIF</span><span class="topo-outside">TMDIYKEYISPD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">SGDHKLVNVG</span><span class="topo-membrane">RTAAVVALIIACLIA</span><span class="topo-inside">PMLGGIGQAF</span><span class="topo-membrane">QYIQEYTGLVSPGILAV</span><span class="topo-outside">FLLGLFWKKTTSKGAII</span><span class="topo-membrane">GVVASIPFALFLKF</span><span class="topo-inside">MPLSMP</span><span class="topo-membrane">FMDQMLYTLLFTMVVI</span><span class="topo-outside">AFTSLSTSINDDDPK</span></span>
<span class="topo-ruler">       490       500       510       520       530</span>
<span class="topo-line"><span class="topo-outside">GISVTSSMFVTDRSFNI</span><span class="topo-membrane">AAYGIMIVLAVLYTL</span><span class="topo-inside">FWVLYK</span><span class="topo-unknown">SGGSPGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>3</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>17</td>
      <td>8</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>18</td>
      <td>25</td>
      <td>47</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>44</td>
      <td>55</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>55</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>69</td>
      <td>85</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>100</td>
      <td>99</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>121</td>
      <td>130</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>137</td>
      <td>151</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>149</td>
      <td>167</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>155</td>
      <td>179</td>
      <td>184</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>156</td>
      <td>185</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>172</td>
      <td>186</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>220</td>
      <td>202</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>239</td>
      <td>250</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>269</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>272</td>
      <td>287</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>323</td>
      <td>302</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>370</td>
      <td>378</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>385</td>
      <td>400</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>395</td>
      <td>415</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>412</td>
      <td>425</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>429</td>
      <td>442</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>443</td>
      <td>459</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>449</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>465</td>
      <td>479</td>
      <td>494</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>497</td>
      <td>495</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>498</td>
      <td>512</td>
      <td>527</td>
      <td>541</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>513</td>
      <td>518</td>
      <td>542</td>
      <td>547</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>530</td>
      <td>548</td>
      <td>559</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3dh4">3DH4</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">UUUUU</span><span class="topo-membrane">UUUUUUUUUUUU</span><span class="topo-outside">AGKSLPWWAVG</span><span class="topo-membrane">ASLIAANISAEQFIGM</span><span class="topo-inside">SGSGYSIGLAI</span><span class="topo-membrane">ASYEWMSAITLIIV</span><span class="topo-outside">GKYFLPIFIEKGIYTIPEFVEKRFNKKLKTI</span><span class="topo-membrane">LAVFWISLYIFVNLTSVLYL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">G</span><span class="topo-inside">GLALETILGIPLMYSI</span><span class="topo-membrane">LGLALFALVYSI</span><span class="topo-unknown">YGGLSA</span><span class="topo-outside">V</span><span class="topo-membrane">VWTDVIQVFFLVLGGF</span><span class="topo-inside">MTTYMAVSFIGGTDGWFAGVSKMVDAAPGHFEMILDQSNPQYMNLPGI</span><span class="topo-membrane">AVLIGGLWVANLYYWGFNQ</span><span class="topo-outside">Y</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IIQRTLAAKSVSEAQKG</span><span class="topo-membrane">IVFAAFLKLIVPFLV</span><span class="topo-inside">VLPGIAAYVITSDPQLMASLGDIAATNLPSAANAD</span><span class="topo-unknown">KAYPWLT</span><span class="topo-inside">QFLPVGVKG</span><span class="topo-membrane">VVFAALAAAIVSSLASMLNSTATIF</span><span class="topo-outside">TMDIYKEYISPD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">SGDHKLVNVG</span><span class="topo-membrane">RTAAVVALIIACLIA</span><span class="topo-inside">PMLGGIGQAF</span><span class="topo-membrane">QYIQEYTGLVSPGILAV</span><span class="topo-outside">FLLGLFWKKTTSKGAII</span><span class="topo-membrane">GVVASIPFALFLKF</span><span class="topo-inside">MPLSMP</span><span class="topo-membrane">FMDQMLYTLLFTMVVI</span><span class="topo-outside">AFTSLSTSINDDDPK</span></span>
<span class="topo-ruler">       490       500       510       520       530</span>
<span class="topo-line"><span class="topo-outside">GISVTSSMFVTDRSFNI</span><span class="topo-membrane">AAYGIMIVLAVLYTL</span><span class="topo-inside">FWVLYK</span><span class="topo-unknown">SGGSPGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>3</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>17</td>
      <td>8</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>18</td>
      <td>28</td>
      <td>47</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>44</td>
      <td>58</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>55</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>69</td>
      <td>85</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>100</td>
      <td>99</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>121</td>
      <td>130</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>137</td>
      <td>151</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>149</td>
      <td>167</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>155</td>
      <td>179</td>
      <td>184</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>156</td>
      <td>185</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>172</td>
      <td>186</td>
      <td>201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>220</td>
      <td>202</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>239</td>
      <td>250</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>269</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>272</td>
      <td>287</td>
      <td>301</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>307</td>
      <td>302</td>
      <td>336</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>314</td>
      <td>337</td>
      <td>343</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>315</td>
      <td>323</td>
      <td>344</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>348</td>
      <td>353</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>370</td>
      <td>378</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>385</td>
      <td>400</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>395</td>
      <td>415</td>
      <td>424</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>412</td>
      <td>425</td>
      <td>441</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>429</td>
      <td>442</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>443</td>
      <td>459</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>449</td>
      <td>473</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>465</td>
      <td>479</td>
      <td>494</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>497</td>
      <td>495</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>498</td>
      <td>512</td>
      <td>527</td>
      <td>541</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>513</td>
      <td>518</td>
      <td>542</td>
      <td>547</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>530</td>
      <td>548</td>
      <td>559</td>
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

### Outward-open conformation structure

The 3DH5 structure reveals vSGLT in an outward-open conformation with galactose and sodium ions bound in the substrate-binding pocket. The sodium ion is coordinated by the side chains of N64, N343, T350, S365, and K294, forming a coordination network that locks galactose in place. Key residues N64, N343, and W251 form hydrogen bonds with galactose, while Y263 adopts a rotamer conformation that opens the extracellular pathway. This structure provides the first high-resolution view of an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter in the outward-open state.

### Alternating-access mechanism

Superposition of the inward-occluded (3DH4) and outward-open (3DH5) structures reveals a rocker-switch mechanism involving rigid-body movement of the extracellular domain (ECD) relative to the transmembrane domain (TMD). The transition involves significant conformational changes in transmembrane helices 1, 5, 6, 7, and 10, while the hash motif (TMs 3, 4, 8, 9) and sugar bundle (TMs 2, 6, 7) remain relatively rigid. This provides direct structural evidence for the alternating-access mechanism in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporters.

### Sodium-dependent gating mechanism

The sodium ion coordination site is critical for substrate binding and gating. In the outward-open conformation, the sodium ion stabilizes the binding pocket, and its absence allows the Y263 rotamer to switch and block substrate release. Molecular dynamics simulations show that sodium departure from the binding site triggers conformational changes that allow galactose to exit. The Y263 residue in TM6 acts as a gate, switching rotamer conformations to control substrate access.

### Inward-open conformation stabilization

The inward-open conformation is partially stabilized by a hydrogen bond between E68 (on the unwound segment of TM1) and S365 (a sodium-coordinating residue). This interaction helps lock the intracellular gate in the open state. The hash motif formed from TMs 3, 4, 8, and 9 provides structural stability during the conformational transition.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — vSGLT crystal structures provide direct evidence for alternating access
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">MFS</a> — Related biological concept
- <a href="/xray-mp-wiki/reagents/ligands/d-galactose/">D-Galactose</a> — Primary substrate of the vSGLT transporter
- <a href="/xray-mp-wiki/reagents/ligands/sodium-ion/">Sodium Ion (Na+)</a> — Essential co-transport ion for vSGLT function
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">vSGLT K294A Mutant</a> — Crystallized variant of vSGLT from same study
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">vSGLT N64A Mutant</a> — Gate mutant studied by molecular dynamics in same study
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations used to study galactose exit mechanism
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)</a> — K294A is a point mutant of vSGLT
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Additive used in purification or crystallization buffers
