---
title: "Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature24464, doi/10.1038##s41467-019-12673-w]
verified: false
---

# Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae)

## Overview

Vrg4 is a [GDP-Mannose](/xray-mp-wiki/reagents/substrates/gdp-mannose) transporter from the yeast Saccharomyces cerevisiae, belonging to the SLC35 family of nucleotide sugar transporters. It is a 10-transmembrane helix protein that shuttles activated monosaccharides (nucleotide sugars) across the Golgi membrane, providing substrates for glycosyltransferases. Vrg4 displays strict specificity for guanine-containing nucleotides and recognizes both GMP and [GDP-Mannose](/xray-mp-wiki/reagents/substrates/gdp-mannose). The transporter operates via an alternating-access mechanism with two structural repeats (TM1-TM5 and TM6-TM10). Vrg4 requires short-chain lipids for activity and was crystallized in the lipidic cubic phase. The structure of the GMP-bound complex revealed that GMP adopts multiple conformations within the binding site, explaining the slower transport rate of GMP compared to GDP-mannose. Lipids mediate dimer formation and regulate transport activity.


## Publications

### doi/10.1038##nature24464

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5oge">5OGE</a></td>
      <td>3.22</td>
      <td>P212121</td>
      <td>Full-length Vrg4</td>
      <td>None (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ogk">5OGK</a></td>
      <td>3.60</td>
      <td>P1</td>
      <td>Full-length Vrg4</td>
      <td>GDP-mannose</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: C-terminal GFP-His6 fusion
- **Induction**: 1.5% galactose
- **Media**: Medium minus leucine with 2% lactate, induced with galactose

**Purification:**

- **Expression system**: Saccharomyces cerevisiae
- **Expression construct**: C-terminal GFP-His6 fusion
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag)

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
      <td>Medium minus leucine, 2% lactate + --</td>
      <td>15L fermentation vessel, 24h growth</td>
    </tr>
    <tr>
      <td>Induction</td>
      <td>Chemical induction</td>
      <td>--</td>
      <td>--</td>
      <td>1.5% galactose from 25% w/v stock, 24h post-induction</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Cell harvesting</td>
      <td>--</td>
      <td>--</td>
      <td>Yeast collected after induction</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a></td>
      <td>-- + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Standard <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a> protocols</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> (10/300) <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> column</td>
      <td>-- + 0.3% DM</td>
      <td>Detergent exchanged for reconstitution</td>
    </tr>
  </tbody>
</table>
**Final sample**: 40 mg/ml in [DDM](/xray-mp-wiki/reagents/detergents/ddm)
**Purity**: >95% by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>40 mg/ml Vrg4 in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>60:40</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryo-cooled directly in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Heavy-atom screening with 1-5 mM <a href="/xray-mp-wiki/reagents/additives/mercury">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivatives; phases determined by long-wavelength anomalous dispersion (Hg/S-SAD) at 2.7 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5oge">5OGE</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSELKTGHAGHNPWA</span><span class="topo-inside">SVANSGP</span><span class="topo-membrane">ISILSYCGSSILMTVTNKFVV</span><span class="topo-outside">NLKDFNM</span><span class="topo-membrane">NFVMLFVQSL</span></span>
<span class="topo-line"><span class="topo-membrane">VCTITLIILRIL</span><span class="topo-inside">G</span><span class="topo-unknown">YAK</span><span class="topo-inside">FRSLNKTDAKNW</span><span class="topo-membrane">FPISFLLVLMIYTSSKAL</span><span class="topo-outside">QYLAV</span><span class="topo-membrane">PIYTIFKNL</span></span>
<span class="topo-line"><span class="topo-membrane">TIILIAYG</span><span class="topo-inside">EVLFFGGSVTS</span><span class="topo-membrane">MELSSFLLMVLSSVVATW</span><span class="topo-outside">GDQ</span><span class="topo-unknown">QAVAAKAASLAEGAAG</span><span class="topo-outside">AVAS</span></span>
<span class="topo-line"><span class="topo-outside">FN</span><span class="topo-membrane">PGYFWMFTNCITSALFVLIM</span><span class="topo-inside">RKRIKLTNFKDFDT</span><span class="topo-membrane">MFYNNVLALPILLLFSFCVE</span><span class="topo-outside">DWS</span><span class="topo-unknown">S</span></span>
<span class="topo-line"><span class="topo-unknown">VNLTNN</span><span class="topo-outside">FSNDSL</span><span class="topo-membrane">TAMIISGVASVGISYCSGWCV</span><span class="topo-inside">RVTS</span><span class="topo-membrane">STTYSMVGALNKLPIALSGLI</span><span class="topo-outside">FF</span></span>
<span class="topo-line"><span class="topo-outside">DAPRNFL</span><span class="topo-membrane">SILSIFIGFLSGIIYAVA</span><span class="topo-inside">KQKKQQAQ</span><span class="topo-unknown">PLRK</span></span>
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
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>43</td>
      <td>23</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>50</td>
      <td>44</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>51</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>88</td>
      <td>77</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>106</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>111</td>
      <td>107</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>128</td>
      <td>112</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>139</td>
      <td>129</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>140</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>160</td>
      <td>158</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>182</td>
      <td>177</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>183</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>216</td>
      <td>203</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>236</td>
      <td>217</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>239</td>
      <td>237</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>246</td>
      <td>240</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>247</td>
      <td>252</td>
      <td>247</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>273</td>
      <td>253</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>277</td>
      <td>274</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>298</td>
      <td>278</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>307</td>
      <td>299</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>325</td>
      <td>308</td>
      <td>325</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>333</td>
      <td>326</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ogk">5OGK</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSELKTGHAGHNPWASVA</span><span class="topo-inside">NSGPIS</span><span class="topo-membrane">ILSYCGSSILMTVTN</span><span class="topo-outside">KFVVNLKDFNMNF</span><span class="topo-membrane">VMLFVQSL</span></span>
