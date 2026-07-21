---
title: "Prostaglandin E2 Receptor EP3 (Prostanoid EP3 Receptor)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41589-018-0160-y, doi/10.1038##s41589-018-0171-8]
verified: agent
uniprot_id: P43115
---

# Prostaglandin E2 Receptor EP3 (Prostanoid EP3 Receptor)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P43115">UniProt: P43115</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prostaglandin-e2/) receptor EP3 is a class A G protein-coupled receptor (GPCR) that mediates the physiological actions of [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prostaglandin-e2/) (PGE2), a major bioactive lipid involved in inflammation, pain, fever, and labor. EP3 is the primary target of , a life-saving uterotonic drug used to prevent postpartum hemorrhage. Two independent crystal structures of the human EP3 receptor were determined in the active-like state: the  free-acid (-FA) bound structure at 2.5 A resolution by [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) at an X-ray free electron laser (XFEL), and the endogenous agonist PGE2-bound structure at 2.9 A resolution by synchrotron [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/). Both structures reveal a completely enclosed ligand-binding pocket with a structured water molecule coordinating the ligand's ring structure, providing the first atomic description of prostaglandin recognition by a prostanoid receptor.


## Publications

### doi/10.1038##s41589-018-0160-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m9t">6M9T</a></td>
      <td>2.50</td>
      <td>Not specified</td>
      <td>Human EP3 isoform A (modified), initial Met removed, ICL3 (residues 260-272) replaced with <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (T4L, A73T), C-terminus truncated after Leu353, Gly286(6.39)Ala mutation</td>
      <td>-FA (free acid form of )</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells (Bac-to-Bac system, Invitrogen)
