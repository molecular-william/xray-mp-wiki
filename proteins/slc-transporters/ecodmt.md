---
title: "EcoDMT - Eremococcus coleocola NRAMP Divalent Metal Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.51913, doi/10.1038##ncomms14033]
verified: false
---

# EcoDMT - Eremococcus coleocola NRAMP Divalent Metal Transporter

## Overview

EcoDMT is a prokaryotic divalent metal transporter from Eremococcus coleocola belonging to the SLC11/NRAMP family. It catalyzes H+-coupled Mn2+ symport and serves as a structural homologue of human DMT1 (SLC11A2), the primary transporter of dietary ferrous  in enterocytes. EcoDMT adopts the  fold characteristic of the [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/), consisting of two topologically related units of five transmembrane helices arranged with opposite orientation. The crystal structure of EcoDMT in complex with the brominated bis-isothiourea inhibitor Br-BIT (PDB 6TL2, 3.8 A) reveals the inhibitor bound to the outward-facing aqueous cavity at the base of a funnel-shaped pocket, with the proximal isothiourea group positioned in direct contact with the metal ion coordination site. This structural characterization, combined with functional studies on both EcoDMT and human DMT1, provides the first detailed mechanistic insight into the pharmacology of SLC11/NRAMP transporters.

## Publications

### doi/10.7554##eLife.51913

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tl2">6TL2</a></td>
      <td>3.8 A</td>
      <td>C2</td>
      <td>Full-length EcoDMT with C-terminal His10-tag (cleaved for crystallization)</td>
      <td>Br-BIT (3,5-bis-isothiourea-1-bromobenzene)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: EcoDMT with C-terminal 3C protease cleavage site and His10-tag, cloned in pBXC3GH/pBXC3H vectors

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
      <td>Cell lysis</td>
      <td>High-pressure cell disruption</td>
      <td>--</td>
      <td>20 mM  pH 7.5, 150 mM NaCl</td>
      <td>Lysis buffer supplemented with 1 mg/mL lysozyme and 20 ug/mL DNase I. HPL6 high-pressure cell disruptor.</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>20 mM  pH 7.5, 150 mM NaCl</td>
      <td>Low-spin at 10,000 x g for 20 min, then ultracentrifugation at 200,000 x g for 1 hr</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>20 mM  pH 7.5, 150 mM NaCl, 10% (w/v)  + 1-2% (w/v)  (or 0.04%  for ITC samples)</td>
      <td>Membranes resuspended and extracted, cleared by centrifugation</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-Sepharose</td>
      <td>20 mM  pH 7.5, 150 mM NaCl, 8.7% (w/v)  + 0.1% (w/v)  (or 0.04%  for ITC)</td>
      <td>Tag cleaved with HRV-3C protease at 5:1 protein:protease ratio for 2 hr during dialysis. Second IMAC step to separate cleaved protein.</td>
    </tr>
    <tr>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Superdex 200 (GE Healthcare)</td>
      <td>20 mM  pH 7.5, 150 mM NaCl, 8.7% (w/v) , 0.1% (w/v)  + 0.1% (w/v) </td>
      <td>Final purification step. Peak fractions pooled and concentrated.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EcoDMT at 7-10 mg/mL in 20 mM  pH 7.5, 150 mM NaCl, 8.7% , 0.1% </td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM  Hcl]] pH 8.0-9.0, 22-26%  400 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>24-well plates, 1 uL protein + 1 uL reservoir equilibrated against 500 uL reservoir. Inhibitor soaks: Br-BIT and oBr-BIT soaked into pre-grown crystals. Data collected at Swiss Light Source beamlines X06SA and X06DA at wavelength 0.92 A (bromine anomalous edge). 3.8 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tl2">6TL2</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNWSTS</span><span class="topo-inside">ITGGQNFQY</span><span class="topo-membrane">LLLSI</span></span>
