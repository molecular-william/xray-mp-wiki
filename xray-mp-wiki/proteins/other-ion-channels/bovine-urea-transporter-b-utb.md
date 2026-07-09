---
title: "Bovine Urea Transporter B (UT-B)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1207362109]
verified: regex
uniprot_id: Q5QF96
---

# Bovine Urea Transporter B (UT-B)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5QF96">UniProt: Q5QF96</a>

<span class="expr-badge">Bos taurus</span>

## Overview

Bovine UT-B is a mammalian urea transporter encoded by the SLC14A1 gene. It is a homotrimeric facilitative urea channel that mediates rapid passive diffusion of urea across cell membranes. UT-B is expressed in kidney vasa recta, erythrocytes, heart, colon, and brain, and plays a critical role in the urinary concentrating mechanism by preventing osmotic diuresis. The first X-ray crystal structure of a mammalian urea transporter was solved at 2.36 Å resolution, revealing a trimeric architecture with each protomer containing a urea conduction pore lined by a narrow selectivity filter with two urea-binding sites (So and Si) separated by a ~5.0 kcal/mol energy barrier at the Sm constriction site. UT-B function is modulated by hypoosmotic stress, with the Sm site serving as the site of osmoregulation.

## Publications

### doi/10.1073##pnas.1207362109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ezc">4EZC</a></td>
      <td>2.36</td>
      <td>--</td>
      <td>Full-length bovine UT-B (AAI05334.1) with C-terminal TEV protease recognition site and octohistidine tag</td>
      <td>Apo (substrate-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ezd">4EZD</a></td>
      <td>2.5</td>
      <td>--</td>
      <td>Full-length bovine UT-B with C-terminal TEV-octohistidine tag</td>
      <td>Selenourea (urea analog)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus system)
- **Construct**: Full-length bovine UT-B gene (AAI05334.1) subcloned into modified pFastBac Dual vector with C-terminal TEV protease recognition site and octohistidine tag
- **Notes**: Infected Sf9 cells harvested 48-60 h post-infection

