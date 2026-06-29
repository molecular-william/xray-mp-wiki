---
title: "VcmN MATE Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.10.004]
verified: false
---

# VcmN MATE Transporter

## Overview

VcmN is a multidrug and toxic compound extrusion (MATE) transporter from the pathogenic bacterium Vibrio cholerae. It belongs to the DinF subfamily of MATE transporters and is driven by an H+ gradient across the membrane. High-resolution crystal structures revealed two distinct conformations associated with different pH conditions: a straight form (PDB 6IDP, 2.2 A) at pH 7.5-8.0 and a bent form (PDB 6IDR, 2.5 A) at pH 5.0, demonstrating that protonation of the conserved Asp35 induces bending of transmembrane helix 1 (TM1) via rearrangement of the hydrogen-bonding network in the N-lobe. The D35N mutant structure (PDB 6IDS, 2.79 A) captured an intermediate conformation, revealing that Asn substitution does not fully mimic protonation. The transport cycle involves a common step among prokaryotic H+-coupled MATE transporters: rearrangement of the N-lobe hydrogen-bonding network, TM1 bending, and shrinkage of the substrate-binding cavity.

## Publications

### doi/10.1016##j.str.2018.10.004

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6idp">6IDP</a></td>
      <td>2.21 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>VcmN C-terminally truncated (residues 1-434) from Vibrio cholerae, crystallized by LCP at pH 7.5-8.0</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (mimic of substrate in N-lobe cavity)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6idr">6IDR</a></td>
      <td>2.50 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>VcmN C-terminally truncated (residues 1-434) from Vibrio cholerae, crystallized by LCP at pH 5.0</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (mimic of substrate in N-lobe cavity)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ids">6IDS</a></td>
      <td>2.79 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>VcmN C-terminally truncated (residues 1-434) D35N mutant from Vibrio cholerae</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (mimic of substrate in N-lobe cavity)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41(DE3) Rosetta strain
- **Construct**: VcmN (1-434) with C-terminal His-tag from Vibrio cholerae

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
      <td>Homogenization and ultracentrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl + --</td>
      <td>Cells disrupted by sonication; membranes collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl, <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tag purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step</td>
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
      <td>Purified VcmN in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> LCP</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals frozen in liquid nitrogen with reservoir solution supplemented with 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystal forms obtained from different pH conditions: straight form (crystal I, pH 7.5-8.0) and bent form (crystal II, pH 5.0). The D35N mutant was crystallized similarly. X-ray data collected at SPring-8 BL32XU (crystals I, II) and Diamond Light Source I24 (D35N). Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/proteins/abc-transporters/pfmate/">PFMATE</a> structure (PDB 3VVN) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6idp">6IDP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAM</span><span class="topo-inside">QTSTSSLAKQL</span><span class="topo-membrane">FQMTWPMLFGVLSLMSFQLVDS</span><span class="topo-outside">AFIGQLGVLPLAAQGFT</span><span class="topo-membrane">MPIQMVI</span></span>
<span class="topo-line"><span class="topo-membrane">IGIQVGLGIATT</span><span class="topo-inside">AVISRAIGAGKTEYAKQLGGLV</span><span class="topo-membrane">IVIGGIGVALIALVLYLLR</span><span class="topo-outside">QPLLGLL</span></span>
<span class="topo-line"><span class="topo-outside">GAPETVFAIID</span><span class="topo-membrane">HYWLWWLASAWTGAMLYFYYSVCR</span><span class="topo-inside">ANGNT</span><span class="topo-membrane">LLPGTLMMVTSVLNLILDPI</span></span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-outside">FTFDLGID</span><span class="topo-membrane">GAAIATIIAFGVGIAIVA</span><span class="topo-inside">PKVAQRQWTSYQWQDLNISQSLTAL</span><span class="topo-membrane">GHIMGPA</span></span>
<span class="topo-line"><span class="topo-membrane">MLSQLLPPLSSMFA</span><span class="topo-outside">TKLLASFGTAAVAAWAL</span><span class="topo-membrane">GSRFEFFALVAVLAMTMSLP</span><span class="topo-inside">PMIGRMLGA</span></span>
<span class="topo-line"><span class="topo-inside">KEITHIRQLVR</span><span class="topo-membrane">IACQFVLGFQLLIALVTYVFA</span><span class="topo-unknown">TPLAELM</span><span class="topo-outside">TSETEVSQILNLH</span><span class="topo-membrane">LVIVPISL</span></span>
<span class="topo-line"><span class="topo-membrane">GALGICMLMVSVANA</span><span class="topo-inside">LGK</span><span class="topo-membrane">SYVALTISALRLFAFYLPCLWLG</span><span class="topo-outside">AHFYGIEGL</span><span class="topo-membrane">FIGALVGNII</span></span>
<span class="topo-line"><span class="topo-membrane">AGWAAWLAYQK</span><span class="topo-inside">ALRSENLYFQ</span></span>
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
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>36</td>
      <td>15</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>37</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>72</td>
      <td>54</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>73</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>113</td>
      <td>95</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>131</td>
      <td>114</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>155</td>
      <td>132</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>160</td>
      <td>156</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>190</td>
      <td>183</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>233</td>
      <td>209</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>254</td>
      <td>234</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>271</td>
      <td>255</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>291</td>
      <td>272</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>292</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>332</td>
      <td>312</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>339</td>
      <td>333</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>340</td>
      <td>352</td>
      <td>340</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>375</td>
      <td>353</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>378</td>
      <td>376</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>401</td>
      <td>379</td>
      <td>401</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>410</td>
      <td>402</td>
      <td>410</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>411</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>441</td>
      <td>432</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6idr">6IDR</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAM</span><span class="topo-outside">QTSTSSLAKQLFQMT</span><span class="topo-membrane">WPMLFGVLSLMSFQLVDS</span><span class="topo-inside">AFIGQLGVLPLAAQGFT</span><span class="topo-membrane">MPIQMVI</span></span>
