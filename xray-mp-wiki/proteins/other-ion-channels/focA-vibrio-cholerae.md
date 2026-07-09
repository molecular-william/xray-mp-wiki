---
title: "FocA (Formate Channel A from Vibrio cholerae)"
created: 2009-11-01
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08610, doi/10.1038##nsmb.1740]
verified: regex
uniprot_id: ['P0AC25', 'Q9KRE7']
---

# FocA (Formate Channel A from Vibrio cholerae)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AC25">UniProt: P0AC25</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KRE7">UniProt: Q9KRE7</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

FocA (formate channel A) is a pentameric membrane channel belonging to the FNT (formate/nitrite transporter) family that functions as a formate transporter. The landmark crystal structure of E. coli FocA (Wang et al., Nature 2009, PDBs 3KCU, 2.24 A; 3KCV, 3.2 A) revealed a pentameric aquaporin-like channel architecture, establishing the FNT family fold. Each protomer consists of six transmembrane helices with a substrate translocation pore through the monomer center, not the pentamer axis. The Vibrio cholerae FocA was subsequently crystallized at 2.13 A (low-formate) and 2.5 A (high-formate) resolution in space group P2_1 2_1 2_1. The selectivity filter comprises a cytoplasmic slit and a central constriction ring (2.3 A diameter). Two formate ions were observed bound in the cytoplasmic slit in the high-formate structure. The channel exhibits flexibility in the Omega loop connecting TM2a and TM3, which modulates the slit dimensions. The structure is similar in overall fold to water and [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) channels ([AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1), GlpF). The E. coli FocA features ten transmembrane helices per protomer with pH-dependent gating.


## Publications

### doi/10.1038##nature08610

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a></td>
      <td>2.24</td>
      <td>Not specified</td>
      <td>E. coli FocA</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a></td>
      <td>3.2</td>
      <td>Not specified</td>
      <td>E. coli FocA</td>
      <td>Not specified</td>
    </tr>
  </tbody>
</table>
 - R-work Not specified%, R-free Not specified%; Data collection: Landmark E. coli FocA structure; pentameric aquaporin-like channel
 - R-work Not specified%, R-free Not specified%; Data collection: E. coli FocA structure; lower resolution form

**Expression:**

