---
title: "Squid Rhodopsin (Class A GPCR, Gq-coupled)"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.C800040200, doi/10.1016##j.jmb.2011.08.044, doi/10.1038##nature06925]
verified: false
---

# Squid Rhodopsin (Class A GPCR, Gq-coupled)

## Overview

Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that interacts with Gq-type G-protein to activate the inositol 1,4,5-triphosphate signaling pathway. The first crystal structure of squid rhodopsin was determined at 3.7 A resolution (PDB 2ZIY), revealing seven transmembrane helices and an amphipathic helix H8 similar to bovine rhodopsin and the human beta2-adrenergic receptor. Notably, squid rhodopsin contains a well-structured cytoplasmic region involved in G-protein interaction, which is flexible or disordered in bovine rhodopsin and beta2-AR. The transmembrane helices 5 and 6 are longer and extrude into the cytoplasm. The distal C-terminal tail contains a short hydrophilic alpha-helix CH after palmitoylated cysteine residues. The cytoplasmic region folds compactly, consisting of CL2, the extended TH5/TH6 region, H8, and the distal C-terminal tail including the CH helix. The Schiff base counterion is Tyr-111 (Asn-87 and Asn-185 are within hydrogen-bonding distance of the Schiff base nitrogen). The crystal structures of the primary photoreaction intermediates bathorhodopsin (Batho) and isorhodopsin (Iso, 9-cis) revealed that light energy absorbed by the protein is converted into distortion energy of the retinal polyene chain: upon photoisomerization, the central moiety moves toward the cytoplasmic side while the ionone ring and Schiff base remain relatively fixed, creating a right-handed screwed configuration.


## Publications

### doi/10.1074##jbc.C800040200

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2ziy">2ZIY</a></td>
      <td>3.7 A</td>
      <td>Not reported</td>
      <td>Squid rhodopsin from Todarodes pacificus, C-terminally truncated by V8 protease cleavage (residues 1-373); dark state with 11-cis-retinal. Structure determined by molecular replacement using bovine rhodopsin (PDB 1GZM). Features extended TH5/TH6, structured CL3, and C-terminal helix CH.</td>
      <td>11-cis-retinal</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) from microvillar membranes; C-terminus truncated by V8 protease cleavage at Glu373 or Glu358

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
      <td>Sucrose flotation of rhabdomeric membranes</td>
      <td>--</td>
      <td>HEPES buffer (5 mM HEPES, pH 7.0, 1 mM EDTA, 1 mM DTT) + --</td>
      <td>Squid retina from Todarodes pacificus caught in the Japan Sea</td>
    </tr>
    <tr>
      <td>V8 protease treatment</td>
      <td>Proteolytic cleavage</td>
      <td>--</td>
      <td>HEPES buffer (5 mM HEPES, pH 7.0, 1 mM EDTA, 1 mM DTT) + --</td>
      <td>50:1 w/w rhodopsin:V8 protease, room temperature, 1 h. Removes unique C-terminal proline-rich extension.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.0, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 2% dodecyl maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilization at 4 C for 1 h</td>
    </tr>
    <tr>
      <td>Anion exchange</td>
      <td>DEAE-cellulose column (flow-through)</td>
      <td>DEAE-cellulose</td>
      <td>50 mM HEPES pH 7.0, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Unbound fraction collected</td>
    </tr>
    <tr>
      <td>Lectin affinity</td>
      <td>Concanavalin A-Sepharose 4B</td>
      <td>Concanavalin A-Sepharose 4B</td>
      <td>50 mM HEPES pH 7.0, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 0.2 M alpha-methyl mannoside. Fractions pooled, dialyzed against buffer A, concentrated by ultrafiltration (Amicon Ultra, Millipore).</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/ml purified squid rhodopsin in 10 mM HEPES pH 7.0, 200 mM NaCl, 2 mM dodecyldimethylamine oxide (<a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>), 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7.0, 8% ethylene glycol, 28% PEG 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days to appear, 2 weeks to stop growing</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Data collected at 100 K on beam line BL45XU at SPring-8</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined by molecular replacement using bovine rhodopsin (PDB 1GZM) as search model. Refinement performed with CNS, REFMAC5, and O. B-factor sharpening used with Bsharp values -50 to -150 A2. Coordinates deposited as PDB 2ZIY. V8 protease treatment removes C-terminal proline-rich extension.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2ziy">2ZIY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GR</span><span class="topo-inside">DLRDNETWWYNPSIIVHPHWREFDQVPDA</span><span class="topo-membrane">VYYSLGIFIGICGIIGCGGNGIVIY</span><span class="topo-outside">LFTKTKSLQTPANM</span><span class="topo-membrane">FIINLAFSDFTFSLVNGFPLMTISCF</span><span class="topo-inside">LKKWIFGFA</span><span class="topo-membrane">ACKVYGFIGGIFGFM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SIMTMAMISI</span><span class="topo-outside">DRYNVIGRPMAASKKMSHRRA</span><span class="topo-membrane">FIMIIFVWLWSVLWAIGPIFGWG</span><span class="topo-inside">AYTLEGVLCNCSFDYISRDSTT</span><span class="topo-membrane">RSNILCMFILGFFGPILIIFFCYF</span><span class="topo-outside">NIVMSVSNHEKEMAAMAKRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NAKELRKAQAGANAEMRLAKI</span><span class="topo-membrane">SIVIVSQFLLSWSPYAVVALL</span><span class="topo-inside">AQFGPLEWVTPY</span><span class="topo-membrane">AAQLPVMFAKASAIHNPMIYSV</span><span class="topo-outside">SHPKFREAISQTFPWVLTCCQFDDKETEDDKDAETEIPAGESSD</span></span>