<span class="topo-line"><span class="topo-membrane">VCTITLIILRIL</span><span class="topo-inside">G</span><span class="topo-unknown">YAK</span><span class="topo-inside">FRSLNKTDA</span><span class="topo-membrane">KNWFPISFLLVLMIYTSS</span><span class="topo-outside">KALQYLAV</span><span class="topo-membrane">PIYTIFKNL</span></span>
<span class="topo-line"><span class="topo-membrane">TIILIAYG</span><span class="topo-inside">EVLFFGGSVTSME</span><span class="topo-membrane">LSSFLLMVLSSVVATW</span><span class="topo-outside">GDQQ</span><span class="topo-unknown">AVAAKAASLAEGAAGAVAS</span></span>
<span class="topo-line"><span class="topo-unknown">F</span><span class="topo-outside">NPGY</span><span class="topo-membrane">FWMFTNCITSALFVLIM</span><span class="topo-inside">RKRIKLTNFKDF</span><span class="topo-membrane">DTMFYNNVLALPILLLFS</span><span class="topo-outside">FCVEDWSS</span></span>
<span class="topo-line"><span class="topo-outside">VNLTNNFSNDSLTAM</span><span class="topo-membrane">IISGVASVGISYCSGWCV</span><span class="topo-inside">RVTSS</span><span class="topo-membrane">TTYSMVGALNKLPIALSGLIF</span><span class="topo-outside">F</span></span>
<span class="topo-line"><span class="topo-outside">DAPRNF</span><span class="topo-membrane">LSILSIFIGFLSGIIYA</span><span class="topo-inside">VAKQKKQQAQ</span><span class="topo-unknown">PLRK</span></span>
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
      <td>19</td>
      <td>24</td>
      <td>19</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>25</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>52</td>
      <td>40</td>
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
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>85</td>
      <td>77</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>103</td>
      <td>86</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>104</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>128</td>
      <td>112</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>141</td>
      <td>129</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>157</td>
      <td>142</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>161</td>
      <td>158</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>185</td>
      <td>182</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>202</td>
      <td>186</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>214</td>
      <td>203</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>232</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>255</td>
      <td>233</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>273</td>
      <td>256</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>278</td>
      <td>274</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>306</td>
      <td>300</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>323</td>
      <td>307</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>333</td>
      <td>324</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ogk">5OGK</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSELKTGHAGHNPWASVA</span><span class="topo-inside">NSGPIS</span><span class="topo-membrane">ILSYCGSSILMTVTN</span><span class="topo-outside">KFVVNLKDFNMN</span><span class="topo-membrane">FVMLFVQSL</span></span>