<span class="topo-line"><span class="topo-membrane">IVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRA</span><span class="topo-outside">RTSRRLGF</span><span class="topo-membrane">IFWILTELAIMATDIAEVIG</span></span>
<span class="topo-line"><span class="topo-membrane">AAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLLN</span><span class="topo-outside">RIGFRK</span><span class="topo-membrane">IEALVVCLIFVILFVFLYQII</span><span class="topo-inside">LS</span></span>
<span class="topo-line"><span class="topo-inside">QPAWHQVAKGLIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLFLH</span><span class="topo-outside">SAISQSRKIDR</span></span>
<span class="topo-line"><span class="topo-outside">TDSSKVAEAVRFSNWD</span><span class="topo-membrane">SNIQLSLAMVVNALLLI</span><span class="topo-inside">MGVAVFKSGAVQDPS</span><span class="topo-unknown">FFGLYQALS</span><span class="topo-inside">NPD</span></span>
<span class="topo-line"><span class="topo-inside">MVSN</span><span class="topo-unknown">PVLAEAAR</span><span class="topo-inside">SGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFIHLRLPL</span><span class="topo-membrane">WLRRLVT</span></span>
<span class="topo-line"><span class="topo-membrane">RLIAIIPVVVC</span><span class="topo-inside">VAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span><span class="topo-outside">PLLMLTDSAAQMG</span></span>
<span class="topo-line"><span class="topo-outside">NQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span><span class="topo-membrane">SQVISIGIILAMI</span></span>
<span class="topo-line"><span class="topo-membrane">GLLIW</span><span class="topo-outside">TIIDIRRFT</span></span>
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
      <td>18</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>25</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>28</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>55</td>
      <td>59</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>73</td>
      <td>68</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>85</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>98</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>93</td>
      <td>100</td>
      <td>105</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>125</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>134</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>151</td>
      <td>147</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>164</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>178</td>
      <td>170</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>210</td>
      <td>191</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>229</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>256</td>
      <td>242</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>273</td>
      <td>269</td>
      <td>285</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>288</td>
      <td>286</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>297</td>
      <td>301</td>
      <td>309</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>298</td>
      <td>304</td>
      <td>310</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>312</td>
      <td>317</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>313</td>
      <td>319</td>
      <td>325</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>339</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>353</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>371</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>390</td>
      <td>384</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>407</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>431</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>467</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>485</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>494</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms14033

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a></td>
      <td>3.3 A</td>
      <td>C2</td>
      <td>Full-length EcoDMT, residues 13-506, outward-facing conformation, wildtype</td>
      <td>None (apo form)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a></td>
      <td>3.6 A</td>
      <td>C2</td>
      <td>Selenomethionine-derivatized EcoDMT, residues 13-506, outward-facing conformation</td>
      <td>SeMet (for anomalous phasing)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a></td>
      <td>3.6 A</td>
      <td>C2</td>
      <td>EcoDMT E129Q mutant, outward-facing conformation</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a></td>
      <td>3.9 A</td>
      <td>C2</td>
      <td>EcoDMT E129A mutant, outward-facing conformation</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a></td>
      <td>3.7 A</td>
      <td>C2</td>
      <td>EcoDMT H236A mutant, outward-facing conformation</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli MC1061
- **Construct**: EcoDMT with C-terminal 3C protease cleavage site and His10-tag, cloned in pBXC3GH/pBXC3H vectors

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSETQSQTMTRPQ</span><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNW</span><span class="topo-inside">STSI</span></span>
<span class="topo-line"><span class="topo-inside">TGGQNFQYLL</span><span class="topo-membrane">LSIIVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRAR</span><span class="topo-outside">TSRRLGF</span><span class="topo-membrane">IFWILTE</span></span>
<span class="topo-line"><span class="topo-membrane">LAIMATDIAEVIGAAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLL</span><span class="topo-outside">NRIGFRK</span><span class="topo-membrane">IEALVVCLIF</span></span>
<span class="topo-line"><span class="topo-membrane">VILFVFLY</span><span class="topo-inside">QIILSQPA</span><span class="topo-unknown">WHQVAKG</span><span class="topo-inside">LIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLF</span></span>
<span class="topo-line"><span class="topo-membrane">LH</span><span class="topo-outside">SAISQSRKIDRTDSSKVAEAVRFSNW</span><span class="topo-membrane">DSNIQLSLAMVVNALLL</span><span class="topo-inside">IMGVAVFKSGAVQDP</span></span>
<span class="topo-line"><span class="topo-inside">SFFGLYQALSNPDMVSNPVLAEAARSGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFI</span></span>
<span class="topo-line"><span class="topo-outside">HLRLPL</span><span class="topo-membrane">WLRRLVTRLIAIIPVVV</span><span class="topo-inside">CVAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span></span>
<span class="topo-line"><span class="topo-outside">PLLMLTDSAAQMGNQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span></span>
<span class="topo-line"><span class="topo-membrane">SQVISIGIILAMIGLLIW</span><span class="topo-outside">TIIDIRRFT</span><span class="topo-unknown">HPKQKALEVLFQ</span></span>
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
      <td>14</td>
      <td>31</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>38</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>41</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>41</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>56</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>98</td>
      <td>105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>113</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>163</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>188</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>196</td>
      <td>188</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>196</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>203</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>242</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>332</td>
      <td>285</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>366</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>383</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>403</td>
      <td>383</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>444</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>480</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>498</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSETQSQTMTRPQ</span><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNW</span><span class="topo-inside">STSI</span></span>
