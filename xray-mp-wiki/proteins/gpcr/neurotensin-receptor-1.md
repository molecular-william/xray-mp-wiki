---
title: "Rat Neurotensin Receptor 1 (NTSR1)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11558, doi/10.1073##PNAS.1317903111, doi/10.1126##sciadv.abe5504]
verified: agent
uniprot_id: P20789
---

# Rat Neurotensin Receptor 1 (NTSR1)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span> <span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P20789">UniProt: P20789</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

The rat [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 (NTSR1) is a class A G protein-coupled receptor (GPCR) belonging to the ghrelin receptor family that binds the tridecapeptide [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) (NTS). NTSR1 is involved in various physiological processes including neurotransmission, pain modulation, and regulation of body temperature. The thermostabilized NTSR1-GW5 construct with T4 lysozyme fusion enabled the first crystal structure of a [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor in complex with NTS(8-13). Subsequently, directed evolution in E. coli yielded signaling-competent NTR1 variants crystallized without fusion proteins. A new crystallization design using a [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 fusion chaperone enabled determination of five new structures: apo-state NTSR1 as well as complexes with nonpeptide inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A, partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/), and the novel full agonist [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/), providing structural rationales for how ligands modulate NTSR1 activation and inactivation.


## Publications

### doi/10.1038##nature11558

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4grv">4GRV</a></td>
      <td>2.80</td>
      <td>—</td>
      <td>NTSR1-GW5-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (GW5 thermostabilizing mutations, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> replacing ICL3)</td>
      <td>NTS(8-13)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (for NTR1 variants) and Sf9 insect cells (for NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)); NTSR1-H4x expressed in E. coli

- **Construct**: NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) for initial structure; TM86V-deltaIC3A/B for evolved structures; NTSR1-H4x (NTSR1-H4 mutant fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone via shared helix) for small-molecule ligand complexes

- **Notes**: NTSR1-H4 is a previously developed highly stable rNTSR1 mutant used for pharmacological studies


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>NTSR1-GW5-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>. Space group P21 with cell dimensions a=46.96, b=69.62, c=97.53, alpha=90, beta=101.7, gamma=90 deg. Data collected at Diamond Light Source beamline I24.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4grv">4GRV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDATSTSESDTAGP</span><span class="topo-outside">NSDLDVNTDIY</span><span class="topo-membrane">SKVLVTAIYLALFVVGTVGNSVTLF</span><span class="topo-inside">TLARK</span><span class="topo-unknown">KSLQ</span><span class="topo-inside">SLQSTVHYHL</span><span class="topo-membrane">GSLALSDLLILLLAMPVELYNFIW</span><span class="topo-outside">VHHPW</span><span class="topo-membrane">AFGDAGCRGYYFLRDAC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TYATALNVASLS</span><span class="topo-inside">VARYLAICHPFKAKTLMSRSRTKKFI</span><span class="topo-membrane">SAIWLASALLAIPMLFTMGL</span><span class="topo-outside">QNRSADGTHPGGLVC</span><span class="topo-membrane">TPIVDTATVKVVIQVNTFMSFLFPMLVISILNT</span><span class="topo-inside">VIANKLTVMVNIFE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">MLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDK</span><span class="topo-unknown">AIG</span><span class="topo-inside">RNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLNNKR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYGSGSVQALRHGVL</span><span class="topo-membrane">VARAVVIAFVVCWLPYHVRRLMFCYIS</span><span class="topo-outside">DEQWTTFLFDF</span><span class="topo-membrane">YHYFYMLTNALAYASSAINPILYN</span><span class="topo-inside">LVSANFRQV</span></span>
<span class="topo-ruler">       490       500       510</span>
<span class="topo-line"><span class="topo-unknown">FLSTLACLCPGWRHRRKAHHHHHHHHHHGG</span></span>
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
      <td>19</td>
      <td>33</td>
      <td>51</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>20</td>
      <td>30</td>
      <td>52</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>55</td>
      <td>63</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>60</td>
      <td>88</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>93</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>65</td>
      <td>74</td>
      <td>97</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>98</td>
      <td>107</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>103</td>
      <td>131</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>132</td>
      <td>136</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>158</td>
      <td>165</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>191</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>193</td>
      <td>211</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>226</td>
      <td>226</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>236</td>
      <td>259</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>283</td>
      <td>1002</td>
      <td>1048</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>286</td>
      <td>1049</td>
      <td>1051</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>287</td>
      <td>400</td>
      <td>1052</td>
      <td>1165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>409</td>
      <td>300</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>436</td>
      <td>309</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>447</td>
      <td>336</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>471</td>
      <td>347</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>480</td>
      <td>371</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>481</td>
      <td>510</td>
      <td>380</td>
      <td>409</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##PNAS.1317903111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4buo">4BUO</a></td>
      <td>3.26</td>
      <td>—</td>
      <td>NTR1-TM86V-deltaIC3A (TM86V mutations, deltaIC3A deletion)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/neurotensin/">Neurotensin</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4buo">4BUO</a></td>
      <td>2.75</td>
      <td>—</td>
      <td>NTR1-TM86V-deltaIC3B</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/neurotensin/">Neurotensin</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (for NTR1 variants) and Sf9 insect cells (for NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)); NTSR1-H4x expressed in E. coli

