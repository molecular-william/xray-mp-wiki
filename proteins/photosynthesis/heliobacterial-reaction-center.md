---
title: "Heliobacterial Reaction Center (HbRC)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan5611]
verified: false
---

# Heliobacterial Reaction Center (HbRC)

## Overview

The heliobacterial reaction center (HbRC) from Heliobacterium modesticaldum is
a homodimeric Type I photosynthetic reaction center that converts light energy
into chemical energy. It is the first homodimeric reaction center structure to
be determined, at 2.2 Å resolution (PDB 5V8K). The HbRC consists of a PshA
homodimer (core) plus two PshX small subunits, binding 54 [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) g
(BChl g), 4 BChl g', two 8'-hydroxychlorophyll a_F, two carotenoids
(4,4'-diaponeurosporene), two lipids, and one [4Fe-4S] cluster. The complex
exhibits perfect C2 symmetry and lacks a bound quinone in the electron transfer
chain — a unique characteristic among all known reaction centers. The HbRC is
the simplest known reaction center and is considered the closest homolog to the
common ancestor of all photosynthetic reaction centers.


## Publications

### doi/10.1126##science.aan5611

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v8k">5V8K</a></td>
      <td>2.2</td>
      <td>—</td>
      <td>HbRC purified from Heliobacterium modesticaldum — homodimeric PshA core + two PshX small subunits</td>
      <td>BChl g (54), BChl g' (4), 8'-OH Chl a_F (2), 4,4'-diaponeurosporene (2), [4Fe-4S] cluster (1)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Heliobacterium modesticaldum (native expression)
- **Construct**: Native HbRC complex — PshA homodimer + PshX small subunits, no affinity tags
- **Notes**: H. modesticaldum is a thermophilic anaerobic phototroph isolated from volcanic soil in Iceland.

**Purification:**

- **Expression system**: Heliobacterium modesticaldum (native)
- **Expression construct**: Native HbRC complex — PshA + PshX subunits

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
      <td>Anaerobic phototrophic growth</td>
      <td>—</td>
      <td></td>
      <td>H. modesticaldum grown under anaerobic conditions in light</td>
    </tr>
    <tr>
      <td>Membrane isolation and HbRC purification</td>
      <td>As described in ref 22 (Sarrou et al., 2012)</td>
      <td>—</td>
      <td></td>
      <td>Purification details in Photosynth. Res. 111, 291-302 (2012). HbRC purified in the absence of <a href="/xray-mp-wiki/reagents/ligands/menaquinone/">Menaquinone</a>.</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified HbRC complex, no bound [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown and diffracted to 2.2 Å resolution. Data collected at Berkeley Center for Structural Biology, Advanced Light Source, and Structural Biology Center at the Advanced Photon Source.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v8k">5V8K</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">NPRAQVFEYFKLKVPATRGAVLK</span><span class="topo-membrane">AHINHLGNVAAMVSF</span><span class="topo-outside">ILVHHLSWDPATQGVLWAP</span><span class="topo-unknown">ATM</span></span>
<span class="topo-line"><span class="topo-unknown">FYARLYQ</span><span class="topo-outside">LGLDAVALSPDALFVARM</span><span class="topo-membrane">HLLAAIILWGFGH</span><span class="topo-inside">VKS</span><span class="topo-unknown">PAEEKFL</span><span class="topo-inside">EKVTMGKA</span><span class="topo-membrane">LVAQ</span></span>
<span class="topo-line"><span class="topo-membrane">FHFFALIATL</span><span class="topo-outside">WGLHMAFYGILGPSGKLEPTGLSFDMFGPITPATMAGNHVA</span><span class="topo-membrane">FGAVFFLGG</span></span>
<span class="topo-line"><span class="topo-membrane">IFHY</span><span class="topo-inside">FAGFNTKRFAFFEKDWEAVL</span><span class="topo-membrane">SVSCQILAFHFATV</span><span class="topo-outside">VFAMIIWQHPQLGFGFMREYAV</span></span>
<span class="topo-line"><span class="topo-outside">SQYAGPELKMIAQSNPGLLVKQAILG</span><span class="topo-membrane">HLVMGIMFWIGGV</span><span class="topo-inside">FHGAHFMLRVLNDPKLAEEMK</span></span>
<span class="topo-line"><span class="topo-inside">DFKFIKRCYDHEFQKKFLA</span><span class="topo-membrane">LIMFGAFLPIFVSYG</span><span class="topo-outside">IATHNTIADIHAASKTGLFAHMTYIN</span></span>
<span class="topo-line"><span class="topo-outside">IGT</span><span class="topo-unknown">PLHDAIF</span><span class="topo-outside">GSKGSISEFVAAH</span><span class="topo-membrane">AIAGGLHFTMVPMW</span><span class="topo-inside">RMVFFSKVSPWTTKVGMKAKRDG</span></span>
<span class="topo-line"><span class="topo-inside">EFPCLGPAYGGTCSISLVDQF</span><span class="topo-membrane">YLAIFFSLQVIA</span><span class="topo-outside">PAWFYIDGCWMGSFVAVAAPYNDIYQA</span></span>
<span class="topo-line"><span class="topo-outside">ALATFNSHNPLHQLSPLTNMGYFSYIIQQTTAMFSRYDGHMIQALLG</span><span class="topo-membrane">AHFIWAFTFSMLF</span></span>
<span class="topo-line"><span class="topo-inside">QY</span><span class="topo-unknown">RGSRDEGAMVLKWAHQQV</span><span class="topo-inside">GV</span><span class="topo-unknown">GFAGKMY</span><span class="topo-inside">NRALSLKEG</span><span class="topo-membrane">KAIGCFLFFKMTIV</span><span class="topo-outside">CMWALAMV</span></span>
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
      <td>23</td>
      <td>9</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>32</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>47</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>67</td>
      <td>66</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>85</td>
      <td>76</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>94</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>101</td>
      <td>107</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>108</td>
      <td>110</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>116</td>
      <td>117</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>130</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>171</td>
      <td>139</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>184</td>
      <td>180</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>204</td>
      <td>193</td>
      <td>212</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>218</td>
      <td>213</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>266</td>
      <td>227</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>279</td>
      <td>275</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>319</td>
      <td>288</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>334</td>
      <td>328</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>335</td>
      <td>363</td>
      <td>343</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>370</td>
      <td>372</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>383</td>
      <td>379</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>392</td>
      <td>405</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>441</td>
      <td>406</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>453</td>
      <td>450</td>
      <td>461</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>527</td>
      <td>462</td>
      <td>535</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>528</td>
      <td>540</td>
      <td>536</td>
      <td>548</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>541</td>
      <td>542</td>
      <td>549</td>
      <td>550</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>560</td>
      <td>551</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>561</td>
      <td>562</td>
      <td>569</td>
      <td>570</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>563</td>
      <td>569</td>
      <td>571</td>
      <td>577</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>570</td>
      <td>578</td>
      <td>578</td>
      <td>586</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>579</td>
      <td>592</td>
      <td>587</td>
      <td>600</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>593</td>
      <td>600</td>
      <td>601</td>
      <td>608</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v8k">5V8K</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">YSPTFNVAH</span><span class="topo-membrane">ILAFFFLFLHIPFY</span><span class="topo-inside">FV</span></span>
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
      <td>9</td>
      <td>13</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>23</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>25</td>
      <td>36</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v8k">5V8K</a> — Chain C (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">NPRAQVFEYFKLKVPATRGAVLK</span><span class="topo-membrane">AHINHLGNVAAMVSF</span><span class="topo-outside">ILVHHLSWDPATQGVLWAP</span><span class="topo-unknown">ATM</span></span>
<span class="topo-line"><span class="topo-unknown">FYARLYQ</span><span class="topo-outside">LGLDAVALSPDALFVARM</span><span class="topo-membrane">HLLAAIILWGFGH</span><span class="topo-inside">VKS</span><span class="topo-unknown">PAEEKFL</span><span class="topo-inside">EKVTMGKA</span><span class="topo-membrane">LVAQ</span></span>
<span class="topo-line"><span class="topo-membrane">FHFFALIATL</span><span class="topo-outside">WGLHMAFYGILGPSGKLEPTGLSFDMFGPITPATMAGNHVA</span><span class="topo-membrane">FGAVFFLGG</span></span>
<span class="topo-line"><span class="topo-membrane">IFHY</span><span class="topo-inside">FAGFNTKRFAFFEKDWEAVL</span><span class="topo-membrane">SVSCQILAFHFATV</span><span class="topo-outside">VFAMIIWQHPQLGFGFMREYAV</span></span>
<span class="topo-line"><span class="topo-outside">SQYAGPELKMIAQSNPGLLVKQAILG</span><span class="topo-membrane">HLVMGIMFWIGGV</span><span class="topo-inside">FHGAHFMLRVLNDPKLAEEMK</span></span>
<span class="topo-line"><span class="topo-inside">DFKFIKRCYDHEFQKKFLA</span><span class="topo-membrane">LIMFGAFLPIFVSYG</span><span class="topo-outside">IATHNTIADIHAASKTGLFAHMTYIN</span></span>
<span class="topo-line"><span class="topo-outside">IGT</span><span class="topo-unknown">PLHDAIF</span><span class="topo-outside">GSKGSISEFVAAH</span><span class="topo-membrane">AIAGGLHFTMVPMW</span><span class="topo-inside">RMVFFSKVSPWTTKVGMKAKRDG</span></span>
<span class="topo-line"><span class="topo-inside">EFPCLGPAYGGTCSISLVDQF</span><span class="topo-membrane">YLAIFFSLQVIA</span><span class="topo-outside">PAWFYIDGCWMGSFVAVAAPYNDIYQA</span></span>
<span class="topo-line"><span class="topo-outside">ALATFNSHNPLHQLSPLTNMGYFSYIIQQTTAMFSRYDGHMIQALLG</span><span class="topo-membrane">AHFIWAFTFSMLF</span></span>
<span class="topo-line"><span class="topo-inside">QY</span><span class="topo-unknown">RGSRDEGAMVLKWAHQQV</span><span class="topo-inside">GV</span><span class="topo-unknown">GFAGKMY</span><span class="topo-inside">NRALSLKEG</span><span class="topo-membrane">KAIGCFLFFKMTIV</span><span class="topo-outside">CMWALAMV</span></span>
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
      <td>23</td>
      <td>9</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>32</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>47</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>67</td>
      <td>66</td>
      <td>75</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>85</td>
      <td>76</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>94</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>101</td>
      <td>107</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>108</td>
      <td>110</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>116</td>
      <td>117</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>130</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>171</td>
      <td>139</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>184</td>
      <td>180</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>204</td>
      <td>193</td>
      <td>212</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>218</td>
      <td>213</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>266</td>
      <td>227</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>279</td>
      <td>275</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>319</td>
      <td>288</td>
      <td>327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>334</td>
      <td>328</td>
      <td>342</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>335</td>
      <td>363</td>
      <td>343</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>370</td>
      <td>372</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>383</td>
      <td>379</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>392</td>
      <td>405</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>441</td>
      <td>406</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>453</td>
      <td>450</td>
      <td>461</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>527</td>
      <td>462</td>
      <td>535</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>528</td>
      <td>540</td>
      <td>536</td>
      <td>548</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>541</td>
      <td>542</td>
      <td>549</td>
      <td>550</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>560</td>
      <td>551</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>561</td>
      <td>562</td>
      <td>569</td>
      <td>570</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>563</td>
      <td>569</td>
      <td>571</td>
      <td>577</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>570</td>
      <td>578</td>
      <td>578</td>
      <td>586</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>579</td>
      <td>592</td>
      <td>587</td>
      <td>600</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>593</td>
      <td>600</td>
      <td>601</td>
      <td>608</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v8k">5V8K</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">YSPTFNVAH</span><span class="topo-membrane">ILAFFFLFLHIPFY</span><span class="topo-inside">FV</span></span>
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
      <td>9</td>
      <td>13</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>23</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>25</td>
      <td>36</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First homodimeric reaction center structure

The HbRC is the first homodimeric reaction center structure solved, exhibiting perfect C2 symmetry. All previously solved RC structures (PbRC, PSI, PSII) are heterodimeric. The homodimeric core preserves characteristics of the ancestral reaction center, providing insight into the evolution of photosynthesis.

### C2 symmetry in electron transfer chain

Due to the homodimeric core, the ET cofactors are arranged into two identical branches about the C2 symmetry axis. The ET chain consists of P800 (a pair of BChl g'), Acc (BChl g), A0 (8'-OH Chl a_F), and FX (a [4Fe-4S] cluster). The two identical branches contrast with the asymmetric branches of heterodimeric RCs.

### No bound quinone in electron transfer

The HbRC lacks a bound quinone in the ET chain — a striking divergence from all other known RCs. The crystallized HbRC lacked [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) (MQ), as it is not bound tightly by the protein. The edge-to-edge distance between A0 and FX is ~10.2 Å (much shorter than the ~14.3 Å in PSI), close enough to allow a maximal ET rate of ~8 × 10^8 s^-1, supporting the hypothesis that ET from A0 to FX does not require an intermediate quinone cofactor.

### Antenna architecture and energy transfer

The HbRC binds 54 BChl g molecules as antenna pigments, forming two layers within the complex. Most are within 6 Å of each other for rapid excitation energy transfer. Only six BChl g molecules (three per symmetric side) are within 13 Å of the ET chain, suggesting that energy transferred to the ET chain arrives via these bridging pigments. The antenna domain is fused to the ET domain, similar to PSI.

### Evolutionary significance

The HbRC displays characteristics expected of the common ancestor of all RCs: a homodimeric core, low number of antenna (B)Chls relative to oxygenic homologs, lack of peripheral antenna complexes, and overall simplicity. While the Firmicutes branched early in bacterial evolution, heliobacteria likely acquired the RC via horizontal gene transfer. Nevertheless, some traits of the last common ancestor are preserved in the HbRC due to its host's anoxic niche, similar to early Earth conditions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/photosynthesis/blastochloris-viridis-photosynthetic-reaction-centre/">Blastochloris viridis Photosynthetic Reaction Centre (RCvir)</a> — Type II heterodimeric RC for evolutionary comparison with the homodimeric Type I HbRC
- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/">Photosystem II</a> — PSII is a Type II heterodimeric RC; HbRC is compared as a Type I homodimeric RC with ancestral features
- <a href="/xray-mp-wiki/concepts/miscellaneous/manganese-calcium-cluster/">Manganese-Calcium Cluster (Mn4Ca Cluster)</a> — HbRC lacks an oxygen-evolving complex; comparison highlights unique features of oxygenic vs anoxygenic photosynthesis
- <a href="/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/">Bacteriochlorophyll</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/ligands/menaquinone/">Menaquinone</a> — Related ligand or cofactor
