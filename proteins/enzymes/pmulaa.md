---
title: "Pasteurella multocida Ascorbate Transporter EIIC (pmUlaA)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41421-018-0037-y]
verified: false
---

# Pasteurella multocida Ascorbate Transporter EIIC (pmUlaA)

## Overview

pmUlaA is the EIIC component of the L-ascorbate (vitamin C) phosphoenolpyruvate-dependent phosphotransferase system (PTS) from Pasteurella multocida. It belongs to the ascorbate/galactitol (AG) superfamily of PTS transporters. The structure was solved in the inward-facing conformation at 3.35 Angstrom resolution, revealing a rigid-body [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) where the substrate-binding core domain moves relative to the V motif domains to transport ascorbate across the membrane. pmUlaA shares 63% sequence identity with the E. coli homolog ecUlaA.


## Publications

### doi/10.1038##s41421-018-0037-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zov">5ZOV</a></td>
      <td>3.35</td>
      <td>—</td>
      <td>Proteolyzed from wild-type pmUlaAB fusion, residues 37-460</td>
      <td>L-ascorbate (vitamin C)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length pmUlaA with C-terminal His x 8 tag, expressed as pmUlaAB fusion (proteolyzed with [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) to obtain pmUlaA)
- **Notes**: Cells disrupted by French Press at 15,000 p.s.i.
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 1.2
- **Media**: Luria broth

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
      <td>Membrane isolation</td>
      <td>High-speed centrifugation</td>
      <td>—</td>
      <td></td>
      <td>Membrane fraction pelleted from clarified lysate</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM ascorbic acid</td>
      <td>Incubated for 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 2 mM ascorbic acid, 0.56% NM</td>
      <td>Eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient, detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> to NM during elution</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl, detergent, 2 mM ascorbic acid</td>
      <td>Polishing step in buffer A with detergent</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Proteolyzed pmUlaA with bound L-ascorbate</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized as a homodimer in the asymmetric unit. Best diffraction to 3.35 Angstrom. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using ecUlaA core domain (PDB 4PR9) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zov">5ZOV</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">METLYNLFLSFNNQVLSKAPFLLGIVACIGYILLKK</span><span class="topo-outside">DT</span><span class="topo-membrane">TTVIKGTIKTIVGFMIVQAGSG</span></span>
<span class="topo-line"><span class="topo-membrane">FLV</span><span class="topo-inside">ANFKPIIEGLSKYHNLTGA</span><span class="topo-unknown">VIDPYTSMQATIQ</span><span class="topo-inside">TM</span><span class="topo-membrane">ADNYAWVGYAVILALFLNILL</span><span class="topo-outside">VV</span></span>
<span class="topo-line"><span class="topo-outside">CRRITGIRTIM</span><span class="topo-membrane">LTGHIMFQQAGLVAVFY</span><span class="topo-inside">MIIGASM</span><span class="topo-membrane">WETVIYTAVLMALYWGISS</span><span class="topo-outside">NIMYKP</span></span>
<span class="topo-line"><span class="topo-outside">TQAVTGGAGFSIG</span><span class="topo-unknown">HQQQIASWIA</span><span class="topo-outside">VKLAPKLGDK</span><span class="topo-unknown">NDTVDKMKLPKWLH</span><span class="topo-outside">I</span><span class="topo-membrane">FHDSISATALVM</span></span>
<span class="topo-line"><span class="topo-membrane">TVFFGIILL</span><span class="topo-inside">S</span><span class="topo-unknown">FGLDNLQQMAG</span><span class="topo-inside">K</span><span class="topo-membrane">THWFMYIFEMGLKFAVAIQIIVTGVRMFVAELS</span><span class="topo-outside">EAFKG</span></span>
<span class="topo-line"><span class="topo-outside">ISERVIPNSVLAIDCAAIYAFSPNAMVFG</span><span class="topo-membrane">FMWGAIGQFVAVGLLL</span><span class="topo-inside">GFSSPIL</span><span class="topo-membrane">IIPGFIPM</span></span>
<span class="topo-line"><span class="topo-membrane">FFSNA</span><span class="topo-outside">TIGVFANQFGGWKSVM</span><span class="topo-membrane">KICFIMGIIEVLGSAWVI</span><span class="topo-inside">HLLATQGTTFN</span><span class="topo-unknown">GWMGMADWAL</span></span>
<span class="topo-line"><span class="topo-unknown">FFPPILQGI</span><span class="topo-inside">VSIP</span><span class="topo-membrane">GFFFVLLTLAIVYMV</span><span class="topo-outside">FASKQLRSEEAA</span><span class="topo-unknown">AAALG</span></span>
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
      <td>37</td>
      <td>38</td>
      <td>37</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>95</td>
      <td>83</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>97</td>
      <td>96</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>118</td>
      <td>98</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>119</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>132</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>155</td>
      <td>149</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>174</td>
      <td>156</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>193</td>
      <td>175</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>203</td>
      <td>194</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>213</td>
      <td>204</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>228</td>
      <td>228</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>249</td>
      <td>229</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>262</td>
      <td>262</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>295</td>
      <td>263</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>329</td>
      <td>296</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>345</td>
      <td>330</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>352</td>
      <td>346</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>365</td>
      <td>353</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>399</td>
      <td>382</td>
      <td>399</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>410</td>
      <td>400</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>430</td>
      <td>433</td>
      <td>430</td>
      <td>433</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>448</td>
      <td>434</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>460</td>
      <td>449</td>
      <td>460</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zov">5ZOV</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">METLYNLFLSFNNQVLSKAPFLLGIVACIGYILLKK</span><span class="topo-outside">DT</span><span class="topo-membrane">TTVIKGTIKTIVGFMIVQAGSG</span></span>