<span class="topo-line"><span class="topo-membrane">VCTITLIILRIL</span><span class="topo-inside">G</span><span class="topo-unknown">YAK</span><span class="topo-inside">FRSLNKTDA</span><span class="topo-membrane">KNWFPISFLLVLMIYTSS</span><span class="topo-outside">KALQYLAV</span><span class="topo-membrane">PIYTIFKNL</span></span>
<span class="topo-line"><span class="topo-membrane">TIILIAYG</span><span class="topo-inside">EVLFFGGSVTSME</span><span class="topo-membrane">LSSFLLMVLSSVVATW</span><span class="topo-outside">GDQQ</span><span class="topo-unknown">AVAAKAASLAEGAAG</span><span class="topo-outside">AVAS</span></span>
<span class="topo-line"><span class="topo-outside">FNPGY</span><span class="topo-membrane">FWMFTNCITSALFVLIM</span><span class="topo-inside">RKRIKLTNFKDF</span><span class="topo-membrane">DTMFYNNVLALPILLLFS</span><span class="topo-outside">FCVEDWSS</span></span>
<span class="topo-line"><span class="topo-outside">VNLTNNFSNDSLTAM</span><span class="topo-membrane">IISGVASVGISYCSGWCV</span><span class="topo-inside">RVTSS</span><span class="topo-membrane">TTYSMVGALNKLPIALSGLIF</span><span class="topo-outside">F</span></span>
<span class="topo-line"><span class="topo-outside">DAPRNF</span><span class="topo-membrane">LSILSIFIGFLSGIIY</span><span class="topo-inside">AVAKQKKQQAQ</span><span class="topo-unknown">PLRK</span></span>
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
      <td>19</td>
      <td>24</td>
      <td>19</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>25</td>
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
      <td>72</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>85</td>
      <td>77</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>103</td>
      <td>86</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>111</td>
      <td>104</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>128</td>
      <td>112</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>141</td>
      <td>129</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>157</td>
      <td>142</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>161</td>
      <td>158</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>185</td>
      <td>177</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>202</td>
      <td>186</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>214</td>
      <td>203</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>232</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>255</td>
      <td>233</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>273</td>
      <td>256</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>278</td>
      <td>274</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>279</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>306</td>
      <td>300</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>322</td>
      <td>307</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>333</td>
      <td>323</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-019-12673-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6s98">6S98</a></td>
      <td>3.30</td>
      <td>P212121</td>
      <td>Full-length Vrg4</td>
      <td>GMP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: C-terminal GFP-His6 fusion
- **Induction**: 1.5% galactose
- **Media**: Medium minus leucine with 2% lactate, induced with galactose


## Biological / Functional Insights

### Nucleotide recognition via FYNN motif

The nucleotide pocket is formed by side chains from TM7 and TM8, interacting via the O6 carbonyl group with Asn221 (TM7) and Ser266 (TM8) and via the N2 amine group with Asn220 (TM7). These specific interactions with the O6 carbonyl of the guanine ring explain the lower IC50 values for GMP compared to AMP, which lacks an oxygen at this position. These asparagine residues are located within a conserved FYNN motif (F218-YNN), present only in transporters that recognize guanine-containing nucleotide sugars. Transport assays on alanine variants of Asn220 or Asn221 show equal reduction in overall transport, while removal of both results in complete loss of function.

### Ribose positioning

The ribose group forms interactions with side chains from both the N- and C-terminal halves of the transporter. The O2 oxygen resides within hydrogen-bonding distance of Tyr28 (TM1), Ser269 (TM8), and Tyr281 (TM9). Tyr28 is strictly conserved and its replacement with alanine abolishes transport. Tyr281 is semi-conserved but generally a bulky side chain; a phenylalanine substitution maintains function while alanine abolishes it, suggesting a bulky side chain is required to optimally position the ribose group and/or the nearby conserved Tyr28.

### Sugar recognition via GALNK motif

The first phosphate is positioned close to Met35 (TM1), while the second phosphate interacts with Lys289 (TM9), which forms part of the GALNK motif (G285-ALNK). Lys289 interacts with both the beta-phosphate and the glycosidic-bond oxygen. Both Lys289Ala and Gly285Ala reduced activity, with the lysine replacement being more severe. The sugar pocket also includes a conserved tyrosine, Tyr114 (TM4), which makes a hydrogen bond to the C2 hydroxyl on the mannose ring. A Tyr114Phe variant displayed reduced transport, highlighting the importance of a hydrogen-bond donor at this position.

