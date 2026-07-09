---
title: "GlpF (Glycerol Facilitator from E. coli)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1067778, doi/10.1126##science.290.5491.481]
verified: regex
uniprot_id: P0AER0
---

# GlpF (Glycerol Facilitator from E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AER0">UniProt: P0AER0</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

GlpF is the [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) facilitator (aquaglyceroporin) from Escherichia coli, a
member of the [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) (AQP) superfamily. It forms a homotetrameric channel
that facilitates the passive diffusion of glycerol and other small linear
polyols across the membrane, while being impermeable to protons and ions.
The original structure of GlpF with bound glycerol was determined at 2.2 A
resolution (Fu et al., Science 2000), revealing three glycerol molecules in
single file within an amphipathic channel. The selectivity filter, formed by
Trp48, Phe200, and Arg206, creates an electrostatic triangle that polarizes
successive hydroxyl groups of permeant alditols. Later structures of the
water-bound form (GlpF-G) and the W48F/F200T mutant were determined at
2.7-2.8 A and 2.1 A resolution, respectively, revealing the structural
basis for water conduction and proton exclusion. Combined with molecular
dynamics simulations, these structures established the mechanism by which
the conserved NPA (Asn-Pro-Ala) motifs and helix dipoles establish a
bipolar water orientation that blocks proton conduction.


## Publications

### doi/10.1126##science.1067778

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1fx8">1FX8</a></td>
      <td>2.2</td>
      <td>—</td>
      <td>Full-length GlpF (<a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>-bound, GlpF+G)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Notes**: Overexpressed, purified, and crystallized as described in Fu et al. (2000) (PDB 1FX8)

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
      <td>Overexpression and purification</td>
      <td>As described in Fu et al. (2000)</td>
      <td>—</td>
      <td></td>
      <td>Purification protocol for GlpF from E. coli as previously established</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>15% (w/w) <a href="/xray-mp-wiki/reagents/additives/d-xylose/">xylose</a> (for GlpF-G) or 15% (w/w) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (for GlpF+G)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryo)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in space group I422, isomorphous to crystals previously grown in 15% (w/w) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (PDB 1FX8). Xylose was used as a non-transported substrate replacement for <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> to obtain the water-bound form.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1fx8">1FX8</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSQTS</span><span class="topo-outside">TLKGQ</span><span class="topo-membrane">CIAEFLGTGLLIFFGVGC</span><span class="topo-inside">VAALKVAGASFGQW</span><span class="topo-membrane">EISVIWGLGVAMAIYLTA</span><span class="topo-outside">GVS</span><span class="topo-unknown">GAHLNPAVTIALWLF</span><span class="topo-outside">ACFDKRK</span><span class="topo-membrane">VIPFIVSQVAGAFCAAALV</span><span class="topo-inside">YGLYYNLFFDFEQTHH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IVRGSVESVDLAGTFSTYPNPHINFVQA</span><span class="topo-membrane">FAVEMVITAILMGLILALT</span><span class="topo-outside">DDGNGVPRGPL</span><span class="topo-membrane">APLLIGLLIAVIGASMG</span><span class="topo-inside">PLT</span><span class="topo-unknown">GFAMNPARDFGPKVF</span><span class="topo-inside">AWLAGWGNVAFTGGRDIPYF</span><span class="topo-membrane">LVPLFGP</span></span>
<span class="topo-ruler">       250       260       270       280 </span>
<span class="topo-line"><span class="topo-membrane">IVGAIVGAFAYRKLI</span><span class="topo-outside">GRHL</span><span class="topo-unknown">PCDICVVEEKETTTPSEQKASL</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>104</td>
      <td>86</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>148</td>
      <td>105</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>198</td>
      <td>196</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>233</td>
      <td>214</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>255</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>259</td>
      <td>256</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>260</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1fx8">1FX8</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSQTS</span><span class="topo-outside">TLKGQ</span><span class="topo-membrane">CIAEFLGTGLLIFFGVGC</span><span class="topo-inside">VAALKVAGASFGQW</span><span class="topo-membrane">EISVIWGLGVAMAIYLTA</span><span class="topo-outside">GVS</span><span class="topo-unknown">GAHLNPAVTIALWLF</span><span class="topo-outside">ACFDKRK</span><span class="topo-membrane">VIPFIVSQVAGAFCAAALV</span><span class="topo-inside">YGLYYNLFFDFEQTHH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IVRGSVESVDLAGTFSTYPNPHINFVQA</span><span class="topo-membrane">FAVEMVITAILMGLILALT</span><span class="topo-outside">DDGNGVPRGPL</span><span class="topo-membrane">APLLIGLLIAVIGASMG</span><span class="topo-inside">PLT</span><span class="topo-unknown">GFAMNPARDFGPKVF</span><span class="topo-inside">AWLAGWGNVAFTGGRDIPYF</span><span class="topo-membrane">LVPLFGP</span></span>