<span class="topo-line"><span class="topo-membrane">FLV</span><span class="topo-inside">ANFKPIIEGLSKYHNLTGA</span><span class="topo-unknown">VIDPYTSMQATIQ</span><span class="topo-inside">TM</span><span class="topo-membrane">ADNYAWVGYAVILALFLNILL</span><span class="topo-outside">VV</span></span>
<span class="topo-line"><span class="topo-outside">CRRITGIRTIM</span><span class="topo-membrane">LTGHIMFQQAGLVAVFY</span><span class="topo-inside">MIIGASM</span><span class="topo-membrane">WETVIYTAVLMALYWGIS</span><span class="topo-outside">SNIMYKP</span></span>
<span class="topo-line"><span class="topo-outside">TQAVTGGAGFSIG</span><span class="topo-unknown">HQQQIASWIA</span><span class="topo-outside">VKLAPKLGDK</span><span class="topo-unknown">NDTVDKMKLPKWLH</span><span class="topo-outside">I</span><span class="topo-membrane">FHDSISATALVM</span></span>
<span class="topo-line"><span class="topo-membrane">TVFFGIILL</span><span class="topo-inside">S</span><span class="topo-unknown">FGLDNLQQMAG</span><span class="topo-inside">K</span><span class="topo-membrane">THWFMYIFEMGLKFAVAIQIIVTGVRMFVAELS</span><span class="topo-outside">EAFKG</span></span>
<span class="topo-line"><span class="topo-outside">ISERVIPNSVLAIDCAAIYAFSPNAMVFG</span><span class="topo-membrane">FMWGAIGQFVAVGLLL</span><span class="topo-inside">GFSSPIL</span><span class="topo-membrane">IIPGFIPM</span></span>
<span class="topo-line"><span class="topo-membrane">FFSNA</span><span class="topo-outside">TIGVFANQFGGWKSVM</span><span class="topo-membrane">KICFIMGIIEVLGSAWVI</span><span class="topo-inside">HLLATQGTTFN</span><span class="topo-unknown">GWMGMADWAL</span></span>
<span class="topo-line"><span class="topo-unknown">FFPPILQGI</span><span class="topo-inside">VSIP</span><span class="topo-membrane">GFFFVLLTLAIVYMV</span><span class="topo-outside">FASKQLRSEEAA</span><span class="topo-unknown">AAALG</span></span>
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
      <td>37</td>
      <td>38</td>
      <td>37</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>63</td>
      <td>39</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>95</td>
      <td>83</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>97</td>
      <td>96</td>
      <td>97</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>118</td>
      <td>98</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>119</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>148</td>
      <td>132</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>155</td>
      <td>149</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>173</td>
      <td>156</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>193</td>
      <td>174</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>203</td>
      <td>194</td>
      <td>203</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>213</td>
      <td>204</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>228</td>
      <td>228</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>249</td>
      <td>229</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>262</td>
      <td>262</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>295</td>
      <td>263</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>329</td>
      <td>296</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>345</td>
      <td>330</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>352</td>
      <td>346</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>365</td>
      <td>353</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>381</td>
      <td>366</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>399</td>
      <td>382</td>
      <td>399</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>400</td>
      <td>410</td>
      <td>400</td>
      <td>410</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>429</td>
      <td>411</td>
      <td>429</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>430</td>
      <td>433</td>
      <td>430</td>
      <td>433</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>448</td>
      <td>434</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>460</td>
      <td>449</td>
      <td>460</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Elevator mechanism of ascorbate transport

The inward-facing structure of pmUlaA completes the transport cycle of the PTS-AG family. Comparison of outward-open (ecUlaA, PDB 4PR9), occluded (ecUlaA), and inward-facing (pmUlaA, PDB 5ZOV) states reveals that ascorbate translocation occurs via a rigid-body movement of the substrate-binding core domain relative to the V motif domains. The core domain undergoes an 11.1 degree rotation and 6.68 Angstrom translocation relative to the V motif. TM2 and TM7 of the V motif domains act as pivots, with the C-terminus of TM7 swinging approximately 46.67 degrees around conserved Gly58 and Gly286 residues to accommodate core domain movement.

### Substrate coordination changes during transport

In the outward-facing state, vitamin C is entirely coordinated by core domain residues. As the core moves inward, Ser59 from V motif 1 contributes a hydrogen bond to the O3 atom of vitamin C in the occluded state. In the inward-facing state, Arg288 from V motif 2 forms a hydrogen bond with the O3 atom, stabilizing the substrate for phosphate transfer from UlaB.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used for membrane solubilization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — Demonstrates elevator mechanism of ascorbate transport
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> — Additive used in purification or crystallization buffers