<span class="topo-line"><span class="topo-inside">TGGQNFQYLL</span><span class="topo-membrane">LSIIVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRAR</span><span class="topo-outside">TSRRLGF</span><span class="topo-membrane">IFWILTE</span></span>
<span class="topo-line"><span class="topo-membrane">LAIMATDIAEVIGAAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLL</span><span class="topo-outside">NRIGFRK</span><span class="topo-membrane">IEALVVCLIF</span></span>
<span class="topo-line"><span class="topo-membrane">VILFVFLY</span><span class="topo-inside">QIILSQPA</span><span class="topo-unknown">WHQVAKG</span><span class="topo-inside">LIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLF</span></span>
<span class="topo-line"><span class="topo-membrane">LH</span><span class="topo-outside">SAISQSRKIDRTDSSKVAEAVRFSNW</span><span class="topo-membrane">DSNIQLSLAMVVNALLL</span><span class="topo-inside">IMGVAVFKSGAVQDP</span></span>
<span class="topo-line"><span class="topo-inside">SFFGLYQALSNPDMVSNPVLAEAARSGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFI</span></span>
<span class="topo-line"><span class="topo-outside">HLRLPL</span><span class="topo-membrane">WLRRLVTRLIAIIPVVV</span><span class="topo-inside">CVAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span></span>
<span class="topo-line"><span class="topo-outside">PLLMLTDSAAQMGNQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span></span>
<span class="topo-line"><span class="topo-membrane">SQVISIGIILAMIGLLIW</span><span class="topo-outside">TIIDIRRFT</span><span class="topo-unknown">HPKQKALEVLFQ</span></span>
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
      <td>14</td>
      <td>31</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>38</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>41</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>41</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>56</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>98</td>
      <td>105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>113</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>163</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>188</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>196</td>
      <td>188</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>196</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>203</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>242</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>332</td>
      <td>285</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>366</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>383</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>403</td>
      <td>383</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>444</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>480</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>498</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSETQSQTMTRPQ</span><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNW</span><span class="topo-inside">STSI</span></span>
<span class="topo-line"><span class="topo-inside">TGGQNFQYLL</span><span class="topo-membrane">LSIIVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRAR</span><span class="topo-outside">TSRRLGF</span><span class="topo-membrane">IFWILTE</span></span>
<span class="topo-line"><span class="topo-membrane">LAIMATDIAEVIGAAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLL</span><span class="topo-outside">NRIGFRK</span><span class="topo-membrane">IEALVVCLIF</span></span>
<span class="topo-line"><span class="topo-membrane">VILFVFLY</span><span class="topo-inside">QIILSQPA</span><span class="topo-unknown">WHQVAKG</span><span class="topo-inside">LIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLF</span></span>
<span class="topo-line"><span class="topo-membrane">LH</span><span class="topo-outside">SAISQSRKIDRTDSSKVAEAVRFSNW</span><span class="topo-membrane">DSNIQLSLAMVVNALLL</span><span class="topo-inside">IMGVAVFKSGAVQDP</span></span>
<span class="topo-line"><span class="topo-inside">SFFGLYQALSNPDMVSNPVLAEAARSGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFI</span></span>
<span class="topo-line"><span class="topo-outside">HLRLPL</span><span class="topo-membrane">WLRRLVTRLIAIIPVVV</span><span class="topo-inside">CVAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span></span>
<span class="topo-line"><span class="topo-outside">PLLMLTDSAAQMGNQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span></span>
<span class="topo-line"><span class="topo-membrane">SQVISIGIILAMIGLLIW</span><span class="topo-outside">TIIDIRRFT</span><span class="topo-unknown">HPKQKALEVLFQ</span></span>
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
      <td>14</td>
      <td>31</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>38</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>41</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>41</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>56</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>98</td>
      <td>105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>113</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>163</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>188</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>196</td>
      <td>188</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>196</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>203</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>242</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>332</td>
      <td>285</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>366</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>383</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>403</td>
      <td>383</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>444</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>480</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>498</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSETQSQTMTRPQ</span><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNW</span><span class="topo-inside">STSI</span></span>