<span class="topo-ruler">       370  </span>
<span class="topo-line"><span class="topo-outside">AAPSADAAQMKE</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>31</td>
      <td>4</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>56</td>
      <td>33</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>58</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>96</td>
      <td>72</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>105</td>
      <td>98</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>130</td>
      <td>107</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>151</td>
      <td>132</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>153</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>196</td>
      <td>176</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>220</td>
      <td>198</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>261</td>
      <td>222</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>282</td>
      <td>263</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>294</td>
      <td>284</td>
      <td>295</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>296</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>372</td>
      <td>318</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.jmb.2011.08.044

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3p1l">3P1L</a></td>
      <td>2.8 A</td>
      <td>P62</td>
      <td>C-terminally truncated <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">squid rhodopsin</a> (residues 1-372, cleaved at Glu373 by V8 protease); bathorhodopsin state (all-trans retinal)</td>
      <td>all-trans retinal</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3p1k">3P1K</a></td>
      <td>2.7 A</td>
      <td>P62</td>
      <td>C-terminally truncated <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">squid rhodopsin</a> (residues 1-357, cleaved at Glu358 by V8 protease); isorhodopsin state (9-cis retinal)</td>
      <td>9-cis retinal</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2brs">2BRS</a></td>
      <td>2.7 A</td>
      <td>P62</td>
      <td>C-terminally truncated <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">squid rhodopsin</a> (dark state, 11-cis)</td>
      <td>11-cis retinal</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) from microvillar membranes; C-terminus truncated by V8 protease cleavage at Glu373 or Glu358

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
      <td>Membrane extraction</td>
      <td>Selective extraction from squid microvillar membranes</td>
      <td>--</td>
      <td>Tris buffer with zinc <a href="/xray-mp-wiki/reagents/buffers/acetate/">acetate</a> + n-octyl beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Rhodopsin extracted selectively from microvillar membranes; all manipulations performed in dim red light (>640 nm)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>In meso crystallization (hexagonal P62 crystals)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Truncated <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">squid rhodopsin</a> solubilized in n-octyl beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryogenic)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K; crystals handled in dim red light (>640 nm)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Hexagonal P62 crystals. Data collected at SPring-8 BL41XU using a 10-micrometer microbeam. Photoreaction states trapped by illumination at specific wavelengths: blue light (473 nm) for bathorhodopsin, yellow light (560 nm) for isorhodopsin, red light (635 nm) for dark-state rhodopsin.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##nature06925

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2brs">2BRS</a></td>
      <td>2.5 A</td>
      <td>P62</td>
      <td>C-terminally truncated <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">squid rhodopsin</a> (residues Glu9-Glu358, cleaved at Glu373 by V8 protease; dark state, 11-cis retinal)</td>
      <td>11-cis retinal</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) from microvillar membranes; C-terminus truncated by V8 protease cleavage at Glu373 or Glu358

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C-terminally truncated squid rhodopsin solubilized in n-octyl beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>3.2 M ammonium sulfate, 32 mM MES pH 6.4, 38 mM EDTA, 10 mM beta-mercaptoethanol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>>6 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% sucrose, flash-frozen in liquid propane at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Hexagonal P62 crystals. Extracted from microvillar membranes with octylglucoside in presence of zinc acetate. V8-protease cleavage at Glu373.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Extended TH5 and TH6 form a structured cytoplasmic domain for G-protein coupling

The 3.7 A crystal structure of squid rhodopsin (PDB 2ZIY) revealed that transmembrane helices 5 and 6 are longer than in bovine rhodopsin and the human beta2-adrenergic receptor, extruding into the cytoplasm. This extension is accompanied by a 12-amino-acid insertion in the CL3 region. TH5 elongates to Lys-239 with a bend at His-230, while TH6 extends from Glu-245 with a bend at Ser-275 before Pro-276 and Tyr-277. Together with CL2, H8, and the distal C-terminal tail, these elements form a compact, well-ordered cytoplasmic domain that is thought to mediate selective recognition and activation of the Gq protein. In bovine rhodopsin and beta2-AR, the corresponding CL3 region is either flexible, disordered, or substituted.

