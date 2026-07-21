---
title: "BbZIP (Bordetella bronchiseptica ZIP metal transporter)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-023-36048-4]
verified: agent
uniprot_id: A0A0H3LM39
---

# BbZIP (Bordetella bronchiseptica ZIP metal transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0H3LM39">UniProt: A0A0H3LM39</a>

<span class="expr-badge">Bordetella bronchiseptica (strain ATCC BAA-588 / NCTC 13252 / RB50)</span>

## Overview

BbZIP (ZIPB) is a prokaryotic ZIP family divalent metal transporter from Bordetella bronchiseptica. The Zrt/Irt-like protein (ZIP) family (SLC39A) imports Zn2+, Fe2+, Mn2+, and other first-row d-block divalent metals into the cytoplasm and is ubiquitously expressed across all kingdoms of life. BbZIP was structurally characterized to establish the transport mechanism for the ZIP family. The protein adopts a two-domain architecture with a transport domain (Domain I: α1/4/5/6) that carries the binuclear metal centre (BMC) and slides vertically as a rigid body against a static scaffold domain (Domain II: α2/3/7/8) that mediates dimerization, consistent with an elevator-type transport mechanism. BbZIP has nine transmembrane helices (α0 plus the conserved α1-α8 core), with the extra N-terminal α0 present in some gufA subfamily members.


## Publications

### doi/10.1038##s41467-023-36048-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tsb">5TSB</a></td>
      <td>2.75</td>
      <td>P 2_1 2_1 2</td>
      <td>Full-length BbZIP with N-terminal His-tag (metal-bound inward-facing conformation, used as MR search model)</td>
      <td>Cd2+ (binuclear metal centre)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8czj">8CZJ</a></td>
      <td>2.75</td>
      <td>P 2_1 2_1 2_1</td>
      <td>Full-length BbZIP with N-terminal His-tag (apo state, metal-free)</td>
      <td>apo (no metal)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length BbZIP from Bordetella bronchiseptica with N-terminal His-tag
- **Induction**: Not specified in detail

**Purification:**