<span class="topo-line"><span class="topo-inside">TGGQNFQYLL</span><span class="topo-membrane">LSIIVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRAR</span><span class="topo-outside">TSRRLGF</span><span class="topo-membrane">IFWILTE</span></span>
<span class="topo-line"><span class="topo-membrane">LAIMATDIAEVIGAAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLL</span><span class="topo-outside">NRIGFRK</span><span class="topo-membrane">IEALVVCLIF</span></span>
<span class="topo-line"><span class="topo-membrane">VILFVFLY</span><span class="topo-inside">QIILSQPA</span><span class="topo-unknown">WHQVAKG</span><span class="topo-inside">LIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLF</span></span>
<span class="topo-line"><span class="topo-membrane">LH</span><span class="topo-outside">SAISQSRKIDRTDSSKVAEAVRFSNW</span><span class="topo-membrane">DSNIQLSLAMVVNALLL</span><span class="topo-inside">IMGVAVFKSGAVQDP</span></span>
<span class="topo-line"><span class="topo-inside">SFFGLYQALSNPDMVSNPVLAEAARSGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFI</span></span>
<span class="topo-line"><span class="topo-outside">HLRLPL</span><span class="topo-membrane">WLRRLVTRLIAIIPVVV</span><span class="topo-inside">CVAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span></span>
<span class="topo-line"><span class="topo-outside">PLLMLTDSAAQMGNQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span></span>
<span class="topo-line"><span class="topo-membrane">SQVISIGIILAMIGLLIW</span><span class="topo-outside">TIIDIRRFT</span><span class="topo-unknown">HPKQKALEVLFQ</span></span>
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
      <td>14</td>
      <td>31</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>38</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>41</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>41</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>56</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>98</td>
      <td>105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>113</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>163</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>188</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>196</td>
      <td>188</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>196</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>203</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>242</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>332</td>
      <td>285</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>366</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>383</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>403</td>
      <td>383</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>444</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>480</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>498</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m87">5M87</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSETQSQTMTRPQ</span><span class="topo-outside">DLSLSDINSTVEVPEGHS</span><span class="topo-unknown">FWKTLLA</span><span class="topo-outside">YSG</span><span class="topo-membrane">PGALVAVGYMDPGNW</span><span class="topo-inside">STSI</span></span>
