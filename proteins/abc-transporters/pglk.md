---
title: "PglK ABC Flippase"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.01.013, doi/10.1038##nature14953]
verified: false
---

# PglK ABC Flippase

## Overview

PglK is an ATP-binding cassette (ABC) flippase from Campylobacter jejuni that translocates lipid-linked oligosaccharide (LLO) across the inner membrane, essential for asparagine-linked protein N-glycosylation. The crystal structure of PglK-E510Q bound to ATPgammaS (PDB 6HRC, 3.2 A) captured an outward semi-occluded state with the two nucleotide-binding domains (NBDs) forming an asymmetric closed dimer. The structure reveals a vase-like cavity with an arginine belt that interacts with the pyrophosphate group of LLO. Combined with extensive molecular dynamics simulations, this study supports a non-alternating-access mechanism for LLO translocation and identifies a surface recognition site between TM2 and TM5 for LLO, suggesting a substrate-hunting mechanism.

## Publications

### doi/10.1016##j.str.2019.01.013

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hrc">6HRC</a></td>
      <td>3.2 A</td>
      <td>--</td>
      <td>PglK-E510Q mutant from Campylobacter jejuni, co-crystallized with ATPgammaS and MgCl2</td>
      <td>ATPgammaS (2 molecules), Mg2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21-Gold (DE3) competent cells
- **Construct**: PglK-E510Q mutant (Walker-B glutamate replaced by Gln) from C. jejuni

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
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Standard membrane protein purification protocol</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA superflow</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tag purification with stepwise elution</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol)</td>
      <td>Buffer exchanged to <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified PglK-E510Q in <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> with ATPgammaS and MgCl2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Na3Citrate pH 5.5, 100 mM NaCl, 18-22% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Long needle crystals appeared over several days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals cryoprotected with reservoir solution supplemented with 25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> and flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>PglK-E510Q co-crystallized with ATPgammaS and MgCl2 yielded long needle crystals showing anisotropic X-ray diffraction to 3.2 A. Data collected at beamline X06SA at the Swiss Light Source. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. The structure shows an outward semi-occluded state with a vase-like cavity and arginine belt essential for LLO binding.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hrc">6HRC</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-outside">LSKEDKN</span><span class="topo-membrane">FLFFLLVFSVFVSFIETFAISLV</span><span class="topo-inside">MPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-inside">KEYLNIPVFEIIVYFGVG</span><span class="topo-membrane">LIVFYVFRALLNAYYFHLLARFS</span><span class="topo-outside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-outside">YEKFTQKNQSEILKSITGEVYNLSTMI</span><span class="topo-membrane">SSFLLLMSEIFVVLLLYALML</span><span class="topo-inside">LINYKIT</span><span class="topo-membrane">LFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-outside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-outside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVL</span><span class="topo-inside">VFIVVFLVLKNESDISGILSTISIFV</span><span class="topo-membrane">LAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYHDLL</span><span class="topo-outside">YYHSSLNIIYQNLRQEEENAAEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-outside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-outside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-outside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-outside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>15</td>
      <td>9</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>38</td>
      <td>16</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>78</td>
      <td>39</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>101</td>
      <td>79</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>147</td>
      <td>102</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>148</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>169</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>297</td>
      <td>272</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>564</td>
      <td>319</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hrc">6HRC</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-outside">LSKEDKN</span><span class="topo-membrane">FLFFLLVFSVFVSFIETFAISL</span><span class="topo-inside">VMPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-inside">KEYLNIPVFEIIVYFGVG</span><span class="topo-membrane">LIVFYVFRALLNAYYFHLLARFS</span><span class="topo-outside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-outside">YEKFTQKNQSEILKSITGEVYNLSTM</span><span class="topo-membrane">ISSFLLLMSEIFVVLLLYALML</span><span class="topo-inside">LINYKIT</span><span class="topo-membrane">LFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-outside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-outside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVL</span><span class="topo-inside">VFIVVFLVLKNESDISGILSTISIFV</span><span class="topo-membrane">LAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYHDLL</span><span class="topo-outside">YYHSSLNIIYQNLRQEEENAAEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-outside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-outside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-outside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-outside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>15</td>
      <td>9</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>37</td>
      <td>16</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>78</td>
      <td>38</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>101</td>
      <td>79</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>146</td>
      <td>102</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>169</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>176</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>271</td>
      <td>251</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>297</td>
      <td>272</td>
      <td>297</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>564</td>
      <td>319</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##nature14953

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a></td>
      <td>2.9</td>
      <td>P1</td>
      <td>PglK-E510Q mutant, apo-inward-1 state</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a></td>
      <td>3.9</td>
      <td>P12_1</td>
      <td>PglK-E510Q mutant, apo-inward-2 state</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a></td>
      <td>5.9</td>
      <td>P4_12_12</td>
      <td>PglK-E510Q mutant, outward-occluded state co-crystallized with ADP and MgCl2</td>
      <td>ADP, Mg2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21-Gold (DE3) competent cells