- **Construct**: NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) for initial structure; TM86V-deltaIC3A/B for evolved structures; NTSR1-H4x (NTSR1-H4 mutant fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone via shared helix) for small-molecule ligand complexes

- **Notes**: NTSR1-H4 is a previously developed highly stable rNTSR1 mutant used for pharmacological studies


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4buo">4BUO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">PGSGP</span><span class="topo-inside">NSDLDVNTDI</span><span class="topo-membrane">YSKVLVTAIYLALFVVGTVGNS</span><span class="topo-outside">VTLFTLARKK</span><span class="topo-unknown">SLQ</span><span class="topo-outside">SLQSTVDYYLGSL</span><span class="topo-membrane">ALSDLLILLLAMPVELYNFIWVH</span><span class="topo-inside">HPW</span><span class="topo-membrane">AFGDAGCRGYYFLRDACTYATAL</span><span class="topo-outside">NVVSLSVE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LYLAICHPFKAKTLMSRSRTKKFISAI</span><span class="topo-membrane">WLASALLAIPMLFTMGL</span><span class="topo-inside">QNLSGDGTHPGGLVC</span><span class="topo-membrane">TPIVDTATLKVVIQVNTFMSFLFPML</span><span class="topo-outside">VASILNTVIANKLTVMVHQ</span><span class="topo-unknown">AAFNMTIE</span><span class="topo-outside">PGRVQALR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">RGVLVLRAVV</span><span class="topo-membrane">IAFVVCWLPYHVRRLMFCYI</span><span class="topo-inside">SDEQWTTFLFD</span><span class="topo-membrane">FYHYFYMLTNALVYVSAAINPI</span><span class="topo-outside">LYNLVSANFRQVFLSTL</span><span class="topo-unknown">ACLCPGTRELEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>47</td>
      <td>51</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>15</td>
      <td>52</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>37</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>47</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>50</td>
      <td>94</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>63</td>
      <td>97</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>86</td>
      <td>110</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>89</td>
      <td>133</td>
      <td>135</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>112</td>
      <td>136</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>147</td>
      <td>159</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>194</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>179</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>205</td>
      <td>226</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>224</td>
      <td>252</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>232</td>
      <td>271</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>297</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>270</td>
      <td>315</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>281</td>
      <td>335</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>303</td>
      <td>346</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>320</td>
      <td>368</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>335</td>
      <td>385</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4buo">4BUO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">PGSGP</span><span class="topo-inside">NSDLDVNTDI</span><span class="topo-membrane">YSKVLVTAIYLALFVVGTVGNS</span><span class="topo-outside">VTLFTLARKK</span><span class="topo-unknown">SLQ</span><span class="topo-outside">SLQSTVDYYLGSL</span><span class="topo-membrane">ALSDLLILLLAMPVELYNFIWVH</span><span class="topo-inside">HPW</span><span class="topo-membrane">AFGDAGCRGYYFLRDACTYATAL</span><span class="topo-outside">NVVSLSVE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LYLAICHPFKAKTLMSRSRTKKFISAI</span><span class="topo-membrane">WLASALLAIPMLFTMGL</span><span class="topo-inside">QNLSGDGTHPGGLVC</span><span class="topo-membrane">TPIVDTATLKVVIQVNTFMSFLFPML</span><span class="topo-outside">VASILNTVIANKLTVMVHQ</span><span class="topo-unknown">AAFNMTIE</span><span class="topo-outside">PGRVQALR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">RGVLVLRAVV</span><span class="topo-membrane">IAFVVCWLPYHVRRLMFCYI</span><span class="topo-inside">SDEQWTTFLFD</span><span class="topo-membrane">FYHYFYMLTNALVYVSAAINPI</span><span class="topo-outside">LYNLVSANFRQVFLSTL</span><span class="topo-unknown">ACLCPGTRELEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>47</td>
      <td>51</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>15</td>
      <td>52</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>37</td>
      <td>62</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>47</td>
      <td>84</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>50</td>
      <td>94</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>63</td>
      <td>97</td>
      <td>109</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>86</td>
      <td>110</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>89</td>
      <td>133</td>
      <td>135</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>112</td>
      <td>136</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>147</td>
      <td>159</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>194</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>179</td>
      <td>211</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>205</td>
      <td>226</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>224</td>
      <td>252</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>232</td>
      <td>271</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>297</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>270</td>
      <td>315</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>281</td>
      <td>335</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>303</td>
      <td>346</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>320</td>
      <td>368</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>335</td>
      <td>385</td>
      <td>399</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.abe5504

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yvr">6YVR</a></td>
      <td>2.5-3.2</td>
      <td>—</td>
      <td>NTSR1-H4x (stabilized NTSR1-H4 mutant fused to <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">DARPIN</a> D12 via shared helix)</td>
      <td>Multiple (NTS8-13, <a href="/xray-mp-wiki/reagents/ligands/sri-9829/">SRI-9829 (Full NTSR1 Agonist)</a>, <a href="/xray-mp-wiki/reagents/ligands/rti-3a/">RTI-3a (Partial NTSR1 Agonist)</a>, <a href="/xray-mp-wiki/reagents/ligands/sr48692/">SR48692</a>, SR142948A, apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (for NTR1 variants) and Sf9 insect cells (for NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)); NTSR1-H4x expressed in E. coli

- **Construct**: NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) for initial structure; TM86V-deltaIC3A/B for evolved structures; NTSR1-H4x (NTSR1-H4 mutant fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone via shared helix) for small-molecule ligand complexes