<span class="topo-line"><span class="topo-membrane">IGIQVGLGIAT</span><span class="topo-outside">TAVISRAIGAGKTEYAKQLGGLV</span><span class="topo-membrane">IVIGGIGVALIALVLYLL</span><span class="topo-unknown">RQPLLGLL</span></span>
<span class="topo-line"><span class="topo-inside">GAPETVFAIIDHY</span><span class="topo-membrane">WLWWLASAWTGAMLYFYYS</span><span class="topo-outside">VCRANGNT</span><span class="topo-membrane">LLPGTLMMVTSVLNLILDPI</span></span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-inside">FTFDLGID</span><span class="topo-membrane">GAAIATIIAFGVGIAIVA</span><span class="topo-outside">PKVAQRQWTSYQWQDLN</span><span class="topo-unknown">ISQSLTAL</span><span class="topo-membrane">GHIMGPA</span></span>
<span class="topo-line"><span class="topo-membrane">MLSQLLPPLSSMFA</span><span class="topo-inside">TKLLASFGTAAVAAWAL</span><span class="topo-membrane">GSRFEFFALVAVLAMTMSLP</span><span class="topo-outside">PMIGRMLGA</span></span>
<span class="topo-line"><span class="topo-outside">KEITHIRQLVRIA</span><span class="topo-membrane">CQFVLGFQLLIALVTYVFA</span><span class="topo-unknown">TPLAELM</span><span class="topo-inside">TSETEVSQILNLH</span><span class="topo-membrane">LVIVPISL</span></span>
<span class="topo-line"><span class="topo-membrane">GALGICMLMVSVAN</span><span class="topo-outside">ALGK</span><span class="topo-membrane">SYVALTISALRLFAFYLPCLWLG</span><span class="topo-inside">AHFYGIEG</span><span class="topo-membrane">LFIGALVGNII</span></span>
<span class="topo-line"><span class="topo-membrane">AGWAAWLAY</span><span class="topo-outside">QKALRSENLYFQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>4</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>19</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>37</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>54</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>94</td>
      <td>72</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>112</td>
      <td>95</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>121</td>
      <td>133</td>
      <td>121</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>152</td>
      <td>134</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>160</td>
      <td>153</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>190</td>
      <td>183</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>191</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>225</td>
      <td>209</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>233</td>
      <td>226</td>
      <td>233</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>234</td>
      <td>254</td>
      <td>234</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>271</td>
      <td>255</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>291</td>
      <td>272</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>332</td>
      <td>314</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>339</td>
      <td>333</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>340</td>
      <td>352</td>
      <td>340</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>374</td>
      <td>353</td>
      <td>374</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>378</td>
      <td>375</td>
      <td>378</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>401</td>
      <td>379</td>
      <td>401</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>409</td>
      <td>402</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>429</td>
      <td>410</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>430</td>
      <td>441</td>
      <td>430</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ids">6IDS</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAM</span><span class="topo-inside">QTSTSSLAKQL</span><span class="topo-membrane">FQMTWPMLFGVLSLMSFQLVNS</span><span class="topo-outside">AFIGQLGVLPLAAQGF</span><span class="topo-membrane">TMPIQMVI</span></span>
