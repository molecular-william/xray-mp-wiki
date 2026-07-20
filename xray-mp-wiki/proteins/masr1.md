---
title: "Delta14-sterol reductase MaSR1 from Methylomicrobium alcaliphilum"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13797]
verified: agent
uniprot_id: G4SW86
---

# Delta14-sterol reductase MaSR1 from Methylomicrobium alcaliphilum

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G4SW86">UniProt: G4SW86</a>

<span class="expr-badge">Methylomicrobium alcaliphilum</span>

## Overview

MaSR1 is a Delta14-sterol reductase from the methanotrophic bacterium Methylomicrobium alcaliphilum 20Z, a homologue of human C14SR (TM7SF2), LBR (lamin B receptor) and DHCR7 (7-dehydrocholesterol reductase). The structure, determined at 2.6 A resolution, reveals ten transmembrane segments (TM1-10) with the catalytic domain comprising the C-terminal half (TM6-10). The enzyme contains two interconnected pockets: one facing the cytoplasm that houses the NADPH cofactor, and another accessible from the lipid bilayer for sterol substrate binding. MaSR1 can reduce the double bond of a [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) biosynthetic intermediate, demonstrating functional conservation with human C14SR.

## Publications

### doi/10.1038##nature13797

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4quv">4QUV</a></td>
      <td>2.6</td>
      <td>unknown</td>
      <td>Full-length MaSR1 with N-terminal 8-His tag, NADPH-bound</td>
      <td>NADPH</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: MaSR1 from Methylomicrobium alcaliphilum 20Z (NCBI GI: 503913803), cloned into pET-21b with N-terminal 8-His tag

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
      <td>Membrane preparation</td>
      <td>French press cell disruption and differential centrifugation</td>
      <td>--</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl + --</td>
      <td>Two passes at 15,000 p.s.i.; low-speed spin followed by high-speed ultracentrifugation</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Incubated for 1 h at 4 C; then centrifuged to obtain solubilized fraction</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-NTA agarose (Qiagen)</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in same buffer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl + 0.4% beta-NG (<a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a>)</td>
      <td>Peak fraction collected for crystallization</td>
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
      <td>MaSR1 in 25 mM Tris-Cl pH 8.0, 150 mM NaCl, 0.4% beta-NG, 2 mM NADPH</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M Tris-Cl pH 7.0, 0.2 M NH4Ac, 30% (v/v) pentaerythritol ethoxylate (15/4 EO/OH)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct flash-freezing in cold nitrogen stream at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> added to crystallization buffer at 1% (v/v) final concentration to improve diffraction. SeMet-labelled protein crystallized in same buffer plus 6 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>. Platinum derivatives obtained by soaking native crystals for 12 h in mother liquor plus 10 mg/ml K2Pt(NO2)4.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4quv">4QUV</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSEQESRDNAAVDAVRQKYGFG</span><span class="topo-outside">F</span><span class="topo-membrane">SWLVLMIALPPLVYYLW</span><span class="topo-inside">ICVTYYQGELVFTSD</span><span class="topo-unknown">AAAWRRFW</span><span class="topo-inside">SHVAPPTWHA</span><span class="topo-membrane">AGLYAAWFLGQAALQVWAP</span><span class="topo-outside">GPTVQGMKLPDGSRLDYRM</span><span class="topo-membrane">NGIFSFLFT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAVVFG</span><span class="topo-inside">LVTMGWLDATVLYDQLGPL</span><span class="topo-membrane">LTVVNIFTFVFAGFLYF</span><span class="topo-outside">WG</span><span class="topo-unknown">LNGKQWERPTGR</span><span class="topo-outside">PFYDYFMGTALNPRIGSLDL</span><span class="topo-membrane">KLFCEARPGMIFWLLMNL</span><span class="topo-inside">SMAAKQYELHGTVTVP</span><span class="topo-membrane">MLLVVGFQSF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">YLIDYFIHE</span><span class="topo-outside">EAVLTTWDIKHEKFG</span><span class="topo-membrane">WMLCWGDLVWLPFTYTLQA</span><span class="topo-inside">QYLVHHTHDLPV</span><span class="topo-membrane">WGIIAIVALNLAGYAIFR</span><span class="topo-outside">GANIQKHHFRRDPNRIVWGKPAKYIKTKQGSLLLTSGWWGIARHMNY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       </span>