- **Notes**: NTSR1-H4 is a previously developed highly stable rNTSR1 mutant used for pharmacological studies


**Purification:**

- **Expression system**: E. coli
- **Expression construct**: NTSR1-H4x (NTSR1-H4 fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12)
- **Tag info**: MBP-TrxA-His8 tag cleaved by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/); octahistidine tag on [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/)

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
      <td>Cell culture and harvest</td>
      <td>Fermentation</td>
      <td>—</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 400 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
      <td>Cells harvested at 5000g for 20 min at 4C, ~7g pellet per L culture</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/reagents/additives/lysozyme/">Lysozyme</a> treatment and sonication</td>
      <td>—</td>
      <td>Resuspension Buffer (100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 400 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>) with 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/lysozyme/">lysozyme</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 0.05 mg/ml DNase I</td>
      <td>Incubated 1 hour while stirring</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside) + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Incubated 1 hour while stirring, followed by 30 min sonication</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Superflow (GE Healthcare)</td>
      <td>Wash Buffer I: 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 600 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 2 mM 2-ME, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; Wash Buffer II: 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 8.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM 2-ME, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Batch incubation overnight; elution with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in Elution Buffer (25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM 2-ME)</td>
    </tr>
    <tr>
      <td>Desalting and tag cleavage</td>
      <td>Size exclusion desalting + protease cleavage</td>
      <td>PD MiniTrap G-25 columns (GE Healthcare)</td>
      <td>G-25 Buffer (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>)</td>
      <td>Protein incubated 3 hours with <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> to cleave MBP and TrxA tags</td>
    </tr>
    <tr>
      <td>Cation exchange chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>SP Sepharose (GE Healthcare)</td>
      <td>G-25 Buffer</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> (<a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/))</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL (GE Healthcare)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> Buffer (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) and vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>NTSR1-H4x crystallized in complex with NTS8-13, <a href="/xray-mp-wiki/reagents/ligands/sri-9829/">SRI-9829 (Full NTSR1 Agonist)</a>, <a href="/xray-mp-wiki/reagents/ligands/rti-3a/">RTI-3a (Partial NTSR1 Agonist)</a>, <a href="/xray-mp-wiki/reagents/ligands/sr48692/">SR48692</a>, SR142948A, and in apo state. <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> crystallization for most complexes; vapor diffusion used for NTSR1-H4x:NTS8-13. For <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>: <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>, 10 mg/ml protein, 50-250 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 0.1 M <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 28-30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 2% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>, 0.04-0.5% NG (<a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a>). For NTSR1-H4bmx: 100 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.4, 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.3% NG, 15% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Vapor diffusion: 100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 27% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>, 0.069-0.15% NG, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Crystals grown at 20C. Cryoprotected with 50 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.4, 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.3% NG, 15% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Data collected at Swiss Light Source beamline X06SA, wavelength 1 A, 100K.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Agonist-induced and inverse agonist-induced conformational changes in NTSR1