- **Expression system**: E. coli
- **Tag info**: N-terminal His-tag

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
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM NaH2PO4 pH 7.5, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.25 mM CdCl2 + 1.5% (w/v) n-dodecyl-β-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membrane fraction solubilized for 1 h at 4°C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td>HisPur Cobalt Resin (Thermo Fisher Scientific)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.3, 300 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.25 mM CdCl2, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with CdCl2 to maintain metal-bound state</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superdex Increase 200 (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.3, 300 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.25 mM CdCl2, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>For cysteine variants, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> added during purification but excluded in gel filtration buffer</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified protein in gel filtration buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified BbZIP at 15 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (protein:monoolein, v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>21°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Stick-shaped crystals appeared after ~1 week; crystallization at low pH (~4.0) was necessary to obtain the apo state</td>
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
      <td>4.0</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>21 C</td>
    </tr>
    <tr>
      <td>Protein:lipid ratio</td>
      <td>2:3 (protein:monoolein, v/v)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 27 % [precipitant] (Peg 200)  
- Sodium Chloride: 20 mM [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5tsb">5TSB</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNQPSSLAADLRGAWHAQAQSHPLITLGLAASAAGVVLLLVAGIVNALTGENRVH</span><span class="topo-inside">V</span><span class="topo-membrane">GYAVLGGAAGFAATALGALM</span><span class="topo-outside">ALGLRAISARTQ</span><span class="topo-membrane">DAMLGFAAGMMLAASAFSLILPGL</span><span class="topo-inside">DAAGTIVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PGPAAA</span><span class="topo-membrane">AVVALGLGLGVLLMLGLDY</span><span class="topo-unknown">FTPHEHERTGHQGPEAAR</span><span class="topo-outside">VNRVWL</span><span class="topo-membrane">FVLTIILHNLPEGMAIGVSFA</span><span class="topo-inside">TGDL</span><span class="topo-membrane">RIGLPLTSAIAIQDVPEGLAVA</span><span class="topo-outside">LALRAVGLPIGRAV</span><span class="topo-membrane">LVAVASGLME</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-membrane">PLGALVGVGIS</span><span class="topo-inside">SGFALA</span><span class="topo-membrane">YPISMGLAAGAMIFVVSHEV</span><span class="topo-unknown">IPETHRNGHET</span><span class="topo-outside">T</span><span class="topo-membrane">ATVGLMAGFALMMFLDTAL</span><span class="topo-unknown">G</span></span>
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
      <td>56</td>
      <td>56</td>
      <td>56</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>88</td>
      <td>77</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>89</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>113</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>127</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>169</td>
      <td>164</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>190</td>
      <td>170</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>194</td>
      <td>191</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>216</td>
      <td>195</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>230</td>
      <td>217</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>251</td>
      <td>231</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>257</td>
      <td>252</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>277</td>
      <td>258</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>289</td>
      <td>289</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>308</td>
      <td>290</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8czj">8CZJ</a> — Chain A (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNQP</span><span class="topo-outside">SSLAADLRGAWHAQAQSH</span><span class="topo-membrane">PLITLGLAASAAGVVLLLVAGIVNAL</span><span class="topo-inside">TGENRVHV</span><span class="topo-membrane">GYAVLGGAAGFAATALGALM</span><span class="topo-outside">ALGLRAISAR</span><span class="topo-membrane">TQDAMLGFAAGMMLAASAFSLIL</span><span class="topo-inside">PGLDAAGTIVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PGPAAA</span><span class="topo-membrane">AVVALGLGLGVLLMLGLDYFT</span><span class="topo-outside">P</span><span class="topo-unknown">HEHERTGHQG</span><span class="topo-outside">PEAARVNRVWLFVL</span><span class="topo-membrane">TIILHNLPEGMAIGVSFA</span><span class="topo-inside">TGDLRI</span><span class="topo-membrane">GLPLTSAIAIQDVPEGLAV</span><span class="topo-outside">ALALRAVGLPIGRAV</span><span class="topo-membrane">LVAVASGLME</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-membrane">PLGALVGVGISSG</span><span class="topo-inside">FALA</span><span class="topo-membrane">YPISMGLAAGAMIFVVSHEVIPETH</span><span class="topo-outside">RNGH</span><span class="topo-membrane">ETTATVGLMAGFALMMFLD</span><span class="topo-inside">TALG</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>48</td>
      <td>23</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>109</td>
      <td>87</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>126</td>
      <td>110</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>172</td>
      <td>159</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>196</td>
      <td>191</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>215</td>
      <td>197</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>230</td>
      <td>216</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>253</td>
      <td>231</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>257</td>
      <td>254</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>282</td>
      <td>258</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>286</td>
      <td>283</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>305</td>
      <td>287</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8czj">8CZJ</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNQP</span><span class="topo-outside">SSLAADLRGAWHAQAQSH</span><span class="topo-membrane">PLITLGLAASAAGVVLLLVAGIVNAL</span><span class="topo-inside">TGENRVHV</span><span class="topo-membrane">GYAVLGGAAGFAATALGALM</span><span class="topo-outside">ALGLRAISAR</span><span class="topo-membrane">TQDAMLGFAAGMMLAASAFSLIL</span><span class="topo-inside">PGLDAAGTIVG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PGPAAA</span><span class="topo-membrane">AVVALGLGLGVLLMLGLDYFT</span><span class="topo-outside">PH</span><span class="topo-unknown">EHERTGHQG</span><span class="topo-outside">PEAARVNRVWLFVL</span><span class="topo-membrane">TIILHNLPEGMAIGVSFA</span><span class="topo-inside">TGDLRI</span><span class="topo-membrane">GLPLTSAIAIQDVPEGLAV</span><span class="topo-outside">ALALRAVGLPIGRAV</span><span class="topo-membrane">LVAVASGLME</span></span>
<span class="topo-ruler">       250       260       270       280       290       300         </span>
<span class="topo-line"><span class="topo-membrane">PLGALVGVGISSG</span><span class="topo-inside">FALA</span><span class="topo-membrane">YPISMGLAAGAMIFVVSHEVIPETH</span><span class="topo-outside">RNGH</span><span class="topo-membrane">ETTATVGLMAGFALMMFLD</span><span class="topo-inside">TALG</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>48</td>
      <td>23</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>109</td>
      <td>87</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>126</td>
      <td>110</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>147</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>149</td>
      <td>148</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>158</td>
      <td>150</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>172</td>
      <td>159</td>
      <td>172</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>190</td>
      <td>173</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>196</td>
      <td>191</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>215</td>
      <td>197</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>230</td>
      <td>216</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>253</td>
      <td>231</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>257</td>
      <td>254</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>282</td>
      <td>258</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>286</td>
      <td>283</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>305</td>
      <td>287</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>309</td>
      <td>306</td>
      <td>309</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Elevator-Type Transport Mechanism

BbZIP operates via an elevator-type mechanism where Domain I (α1/α4/α5/α6) slides as a rigid body ~8 Å vertically against Domain II (α2/α3/α7/α8). The binuclear metal centre (BMC) is carried by Domain I, and its vertical translocation exposes the transport site alternately to each side of the membrane. Metal release disassembles the primary M1 site, weakening interdomain interactions and facilitating the conformational switch. A repeat-swap homology model of the outward-facing conformation (OFC) was experimentally validated by cysteine accessibility assays and Hg2+-mediated chemical crosslinking.

### Two-Domain Architecture

The apo state structure revealed that BbZIP comprises two structurally independent domains. Evolutionary covariance analysis confirmed this architecture, showing far more intradomain than interdomain predicted interactions. The greasy domain interface is lined with conserved small residues (Ala, Gly, Ser); mutation of these to bulky amino acids in human ZIP4 severely impaired transport, supporting the requirement for a smooth sliding interface typical of elevator transporters.

### Dimerization

BbZIP forms a dimer mediated by Domain II (the scaffold domain) in both detergent and native membranes. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) in Amphipol A8-35 showed near-symmetrical dimer particles. The dimer appears dynamic, existing in a monomer-dimer equilibrium. Covariance analysis and cysteine crosslinking support a dimer interface involving α2 (Domain II of one protomer) and α8 (Domain II of the second protomer), with the scaffold domains forming a static dimeric base while the transport domains move independently.


## Cross-References

- <a href="/xray-mp-wiki/concepts/elevator-type-transport-mechanism/">Elevator-type transport mechanism</a> — BbZIP is demonstrated to be an elevator-type transporter with rigid-body vertical sliding of the transport domain
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in the context of DDM
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in the context of Hepes
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in the context of Peg
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo Em</a> — Referenced in the context of Cryo Em
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in the context of Imidazole
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in the context of Glycerol
- <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> — Referenced in the context of TCEP