- **Construct**: PglK-E510Q mutant (Walker-B glutamate replaced by Gln) from C. jejuni

**Purification:**

- **Expression system**: E. coli BL21-Gold (DE3)
- **Expression construct**: PglK with N-terminal His10 tag
- **Tag info**: N-terminal His10 affinity tag

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
      <td>Modified TB medium with 1% <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> + --</td>
      <td>30 L fermentor; induced with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> for 1 h at 37 C</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Microfluidizer</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 7 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.5 mM PMSF + --</td>
      <td>M-110L microfluidizer at 15,000 psi chamber pressure</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl + --</td>
      <td>Membranes pelleted at 100,000g for 30 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 7 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Stirring for 2 h at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>NiNTA superflow (Qiagen)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.016-0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (first wash), then 0.016-0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (second wash)</td>
      <td>Eluted with 200 mM NaCl, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL (GE Healthcare)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl + 0.016-0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Peak fractions pooled and concentrated to 8-10 mg/ml</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~8-10 mg/ml in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 200 mM NaCl, 0.016-0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop or hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PglK-E510Q in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (apo-inward-1, 2.9 A) or <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> (apo-inward-2, 3.9 A)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Various reservoir conditions (see PDB entries for full details)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo-inward-1 crystallized in <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> at 2.9 A resolution (space group P1). Apo-inward-2 crystallized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> at 3.9 A (space group P12_1). Outward-occluded state crystallized with 5-10 mM ADP and 5-10 mM MgCl2 at 5.9 A (space group P4_12_12). Side-chain register of outward-occluded model validated by anomalous diffraction data of Hg-soaked crystals and <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> derivative.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAISLV</span><span class="topo-outside">MPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTMI</span><span class="topo-membrane">SSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYH</span><span class="topo-inside">DLLYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>38</td>
      <td>12</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>79</td>
      <td>39</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>147</td>
      <td>102</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>148</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>564</td>
      <td>316</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAIS</span><span class="topo-outside">LVMPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTM</span><span class="topo-membrane">ISSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYHDL</span><span class="topo-inside">LYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>36</td>
      <td>12</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>79</td>
      <td>37</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>146</td>
      <td>102</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>295</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>564</td>
      <td>318</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAISLV</span><span class="topo-outside">MPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTMI</span><span class="topo-membrane">SSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYH</span><span class="topo-inside">DLLYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>38</td>
      <td>12</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>79</td>
      <td>39</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>147</td>
      <td>102</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>148</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>564</td>
      <td>316</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAIS</span><span class="topo-outside">LVMPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTM</span><span class="topo-membrane">ISSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYHDL</span><span class="topo-inside">LYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>36</td>
      <td>12</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>79</td>
      <td>37</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>146</td>
      <td>102</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>295</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>564</td>
      <td>318</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAISLV</span><span class="topo-outside">MPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTMI</span><span class="topo-membrane">SSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYH</span><span class="topo-inside">DLLYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>38</td>
      <td>12</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>79</td>
      <td>39</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>147</td>
      <td>102</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>168</td>
      <td>148</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>315</td>
      <td>295</td>
      <td>315</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>564</td>
      <td>316</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c78">5C78</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">M</span><span class="topo-unknown">VKKLFFI</span><span class="topo-inside">LSK</span><span class="topo-membrane">EDKNFLFFLLVFSVFVSFIETFAIS</span><span class="topo-outside">LVMPFITLASDFSYFDRNKYLISL</span></span>