- **Construct**: Human EP3 receptor. Paper 1 (0160-y): N-terminal HA signal peptide + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) + 10xHis tag, ICL3 replaced with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (A73T). Paper 2 (0171-8): Codon-optimized human EP3 isoform I with N-terminal HA signal + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) + 3C site, C-terminal 10xHis tag, mbIIG2 fusion in ICL2/ICL3 with GS-rich linker

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
      <td>Cell culture and infection</td>
      <td>Sf9 cells infected with recombinant baculovirus at 2x10^6 cells/ml</td>
      <td>—</td>
      <td></td>
      <td>Grown in the presence of 1 uM  methyl ester</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Three rounds of washing and ultracentrifugation at 250,000g</td>
      <td>—</td>
      <td>10 mM  pH 7.5, 10 mM , 20 mM KCl, -free protease inhibitor cocktail</td>
      <td>Second wash: 10 mM  pH 7.5, 1 M NaCl, 10 mM , 20 mM KCl</td>
    </tr>
    <tr>
      <td>Alkylation</td>
      <td>Incubation with 2 mg/ml  at room temperature for 1 h, then 30 min at 4C</td>
      <td>—</td>
      <td></td>
      <td>After resuspending membranes in lysis buffer with 20% </td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Stirred for 2 h at 4C</td>
      <td>—</td>
      <td>50 mM  pH 7.5, 800 mM NaCl, 1% , 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td> resin (Clontech), overnight batch binding at 4C</td>
      <td> IMAC resin</td>
      <td>Wash 1: 50 mM  pH 7.2, 150 mM NaCl, 10 mM , 8 mM , 0.1% , 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/), 10% , 20 mM . Wash 2: 50 mM  pH 7.5, 150 mM NaCl, 0.05% , 0.01% <a href="/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/">CHS</a>, 10% , 20 mM </td>
      <td>Eluted with 2.5 CV of elution buffer</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentration for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) crystallization</td>
      <td>—</td>
      <td></td>
      <td>Protein concentrated for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) reconstitution</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified EP3-T4L with -FA</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>. Diffraction data collected at LCLS XFEL using <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> (SFX) at room temperature. Structure determined at 2.5 A resolution.</td>
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
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m9t">6M9T</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">VFADYKDDDDGAPKETRGYGGDAPFCTRLNHSYTGMWAPERSAEARGNLTRPPGSGE</span><span class="topo-outside">DCGSVSVA</span><span class="topo-membrane">FPITMLLTGFVGNALAMLLVS</span><span class="topo-inside">RSYRRRESKRKKSFLL</span><span class="topo-membrane">CIGWLALTDLVGQLLTTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">VVI</span><span class="topo-outside">VVYLSKQRWEHIDPSGRLCT</span><span class="topo-membrane">FFGLTMTVFGLSSLFIASAMAV</span><span class="topo-inside">ERALAIRAPHWYASHMKTRATR</span><span class="topo-membrane">AVLLGVWLAVLAFALLPVL</span><span class="topo-outside">GVGQYTVQWPGTWCFIST</span><span class="topo-unknown">GRGGNGTSSSH</span><span class="topo-outside">NW</span><span class="topo-membrane">GNL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FFASAFAFLGLLALTVTFSCNL</span><span class="topo-inside">ATIKALVSRGSNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDATVRGILRNAKLKPVY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">DSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYGSWGRITTETAI</span><span class="topo-membrane">QLMAIMCVLSVCWSPLLIMMLKMIF</span><span class="topo-outside">N</span><span class="topo-unknown">QTSVEHCKT</span></span>
<span class="topo-ruler">       490       500       510       520       530       </span>
<span class="topo-line"><span class="topo-unknown">HT</span><span class="topo-outside">EKQKECNF</span><span class="topo-membrane">FLIAVRLASLNQILDPWVYLLLRKIL</span><span class="topo-inside">GRPLEVL</span><span class="topo-unknown">FQGPHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>58</td>
      <td>65</td>
      <td>46</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>86</td>
      <td>54</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>75</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>123</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>143</td>
      <td>112</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>132</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>187</td>
      <td>154</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>206</td>
      <td>176</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>224</td>
      <td>195</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>237</td>
      <td>224</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>262</td>
      <td>226</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>445</td>
      <td>251</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>446</td>
      <td>470</td>
      <td>283</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>471</td>
      <td>471</td>
      <td>308</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>490</td>
      <td>320</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>516</td>
      <td>328</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>517</td>
      <td>523</td>
      <td>2000</td>
      <td>2006</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41589-018-0171-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ak3">6AK3</a></td>
      <td>2.90</td>
      <td>P 21</td>
      <td>Human EP3 with mbIIG2 fusion (modified ) in ICL2/ICL3, quadruple thermostabilizing mutations A173I(4.41), V185S(4.53), S258D(5.65), C289L(6.42)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/prostaglandin-e2/">Prostaglandin E2 (PGE2, Dinoprostone)</a> (PGE2)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells (Bac-to-Bac system, Invitrogen)
