---
title: "bcMalT (Bacillus cereus Maltose Transporter)"
created: 2026-05-28
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.04.003, doi/10.1073##pnas.1800647115]
verified: agent
uniprot_id: Q63GK8
---

# bcMalT (Bacillus cereus Maltose Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q63GK8">UniProt: Q63GK8</a>

<span class="expr-badge">Bacillus cereus (strain ZK / E33L)</span>

## Overview

bcMalT is a [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter from Bacillus cereus, belonging to the Glucose superfamily of enzyme IIC (EIIC) components of the phosphoenolpyruvate:carbohydrate phosphotransferase system (PTS). It is the first crystal structure of a Glucose superfamily EIIC transporter in an outward-facing occluded conformation. The protein undergoes a large rigid-body motion of its substrate-binding domain, moving the substrate-binding cavity by approximately 20 A between inward-facing and outward-facing states, consistent with an elevator-car transport mechanism.


## Publications

### doi/10.1016##j.str.2016.04.003

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5iws">5IWS</a></td>
      <td>2.55</td>
      <td>I222</td>
      <td>Trypsinized EIIC domain (residues 8-450)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: His6-tagged EIIC domain from Bacillus cereus (Uniprot Q63GK8), cloned into pMCSG28 vector, [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-derivatized
- **Notes**: Gene cloned from Bacillus cereus E33L chromosome. Cells grown in SeMet-containing minimal media, induced with 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 20 C overnight.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) on full-length protein, trypsinized to yield EIIC domain only

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
      <td><a href="/xray-mp-wiki/methods/purification/sonication/">Sonication</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% glycerol, 2 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">Beta-Mercaptoethanol</a>, 25 ug/mL <a href="/xray-mp-wiki/reagents/additives/dnase/">DNase I</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF (Phenylmethylsulfonyl Fluoride)</a></td>
      <td>Cells resuspended and sonicated until fully lysed</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> (Anatrace)</td>
      <td>Gentle shaking for 2 hours at room temperature, centrifuged 45 min at 55,000g</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta) affinity (<a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a>, Clontech)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON Cobalt Affinity Resin</a> cobalt affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>Washed with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, eluted with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>Limited proteolysis</td>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin">Trypsin</a> digestion</td>
      <td>—</td>
      <td></td>
      <td>1:20 wt ratio bcMalT to <a href="/xray-mp-wiki/reagents/additives/trypsin">Trypsin</a>, 30 min at room temperature, yielded EIIC domain (~50.84 kDa)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> (<a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/300 GL)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM trehalose, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM (n-Decyl-beta-D-Maltoside)</a>, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">Beta-Mercaptoethanol</a></td>
      <td>Full-length EIICB protein unstable at high concentrations in detergent; trypsinized EIIC domain used for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>50-55 mg/mL trypsinized EIIC domain in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10 mM trehalose, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM (n-Decyl-beta-D-Maltoside)</a>, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">Beta-Mercaptoethanol</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (protein solution:molten <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>, w:w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Approximately 3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>6.7</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Protein:lipid ratio</td>
      <td>2:3 (protein solution:molten <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>, w:w)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 400: 39 % [precipitant] (Polyethylene Glycol 400 (PEG400))  