<span class="topo-line"><span class="topo-membrane">IGIQVGLGIATT</span><span class="topo-inside">AVISRAIGAGKTEYAKQLGGLV</span><span class="topo-membrane">IVIGGIGVALIALVLYLLR</span><span class="topo-unknown">QPLLGLL</span></span>
<span class="topo-line"><span class="topo-outside">GAPETVFAIID</span><span class="topo-membrane">HYWLWWLASAWTGAMLYFYYSVCR</span><span class="topo-inside">ANGNT</span><span class="topo-membrane">LLPGTLMMVTSVLNLILDPI</span></span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-outside">FTFDLGID</span><span class="topo-membrane">GAAIATIIAFGVGIAIVAP</span><span class="topo-inside">KVAQRQWTSYQWQDLN</span><span class="topo-unknown">ISQSLTAL</span><span class="topo-membrane">GHIMGPA</span></span>
<span class="topo-line"><span class="topo-membrane">MLSQLLPPLSSMFA</span><span class="topo-outside">TKLLASFGTAAVAAW</span><span class="topo-membrane">ALGSRFEFFALVAVLAMTMSLP</span><span class="topo-inside">PMIGRMLGA</span></span>
<span class="topo-line"><span class="topo-inside">KEITHIRQLV</span><span class="topo-membrane">RIACQFVLGFQLLIALVTYVFA</span><span class="topo-unknown">TPLAELM</span><span class="topo-outside">TSETEVSQILNLH</span><span class="topo-membrane">LVIVPISL</span></span>
<span class="topo-line"><span class="topo-membrane">GALGICMLMVSVANA</span><span class="topo-inside">LGK</span><span class="topo-membrane">SYVALTISALRLFAFYLPCLWLG</span><span class="topo-outside">AHFYGIEG</span><span class="topo-membrane">LFIGALVGNII</span></span>
<span class="topo-line"><span class="topo-membrane">AGWAAWLAYQK</span><span class="topo-inside">ALRSENLYFQ</span></span>
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
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>36</td>
      <td>15</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>52</td>
      <td>37</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>72</td>
      <td>53</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>94</td>
      <td>73</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>113</td>
      <td>95</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>120</td>
      <td>114</td>
      <td>120</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>121</td>
      <td>131</td>
      <td>121</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>155</td>
      <td>132</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>160</td>
      <td>156</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>190</td>
      <td>183</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>209</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>225</td>
      <td>210</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>233</td>
      <td>226</td>
      <td>233</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>234</td>
      <td>254</td>
      <td>234</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>269</td>
      <td>255</td>
      <td>269</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>291</td>
      <td>270</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>339</td>
      <td>333</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>340</td>
      <td>352</td>
      <td>340</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>375</td>
      <td>353</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>378</td>
      <td>376</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>401</td>
      <td>379</td>
      <td>401</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>409</td>
      <td>402</td>
      <td>409</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>431</td>
      <td>410</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>441</td>
      <td>432</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### H+-dependent conformational change of TM1

The crystal structures of VcmN in two distinct conformations (straight and bent forms) revealed that protonation of the conserved Asp35 in TM1 induces bending of the TM1 helix at Pro20 and Gly24. This rearrangement of the hydrogen-bonding network in the N-lobe causes shrinkage of the substrate-binding cavity, which likely extrudes bound substrates toward the extracellular side. The D35N mutation only partially mimics protonation, capturing an intermediate TM1 conformation.

### Conserved transport mechanism in prokaryotic H+-coupled MATE transporters

Structural comparison of VcmN with [PFMATE](/xray-mp-wiki/proteins/abc-transporters/pfmate/) (Pyrococcus furiosus) reveals a similar TM1 bending mechanism, suggesting a conserved step in the transport cycle shared among prokaryotic H+-driven MATE transporters. The key residues involved in the hydrogen-bonding network (Asp35, Asn174, Asp178, Thr196) and the TM1 kink (Pro20) are conserved in both H+-driven and Na+-driven DinF subfamily members.

### D35N does not fully mimic protonation

The D35N mutant structure shows that Asn substitution does not completely reproduce the protonated state of Asp35. The TM1 helix of the D35N mutant occupies a conformation intermediate between the straight and bent forms, indicating that the differences in chemical properties between Asp and Asn are not negligible for functional studies of proton-driven transporters.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization and purification detergent
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used for LCP crystallization; monoolein molecules in N-lobe cavity mimic substrates
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Primary crystallization method for VcmN
- <a href="/xray-mp-wiki/proteins/abc-transporters/pfmate/">PfMATE Transporter</a> — Homologous MATE transporter used as search model for molecular replacement
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