### Disease mutations in human SLC35C1

Homology modeling of the human [GDP-Fucose](/xray-mp-wiki/reagents/substrates/gdp-fucose) transporter ([SLC35C1 Human GDP-Fucose Transporter](/xray-mp-wiki/proteins/slc35c1)) reveals the GTAKA motif replacing GALNK in the sugar pocket. Disease mutations causing leukocyte adhesion deficiency II (Arg147Cys and Thr308Arg) map to residues near the sugar binding site. Thr308 is on the same helix as the GTAKA motif and packs against TM10, while Arg147 is equivalent to Lys118 in Vrg4 and resides close to the sugar binding site. These mutations likely disrupt the sugar binding site.

### Alternating-access mechanism

Vrg4 uses an alternating-access mechanism with two structural repeat units (TM1-TM5 and TM6-TM10) related by a two-fold rotation in the plane of the membrane. The bound [GDP-Mannose](/xray-mp-wiki/reagents/substrates/gdp-mannose) sits at the center of rotation. The crystal structure captures the open-to-lumen state, with TM6-TM7 packed against TM8-TM9 to seal the cavity from the cytoplasm, while TM1-TM2 and TM3-TM4 are opened out. Repeat-swapped modeling reveals the open-to-cytoplasm state.

### Lipid dependence

Vrg4 requires short-chain-length lipids for function. [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) lipids were observed at the dimer interface in the crystal structure, contributing ~60% to the total buried surface area of 1514 A2. The hydrophobic belt is notably shorter (~30 A) than that observed for plasma or inner membrane transporters (~40 A). Lipid-mediated dimerization was suggested by the absence of lipid density at these sites in monomeric molecules in the unit cell.

### GMP binding induces multiple conformations

The crystal structure of Vrg4 bound to GMP at 3.3 Å resolution revealed that GMP adopts three distinct conformations across the binding sites in the unit cell. Two of the three GMP molecules adopt extended conformations, while the third adopts a bent configuration with the phosphate group pointing towards the Golgi lumen. This positional flexibility of GMP explains its slower transport rate compared to GDP-mannose (IC50 7 µM vs 50 µM for AMP). The reduced number of stable interactions between GMP and the binding pocket, particularly with K289 of the GALNK motif, results in less efficient coupling between ligand binding and the conformational changes needed for transport.

### Lipid-mediated dimerization regulates transport

In the membrane, Vrg4 forms dimers through a lipid-mediated interface involving TM5 and TM10. Two well-ordered monoolein lipid molecules contribute ~60% of the buried surface area at the dimer interface. Molecular dynamics simulations show that phospholipids (DPPC/DMPC) accumulate at this interface, accommodating up to four lipids as a bilayer. Dominant-negative assays demonstrate that while Vrg4 forms oligomers in liposome membranes, each monomer acts as an independent functional unit. The dimer interface likely provides structural stability rather than being directly required for transport activity.

### Short-chain lipid dependence mechanism

Molecular dynamics simulations identified a secondary lipid binding site in a shallow groove between TM1, TM9, and TM10 that exclusively accommodates short-chain DMPC lipids (C14:0) but not longer-chain DPPC (C16:0). This site connects TM9 (which contains the GALNK motif) with TM1 (which contains the gating residue Y28), providing a structural link between the pairs of gating helices. This explains the strict requirement for short-chain lipids for Vrg4 function and suggests that local bilayer properties such as thickness and lipid ordering regulate transporter activity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — LCP crystallization lipid
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent for purification
- <a href="/xray-mp-wiki/reagents/detergents/decyl-maltoside/">Decyl Maltoside (DM)</a> — Detergent for reconstitution
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a> — Crystallization precipitant
- <a href="/xray-mp-wiki/reagents/buffers/sodium-citrate/">Sodium Citrate</a> — Crystallization buffer
- <a href="/xray-mp-wiki/reagents/ligands/gdp/">Guanosine Diphosphate (GDP)</a> — Substrate analog
- <a href="/xray-mp-wiki/reagents/ligands/gmp/">Guanosine Monophosphate (GMP)</a> — Substrate analog
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sl35-family/">SLC35 Family (Nucleotide Sugar Transporters)</a> — Transporter family classification
- <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> — Entity mentioned in text