- **Expression system**: E. coli (C43)
- **Construct**: Full-length FocA from Vibrio cholerae (280 residues), C-terminal decahistidine tag, pBAD vector
- **Notes**: Overexpressed from pBAD vector in E. coli C43 cells

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKAT</span><span class="topo-outside">KHPLKTF</span><span class="topo-membrane">YLAITAGVFISIAFVFYITAT</span><span class="topo-inside">TGTGTMPFGM</span><span class="topo-membrane">AKLVGGICFSLGLILCVVC</span><span class="topo-outside">GADLFTSTVLIVVAKASGRITWGQLAKN</span><span class="topo-membrane">WLNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGE</span><span class="topo-inside">YMTANG</span><span class="topo-unknown">QWGLNVLQTADH</span><span class="topo-inside">KVHHTF</span><span class="topo-membrane">IEAVCLGILANLMVCLAVWMS</span><span class="topo-outside">YSGRSL</span><span class="topo-membrane">MDKAFIMVLPVAMFVASGFEHSIANMFMIPM</span><span class="topo-inside">GIVIRDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-inside">NFSHLTV</span><span class="topo-membrane">MNFITDNLIPVTIGNIIGGGLLVGL</span><span class="topo-outside">TYWVIYLR</span><span class="topo-unknown">ENDHH</span></span>
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
      <td>1</td>
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>57</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>113</td>
      <td>86</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>143</td>
      <td>138</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>155</td>
      <td>144</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>156</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>188</td>
      <td>183</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>219</td>
      <td>189</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>220</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>272</td>
      <td>248</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>280</td>
      <td>273</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>281</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKAT</span><span class="topo-outside">KHPLKTF</span><span class="topo-membrane">YLAITAGVFISIAFVFYITAT</span><span class="topo-inside">TGTGTMPFGM</span><span class="topo-membrane">AKLVGGICFSLGLILCVVCG</span><span class="topo-outside">ADLFTSTVLIVVAKASGRITWGQLAKN</span><span class="topo-membrane">WLNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGE</span><span class="topo-inside">YMTANG</span><span class="topo-unknown">QWGLNVLQTADHK</span><span class="topo-inside">VHHT</span><span class="topo-membrane">FIEAVCLGILANLMVCLAVWMS</span><span class="topo-outside">YSGRSL</span><span class="topo-membrane">MDKAFIMVLPVAMFVASGFEHSIANMFMIPM</span><span class="topo-inside">GIVIRDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-inside">NFSHLTV</span><span class="topo-membrane">MNFITDNLIPVTIGNIIGGGLLVGL</span><span class="topo-outside">TYWVIYLR</span><span class="topo-unknown">ENDHH</span></span>
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
      <td>1</td>
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>57</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>67</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>87</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>143</td>
      <td>138</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>156</td>
      <td>144</td>
      <td>156</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>160</td>
      <td>157</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>161</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>188</td>
      <td>183</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>219</td>
      <td>189</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>220</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>272</td>
      <td>248</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>280</td>
      <td>273</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>281</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKAT</span><span class="topo-outside">KHPLKTF</span><span class="topo-membrane">YLAITAGVFISIAFVFYITAT</span><span class="topo-inside">TGTGTMPFGM</span><span class="topo-membrane">AKLVGGICFSLGLILCVVC</span><span class="topo-outside">GADLFTSTVLIVVAKA</span><span class="topo-unknown">SGRITWGQL</span><span class="topo-outside">AK</span><span class="topo-membrane">NWLNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGE</span><span class="topo-inside">YMTANG</span><span class="topo-unknown">QWGLNVLQTADH</span><span class="topo-inside">KVHHTF</span><span class="topo-membrane">IEAVCLGILANLMVCLAVWMS</span><span class="topo-outside">YSGRSL</span><span class="topo-membrane">MDKAFIMVLPVAMFVASGFEHSIANMFMIPM</span><span class="topo-inside">GIVIRDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-inside">NFSHLTV</span><span class="topo-membrane">MNFITDNLIPVTIGNIIGGGLLVGL</span><span class="topo-outside">TYWV</span><span class="topo-unknown">IYLRENDHH</span></span>
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
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>57</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>101</td>
      <td>86</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>110</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>112</td>
      <td>111</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>137</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>143</td>
      <td>138</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>155</td>
      <td>144</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>156</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>188</td>
      <td>183</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>219</td>
      <td>189</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>220</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>272</td>
      <td>248</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>276</td>
      <td>273</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>285</td>
      <td>277</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKAT</span><span class="topo-outside">KHPLKTF</span><span class="topo-membrane">YLAITAGVFISIAFVFYITAT</span><span class="topo-inside">TGTGTMPFGM</span><span class="topo-membrane">AKLVGGICFSLGLILCVVC</span><span class="topo-outside">GADLFTSTVLIVVAKASGRITWGQLAKN</span><span class="topo-membrane">WLNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGE</span><span class="topo-inside">YMTANG</span><span class="topo-unknown">QWGLNVLQTADH</span><span class="topo-inside">KVHHTF</span><span class="topo-membrane">IEAVCLGILANLMVCLAVWMS</span><span class="topo-outside">YSGRSL</span><span class="topo-membrane">MDKAFIMVLPVAMFVASGFEHSIANMFMIPM</span><span class="topo-inside">GIVIRDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-inside">NFSHLTVMNF</span><span class="topo-membrane">ITDNLIPVTIGNIIGGGLLVGL</span><span class="topo-outside">TYWV</span><span class="topo-unknown">IYLRENDHH</span></span>
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
      <td>1</td>
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>35</td>
      <td>29</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>57</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>113</td>
      <td>86</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>143</td>
      <td>138</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>155</td>
      <td>144</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>156</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>188</td>
      <td>183</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>219</td>
      <td>189</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>250</td>
      <td>220</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>272</td>
      <td>251</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>276</td>
      <td>273</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>285</td>
      <td>277</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcu">3KCU</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKATK</span><span class="topo-outside">HPLKTF</span><span class="topo-membrane">YLAITAGVFISIAFVFYITAT</span><span class="topo-inside">TGTGTMPFGM</span><span class="topo-membrane">AKLVGGICFSLGLILCVVC</span><span class="topo-outside">GADLFTSTVLIVVAKASGRITWGQLAKN</span><span class="topo-membrane">WLNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLS</span><span class="topo-inside">GEYMTANG</span><span class="topo-unknown">QWGLNVLQTADH</span><span class="topo-inside">KVHHTF</span><span class="topo-membrane">IEAVCLGILANLMVCLAVWMS</span><span class="topo-outside">YSGRSL</span><span class="topo-membrane">MDKAFIMVLPVAMFVASGFEHSIANMFMIPM</span><span class="topo-inside">GIVIRDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-inside">NFSHLTV</span><span class="topo-membrane">MNFITDNLIPVTIGNIIGGGLLVGL</span><span class="topo-outside">TYWVIY</span><span class="topo-unknown">LRENDHH</span></span>
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
      <td>1</td>
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>56</td>
      <td>36</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>66</td>
      <td>57</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>113</td>
      <td>86</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>135</td>
      <td>114</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>143</td>
      <td>136</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>155</td>
      <td>144</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>156</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>182</td>
      <td>162</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>188</td>
      <td>183</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>219</td>
      <td>189</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>247</td>
      <td>220</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>272</td>
      <td>248</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>278</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>285</td>
      <td>279</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKATK</span><span class="topo-inside">HPLKTFYLA</span><span class="topo-membrane">ITAGVFISIAFVFYITATT</span><span class="topo-outside">GTGTMP</span><span class="topo-membrane">FGMAKLVGGICFSLGLILC</span><span class="topo-inside">VVCGADLFTSTVLIVVAKASGRITWGQLAKNW</span><span class="topo-membrane">LNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGEYMTA</span><span class="topo-outside">NGQWGLN</span><span class="topo-membrane">VLQTADHKVHHTFIEAVCLGILANLMVCLAV</span><span class="topo-inside">WMSYSGRSLMDKA</span><span class="topo-membrane">FIMVLPVAMFVASG</span><span class="topo-unknown">F</span><span class="topo-membrane">EHSIANMFMIPMGIVIRDF</span><span class="topo-outside">ASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">NFSHL</span><span class="topo-membrane">TVMNFITDNLIPVTIGNIIGGGLL</span><span class="topo-inside">VGLTYWVIYL</span><span class="topo-unknown">RENDHH</span></span>
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
      <td>1</td>
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>114</td>
      <td>83</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>141</td>
      <td>115</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>148</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>179</td>
      <td>149</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>226</td>
      <td>208</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>227</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>279</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>285</td>
      <td>280</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKATK</span><span class="topo-inside">HPLKTFYLA</span><span class="topo-membrane">ITAGVFISIAFVFYITATT</span><span class="topo-outside">GTGTMP</span><span class="topo-membrane">FGMAKLVGGICFSLGLILCV</span><span class="topo-inside">VCGADLFTSTVLIVVAKASGRITWGQLAKNW</span><span class="topo-membrane">LNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGEYMT</span><span class="topo-outside">ANGQWGLN</span><span class="topo-membrane">VLQTADHKVHHTFIEAVCLGILANLMVCLAV</span><span class="topo-inside">WMSYSGRSLMDKA</span><span class="topo-membrane">FIMVLPVAMFVASG</span><span class="topo-unknown">F</span><span class="topo-membrane">EHSIANMFMIPMGIVI</span><span class="topo-outside">RDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">NFSHL</span><span class="topo-membrane">TVMNFITDNLIPVTIGNIIGGGLL</span><span class="topo-inside">VGLTYWVIYL</span><span class="topo-unknown">RENDHH</span></span>
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
      <td>1</td>
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>83</td>
      <td>64</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>114</td>
      <td>84</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>140</td>
      <td>115</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>148</td>
      <td>141</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>179</td>
      <td>149</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>245</td>
      <td>224</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>279</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>285</td>
      <td>280</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKATK</span><span class="topo-inside">HPLKTFYLA</span><span class="topo-membrane">ITAGVFISIAFVFYITATT</span><span class="topo-outside">GTGTMP</span><span class="topo-membrane">FGMAKLVGGICFSLGLILCV</span><span class="topo-inside">VCGADLFTSTVLIVVAKASGRITWGQLAKNW</span><span class="topo-membrane">LNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGEYMTA</span><span class="topo-outside">NGQWGLN</span><span class="topo-membrane">VLQTADHKVHHTFIEAVCLGILANLMVCLAV</span><span class="topo-inside">WMSYSGRSLMDKA</span><span class="topo-membrane">FIMVLPVAMFVASG</span><span class="topo-unknown">F</span><span class="topo-membrane">EHSIANMFMIPMGIVI</span><span class="topo-outside">RDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">NFSHL</span><span class="topo-membrane">TVMNFITDNLIPVTIGNIIGGGLL</span><span class="topo-inside">VGLTYWVIYL</span><span class="topo-unknown">RENDHH</span></span>
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
      <td>1</td>
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>83</td>
      <td>64</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>114</td>
      <td>84</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>141</td>
      <td>115</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>148</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>179</td>
      <td>149</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>245</td>
      <td>224</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>279</td>
      <td>270</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>285</td>
      <td>280</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a> — Chain D (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKATK</span><span class="topo-inside">HPLKTFYLA</span><span class="topo-membrane">ITAGVFISIAFVFYITATT</span><span class="topo-outside">GTGTMP</span><span class="topo-membrane">FGMAKLVGGICFSLGLILC</span><span class="topo-inside">VVCGADLFTSTVLIVVAKASGRITWGQLAKNW</span><span class="topo-membrane">LNVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGEYMT</span><span class="topo-outside">ANGQWGLN</span><span class="topo-membrane">VLQTADHKVHHTFIEAVCLGILANLMVCLAV</span><span class="topo-inside">WMSYSGRSLMDKA</span><span class="topo-membrane">FIMVLPVAMFVASG</span><span class="topo-unknown">F</span><span class="topo-membrane">EHSIANMFMIPMGIVI</span><span class="topo-outside">RDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">NFSHL</span><span class="topo-membrane">TVMNFITDNLIPVTIGNIIGGGLL</span><span class="topo-inside">VGLTYWVIYLR</span><span class="topo-unknown">ENDHH</span></span>
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
      <td>1</td>
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>114</td>
      <td>83</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>140</td>
      <td>115</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>148</td>
      <td>141</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>179</td>
      <td>149</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>245</td>
      <td>224</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>280</td>
      <td>270</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>281</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kcv">3KCV</a> — Chain E (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKADNPFDLLLPAAMAKVAEEAGVYKAT</span><span class="topo-inside">KHPLKTFYLA</span><span class="topo-membrane">ITAGVFISIAFVFYITATT</span><span class="topo-outside">GTGTMP</span><span class="topo-membrane">FGMAKLVGGICFSLGLILC</span><span class="topo-inside">VVCGADLFTSTVLIVVAKASGRITWGQLAKNWL</span><span class="topo-membrane">NVYFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">NLVGALLFVLLMWLSGEYMTA</span><span class="topo-outside">NGQWGLN</span><span class="topo-membrane">VLQTADHKVHHTFIEAVCLGILANLMVCLAV</span><span class="topo-inside">WMSYSGRSLMDKA</span><span class="topo-membrane">FIMVLPVAMFVASG</span><span class="topo-unknown">F</span><span class="topo-membrane">EHSIANMFMIPMGIVI</span><span class="topo-outside">RDFASPEFWTAVGSAPE</span></span>
<span class="topo-ruler">       250       260       270       280     </span>
<span class="topo-line"><span class="topo-outside">NFSHL</span><span class="topo-membrane">TVMNFITDNLIPVTIGNIIGGGLL</span><span class="topo-inside">VGLTYWVIYLR</span><span class="topo-unknown">ENDHH</span></span>
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
      <td>1</td>
      <td>28</td>
      <td>1</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>29</td>
      <td>38</td>
      <td>29</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>39</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>64</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>115</td>
      <td>83</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>141</td>
      <td>116</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>148</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>179</td>
      <td>149</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>192</td>
      <td>180</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>245</td>
      <td>224</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>246</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>280</td>
      <td>270</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>285</td>
      <td>281</td>
      <td>285</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.1740

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a></td>
      <td>2.13</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length FocA from Vibrio cholerae (280 residues)</td>
      <td>Formate (20 mM in crystallization)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a></td>
      <td>2.5</td>
      <td>P2_1 2_1 2_1</td>
      <td>Full-length FocA from Vibrio cholerae (280 residues)</td>
      <td>Formate (120 mM in crystallization; 2 formate ions bound)</td>
    </tr>
  </tbody>
</table>
 - R-work 18.0%, R-free 21.0%; Atoms: 9818; Data collection: SIRAS phasing with platinum derivative; noncrystallographic symmetry averaging
 - R-work 17.0%, R-free 22.0%; Atoms: 9844; Data collection: High-formate crystal form with 2 bound formate ions in cytoplasmic slit

**Expression:**

- **Expression system**: E. coli (C43)
- **Construct**: Full-length FocA from Vibrio cholerae (280 residues), C-terminal decahistidine tag, pBAD vector
- **Notes**: Overexpressed from pBAD vector in E. coli C43 cells

**Purification:**

- **Expression system**: E. coli (C43)
- **Tag info**: C-terminal decahistidine tag

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
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> solubilization</td>
      <td>—</td>
      <td>1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membrane solubilization after cell disruption</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Co2+ affinity (<a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Co2+ resin</td>
      <td>—</td>
      <td>Incubated overnight; washed then eluted</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> Co2+ resin</td>
      <td>1.1% octylglucoside + 20 mM sodium formate + 100 mM NaCl + 8% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a>, pH 7.5</td>
      <td>Elution from <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC (Sephadex 200)</td>
      <td>Sephadex 200 (Akta FPLC, GE Healthcare)</td>
      <td>Elution buffer from affinity step</td>
      <td>Peak fractions collected and concentrated to ~8 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~8 mg/mL FocA in elution buffer (1.1% octylglucoside, 20 mM sodium formate, 100 mM NaCl, 8% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 7.5)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>32% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 550 monomethyl ether + 25 mM <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a></td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Low-formate crystals grown with 20 mM formate; high-formate crystals with 120 mM sodium formate + 20 mM <a href="/xray-mp-wiki/reagents/buffers/mops">MOPS</a> pH 6.7</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAIT</span><span class="topo-inside">GEGKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITGE</span><span class="topo-inside">GKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQF</span><span class="topo-outside">MEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>34</td>
      <td>24</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAI</span><span class="topo-inside">TGEGKAKKAAYKSFLLA</span><span class="topo-membrane">ISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQF</span><span class="topo-outside">MEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-unknown">I</span><span class="topo-outside">KYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYLK</span><span class="topo-unknown">D</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>37</td>
      <td>21</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>55</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>245</td>
      <td>223</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>279</td>
      <td>269</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>280</td>
      <td>280</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITGEGKA</span><span class="topo-inside">KKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain E (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITG</span><span class="topo-inside">EGKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>34</td>
      <td>23</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAIT</span><span class="topo-inside">GEGKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>21</td>
      <td>1</td>
      <td>21</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITGE</span><span class="topo-inside">GKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQF</span><span class="topo-outside">MEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>1</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>34</td>
      <td>24</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAI</span><span class="topo-inside">TGEGKAKKAAYKSFLLA</span><span class="topo-membrane">ISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQF</span><span class="topo-outside">MEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-unknown">I</span><span class="topo-outside">KYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYLK</span><span class="topo-unknown">D</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>37</td>
      <td>21</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>55</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>137</td>
      <td>114</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>138</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>245</td>
      <td>223</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>279</td>
      <td>269</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>280</td>
      <td>280</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain D (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITGEGKA</span><span class="topo-inside">KKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>34</td>
      <td>27</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kly">3KLY</a> — Chain E (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEHNQFDSLLPPQMAERAAITG</span><span class="topo-inside">EGKAKKAAYKSF</span><span class="topo-membrane">LLAISAGIQIGIAFVFYTVVT</span><span class="topo-outside">TGAHDMPYG</span><span class="topo-membrane">VTKLLGGLAFSLGLILVV</span><span class="topo-inside">ITGGELFTSSVLILVAKASGKISWKELVRNW</span><span class="topo-membrane">TVVYFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LCGSIILVFIMLATRQ</span><span class="topo-outside">FMEDGGQLGLNAMAISQHKLHH</span><span class="topo-membrane">TFLQAFALGLMCNILVCLAV</span><span class="topo-inside">WMTFSARSLTDK</span><span class="topo-membrane">VMVLILPVAMFVSSGFEHCIANMFQVPMAIG</span><span class="topo-outside">IKYFAPESFWAMTGANIAQ</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-outside">YADLN</span><span class="topo-membrane">FVNFIVNNLIPVTLGNIVGGGVF</span><span class="topo-inside">VGMWYWLIYL</span><span class="topo-unknown">KD</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>34</td>
      <td>23</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>55</td>
      <td>35</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>64</td>
      <td>56</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>65</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>113</td>
      <td>83</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>136</td>
      <td>114</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>137</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>159</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>190</td>
      <td>179</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>221</td>
      <td>191</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>245</td>
      <td>222</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>268</td>
      <td>246</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>278</td>
      <td>269</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>280</td>
      <td>279</td>
      <td>280</td>
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

### Landmark FocA structure reveals pentameric aquaporin-like architecture

The first crystal structure of E. coli FocA (Wang et al., Nature 2009, PDBs 3KCU, 3KCV) revealed a pentameric assembly with each protomer forming an independent pore, similar to aquaporins but with distinct selectivity features. This landmark structure established the structural basis for the FNT (formate/nitrite transporter) family and demonstrated that formate channels share the aquaporin fold despite lacking sequence homology.

### Formate selectivity filter architecture

The FocA selectivity filter consists of a cytoplasmic slit (2.1 x 4.1 A) and a central constriction ring (2.3 A diameter). The slit is formed by Leu78 (TM2a), Leu88 and Thr90 (Omega loop), and Val174 (TM4). His208 (S loop) sits on the periplasmic side. The central ring is formed by Phe74 (TM2a), Phe201 (TM5a), His208 C-beta (S loop), and Ala211 (TM5b). The pore is basic on the cytoplasmic one-third and hydrophobic on the periplasmic two-thirds. All selectivity filter residues are highly conserved among FNT members including both FocA and NirC.

### Two formate ions bound in cytoplasmic slit

In the high-formate (2.5 A) structure, two formate ions (FMT1 and FMT2) are bound in the cytoplasmic slit. FMT2 forms hydrogen bonds with His208 (N epsilon 2 atom) and van der Waals contacts with Leu88, Thr90, and Asn171. FMT1 sits closer to the cytoplasmic surface, forming hydrogen bonds with FMT2 and van der Waals contacts with Leu88, Phe89, and Asn171. This provides a structural basis for substrate selectivity: the slit dimensions and hydrogen bonding network specifically accommodate formate in a coin-in-slot orientation.

### Omega loop flexibility modulates slit dimensions

The Omega loop connecting TM2a and TM3 adopts two distinct configurations (UP and DOWN) across the five monomers in the crystal. In the UP configuration (monomers A-C), Thr90 and Ser91 are positioned within the slit, narrowing it to 2.1 x 4.1 A. In the DOWN configuration (monomers D-E), the Omega loop moves away, widening the slit to 2.1 x 7.2 A. This flexibility may have mechanistic consequences for substrate access and selectivity, analogous to variations observed in the E. coli water channel AqpZ.

### Pentameric architecture with monomeric transport pores

FocA forms a homopentamer with a diameter of 82 A and thickness of 58 A. The monomer-monomer interface is large (~1,450 A^2) with high surface complementarity (0.68), comparable to antibody-antigen interfaces. However, unlike many pentameric channels, the transport pore is located within each monomer (not at the pentamer axis). The central pentamer pore is too wide to be a selectivity filter and is probably occupied by lipid molecules in the native membrane.

### Transport activity confirmed by 14C formate uptake

Concentrative uptake assay demonstrated formate transport into proteoliposomes reconstituted with purified FocA at pH 6.7. No pH or electrochemical gradient existed across the proteoliposome membrane, suggesting FocA functions as a formate channel or uniporter. The assay used 14C-labeled sodium formate with E. coli total phospholipid proteoliposomes.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/fnt-family/">FNT Family (Formate/Nitrite Transporter Family)</a> — FocA is a member of the FNT family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/hsc/">HSC (Hydrosulfide Channel from Clostridium difficile)</a> — Related FNT family channel; extensively compared with FocA in the paper
- <a href="/xray-mp-wiki/proteins/other-ion-channels/hiteha/">HiTehA (TehA from Haemophilus influenzae)</a> — Related anion channel within the FNT superfamily
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">Aqp1 (Aquaporin 1 from E. coli)</a> — Water channel with similar monomeric pore architecture
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">GlpF (Glycerol Facilitator from E. coli)</a> — Glycerol channel with similar monomeric pore architecture
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Ion Channel Selectivity Filter</a> — FocA selectivity filter with cytoplasmic slit and central constriction ring
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> — Entity mentioned in text
