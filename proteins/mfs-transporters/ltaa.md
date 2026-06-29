---
title: "LtaA — S. aureus Lipid-Linked Disaccharide Flippase"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-020-0425-5]
verified: false
---

# LtaA — S. aureus Lipid-Linked Disaccharide Flippase

## Overview

LtaA is a proton-coupled antiporter flippase from Staphylococcus aureus
that translocates the lipid-linked disaccharide gentiobiosyl-diacylglycerol
(anchor-LLD) across the plasma membrane, a rate-limiting step in
lipoteichoic acid (LTA) biogenesis. LtaA belongs to the Major Facilitator
Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) of transporters and is essential for S. aureus survival
under acidic physiological conditions encountered in the human nasopharynx,
mucous membranes, and skin. Its structure reveals an amphiphilic central
cavity with an N-terminal hydrophilic pocket that binds the gentiobiosyl
headgroup and a C-terminal hydrophobic pocket that accommodates the
diacylglycerol lipid tails.


## Publications

### doi/10.1038##s41594-020-0425-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6s7v">6S7V</a></td>
      <td>3.3</td>
      <td>C2221</td>
      <td>Full-length S. aureus LtaA with N-terminal His10 tag (removed post-purification)</td>
      <td>None (apo structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21-Gold (DE3)
- **Construct**: Full-length S. aureus LtaA with N-terminal His10 affinity tag and TEV protease cleavage site
- **Notes**: SeMet derivative produced in M9 medium with amino acids/SeMet cocktail
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/)
- **Media**: Terrific Broth supplemented with 1% [Glucose](/xray-mp-wiki/reagents/additives/glucose/)

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
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.5 mM PMSF</td>
      <td>Cells resuspended and disrupted; membranes collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Incubated for 2 h at 4°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA affinity</td>
      <td>Ni-NTA Superflow</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash followed by elution with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>TEV protease cleavage</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Overnight treatment; TEV removed by secondary Ni-NTA pass</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a></td>
      <td>Main peak collected; buffer exchanged to 0.1% Cymal-7 using PD-10 desalting column</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LtaA at 6.0 mg/mL in 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.1% Cymal-7</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30-70 mM magnesium acetate, 80-120 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.5, 30-34% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 days to appearance, 1 week to full size</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Plate-shaped crystals; dehydrated and cryoprotected by increasing <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300 concentration; in situ annealing performed</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6s7v">6S7V</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">ANHKNFI</span><span class="topo-membrane">LMLIILFLMEFARGMYILSYI</span><span class="topo-outside">NFLPTVTSIAVAITSL</span><span class="topo-membrane">AFSIHFIADASTNFVI</span></span>
<span class="topo-line"><span class="topo-membrane">G</span><span class="topo-inside">FLLKKFGTKIV</span><span class="topo-membrane">LTTGFILAFTSLFLVIWFP</span><span class="topo-outside">ASPF</span><span class="topo-membrane">VIIFSAMMLGIAVSPIWVIML</span><span class="topo-inside">SSVE</span></span>
<span class="topo-line"><span class="topo-inside">EDKRG</span><span class="topo-membrane">KQMGYVYFSWLLGLLVGMVFMNLL</span><span class="topo-outside">IKVHPTR</span><span class="topo-membrane">FAFMMSLVVLIAWILY</span><span class="topo-inside">YFVDVKLT</span></span>
<span class="topo-line"><span class="topo-inside">NYNTRPVKAQ</span><span class="topo-unknown">LRQIVDVTKR</span><span class="topo-inside">HL</span><span class="topo-membrane">LLFPGILLQGAAIAALVP</span><span class="topo-outside">ILPTYATKVINVSTIEYTVA</span></span>
<span class="topo-line"><span class="topo-outside">III</span><span class="topo-membrane">GGIGCAVSMLFLSKLIDNRS</span><span class="topo-inside">RNFM</span><span class="topo-membrane">YGVILSGFILYMILIFTL</span><span class="topo-outside">SMIVNIHI</span><span class="topo-membrane">LWIIALA</span></span>
<span class="topo-line"><span class="topo-membrane">IGLMYGILLPAWNTFM</span><span class="topo-inside">ARFIKSDEQEETW</span><span class="topo-membrane">GVFNSIQGFGSMIGPLFG</span><span class="topo-outside">GLITQFTNNLN</span><span class="topo-membrane">NT</span></span>
<span class="topo-line"><span class="topo-membrane">FYFSALIFLVLAVFYGS</span><span class="topo-inside">Y</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>23</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>44</td>
      <td>44</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>60</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>72</td>
      <td>77</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>91</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>95</td>
      <td>107</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>116</td>
      <td>111</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>132</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>149</td>
      <td>141</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>156</td>
      <td>165</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>172</td>
      <td>172</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>188</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>200</td>
      <td>206</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>201</td>
      <td>202</td>
      <td>216</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>218</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>243</td>
      <td>236</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>263</td>
      <td>259</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>267</td>
      <td>279</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>285</td>
      <td>283</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>293</td>
      <td>301</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>316</td>
      <td>309</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>329</td>
      <td>332</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>347</td>
      <td>345</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>358</td>
      <td>363</td>
      <td>373</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>377</td>
      <td>374</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>378</td>
      <td>378</td>
      <td>393</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Proton-Coupled Lipid Flipping Mechanism

LtaA is identified as a new class of flippase that energizes lipid translocation
by coupling to a transmembrane proton gradient. The mechanism follows an
antiporter alternating-access cycle: deprotonated LtaA in an inward-facing
conformation binds anchor-LLD, transitions to an outward-facing state,
releases the substrate into the membrane, and becomes protonated at residue
E32 to facilitate the return to the inward-facing state. This represents the
first description of a proton-coupled lipid flippase.

### pH Sensing Role in S. aureus Survival

LtaA acts as a pH-sensing flippase that increases anchor-LLD transport under
low pH conditions, enlarging the LTA population at the outer leaflet. Increased
LTA provides a buffering mechanism against acidification via the highly
negatively charged LTA backbone polymer. Deletion of ltaA causes strong growth
retardation at low pH (5.0-6.5) and at 5% CO2, conditions encountered in
human nasopharynx and skin. This establishes LtaA as essential for S. aureus
survival under physiologically relevant acidic conditions.

### Substrate Selectivity and Inhibitor Design

LtaA displays high selectivity for the gentiobiosyl headgroup of anchor-LLD.
Flipping activity is inhibited by gentiobiose (beta-D-Glc-(1,6)-D-Glc) in a
concentration-dependent manner, but not by other disaccharides (lactose,
[Trehalose](/xray-mp-wiki/reagents/additives/trehalose/), [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/)). This provides the structural basis for designing
inhibitors targeting LTA assembly.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — LtaA is an MFS family transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — LtaA follows the antiporter alternating-access cycle
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