<span class="topo-line"><span class="topo-membrane">FGDLMIALSWCLPAAF</span><span class="topo-inside">GS</span><span class="topo-membrane">PIPYFHIVYFTILLL</span><span class="topo-outside">HREKRDDAMCLAKYGEDWLQYRKKVPWRIVPKIY</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>40</td>
      <td>24</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>55</td>
      <td>41</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>63</td>
      <td>56</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>64</td>
      <td>73</td>
      <td>64</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>92</td>
      <td>74</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>111</td>
      <td>93</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>126</td>
      <td>112</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>127</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>162</td>
      <td>146</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>164</td>
      <td>163</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>196</td>
      <td>177</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>214</td>
      <td>197</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>230</td>
      <td>215</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>249</td>
      <td>231</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>264</td>
      <td>250</td>
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
      <td>284</td>
      <td>295</td>
      <td>284</td>
      <td>295</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>313</td>
      <td>296</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>360</td>
      <td>314</td>
      <td>360</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>376</td>
      <td>361</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>378</td>
      <td>377</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>393</td>
      <td>379</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>427</td>
      <td>394</td>
      <td>427</td>
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

### Two-pocket catalytic architecture

The C-terminal half (TM6-10) of MaSR1 contains two interconnected pockets. The NADPH-binding pocket faces the cytoplasm and houses the adenine-ribose moiety of NADPH (the nicotinamide ring is disordered in the absence of substrate). The sterol-binding pocket is accessible from the lipid bilayer. The reducing end of NADPH meets the sterol substrate at the juncture of the two pockets.

### Signature motif for sterol recognition

The sterol binding pocket contains a signature motif of Tyr241 bonded to Asp363 that forms triangular hydrogen bonds coordinating the beta-3 hydroxyl of the sterol substrate. This is analogous to Tyr58-Glu120 in soluble steroid 5-beta-reductase (AKR1D1). The Y241F/D363A double mutant loses sterol reductase activity.

### Disease relevance

Mutations in human homologues LBR and DHCR7 cause genetic diseases including Pelger-Huet anomaly (PHA), Greenberg skeletal dysplasia (HEM), and Smith-Lemli-Opitz syndrome (SLOS). Structural models based on MaSR1 map these disease mutations to the sterol reductase catalytic domain, affecting cofactor binding or sterol entry/binding sites.

### Structural homology with ICMT

A DALI search identified isoprenylcysteine carboxyl methyltransferase (ICMT, PDB 4A2N) as the closest structural homologue for the TM6-10 segments, suggesting a similar role for the C14SR domain of LBR in recognizing farnesylated cysteine substrates such as prelamin A or lamin B.

### Substrate promiscuity

MaSR1 can reduce the double bond of both C27Delta8,14 (a [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) intermediate) and yeast ergosta-8,14-dien-ol, demonstrating broad substrate recognition consistent with LBR which compensates for C14SR function in knockout mice.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl-beta-D-glucopyranoside (OG/beta-NG)</a> — Detergent used in final purification and crystallization
- <a href="/xray-mp-wiki/reagents/ligands/nadph/">NADPH</a> — Reducing cofactor bound in the NADPH-binding pocket
- <a href="/xray-mp-wiki/methods/purification/nickel-nta-affinity-chromatography/">Nickel-NTA Affinity Chromatography</a> — Primary purification method via His-tag
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Final purification step on Superdex-200
- <a href="/xray-mp-wiki/reagents/additives/dtt/">Dithiothreitol (DTT)</a> — Reducing agent used in SeMet crystallization
- <a href="/xray-mp-wiki/proteins/enzymes/beetle-icmt/">ICMT from beetles</a> — Closest structural homologue identified by DALI search
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