- **Construct**: Human EP3 receptor. Paper 1 (0160-y): N-terminal HA signal peptide + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) + 10xHis tag, ICL3 replaced with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (A73T). Paper 2 (0171-8): Codon-optimized human EP3 isoform I with N-terminal HA signal + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) + 3C site, C-terminal 10xHis tag, mbIIG2 fusion in ICL2/ICL3 with GS-rich linker

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified EP3-mbIIG2 with PGE2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>. Data collected at SPring-8 synchrotron. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. Space group P21, unit cell a=66.1, b=42.3, c=161.3 A, beta=96.1 deg.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ak3">6AK3</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPTSSGED</span><span class="topo-outside">CGS</span><span class="topo-membrane">VSVAFPITMLLTGFVGNALAML</span><span class="topo-inside">LVSRSYR</span><span class="topo-unknown">RRESKRK</span><span class="topo-inside">KSFLLC</span><span class="topo-membrane">IGWLALTDLVGQLLTTPVVIVVYL</span><span class="topo-outside">SK</span><span class="topo-unknown">Q</span><span class="topo-outside">RWEHIDPSG</span><span class="topo-membrane">RLCTFFGLTMTVFGLSSLFIASAMAV</span><span class="topo-inside">ERALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRAPHWYASHMKTRITR</span><span class="topo-membrane">AVLLGVWLASLAFALLPVLGVGQYT</span><span class="topo-outside">VQWPGTWCFISTG</span><span class="topo-unknown">RGGQGTSSSHNW</span><span class="topo-outside">G</span><span class="topo-membrane">NLFFASAFAFLGLLALTVTFSCNLATI</span><span class="topo-inside">KALVDRCRAKA</span><span class="topo-unknown">TASQSS</span><span class="topo-inside">AQWGRITT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ETA</span><span class="topo-membrane">IQLMGIMLVLSVCWSPLLIMMLKMI</span><span class="topo-outside">F</span><span class="topo-unknown">QQTSVEHCKTHTEKQ</span><span class="topo-outside">KECNF</span><span class="topo-membrane">FLIAVRLASLNQILDPWVYLLL</span><span class="topo-inside">RKILLRAKYG</span><span class="topo-unknown">QLELEVLFQADLEDNWETLNDNLKVIEKADNAAQVKDAL</span></span>
<span class="topo-ruler">       370       380       390       400       410         </span>
<span class="topo-line"><span class="topo-unknown">TKMRAAALDAGSGSGHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTINAYIQKYG</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>9</td>
      <td>11</td>
      <td>47</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>33</td>
      <td>50</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>40</td>
      <td>72</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>86</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>77</td>
      <td>92</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>79</td>
      <td>116</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>119</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>115</td>
      <td>128</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>154</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>162</td>
      <td>176</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>175</td>
      <td>201</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>188</td>
      <td>226</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>215</td>
      <td>227</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>254</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>243</td>
      <td>271</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>268</td>
      <td>282</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>269</td>
      <td>307</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>323</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>328</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>321</td>
      <td>350</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ak3">6AK3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPTSSGED</span><span class="topo-outside">CGS</span><span class="topo-membrane">VSVAFPITMLLTGFVGNALAML</span><span class="topo-inside">LVSRS</span><span class="topo-unknown">Y</span><span class="topo-inside">R</span><span class="topo-unknown">RRESKRK</span><span class="topo-inside">KSFLLC</span><span class="topo-membrane">IGWLALTDLVGQLLTTPVVIVVYL</span><span class="topo-outside">SK</span><span class="topo-unknown">Q</span><span class="topo-outside">RWEHIDP</span><span class="topo-unknown">S</span><span class="topo-outside">G</span><span class="topo-membrane">RLCTFFGLTMTVFGLSSLFIASAMAV</span><span class="topo-inside">ERALA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRAPHWYASHMKTRITR</span><span class="topo-membrane">AVLLGVWLASLAFALLPVLGVGQYT</span><span class="topo-outside">VQWPGTWCFISTG</span><span class="topo-unknown">RGGQGTSSSHNW</span><span class="topo-outside">G</span><span class="topo-membrane">NLFFASAFAFLGLLALTVTFSCNLATI</span><span class="topo-inside">KALVDRCRAKA</span><span class="topo-unknown">TASQSS</span><span class="topo-inside">AQWGRITT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ETA</span><span class="topo-membrane">IQLMGIMLVLSVCWSPLLIMMLKMI</span><span class="topo-outside">F</span><span class="topo-unknown">QQTSVEHCKTHTEKQ</span><span class="topo-outside">KECNF</span><span class="topo-membrane">FLIAVRLASLNQILDPWVYLLL</span><span class="topo-inside">RKILLR</span><span class="topo-unknown">KFCQLELEVLFQADLEDNWETLNDNLKVIEKADNAAQVKDALT</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-unknown">KMRAAALDAGSGSGHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTIN</span><span class="topo-inside">ADL</span><span class="topo-unknown">Q</span><span class="topo-inside">KYG</span></span>
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
      <td>9</td>
      <td>11</td>
      <td>47</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>33</td>
      <td>50</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>38</td>
      <td>72</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>40</td>
      <td>78</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>86</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>77</td>
      <td>92</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>79</td>
      <td>116</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>119</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>89</td>
      <td>127</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>115</td>
      <td>128</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>137</td>
      <td>154</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>162</td>
      <td>176</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>175</td>
      <td>201</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>188</td>
      <td>226</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>215</td>
      <td>227</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>226</td>
      <td>254</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>243</td>
      <td>271</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>268</td>
      <td>282</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>269</td>
      <td>307</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>323</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>328</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>317</td>
      <td>350</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>414</td>
      <td>1001</td>
      <td>1003</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>418</td>
      <td>1104</td>
      <td>1106</td>
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