<span class="topo-line"><span class="topo-outside">KEYLNIPVFEIIVYFGVGL</span><span class="topo-membrane">IVFYVFRALLNAYYFHLLARFS</span><span class="topo-inside">KGRKHAIAYKVFSKFLNIN</span></span>
<span class="topo-line"><span class="topo-inside">YEKFTQKNQSEILKSITGEVYNLSTM</span><span class="topo-membrane">ISSFLLLMSEIFVVLLLYALML</span><span class="topo-outside">LINYKI</span><span class="topo-membrane">TLFLSI</span></span>
<span class="topo-line"><span class="topo-membrane">FMVLNAFILVKILSPII</span><span class="topo-inside">KKAGLRREEAMKNFFEILNTNLNNFKFIKLKTKEDGVLSLFKA</span></span>
<span class="topo-line"><span class="topo-inside">QSEAFSKANI</span><span class="topo-membrane">TNESVAAVPRIYLEGIGFCVLVF</span><span class="topo-outside">IVVFLVLKNESDISGILSTIS</span><span class="topo-membrane">IFVLAL</span></span>
<span class="topo-line"><span class="topo-membrane">YRLMPSANRIITSYHDL</span><span class="topo-inside">LYYHSSLNIIYQNLRQEEENLGEGKLSFNQELKICNLSFGYEG</span></span>
<span class="topo-line"><span class="topo-inside">KKYLFKNLNLNIKKGEKIAFIGESGCGKSTLVDLIIGLLKPKEGQILIDKQELNASNAKN</span></span>
<span class="topo-line"><span class="topo-inside">YRQKIGYIPQNIYLFNDSIAKNITFGDAVDEEKLNKVIKQANLEHFIKNLPQGVQTKVGD</span></span>
<span class="topo-line"><span class="topo-inside">GGSNLSGGQKQRIAIARALYLEPEILVLDQATSALDTQSEAKIMDEIYKISKDKTMIIIA</span></span>
<span class="topo-line"><span class="topo-inside">HRLSTITQCDKVYRLEHGKLKEEK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>36</td>
      <td>12</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>79</td>
      <td>37</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>80</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>146</td>
      <td>102</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>168</td>
      <td>147</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>197</td>
      <td>175</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>250</td>
      <td>198</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>273</td>
      <td>251</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>294</td>
      <td>274</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>295</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>564</td>
      <td>318</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Outward semi-occluded state with asymmetric NBD dimer

The ATPgammaS-bound PglK structure reveals an asymmetric closed NBD dimer where one ATPgammaS is Mg2+-bound with canonical catalytic residue arrangement, while the other site is Mg2+-free with an alternative Q-loop conformation. This asymmetry suggests non-simultaneous ATP hydrolysis at the two NBDs, supporting an alternating ATP hydrolysis mechanism.

### LLO recognition site and substrate-hunting mechanism

Docking and MD simulations identified a positively charged surface recognition site between TM2 and TM5 (residues H95, R99, R104, K247) that binds the pyrophosphate group of LLO. Mutagenesis of these residues disrupts LLO-stimulated ATPase activity and flipping. The results suggest PglK employs a substrate-hunting mechanism to locally increase LLO concentration before translocation.

### Energetics of LLO flipping

Potential of mean force (PMF) calculations showed an energetic barrier of ~6-8 kBT for LLO translocation. The sugar-first pathway is energetically smoother than pyrophosphate-first. An applied membrane potential (-80 mV) reduces the barrier, consistent with coupling to electrochemical potential. Aromatic residues on the PglK surface facilitate sugar passage via stacking interactions.

### LLO flippase mechanism — credit card swipe model

Crystal structures of PglK in apo-inward (2.9 A, 3.9 A) and ADP-bound outward-occluded (5.9 A) states, combined with in vitro flipping assays and in vivo studies, reveal a unique flipping mechanism distinct from classical alternating access. The pyrophosphate-oligosaccharide head group enters the outward-facing translocation cavity and interacts with positively charged arginine residues (R86, R260, R302, R309), while the polypropenyl lipid tail binds the transporter surface via the external helix (EH) and remains exposed to the lipid bilayer throughout the reaction. The EH forms hydrophobic grooves that anchor the lipid tail and are essential for LLO-stimulated ATPase activity. PglK appears to adopt outward-facing states directly rather than cycling through inward-facing conformations for substrate binding, resembling a credit card swipe model where the lipid tail stays in the membrane while the head group is translocated through a spacious cavity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization detergent
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for crystallization and activity measurements
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — Extensive MD simulations used to study LLO recognition and translocation
- <a href="/xray-mp-wiki/methods/purification/ninta-affinity-chromatography/">Ni-NTA Affinity Chromatography</a> — Primary purification method for PglK
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography (SEC)</a> — Final polishing step
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
