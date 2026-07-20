---
title: "AfUbiA - Archaeoglobus fulgidus UbiA Family Prenyltransferase"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1371##journal.pbio.1001911]
verified: agent
uniprot_id: O28625
---

# AfUbiA - Archaeoglobus fulgidus UbiA Family Prenyltransferase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O28625">UniProt: O28625</a>

<span class="expr-badge">Archaeoglobus fulgidus</span>

## Overview

AfUbiA is a membrane-embedded prenyltransferase from the archaeon *Archaeoglobus fulgidus*, belonging to the UbiA family that catalyzes Mg2+-dependent transfer of hydrophobic polyprenyl chains onto acceptor molecules. The structure was solved by X-ray crystallography in unliganded form and bound to Mg2+ with either geranyl diphosphate (GPP) or dimethylallyl diphosphate (DMAPP). AfUbiA contains nine transmembrane helices arranged as two pseudosymmetric four-helix bundles, with the active site located in a central cavity at the cytoplasmic interface. The active site contains two conserved aspartate-rich motifs that coordinate Mg2+ ions and the diphosphate moiety of the prenyl donor. AfUbiA is a structural model for understanding the human homolog UBIAD1, mutations in which cause Schnyder crystalline corneal dystrophy.


## Publications

### doi/10.1371##journal.pbio.1001911

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a></td>
      <td>2.5</td>
      <td>—</td>
      <td>Full-length AfUbiA with N-terminal polyhistidine tag (removed)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/gpp/">GPP</a> (geranyl diphosphate)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a></td>
      <td>2.4</td>
      <td>—</td>
      <td>Full-length AfUbiA with N-terminal polyhistidine tag (removed)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/dmapp/">DMAPP</a> (dimethylallyl diphosphate)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a></td>
      <td>3.2</td>
      <td>—</td>
      <td>Full-length AfUbiA with N-terminal polyhistidine tag (removed), <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a>-substituted</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: N-terminal polyhistidine tag
- **Notes**: pET vector; [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) induction at 20°C for 15 h; also expressed as [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)-substituted protein in minimal medium

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/) BL21(DE3)
- **Expression construct**: N-terminal polyhistidine tag (cleavable by [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/))

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
      <td>Membrane solubilization</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (DM)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Metal Affinity Resin</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">[Superdex 200</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) 10/300 GL</td>
      <td>—</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 40 mM <a href="/xray-mp-wiki/reagents/detergents/og/">n-octyl-beta-D-glucopyranoside</a> (OG)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>35 mg/ml AfUbiA</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> crystals flash frozen directly)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals soaked in 1 mM <a href="/xray-mp-wiki/reagents/additives/gpp/">GPP</a> or 1 mM <a href="/xray-mp-wiki/reagents/additives/dmapp/">DMAPP</a> before harvesting; <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> crystals do not require additional cryoprotectant</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>12.5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>20000, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.7</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a>-detergent crystal form; used for <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD phasing</a> at 3.2 Å</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 550 MME, 100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.6, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl₂)</a>, 100 mM CdCl2</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Serial mother liquor solutions with 5-25% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Cd2+ co-crystallization for Mg2+ site verification</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSSLANINQIDVP</span><span class="topo-inside">S</span><span class="topo-membrane">KYLRLLRPVAWLCFLLPYAVGFGF</span><span class="topo-outside">GITPNASLQHAV</span><span class="topo-membrane">LGLLSFAFWMAFSFTINAL</span><span class="topo-inside">YDRDVDRLHDG</span><span class="topo-unknown">RVKD</span><span class="topo-inside">LNLSMQPLVTGEI</span><span class="topo-membrane">SVREAWLYCIAFLALSLATAA</span><span class="topo-outside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">INEK</span><span class="topo-membrane">FFLAMLGANIIGYVYSAPP</span><span class="topo-inside">RFKAWPVM</span><span class="topo-membrane">DVICNALAAVLAFYAGL</span><span class="topo-outside">SIGGAEV</span><span class="topo-membrane">PIAIYPAAFFLAATFY</span><span class="topo-inside">IPTAVSDYEFDKKAGLKNTPVFFGPERALKSLYP</span><span class="topo-membrane">LSAITVILWAYVFLM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">ERIE</span><span class="topo-membrane">IKVISPLIIAYTLIYT</span><span class="topo-inside">FIINSRWDGEKLNVSPN</span><span class="topo-membrane">LILTPFGIISALFIAY</span><span class="topo-outside">GFAVISV</span><span class="topo-unknown">LG</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39</td>
      <td>16</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>40</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>70</td>
      <td>52</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>81</td>
      <td>71</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>85</td>
      <td>82</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>86</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>119</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>124</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>143</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>151</td>
      <td>144</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>168</td>
      <td>152</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>169</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>191</td>
      <td>176</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>225</td>
      <td>192</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>226</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>245</td>
      <td>242</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>261</td>
      <td>246</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>262</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>294</td>
      <td>279</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>301</td>
      <td>295</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>303</td>
      <td>302</td>
      <td>303</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSSLANINQIDVP</span><span class="topo-inside">S</span><span class="topo-membrane">KYLRLLRPVAWLCFLLPYAVGFGF</span><span class="topo-outside">GITPNASLQHAV</span><span class="topo-membrane">LGLLSFAFWMAFSFTINAL</span><span class="topo-inside">YDRDVDRLHDG</span><span class="topo-unknown">RVKD</span><span class="topo-inside">LNLSMQPLVTGEI</span><span class="topo-membrane">SVREAWLYCIAFLALSLATAA</span><span class="topo-outside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">INEK</span><span class="topo-membrane">FFLAMLGANIIGYVYSAPP</span><span class="topo-inside">RFKAWPVM</span><span class="topo-membrane">DVICNALAAVLAFYAGL</span><span class="topo-outside">SIGGAEV</span><span class="topo-membrane">PIAIYPAAFFLAATFY</span><span class="topo-inside">IPTAVSDYEFDKKAGLKNTPVFFGPERALKSLYP</span><span class="topo-membrane">LSAITVILWAYVFLM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">ERIE</span><span class="topo-membrane">IKVISPLIIAYTLIYT</span><span class="topo-inside">FIINSRWDGEKLNVSPN</span><span class="topo-membrane">LILTPFGIISALFIAY</span><span class="topo-outside">GFAVISV</span><span class="topo-unknown">LG</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39</td>
      <td>16</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>40</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>70</td>
      <td>52</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>81</td>
      <td>71</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>85</td>
      <td>82</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>86</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>119</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>124</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>143</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>151</td>
      <td>144</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>168</td>
      <td>152</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>169</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>191</td>
      <td>176</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>225</td>
      <td>192</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>226</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>245</td>
      <td>242</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>261</td>
      <td>246</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>262</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>294</td>
      <td>279</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>301</td>
      <td>295</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>303</td>
      <td>302</td>
      <td>303</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4tq3">4TQ3</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDSSLANINQIDVP</span><span class="topo-inside">S</span><span class="topo-membrane">KYLRLLRPVAWLCFLLPYAVGFGF</span><span class="topo-outside">GITPNASLQHAV</span><span class="topo-membrane">LGLLSFAFWMAFSFTINAL</span><span class="topo-inside">YDRDVDRLHDG</span><span class="topo-unknown">RVKD</span><span class="topo-inside">LNLSMQPLVTGEI</span><span class="topo-membrane">SVREAWLYCIAFLALSLATAA</span><span class="topo-outside">A</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">INEK</span><span class="topo-membrane">FFLAMLGANIIGYVYSAPP</span><span class="topo-inside">RFKAWPVM</span><span class="topo-membrane">DVICNALAAVLAFYAGL</span><span class="topo-outside">SIGGAEV</span><span class="topo-membrane">PIAIYPAAFFLAATFY</span><span class="topo-inside">IPTAVSDYEFDKKAGLKNTPVFFGPERALKSLYP</span><span class="topo-membrane">LSAITVILWAYVFLM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">ERIE</span><span class="topo-membrane">IKVISPLIIAYTLIYT</span><span class="topo-inside">FIINSRWDGEKLNVSPN</span><span class="topo-membrane">LILTPFGIISALFIAY</span><span class="topo-outside">GFAVISV</span><span class="topo-unknown">LG</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>39</td>
      <td>16</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>40</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>70</td>
      <td>52</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>81</td>
      <td>71</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>85</td>
      <td>82</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>86</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>119</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>124</td>
      <td>120</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>143</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>151</td>
      <td>144</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>168</td>
      <td>152</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>175</td>
      <td>169</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>191</td>
      <td>176</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>225</td>
      <td>192</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>241</td>
      <td>226</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>245</td>
      <td>242</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>261</td>
      <td>246</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>262</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>294</td>
      <td>279</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>301</td>
      <td>295</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>303</td>
      <td>302</td>
      <td>303</td>
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