Five new NTSR1 structures with small-molecule ligands revealed distinct conformational states. Full agonists NTS8-13 and [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/) induce contraction of the extracellular binding pocket, while inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A favor expansion of the extracellular opening of helices VI and VII, causing constriction at the intracellular portion. The partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/) induces an intermediate contraction. This demonstrates that ligand efficacy correlates with the ability to mimic the binding mode of the endogenous agonist [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/).

### Role of L-Leu and adamantyl moieties in agonism vs inverse agonism

The bulky adamantyl moiety of inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A exerts a steric effect that widens the hydrophobic subpocket at F331(6.58), hindering contraction of the extracellular receptor portion. In contrast, the isobutyl side chain of L-Leu (present in agonists) is optimally shaped to induce and stabilize a contracted arrangement of TM6 at its extracellular tip. Replacing the adamantyl moiety of [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) with an L-Leu side chain converts this inverse agonist into the partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/).

### ECL3 and TM7 interactions crucial for NTSR1 activation

All agonists form contacts with ECL3, TM6, and TM7 on one wall of the binding site, and with the ECL2 beta-hairpin and TM2 on the opposite wall. This anchoring pattern is important for inducing contraction of the extracellular receptor portion. NTS8-13 interacts with W339(ECL3), F344(7.28), Y347(7.31), and H348(7.32) in TM7. Mutagenesis of these residues causes moderate drops in agonist affinity but substantially stronger reductions in Gq potency (100-1000 fold), suggesting they stabilize contracted binding site conformation.

### Polar network and hydrophobic core in activation transmission

A network of polar interactions beneath the agonist binding site links the extracellular conformational changes to the intracellular G protein interface. Key residues include D150(3.33), R328(6.55), N355(7.39), and Y351(7.35) in the polar network, and F358(7.42), Y324(6.51), W321(6.48), and F317(6.44) in the hydrophobic cascade. D150(3.33)A, R328(6.55)M, and N355(7.39)A mutations markedly reduce agonist potency without strongly affecting affinity, confirming their role in activation signal transmission.


## Cross-References

- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — T4L fusion replacing ICL3 in NTSR1-GW5-T4L construct
- <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">Designed Ankyrin Repeat Protein (DARPin)</a> — DARPin D12 fusion chaperone used for NTSR1-H4x crystallization
- <a href="/xray-mp-wiki/proteins/gpcr/tm86v-delta-ic3a/">NTSR1 TM86V-deltaIC3A Mutant</a> — Evolved NTR1 variant crystallized without fusion proteins
- <a href="/xray-mp-wiki/reagents/detergents/decyl-maltoside/">Decyl Maltoside (DM)</a> — Detergent used for NTSR1 solubilization and thermostability measurement
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for NTSR1 solubilization
- <a href="/xray-mp-wiki/reagents/ligands/sr48692/">SR48692</a> — Non-peptide inverse agonist co-crystallized with NTSR1-H4x
- <a href="/xray-mp-wiki/reagents/ligands/neurotensin/">Neurotensin</a> — Endogenous peptide agonist used for comparison with small-molecule ligands
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine (Buffer)</a> — Used in cryoprotection solution for NTSR1-H4bmx crystals
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