<span class="topo-line"><span class="topo-inside">TGGQNFQYLL</span><span class="topo-membrane">LSIIVISSLLAMLLQN</span><span class="topo-outside">MAAKLGIVCQLD</span><span class="topo-unknown">LAQAIRAR</span><span class="topo-outside">TSRRLGF</span><span class="topo-membrane">IFWILTE</span></span>
<span class="topo-line"><span class="topo-membrane">LAIMATDIAEVIGAAIAL</span><span class="topo-inside">YLLFKIPIF</span><span class="topo-membrane">LAVVITVLDVFLLLLL</span><span class="topo-outside">NRIGFRK</span><span class="topo-membrane">IEALVVCLIF</span></span>
<span class="topo-line"><span class="topo-membrane">VILFVFLY</span><span class="topo-inside">QIILSQPA</span><span class="topo-unknown">WHQVAKG</span><span class="topo-inside">LIPSWASVQTSPKIGGQTPL</span><span class="topo-membrane">SASLGIIGATIMPHNLF</span></span>
<span class="topo-line"><span class="topo-membrane">LH</span><span class="topo-outside">SAISQSRKIDRTDSSKVAEAVRFSNW</span><span class="topo-membrane">DSNIQLSLAMVVNALLL</span><span class="topo-inside">IMGVAVFKSGAVQDP</span></span>
<span class="topo-line"><span class="topo-inside">SFFGLYQALSNPDMVSNPVLAEAARSGVLSTL</span><span class="topo-membrane">FAVALLASGQNSTITGTITG</span><span class="topo-outside">QVIMEGFI</span></span>
<span class="topo-line"><span class="topo-outside">HLRLPL</span><span class="topo-membrane">WLRRLVTRLIAIIPVVV</span><span class="topo-inside">CVAITSHQGSLDEHQALNNL</span><span class="topo-membrane">MNNSQVFLALALPFSIV</span></span>
<span class="topo-line"><span class="topo-outside">PLLMLTDSAAQMGNQFKNTRWVKV</span><span class="topo-membrane">MGWLTVIILTLLNLISISSQIA</span><span class="topo-inside">GFFGDNPSSQDLLL</span></span>
<span class="topo-line"><span class="topo-membrane">SQVISIGIILAMIGLLIW</span><span class="topo-outside">TIIDIRRFT</span><span class="topo-unknown">HPKQKALEVLFQ</span></span>
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
      <td>14</td>
      <td>31</td>
      <td>13</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>38</td>
      <td>31</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>41</td>
      <td>38</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>56</td>
      <td>41</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>56</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>70</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>98</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>106</td>
      <td>98</td>
      <td>105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>113</td>
      <td>106</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>138</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>147</td>
      <td>138</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>163</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>170</td>
      <td>163</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>188</td>
      <td>170</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>196</td>
      <td>188</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>203</td>
      <td>196</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>204</td>
      <td>223</td>
      <td>203</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>242</td>
      <td>223</td>
      <td>241</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>268</td>
      <td>242</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>285</td>
      <td>268</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>332</td>
      <td>285</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>332</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>366</td>
      <td>352</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>383</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>403</td>
      <td>383</td>
      <td>402</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>403</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>444</td>
      <td>420</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>444</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>480</td>
      <td>466</td>
      <td>479</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>498</td>
      <td>480</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>507</td>
      <td>498</td>
      <td>506</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Competitive inhibitor binding at the metal coordination site

The crystal structure of EcoDMT in complex with Br-BIT (PDB 6TL2) at 3.8 A reveals the inhibitor bound at the base of a funnel-shaped extracellular aqueous pocket leading to the metal ion coordination site. The proximal isothiourea group of Br-BIT is positioned in direct interaction distance with Asp51 of the conserved metal binding site, explaining the competitive inhibition mechanism. The distal isothiourea group is not resolved in the electron density, reflecting its conformational flexibility.

### Outward-facing locked conformation

Br-BIT binding locks EcoDMT in the substrate-free outward-facing conformation. By occupying the metal binding pocket, the inhibitor prevents substrate loading and the subsequent conformational transition to the inward-facing state. The compound is positively charged and poorly membrane permeable, consistent with binding from the extracellular side.

### Species-dependent binding at the distal pocket

Mutagenesis of residues on alpha-helix 11 (Asn456, Ser459, Gln463) in EcoDMT shows only small effects on inhibition (2-fold Ki increase), whereas equivalent mutations in human DMT1 (S476V, N520L, F523A) cause 10-100 fold reductions in potency. This indicates stronger, more specific interactions at the distal side of the binding pocket in the human transporter compared to the prokaryotic homologue, reflecting the poor conservation of residues on alpha-11.

### Structure-activity relationship of bis-isothiourea compounds

Seven bis-isothiourea compounds with varying aromatic scaffolds were characterized. TEBIT and TMBIT are the most potent (IC50 0.27-0.35 uM on hDMT1). The brominated compounds Br-BIT (4.66 uM) and Br-DBFIT (1.24 uM) show intermediate potency. Replacement of isothiourea groups with bulkier thio-2-imidazoline groups severely reduces potency (IC50 161 uM), confirming the critical role of the isothiourea moiety for metal binding site interaction.