- Sodium Chloride: 450 mM [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iws">5IWS</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ITSFD</span><span class="topo-inside">FWQKF</span><span class="topo-membrane">GKALLVVVAVMPAAGLMISIG</span><span class="topo-outside">KLIGMSAGDINAVHTIARV</span><span class="topo-membrane">MEDIGWAIITNLHILFAVAIGGSW</span><span class="topo-inside">AKDRA</span><span class="topo-membrane">GGAFAALLAFVLTNRIT</span><span class="topo-outside">GAIFGVNAEMLADSKAKVSSVLAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DLIVKDYFTSVLGAPALNM</span><span class="topo-membrane">GVFVGIITGFLGATLY</span><span class="topo-inside">NKYYNYNKLPQALAFFNGKR</span><span class="topo-membrane">FVPFVVIVWSTVTAIVLSLLW</span><span class="topo-outside">PFIQSGLNEFGRWIAASKDSAPIVAP</span><span class="topo-unknown">FVYGTLERLLLPFGLHHM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">LT</span><span class="topo-outside">IPMNYTELGGTYTMLTGSKVGQVVAGQDPLWLAWITDLNNLLANGDTKAYNDLLNNVVPARFK</span><span class="topo-membrane">AGQVIGSTAALMGIA</span><span class="topo-inside">FAMFRNVDKEKRAKYKPMFL</span><span class="topo-unknown">SAALAVFLTGVTEPIEFMFM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470</span>
<span class="topo-line"><span class="topo-unknown">F</span><span class="topo-inside">IAP</span><span class="topo-membrane">VLYVVYAITTGLAFALA</span><span class="topo-outside">DLINLRVHAFGFIELITRTPMMVNAGLTRDL</span><span class="topo-membrane">INFVIVSLVFFGLNFTLF</span><span class="topo-inside">NFLIKKFNLPTPGRAGNY</span><span class="topo-unknown">IDNEDEASEGTGNVQDGSLATK</span></span>
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
      <td>5</td>
      <td>3</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>13</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>74</td>
      <td>53</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>79</td>
      <td>77</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>82</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>139</td>
      <td>99</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>155</td>
      <td>142</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>175</td>
      <td>158</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>196</td>
      <td>178</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>222</td>
      <td>199</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>242</td>
      <td>225</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>305</td>
      <td>245</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>320</td>
      <td>308</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>340</td>
      <td>323</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>361</td>
      <td>343</td>
      <td>363</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>362</td>
      <td>364</td>
      <td>364</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>381</td>
      <td>367</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>412</td>
      <td>384</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>430</td>
      <td>415</td>
      <td>432</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>448</td>
      <td>433</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>451</td>
      <td>472</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5iws">5IWS</a> — Chain C (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ITSFD</span><span class="topo-inside">FWQKF</span><span class="topo-membrane">GKALLVVVAVMPAAGLMISIG</span><span class="topo-outside">KLIGMSAGDINAVHTIARV</span><span class="topo-membrane">MEDIGWAIITNLHILFAVAIGGSW</span><span class="topo-inside">AKDRA</span><span class="topo-membrane">GGAFAALLAFVLTNRIT</span><span class="topo-outside">GAIFGVNAEMLADSKAKVSSVLAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DLIVKDYFTSVLGAPALNM</span><span class="topo-membrane">GVFVGIITGFLGATLY</span><span class="topo-inside">NKYYNYNKLPQALAFFNGKR</span><span class="topo-membrane">FVPFVVIVWSTVTAIVLSLLW</span><span class="topo-outside">PFIQSGLNEFGRWIAASKDSAPIVAP</span><span class="topo-unknown">FVYGTLERLLLPFGLHHM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">LT</span><span class="topo-outside">IPMNYTELGGTYTMLTGSKVGQVVAGQDPLWLAWITDLNNLLANGDTKAYNDLLNNVVPARFK</span><span class="topo-membrane">AGQVIGSTAALMGIA</span><span class="topo-inside">FAMFRNVDKEKRAKYKPMFL</span><span class="topo-unknown">SAALAVFLTGVTEPIEFMFM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470</span>
<span class="topo-line"><span class="topo-unknown">F</span><span class="topo-inside">IAP</span><span class="topo-membrane">VLYVVYAITTGLAFALA</span><span class="topo-outside">DLINLRVHAFGFIELITRTPMMVNAGLTRDL</span><span class="topo-membrane">INFVIVSLVFFGLNFTLF</span><span class="topo-inside">NFLIKKFNLPTPGRAGNY</span><span class="topo-unknown">IDNEDEASEGTGNVQDGSLATK</span></span>
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
      <td>5</td>
      <td>3</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>13</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>34</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>74</td>
      <td>53</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>79</td>
      <td>77</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>82</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>139</td>
      <td>99</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>155</td>
      <td>142</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>175</td>
      <td>158</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>196</td>
      <td>178</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>222</td>
      <td>199</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>242</td>
      <td>225</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>305</td>
      <td>245</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>320</td>
      <td>308</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>340</td>
      <td>323</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>361</td>
      <td>343</td>
      <td>363</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>362</td>
      <td>364</td>
      <td>364</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>381</td>
      <td>367</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>412</td>
      <td>384</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>430</td>
      <td>415</td>
      <td>432</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>448</td>
      <td>433</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>470</td>
      <td>451</td>
      <td>472</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1800647115

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bvg">6BVG</a></td>
      <td>3.2</td>
      <td>I222</td>
      <td>bcMalT T280C/E54C double-cysteine mutant, Hg2+-crosslinked, inward-facing conformation</td>
      <td><a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: His6-tagged EIIC domain from Bacillus cereus (Uniprot Q63GK8), cloned into pMCSG28 vector, [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-derivatized
- **Notes**: Gene cloned from Bacillus cereus E33L chromosome. Cells grown in SeMet-containing minimal media, induced with 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg) at 20 C overnight.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bvg">6BVG</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ITS</span><span class="topo-membrane">FDFWQKFGKALLVVVAVMPAAGLMISIGKLI</span><span class="topo-inside">GMSAGDINAVHTIARV</span><span class="topo-membrane">MCDIGWAIITNLHILFAVAIGGSWAKD</span><span class="topo-unknown">R</span><span class="topo-membrane">AGGAFAALLAFVLTNRIT</span><span class="topo-inside">GAIFGVNAEMLADSKAKVSSVLAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DLIVKDYFTSVLGAPALNM</span><span class="topo-membrane">GVFVGIITGFLGATLYNKYY</span><span class="topo-outside">NYNKLPQA</span><span class="topo-membrane">LAFFNGKRFVPFVVIVWSTVTAIVLSLLW</span><span class="topo-inside">PFIQSGLNEFGRWIAASKDSA</span><span class="topo-membrane">PIVAPFVYGTLERLLLPF</span><span class="topo-unknown">G</span><span class="topo-membrane">LHHM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LTIPMNYTELGG</span><span class="topo-inside">TYTMLTGSKVGQVVAGQDPLWLAWICDLNNLLANGDTKAYNDLLNNVVP</span><span class="topo-membrane">ARFKAGQVIGSTAALMGIAFA</span><span class="topo-outside">MFRNVDKEKRAKYKPMFLSAA</span><span class="topo-unknown">LAVFLTGVTEPIE</span><span class="topo-outside">FMFM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440         </span>
<span class="topo-line"><span class="topo-outside">FIAPVL</span><span class="topo-membrane">YVVYAITTGLAFALADLI</span><span class="topo-unknown">NLRVHAFGFIELITRTPMMV</span><span class="topo-inside">NAGLT</span><span class="topo-membrane">RDLINFVIVSLVFFGLNFTLFNF</span><span class="topo-outside">LIKKFNLPTPGRAGNYI</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>3</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>34</td>
      <td>6</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>50</td>
      <td>37</td>
      <td>52</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>77</td>
      <td>53</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>81</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>139</td>
      <td>99</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>142</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>162</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>196</td>
      <td>170</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>217</td>
      <td>199</td>
      <td>219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>220</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>252</td>
      <td>239</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>301</td>
      <td>255</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>322</td>
      <td>304</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>343</td>
      <td>325</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>356</td>
      <td>346</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>357</td>
      <td>366</td>
      <td>359</td>
      <td>368</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>384</td>
      <td>369</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>404</td>
      <td>388</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>409</td>
      <td>407</td>
      <td>411</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>432</td>
      <td>412</td>
      <td>434</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>433</td>
      <td>449</td>
      <td>435</td>
      <td>451</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bvg">6BVG</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ITS</span><span class="topo-membrane">FDFWQKFGKALLVVVAVMPAAGLMISIGKLI</span><span class="topo-inside">GMSAGDINAVHTIARV</span><span class="topo-membrane">MCDIGWAIITNLHILFAVAIGGSWAKD</span><span class="topo-unknown">R</span><span class="topo-membrane">AGGAFAALLAFVLTNRIT</span><span class="topo-inside">GAIFGVNAEMLADSKAKVSSVLAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DLIVKDYFTSVLGAPALN</span><span class="topo-membrane">MGVFVGIITGFLGATLYNKYY</span><span class="topo-outside">NYNKLPQA</span><span class="topo-membrane">LAFFNGKRFVPFVVIVWSTVTAIVLSLLW</span><span class="topo-inside">PFIQSGLNEFGRWIAASKDSA</span><span class="topo-membrane">PIVAPFVYGTLERLLLPF</span><span class="topo-unknown">G</span><span class="topo-membrane">LHHM</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LTIPMNYTELGG</span><span class="topo-inside">TYTMLTGSKVGQVVAGQDPLWLAWICDLNNLLANGDTKAYNDLLNNVVP</span><span class="topo-membrane">ARFKAGQVIGSTAALMGIAFA</span><span class="topo-outside">MFRNVDKEKRAKYKPMFLSAA</span><span class="topo-unknown">LAVFLTGVTEPIE</span><span class="topo-outside">FMFM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440         </span>
<span class="topo-line"><span class="topo-outside">FIAPVL</span><span class="topo-membrane">YVVYAITTGLAFALADLI</span><span class="topo-unknown">NLRVHAFGFIELITRTPMMV</span><span class="topo-inside">NAGLT</span><span class="topo-membrane">RDLINFVIVSLVFFGLNFTLFNF</span><span class="topo-outside">LIKKFNLPTPGRAGNYI</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>3</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>34</td>
      <td>6</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>50</td>
      <td>37</td>
      <td>52</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>77</td>
      <td>53</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>81</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>138</td>
      <td>99</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>159</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>167</td>
      <td>162</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>196</td>
      <td>170</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>217</td>
      <td>199</td>
      <td>219</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>235</td>
      <td>220</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>252</td>
      <td>239</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>253</td>
      <td>301</td>
      <td>255</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>322</td>
      <td>304</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>343</td>
      <td>325</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>356</td>
      <td>346</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>357</td>
      <td>366</td>
      <td>359</td>
      <td>368</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>384</td>
      <td>369</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>404</td>
      <td>388</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>409</td>
      <td>407</td>
      <td>411</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>432</td>
      <td>412</td>
      <td>434</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>433</td>
      <td>449</td>
      <td>435</td>
      <td>451</td>
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

### Maltose-specific binding and transport

bcMalT selectively binds and transports maltose. Scintillation proximity assay (SPA) with radiolabeled maltose showed an IC50 of 4.5 +/- 1.1 uM for competitive binding by unlabeled maltose. Reconstitution into proteoliposomes demonstrated maltose uptake via facilitated diffusion, reaching steady state after 10 minutes at 5-fold higher accumulation than control liposomes. No significant binding was observed for glucose, [Trehalose](/xray-mp-wiki/reagents/additives/trehalose), sucrose (except weak sucrose binding), or other tested sugars, indicating strict requirement for both sugar moieties and sensitivity to the alpha-1,4 glycosidic linkage.

### Elevator-car transport mechanism

Comparison of bcMalT (outward-facing occluded) with bcChbC (inward-facing occluded, PDB 3G5R) reveals a rigid-body displacement of the C-terminal substrate-binding domain by 44 degrees rotation and 9 A translation toward the periplasm, moving the substrate-binding cavity by approximately 20 A. Molecular dynamics simulations showed that TM7 rotation can open the cavity to the periplasm, suggesting an outward-facing open state. This supports an elevator-car mechanism where the substrate-binding domain carrying the intact ligand moves between inward-facing and outward-facing states.

### Active site architecture and substrate recognition

Each protomer contains a large cavity in the substrate-binding domain where [Maltose](/xray-mp-wiki/reagents/additives/maltose) is bound. Conserved residues forming hydrogen bonds include Glu355 (HP1) and His240 (TM7) interacting with C6 hydroxyl of the non-reducing sugar, Thr354 (HP1), Arg232 and Glu231 (TM6) with the non-reducing sugar, Lys307 (TM8) and His241 (TM7) stabilizing the reducing sugar, and Phe393 (HP2) contributing stacking interactions. These residues are strongly conserved within the Glc subfamily of EIIC transporters.

### Direct structural evidence for elevator mechanism from inward-facing bcMalT-X

The crystal structure of bcMalT cross-linked in an inward-facing conformation (bcMalT-X, 3.2 A) provides direct visualization of both outward- and inward-facing states on the same transporter. The substrate-binding domain undergoes a rigid-body 9 A vertical translation and 45 degree rotation relative to the dimerization domain. The amphipathic helix AH2 bends at a conserved Pro199 hinge, changing angle from 137.5 to 117.0 degrees to accommodate the domain motion. The structure was validated by all-atom MD simulations showing stability of the inward-facing state with or without Hg2+ cross-linking, and by smFRET experiments confirming a two-state equilibrium with a ~5:1 preference for the outward-facing conformation (free energy difference ~2-4 kJ/mol). The structure confirms the elevator-type mechanism for the glucose superfamily of EIIC transporters. 


## Cross-References

- <a href="/xray-mp-wiki/proteins/bc-chbc">bcChbC (Bacillus cereus Chitobiose Transporter)</a> — Comparison structure; inward-facing occluded conformation of [Glucose](/xray-mp-wiki/reagents/additives/glucose) superfamily EIIC
- <a href="/xray-mp-wiki/concepts/elevator-mechanism">Elevator Mechanism</a> — bcMalT provides structural evidence for elevator-car transport in EIIC transporters
- <a href="/xray-mp-wiki/concepts/alternating-access-mechanism">Alternating-Access Mechanism</a> — bcMalT and bcChbC represent outward- and inward-facing states of the alternating-access cycle
- <a href="/xray-mp-wiki/reagents/additives/maltose">Maltose</a> — bcMalT selectively binds and transports [Maltose](/xray-mp-wiki/reagents/additives/maltose); IC50 4.5 uM
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase Crystallization</a> — bcMalT crystallized using LCP method with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein)
- <a href="/xray-mp-wiki/reagents/detergents/ddm">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) used for membrane protein solubilization during bcMalT purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao">Lauryldimethylamine N-oxide (LDAO)</a> — [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao) used for functional assays and proteoliposome reconstitution
- <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> — [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) used as lipid matrix in LCP crystallization of bcMalT
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