**Purification:**

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/sf9-expression-system/) insect cells
- **Expression construct**: C-terminal [TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-octohistidine tagged UT-B

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
      <td>Cell harvesting and lysis</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a> infection of <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> insect cells</td>
      <td>—</td>
      <td></td>
      <td>Infected cells harvested 48-60 h post-infection</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a> (IMAC)</td>
      <td>-- (octohistidine tag)</td>
      <td></td>
      <td>C-terminal octohistidine tag used for purification</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage</td>
      <td>—</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> recognition site between UT-B and octohistidine tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Gel filtration</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified UT-B in detergent solution
**Yield**: --
**Purity**: --

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified bovine UT-B in detergent solution</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
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
      <td>Native UT-B crystals diffracted to 2.36 Å. Selenourea-bound crystals obtained by cocrystallization with 20 mM selenourea, diffracted to 2.5 Å. Data collected at selenium K-absorption edge for anomalous signal.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with selenourea</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Bovine UT-B with 20 mM selenourea</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
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
      <td>Selenourea used as a urea analog that produces strong anomalous signal for unambiguous identification of binding si<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a></td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezc">4EZC</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWLK</span><span class="topo-inside">DKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSALN</span><span class="topo-inside">SVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTWQT</span><span class="topo-membrane">HLLALACALFTAYLG</span><span class="topo-unknown">ASMSHVMA</span><span class="topo-outside">VVGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQS</span><span class="topo-unknown">RKRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>45</td>
      <td>38</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>46</td>
      <td>48</td>
      <td>46</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>169</td>
      <td>161</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>303</td>
      <td>296</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>318</td>
      <td>304</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>326</td>
      <td>319</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>327</td>
      <td>332</td>
      <td>327</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>375</td>
      <td>348</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>384</td>
      <td>376</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezc">4EZC</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWL</span><span class="topo-inside">KDKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSAL</span><span class="topo-inside">NSVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTW</span><span class="topo-membrane">QTHLLALACALFTAYLGASM</span><span class="topo-unknown">SHVMAV</span><span class="topo-outside">VGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQSR</span><span class="topo-unknown">KRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>38</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>159</td>
      <td>143</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>169</td>
      <td>160</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>301</td>
      <td>296</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>321</td>
      <td>302</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>327</td>
      <td>322</td>
      <td>327</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>328</td>
      <td>332</td>
      <td>328</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>376</td>
      <td>348</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>384</td>
      <td>377</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezc">4EZC</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWL</span><span class="topo-inside">KDKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSAL</span><span class="topo-inside">NSVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTWQT</span><span class="topo-membrane">HLLALACALFTAYLG</span><span class="topo-outside">ASMSHVMAVVGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQSR</span><span class="topo-unknown">KRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>38</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>159</td>
      <td>143</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>169</td>
      <td>160</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>303</td>
      <td>296</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>318</td>
      <td>304</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>332</td>
      <td>319</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>376</td>
      <td>348</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>384</td>
      <td>377</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezd">4EZD</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWL</span><span class="topo-inside">KDKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSALN</span><span class="topo-inside">SVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTW</span><span class="topo-membrane">QTHLLALACALFTAYLGASM</span><span class="topo-outside">SHVMAVVGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQS</span><span class="topo-unknown">RKRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>38</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>169</td>
      <td>161</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>301</td>
      <td>296</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>321</td>
      <td>302</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>332</td>
      <td>322</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>375</td>
      <td>348</td>
      <td>375</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>384</td>
      <td>376</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezd">4EZD</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWL</span><span class="topo-inside">KDKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSALN</span><span class="topo-inside">SVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTW</span><span class="topo-membrane">QTHLLALACALFTAYLGASM</span><span class="topo-outside">SHVMAVVGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQSR</span><span class="topo-unknown">KRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>38</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>169</td>
      <td>161</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>301</td>
      <td>296</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>321</td>
      <td>302</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>332</td>
      <td>322</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>376</td>
      <td>348</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>384</td>
      <td>377</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ezd">4EZD</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDDNPTAVKLDQGGNQAPQGRGRRCLPKAL</span><span class="topo-inside">GYITGDM</span><span class="topo-unknown">KEFANWL</span><span class="topo-inside">KDKP</span><span class="topo-unknown">QALQFVDWVLRGISQVVFV</span><span class="topo-inside">S</span><span class="topo-membrane">NPISGILILVGLLVQ</span><span class="topo-outside">NPWC</span><span class="topo-membrane">ALNGCVGTVVSTLTALLL</span><span class="topo-inside">SQDRSAITAG</span><span class="topo-membrane">LQGYN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ATLVGILM</span><span class="topo-outside">AIYSDKGNYFWWLL</span><span class="topo-membrane">FPVSAMSMTCPVFSSALN</span><span class="topo-inside">SVLSKWDLP</span><span class="topo-membrane">VFTLPFNMALSMY</span><span class="topo-outside">LSATGHYNPFFPSTLITPVTSVPNVTWPDLSALQLLKSL</span><span class="topo-unknown">PVGVGQIYGC</span><span class="topo-outside">DNPW</span><span class="topo-membrane">TGGIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LGAILLSSP</span><span class="topo-inside">L</span><span class="topo-membrane">MCLHAAIGSLLGIIA</span><span class="topo-outside">GLSLSAPFEDIYAGLW</span><span class="topo-membrane">GFNSSLACIAIGGT</span><span class="topo-inside">FMALTW</span><span class="topo-membrane">QTHLLALACALFTAYLGASM</span><span class="topo-outside">SHVMAVVGLPS</span><span class="topo-membrane">GTWPFCLATLLFLLL</span><span class="topo-inside">TTKNPNIYKMPIS</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">KVTYPEENRIFYLQSR</span><span class="topo-unknown">KRTVQGPL</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>31</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>38</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>45</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>83</td>
      <td>69</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>84</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>115</td>
      <td>106</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>128</td>
      <td>116</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>142</td>
      <td>129</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>160</td>
      <td>143</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>169</td>
      <td>161</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>221</td>
      <td>183</td>
      <td>221</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>222</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>235</td>
      <td>232</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>281</td>
      <td>266</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>295</td>
      <td>282</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>301</td>
      <td>296</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>321</td>
      <td>302</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>322</td>
      <td>332</td>
      <td>322</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>347</td>
      <td>333</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>376</td>
      <td>348</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>384</td>
      <td>377</td>
      <td>384</td>
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

### Trimeric architecture and pore structure

UT-B forms a homotrimer with each protomer containing an independent urea conduction pore. The pore is formed at the interface of two pseudo-symmetrical halves (TM1-5 and TM6-10), lined by conserved urea signature sequence residues. The selectivity filter contains three regions: So (rectangular, oxygen ladder), Si (rectangular, oxygen ladder), and Sm (constricted, hydrophobic region with pseudo-symmetry-related threonine residues T172 and T334).

### Two urea-binding sites with an energy barrier

The selectivity filter has two urea-binding sites (So and Si) separated by an approximately 5.0 kcal/mol energy barrier at the Sm site. So and Si sites contain oxygen ladders (arrays of carbonyl and side-chain oxygen atoms) that coordinate urea via hydrogen bonds. MD simulations show that urea molecules are partially hydrated in So and Si (1.5-2.0 hydrogen bonds with water) but become completely dehydrated at the Sm site, accounting for the energetic barrier.

### Osmoregulation at the Sm site

UT-B function is modulated by hypoosmotic stress. Oocyte uptake assays showed ~2-fold increase in urea uptake under hypotonic conditions. The T172S/T334S double mutant (conserving hydrogen bonding at the Sm site) had similar basal activity to wild-type but lacked the hypoosmotic response, demonstrating that the Sm site is the site of osmoregulation. The T334V mutant (removing hydrogen bond capacity) abolished urea transport, confirming the functional importance of the Sm site threonine residues.

### Comparison with bacterial dvUT

The mammalian UT-B structure is similar to the bacterial dvUT (Desulfovibrio vulgaris urea transporter) but with key differences. The largest difference is a phenylalanine-to-glycine mutation in the So site (position 230 in UT-B), compensated by a leucine residue on helix TM3a that takes the place of the aromatic ring. The N-terminal amphipathic helix orientation also differs, though this may be affected by crystal contacts in the bacterial structure.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/urea-transporter-dvut/">Urea Transporter from Desulfovibrio vulgaris (dvUT)</a> — Bacterial homolog of mammalian UT-B; comparison of pore architecture and selectivity filter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin</a> — Structural and mechanistic parallels between urea transporters and aquaporins (ar/R motif, Sm site analogy)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Selectivity Filter</a> — The oxygen ladder and Sm site selectivity mechanism of UT-B is a key example of filter-based substrate discrimination
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-like-mechanism/">Channel-like Mechanism</a> — UT-B operates by a channel-like mechanism rather than alternating-access transport