### No metal chelation by inhibitors

[ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) confirmed that bis-isothiourea compounds do not chelate divalent metal ions (Mn2+), ruling out indirect inhibition via substrate sequestration. The inhibition arises from direct protein-inhibitor interactions.

### Outward-Facing Conformation of EcoDMT Reveals the SLC11 Transport Cycle

The crystal structure of EcoDMT at 3.3 A resolution (ncomms14033) reveals the first outward-facing conformation of any SLC11/NRAMP family member. The protein comprises 12 transmembrane helices (compared to 11 in ScaDMT), with the additional C-terminal helix 12 located at the periphery. The transporter displays a pseudo-symmetric relationship between two structurally analogous domains (helices 1-5 and 6-10). Comparison with the inward-facing ScaDMT structure defines the conformational changes underlying transition-metal ion transport by the alternate-access mechanism, involving movements of helices 1 and 6 around a hinge at the ion-binding region.

### Proton-Coupled Mn2+ Transport in EcoDMT

EcoDMT mediates proton-coupled uptake of Mn2+ with a KM of 18.2 uM (at pH 7.2). Transport is coupled to H+ cotransport, analogous to human DMT1. The transition-metal ion-binding site at the center of the transporter is composed of residues Asp51, Asn54, Met234, and a backbone carbonyl from helix 6a. Mutants of these binding site residues (D51A, N54A, M234A) severely affect or abolish both Mn2+ and H+ transport, and no uncoupled proton leak was observed, confirming that H+ transport requires conformational changes of the ion-binding site.

### His236 as the Primary Proton Acceptor

A conserved histidine on alpha-helix 6b (His236 in EcoDMT, His267 in human DMT1) was identified as the likely primary proton acceptor. Mutation H236A preserves Mn2+ transport (KM 18.1 uM, Vmax reduced to ~50% of WT) but severely disrupts H+ transport, effectively uncoupling metal ion transport from proton cotransport. In the outward-facing structure, His236 is located near the surface of the aqueous path leading to the transition-metal ion-binding site. In the inward-facing structure (ScaDMT), it is positioned at the crossroad of two potential intracellular proton exit pathways. Glu129 was also investigated as a potential proton acceptor, but the conservative E129Q mutation (retaining H-bonding ability) showed WT-like behavior, ruling out Glu129 as the primary H+ acceptor.

### H+-Coupled Transport Mechanism in the SLC11 Family

The combined structural data from EcoDMT (outward-facing) and ScaDMT (inward-facing) define the alternating-access mechanism for H+-coupled transition-metal ion transport. Two scenarios are proposed for proton coupling: (1) the proton is released via the main metal ion exit path together with Mn2+, or (2) the proton exits via a narrow side tunnel lined by conserved acidic and basic residues (Glu119, Asp126, Glu129 on helix 3; Arg368, Arg369, Arg373 on helix 9 in EcoDMT). The acidic and basic residues lining the narrow aqueous cavity are conserved among SLC11 family members but absent from LeuT and other Na+-coupled transporters, suggesting a specialized proton exit pathway unique to the SLC11 family.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/dra-nramp/">Deinococcus radiodurans Nramp (DraNramp)</a> — Related SLC11/NRAMP family transporter with high-resolution structures of the transport cycle
- <a href="/xray-mp-wiki/proteins/slc-transporters/sca-dmt/">ScaDMT</a> — Related SLC11/NRAMP family transporter from Staphylococcus capitis
- <a href="/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/">SLC11 (NRAMP) Family</a> — EcoDMT is a member of the SLC11/NRAMP family of divalent metal transporters
- <a href="/xray-mp-wiki/concepts/miscellaneous/leut-return-state-mechanism/">LeuT Return State Mechanism</a> — EcoDMT adopts the LeuT fold characteristic of the APC superfamily
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Crystallization method used to grow EcoDMT crystals
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Detergent used for purification and crystallization
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">Leut</a> — Referenced in ecodmt text
- <a href="/xray-mp-wiki/reagents/additives/iron/">Iron</a> — Referenced in ecodmt text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in ecodmt text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in ecodmt text