### Short hydrophilic C-terminal helix CH

The distal C-terminal tail of squid rhodopsin contains a short hydrophilic alpha-helix (CH) formed by residues Asp-341 to Asp-347, located after the palmitoylated cysteine residues that anchor H8 to the membrane. The residues in the distal C-terminal tail interact with neighboring residues in CL2, the extruded TH5/TH6, and the short helix H8. After helix CH, the C-terminal tail from Lys-348 to Glu-373 interacts closely with the extended TH5/TH6 region and returns to the putative membrane surface in an extended structure via polar interactions with CL2.

### Schiff base environment and counterion

The Schiff base connecting 11-cis-retinal to Lys-305 has Tyr-111 as its counterion, in contrast to bovine rhodopsin where Glu-113 serves this role. Asn-87 and Asn-185 residues are located within hydrogen-bonding distances from the nitrogen atom of the Schiff base. This arrangement is consistent with a slower photoisomerization rate in squid rhodopsin compared to bovine rhodopsin.

### Distinct electrostatic profile for Gq coupling specificity

The electrostatic potentials of the cytoplasmic surfaces of squid rhodopsin have a profile characteristic of intracellular GPCR domains. The distinct electrostatic profiles between squid rhodopsin (Gq-coupled) and bovine rhodopsin (Gt-coupled) are located around the TH5 intracellular surface region. The corresponding TH5 region was important for Gi coupling but less so for Gq in BLT1 (leukotriene B4 receptor). The compact hydrophilic intracellular domain of squid rhodopsin, anchored by cysteine palmitoylations at H8, is proposed to participate in recognizing and activating the Gq protein on the lateral membrane surface.

### Retinal distortion stores light energy in bathorhodopsin

The bathorhodopsin structure reveals that upon photoisomerization (11-cis to all-trans), the retinal central moiety moves largely toward the cytoplasmic side while the ionone ring and Schiff base undergo limited movement. The polyene chain takes on a right-handed screwed configuration with twisted C7=C8, C9=C10, and C11=C12 bonds. The C13 methyl pushes Ser187 into the E-II loop, and the C9 methyl pushes Phe188. This distortion stores approximately 35 kcal/mol of energy, conserved between vertebrate and invertebrate rhodopsins.

### Structural differences from [bovine rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/)

[Squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) differs from [bovine rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) in the retinal-binding pocket: the beta-ionone ring is surrounded by aromatic residues (vs glutamate in bovine), and the retinal polyene chain associates with helix III backbone over three helical turns (vs polar residue Thr118 in bovine). The Schiff base H-bond partner is Asn87 or Tyr111 (vs Gly89 and Glu113 in bovine). These differences slow cis-trans isomerization in [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) compared to bovine while maintaining similar bathorhodopsin energy levels.

### X-ray radiation damage in rhodopsin

Significant X-ray radiation damage was characterized: (1) retinal isomerization to an orange species (precursor of retro form) at approximately 4 x 10^14 photons/mm^2, (2) breakage of disulfide bond between Cys108 and Cys186, (3) loss of electron density at Asp80 (decarboxylation/radiolysis). These changes produce photochemically inactive products that can be distinguished from functional photointermediates. Data collection must account for approximately 50% protein damage at doses of 3 x 10^15 photons/mm^2.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Primary detergent for squid rhodopsin extraction and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization in 2% DDM for the 3.7 A structure determination
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Crystallization precipitant at 3.2 M in sitting-drop vapor diffusion
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES (2-(N-Morpholino)ethanesulfonic Acid)</a> — Crystallization buffer at 32 mM, pH 6.4
- <a href="/xray-mp-wiki/reagents/ligands/11-cis-retinal/">11-cis-Retinal</a> — Chromophore covalently bound to Lys305 via protonated Schiff base in the dark state
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (sodium acetate)</a> — Zinc acetate used in squid rhodopsin extraction buffer
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Used in extraction buffer for squid rhodopsin purification
- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin (Dark State)</a> — Comparative vertebrate rhodopsin; key reference for retinal-binding pocket and cytoplasmic region differences
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Comparative GPCR structure; squid rhodopsin has structured CL3 vs disordered in beta2 AR
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/">GPCR G-Protein Coupling</a> — Squid rhodopsin is model for Gq-coupled GPCR with structured cytoplasmic domain
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Cryoprotectant at 20% used for flash-freezing squid rhodopsin crystals