### UbiA Family Prenyltransferase Mechanism

The substrate-bound structures reveal a three-stage catalytic mechanism: (i) ionization of the prenyl diphosphate to form a carbocation intermediate, stabilized by the diphosphate leaving group coordinated by Mg2+ and conserved arginine/lysine residues; (ii) condensation of the carbocation with the prenyl acceptor; (iii) elimination of a proton to regenerate the aromatic acceptor. A highly conserved tyrosine (Y139 in AfUbiA, present in 97% of >10,000 UbiA sequences) is proposed to stabilize the carbocation intermediate via cation-pi interactions. The two aspartate-rich motifs (N68/D72 in TM2 and D198/D202 in TM6) coordinate two Mg2+ ions. Functional assays on E. coli MenA confirmed the essentiality of these residues.

### Structural Basis for Schnyder Corneal Dystrophy Mutations

Missense mutations at 19 different residues of human UBIAD1 cause Schnyder crystalline corneal dystrophy (SCD), a genetic disease causing blindness. Of these, 16 map to the active site region of AfUbiA, clustering around the conserved aspartate-rich motifs and substrate-binding cavity. This conservation suggests the catalytic mechanism is shared between archaeal AfUbiA and human UBIAD1, making AfUbiA a valuable structural model for understanding SCD pathology.

### Hydrophobic Tunnel for Long Prenyl Substrates

The central cavity extends into a long, narrow hydrophobic tunnel that opens into the membrane bilayer, allowing the protein to bind significantly longer polyprenyl chains (up to C60). The tunnel can accommodate up to six prenyl units, and even longer polyprenyls could extend directly into the hydrophobic core of the bilayer. This explains how UbiA family members utilize prenyl donors of varying lengths.

### Structural Similarity to Soluble trans-IPPS Enzymes

Despite negligible sequence identity, the four-helix bundles of AfUbiA (helices 1-8) are superposable on those of soluble trans-isoprenyl diphosphate synthases (trans-IPPS) such as farnesyl diphosphate synthase (FPPS). This suggests that the UbiA fold arose from the duplication of an ancient four-helix, dimeric protein and that the catalytic mechanism is evolutionarily conserved between soluble and membrane-embedded prenyltransferases.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/gpp/">Geranyl Diphosphate (GPP)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used in purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Reagent used in the study