<span class="topo-ruler">       250       260       270       280 </span>
<span class="topo-line"><span class="topo-membrane">IVGAIVGAFAYRKLI</span><span class="topo-outside">GRHL</span><span class="topo-unknown">PCDICVVEEKETTTPSEQKASL</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>104</td>
      <td>86</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>148</td>
      <td>105</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>198</td>
      <td>196</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>233</td>
      <td>214</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>255</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>259</td>
      <td>256</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>260</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1fx8">1FX8</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSQTS</span><span class="topo-outside">TLKGQ</span><span class="topo-membrane">CIAEFLGTGLLIFFGVGC</span><span class="topo-inside">VAALKVAGASFGQW</span><span class="topo-membrane">EISVIWGLGVAMAIYLTA</span><span class="topo-outside">GVS</span><span class="topo-unknown">GAHLNPAVTIALWLF</span><span class="topo-outside">ACFDKRK</span><span class="topo-membrane">VIPFIVSQVAGAFCAAALV</span><span class="topo-inside">YGLYYNLFFDFEQTHH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IVRGSVESVDLAGTFSTYPNPHINFVQA</span><span class="topo-membrane">FAVEMVITAILMGLILALT</span><span class="topo-outside">DDGNGVPRGPL</span><span class="topo-membrane">APLLIGLLIAVIGASMG</span><span class="topo-inside">PLT</span><span class="topo-unknown">GFAMNPARDFGPKVF</span><span class="topo-inside">AWLAGWGNVAFTGGRDIPYF</span><span class="topo-membrane">LVPLFGP</span></span>
<span class="topo-ruler">       250       260       270       280 </span>
<span class="topo-line"><span class="topo-membrane">IVGAIVGAFAYRKLI</span><span class="topo-outside">GRHL</span><span class="topo-unknown">PCDICVVEEKETTTPSEQKASL</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>104</td>
      <td>86</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>148</td>
      <td>105</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>198</td>
      <td>196</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>233</td>
      <td>214</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>255</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>259</td>
      <td>256</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>260</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1fx8">1FX8</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSQTS</span><span class="topo-outside">TLKGQ</span><span class="topo-membrane">CIAEFLGTGLLIFFGVGC</span><span class="topo-inside">VAALKVAGASFGQW</span><span class="topo-membrane">EISVIWGLGVAMAIYLTA</span><span class="topo-outside">GVS</span><span class="topo-unknown">GAHLNPAVTIALWLF</span><span class="topo-outside">ACFDKRK</span><span class="topo-membrane">VIPFIVSQVAGAFCAAALV</span><span class="topo-inside">YGLYYNLFFDFEQTHH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IVRGSVESVDLAGTFSTYPNPHINFVQA</span><span class="topo-membrane">FAVEMVITAILMGLILALT</span><span class="topo-outside">DDGNGVPRGPL</span><span class="topo-membrane">APLLIGLLIAVIGASMG</span><span class="topo-inside">PLT</span><span class="topo-unknown">GFAMNPARDFGPKVF</span><span class="topo-inside">AWLAGWGNVAFTGGRDIPYF</span><span class="topo-membrane">LVPLFGP</span></span>
<span class="topo-ruler">       250       260       270       280 </span>
<span class="topo-line"><span class="topo-membrane">IVGAIVGAFAYRKLI</span><span class="topo-outside">GRHL</span><span class="topo-unknown">PCDICVVEEKETTTPSEQKASL</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>28</td>
      <td>11</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>104</td>
      <td>86</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>148</td>
      <td>105</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>167</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>178</td>
      <td>168</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>198</td>
      <td>196</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>214</td>
      <td>233</td>
      <td>214</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>255</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>259</td>
      <td>256</td>
      <td>259</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>281</td>
      <td>260</td>
      <td>281</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.290.5491.481

**Expression:**

- **Expression system**: E. coli
- **Notes**: Overexpressed, purified, and crystallized as described in Fu et al. (2000) (PDB 1FX8)

**Purification:**

- **Expression system**: E. coli K12
- **Expression construct**: GlpF with N-terminal [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) and thrombin cleavage site
- **Tag info**: [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), removed by thrombin cleavage

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
      <td>Nickel affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6 Tag</a> purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td></td>
      <td>Purified by SEC after nickel affinity</td>
    </tr>
  </tbody>