### First atomic structures of a prostanoid receptor

The EP3--FA (2.5 A) and EP3-PGE2 (2.9 A) structures represent the first crystal structures of a prostanoid receptor bound to prostaglandin ligands, providing the first atomic description of prostaglandin recognition and signaling through a GPCR. The structures reveal how the prostaglandin scaffold interacts with the receptor and explain the molecular basis for ligand selectivity among EP receptor subtypes.

### Completely enclosed ligand-binding pocket

Both structures reveal a completely enclosed binding pocket for the prostaglandin ligand. ECL2 forms a lid that occludes access to the orthosteric site, making the binding pocket totally enclosed. This closed conformation likely contributes to the long residence time of  on EP3 and may represent an induced-fit mechanism upon ligand binding. The enclosed pocket contrasts with many other GPCRs that have solvent-exposed binding sites.

### Structured water molecule in the binding pocket

A structured water molecule is observed coordinating the E-ring of -FA (and PGE2) in the binding pocket, forming hydrogen bonds with the ligand hydroxyl groups and receptor side chains. This water molecule, resolved at 2.5 A resolution, plays a key role in stabilizing the ligand-receptor interaction. The ability to detect this water was enabled by the high resolution of the XFEL structure.

### Key binding pocket residues for ligand recognition

The prostaglandin binding pocket is formed by residues from TM1 (P55, M58), TM2 (Q103, T106, T107, V110, Y114), TM3 (M137, G141), ECL2 (T206, W207, F209), TM5 (F234), TM6 (W295, L298), and TM7 (L329, V332, R333, S336, Q339). Arg333(7.40) forms a critical salt bridge with the ligand carboxylate and is conserved among all prostaglandin receptors. Gly141(3.36) at the bottom of the pocket interacts with the omega-chain of the ligand, and mutation to larger residues reduces signaling potency by three orders of magnitude.

### ECL2 as a determinant of ligand selectivity

ECL2 in EP3 adopts a unique conformation that forms the lid of the binding pocket. Comparison with EP4 and rhodopsin ECL2 conformations reveals structural differences that contribute to ligand selectivity among EP receptor subtypes. The ECL2 residues T206, W207, and F209 are directly involved in ligand coordination.

### Active-like receptor conformation

Both structures exhibit active-like conformational features including displacement of TM6 relative to inactive-state GPCRs. The canonical toggle switch W295(6.48) is in an active conformation. Comparison with Gi/o-coupled active GPCRs (, mu-opioid receptor, A1 adenosine receptor, 5-HT1B) shows TM6 displacement of 2.1-7.6 A depending on the reference structure.

### Structural basis for EP3-selective agonists

The structures explain how prostaglandin derivatives achieve EP3 selectivity. Branched carbon 16 substitutions (-FA, TEI-3356) contact Gly141(3.36) constraining the omega-chain. Bulky groups at the omega-chain extremity (MB-28767, sulprostone, -63799) form additional hydrophobic interactions. EP1 and EP2 have larger residues at position 6.51 (Met, Phe) that would clash with constrained omega-chains, conferring selectivity toward EP3 and EP4.

### Thermostabilization of EP3 for crystallography

The Morimoto et al. structure used a quadruple mutant (A173I, V185S, S258D, C289L) identified through fluorescence-detection [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (FSEC) thermostability screening. V185S forms a hydrogen bond with S143(3.38), contributing to . These mutations did not significantly affect PGE2 binding affinity or signaling activity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — EP3 structures represent active-like state of a prostanoid receptor
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Primary detergent for EP3 solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Lipid additive for EP3 stabilization during purification
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — T4L fusion in ICL3 used in the EP3-misoprostol structure (Audet et al.)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — LCP method used for both EP3 crystal structures
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography (SFX)</a> — XFEL data collection used for the 2.5 A EP3-misoprostol structure
- <a href="/xray-mp-wiki/reagents/ligands/misoprostol/">Misoprostol</a> — Referenced in ep3-receptor text
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> — Referenced in ep3-receptor text
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Referenced in ep3-receptor text
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a> — Referenced in ep3-receptor text