</table>
**Final sample**: 15-20 mg/ml in crystallization buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>28% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 2000, 100 mM <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a>, 15% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 35 mM <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 300 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl₂</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">[DTT</a>](/xray-mp-wiki/reagents/additives/dtt/)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryo)</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Selectivity filter and amphipathic channel mechanism

The GlpF channel is strongly amphipathic, with a hydrophobic corner formed by Trp48 and Phe200 and polar interactions provided by Arg206, Gly199, and Ala201. The selectivity filter is only large enough to accommodate a single CH-OH group at a time, requiring alditols to pass in single file. G2 and G3 are tightly organized in the selectivity filter, where the alkyl backbone of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is wedged against the hydrophobic corner and successive hydroxyl groups form hydrogen bonds with acceptor and donor atoms. An electrostatic triangle formed by Glu152 (via main-chain amides of Phe200 and Ala201), Arg206, and the carbonyls of Gly199/Phe200 polarizes successive OH groups on permeant alditols. The structure shows that any permeant molecule must be polarizable in section parallel to the plane of the membrane.

### Stereoselective preference for glycerol and linear carbohydrates

GlpF demonstrates stereoselectivity for linear alditols. Ribitol (all OH groups with same stereospecific relation) shows ~10-fold faster transport than D-arabitol (mixed hydroxyl arrangement), measured by stopped-flow light scattering of reconstituted proteoliposomes. The carbon backbone must line up along the channel axis, and CHOH groups adjacent to the G2 site place carbon in one of two tetrahedrally disposed sites with different environments, explaining the stereoselectivity.

### Bipolar water orientation mechanism for proton exclusion

The mechanism of proton exclusion in aquaporins is based on a bipolar orientation of water molecules within the channel. MD simulations of GlpF-G reveal a hydrogen-bonded single file of water molecules in the 20 A constriction region. Starting from the NPA center (Asn68 and Asn203), water molecules are oriented in opposite directions in the two halves of the channel, with their hydrogen atoms pointing toward the exits. The central water molecule at the NPA motifs is hydrogen bonded to the NH2 groups of both Asn68 and Asn203, with its dipole restrained perpendicular to the channel axis. This arrangement prevents the formation of a Grotthuss-type proton wire, as the bipolar orientation means successive O-H bonds are oriented away from the central water.

### Role of NPA motifs and helix dipoles in water orientation

The conserved NPA (Asn-Pro-Ala) motifs and the alpha-helices M3 and M7 together establish the electrostatic field that maintains bipolar water orientation. The Asn68 and Asn203 NH2 groups specifically hydrogen bond to a single water molecule at the channel center, making its lone electron pairs unavailable as proton acceptors. Opposite the NPA motifs across the channel are only hydrophobic residues (Ile187, Val52, Leu159) that prohibit alternative hydrogen bonding patterns. The dipoles of the half-membrane spanning helices M3 and M7 generate electrostatic fields directed toward the channel center. MD simulations where these charges were turned off resulted in breakdown of the bipolar orientation and formation of a uniform water orientation (potential proton wire).

### Selectivity filter and water permeability

The selectivity filter (SF) region of GlpF shows low water occupancy in both crystal structures and MD simulations, contributing to the low water permeation rate. The SF-lining residues Trp48, Phe200, and Arg206 undergo subtle conformational changes between the [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)-bound and water-bound states. The W48F/F200T double mutant increases both the size and polarity of the SF region, resulting in a 25% increase in water permeation (light scattering assays) and a 38% increase in permeation events (MD simulations). Water density at the SF region increases significantly in the mutant, while the bipolar water orientation is preserved, predicting that this mutant also remains impermeable to protons.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin</a> — GlpF is a member of the aquaporin superfamily; the proton exclusion mechanism described here applies to the entire AQP family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/">Aquaporin Z (AqpZ)</a> — Related aquaporin water channel from E. coli; same superfamily as GlpF
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/">Human Aquaporin 2</a> — Human homolog in the aquaporin family; same NPA motif mechanism
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/">Human Aquaporin 4</a> — Human homolog in the aquaporin family; conserved NPA motif and bipolar water orientation mechanism
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in glpf text
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6 Tag</a> — Referenced in glpf text
- <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> — Referenced in glpf text
- <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> — Referenced in glpf text
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in glpf text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">Aquaporin-1 (AQP1)</a> — Water-specific aquaporin used as structural comparison; AQP1 constriction region is narrower and more hydrophilic, excluding glycerol
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">Glpf</a> — Referenced in glycerol-facilitator text
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Referenced in glycerol-facilitator text
