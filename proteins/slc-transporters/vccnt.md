---
title: "vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)"
created: 2026-06-21
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10882]
verified: false
---

# vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)

## Overview

vcCNT is a concentrative nucleoside transporter from Vibrio cholerae, a member of the SLC28 family of ion-coupled nucleoside transporters. It uses a sodium ion gradient to transport nucleosides across the cell membrane. The crystal structure was solved at 2.4 Å resolution in complex with uridine, revealing a novel fold with a trimeric architecture and an inward-facing occluded conformation.


## Publications

### doi/10.1038##nature10882

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3tij">3TIJ</a></td>
      <td>2.4</td>
      <td>P6_2</td>
      <td>residues 2-416 (full-length construct with His10-MBP fusion removed)</td>
      <td>Uridine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: vcCNT cloned into modified pET26 vector with pelB leader sequence and PreScission Protease-cleavable His10-maltose-binding protein fusion
- **Notes**: Expressed in E. coli C41 (DE3) cells

**Purification:**

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: vcCNT with N-terminal His10-MBP fusion (cleavable by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/))
- **Tag info**: His10-MBP fusion, cleaved with [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

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
      <td>Homogenization (Avestin)</td>
      <td>—</td>
      <td>— + —</td>
      <td>Cells lysed with homogenizer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>— + 30 mM dodecyl maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>2 h at 4 °C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Co2+ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ affinity resin</td>
      <td>— + —</td>
      <td>Eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>—</td>
      <td>— + —</td>
      <td>Digested overnight with <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris-HCl pH 8.0, 150 mM NaCl, 2 mM dithiothreitol + 5 mM decyl maltoside (DM)</td>
      <td>Presence of 1 mM uridine</td>
    </tr>
  </tbody>
</table>
**Final sample**: vcCNT in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DM, 2 mM DTT, 1 mM uridine

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Microbatch-under-oil</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~10 mg/ml vcCNT in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DM, 2 mM DTT, 1 mM uridine</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM CaCl2, 37-42% PEG400, 100 mM buffer (Tris-HCl pH 9.0 or <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.5)</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10-14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>32.5% PEG400</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown over pH range 5.6-9.5; data collected from crystals at pH 9.0 (Tris-HCl) and pH 9.5 (<a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a>). Platinum derivatives prepared by soaking in 2.5 mM K2Pt(CNS)6 for 2-4 h.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tij">3TIJ</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPAVPRM</span><span class="topo-outside">SLFMS</span><span class="topo-membrane">LIGMAVLLGIAVLLS</span><span class="topo-inside">SNRKAI</span><span class="topo-membrane">NLRTVGGAFAIQFSLGAFI</span><span class="topo-outside">LYV</span><span class="topo-unknown">PWGQE</span></span>
<span class="topo-line"><span class="topo-unknown">LLRGFSDAVSNVINYGNDGTSFLF</span><span class="topo-outside">GGLVSGKMFEVFGGGGFIFAFRVL</span><span class="topo-membrane">PTLIFFSALISV</span></span>
<span class="topo-line"><span class="topo-membrane">LYYL</span><span class="topo-inside">G</span><span class="topo-unknown">VMQWVIRILGGGLQKAL</span><span class="topo-inside">GTSRAESMSAAANIFVGQTEAPLVVRPFVPKMTQSELF</span></span>
<span class="topo-line"><span class="topo-membrane">AVMCGGLASIAGGVLAG</span><span class="topo-outside">YASMGVKIEYL</span><span class="topo-membrane">VAASFMAAPGGLLFAKLMM</span><span class="topo-inside">PETEKPQD</span><span class="topo-unknown">NEDIT</span></span>
<span class="topo-line"><span class="topo-unknown">LDGGDD</span><span class="topo-inside">K</span><span class="topo-membrane">PANVIDAAAGGASAGLQLALNVGAMLIAFIGLI</span><span class="topo-outside">ALINGMLGGIGGWFGMPELK</span></span>
<span class="topo-line"><span class="topo-outside">LEMLLGWLFAPLAFLIGVPWNEATVAGEFIGLKTVANEFVAYSQFAPYLTEAAPVVLSEK</span></span>
<span class="topo-line"><span class="topo-outside">TKAIISF</span><span class="topo-membrane">ALCGFANLSSIAILLGGL</span><span class="topo-inside">GSLAPKRRGDIARM</span><span class="topo-membrane">GVKAVIAGTLSNLMAATIA</span><span class="topo-outside">GF</span></span>
<span class="topo-line"><span class="topo-outside">FL</span><span class="topo-unknown">SF</span></span>
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
      <td>7</td>
      <td>-5</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12</td>
      <td>2</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>7</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>33</td>
      <td>22</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>28</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>55</td>
      <td>47</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>84</td>
      <td>50</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>108</td>
      <td>79</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>119</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>142</td>
      <td>120</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>180</td>
      <td>137</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>197</td>
      <td>175</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>208</td>
      <td>192</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>227</td>
      <td>203</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>235</td>
      <td>222</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>246</td>
      <td>230</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>247</td>
      <td>247</td>
      <td>241</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>280</td>
      <td>242</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>367</td>
      <td>275</td>
      <td>361</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>385</td>
      <td>362</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>399</td>
      <td>380</td>
      <td>393</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>418</td>
      <td>394</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>422</td>
      <td>413</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>424</td>
      <td>417</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tij">3TIJ</a> — Chain B (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPAVPRM</span><span class="topo-outside">SL</span><span class="topo-membrane">FMSLIGMAVLLGIAVLL</span><span class="topo-inside">SSNRKAINLRTV</span><span class="topo-membrane">GGAFAIQFSLGAFILYV</span><span class="topo-unknown">PWGQE</span></span>
<span class="topo-line"><span class="topo-unknown">LLRGFSDAVSNVINYGNDGTSFLF</span><span class="topo-outside">GGLVSGKMFEVFGGGGFIFAFRVL</span><span class="topo-membrane">PTLIFFSALISV</span></span>
<span class="topo-line"><span class="topo-membrane">LYYL</span><span class="topo-inside">G</span><span class="topo-unknown">VMQWVIRILGGGLQKAL</span><span class="topo-inside">GTSRAESMSAAANIFVGQTEAPLVVRPFVPKMTQSELF</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">VMCGGLASIAGGVLAGYA</span><span class="topo-outside">SMGVKI</span><span class="topo-membrane">EYLVAASFMAAPGGLLFA</span><span class="topo-inside">KLMMPETEKPQD</span><span class="topo-unknown">NEDIT</span></span>
<span class="topo-line"><span class="topo-unknown">LDGGDD</span><span class="topo-inside">K</span><span class="topo-membrane">PANVIDAAAGGASAGLQLALNVGAMLIAFIGLI</span><span class="topo-outside">ALINGMLGGIGGWFGMPELK</span></span>
<span class="topo-line"><span class="topo-outside">LEMLLGWLFAPLAFLIGVPWNEATVAGEFIGLKTVANEFVAYSQFAPYLTEAAPVVLSEK</span></span>
<span class="topo-line"><span class="topo-outside">TKAI</span><span class="topo-membrane">ISFALCGFANLSSIAILLGG</span><span class="topo-inside">LGSLAPKRRGDIARMG</span><span class="topo-membrane">VKAVIAGTLSNLMAATIAGF</span></span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-outside">L</span><span class="topo-unknown">SF</span></span>
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
      <td>7</td>
      <td>-5</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>2</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>4</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>38</td>
      <td>21</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>56</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>55</td>
      <td>51</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>84</td>
      <td>50</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>108</td>
      <td>79</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>119</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>142</td>
      <td>120</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>181</td>
      <td>137</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>199</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>205</td>
      <td>194</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>223</td>
      <td>200</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>235</td>
      <td>218</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>246</td>
      <td>230</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>247</td>
      <td>247</td>
      <td>241</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>280</td>
      <td>242</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>364</td>
      <td>275</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>384</td>
      <td>359</td>
      <td>378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>400</td>
      <td>379</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>422</td>
      <td>416</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>424</td>
      <td>417</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tij">3TIJ</a> — Chain C (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPAVPRM</span><span class="topo-outside">S</span><span class="topo-membrane">LFMSLIGMAVLLGIAVLL</span><span class="topo-inside">SSNRKAINLRT</span><span class="topo-membrane">VGGAFAIQFSLGAFIL</span><span class="topo-outside">YV</span><span class="topo-unknown">PWGQE</span></span>
<span class="topo-line"><span class="topo-unknown">LLRGFSDAVSNVINYGNDGTSFLF</span><span class="topo-outside">GGLVSGKMFEVFGGGGFIFAFRVL</span><span class="topo-membrane">PTLIFFSALISV</span></span>
<span class="topo-line"><span class="topo-membrane">LYYL</span><span class="topo-inside">G</span><span class="topo-unknown">VMQWVIRILGGGLQKAL</span><span class="topo-inside">GTSRAESMSAAANIFVGQTEAPLVVRPFVPKMTQSELF</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">VMCGGLASIAGGVLAGY</span><span class="topo-outside">ASMGVKIE</span><span class="topo-membrane">YLVAASFMAAPGGLLFA</span><span class="topo-inside">KLMMPETEKPQD</span><span class="topo-unknown">NEDIT</span></span>
<span class="topo-line"><span class="topo-unknown">LDGGDD</span><span class="topo-inside">K</span><span class="topo-membrane">PANVIDAAAGGASAGLQLALNVGAMLIAFIGLI</span><span class="topo-outside">ALINGMLGGIGGWFGMPELK</span></span>
<span class="topo-line"><span class="topo-outside">LEMLLGWLFAPLAFLIGVPWNEATVAGEFIGLKTVANEFVAYSQFAPYLTEAAPVVLSEK</span></span>
<span class="topo-line"><span class="topo-outside">TKAI</span><span class="topo-membrane">ISFALCGFANLSSIAIL</span><span class="topo-inside">LGGLGSLAPKRRGDIARMG</span><span class="topo-membrane">VKAVIAGTLSNLMAATIAGF</span></span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-outside">L</span><span class="topo-unknown">SF</span></span>
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
      <td>7</td>
      <td>-5</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8</td>
      <td>2</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>26</td>
      <td>3</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>21</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>53</td>
      <td>32</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>55</td>
      <td>48</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>84</td>
      <td>50</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>85</td>
      <td>108</td>
      <td>79</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>125</td>
      <td>119</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>142</td>
      <td>120</td>
      <td>136</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>143</td>
      <td>181</td>
      <td>137</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>176</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>206</td>
      <td>193</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>223</td>
      <td>201</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>235</td>
      <td>218</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>246</td>
      <td>230</td>
      <td>240</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>247</td>
      <td>247</td>
      <td>241</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>280</td>
      <td>242</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>364</td>
      <td>275</td>
      <td>358</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>381</td>
      <td>359</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>400</td>
      <td>376</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>395</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>422</td>
      <td>416</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>424</td>
      <td>417</td>
      <td>418</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Overall Architecture

vcCNT crystallizes as a homotrimer shaped like an inverted triangular basin with the mouth facing the intracellular side. Each protomer contains eight transmembrane helices (TM1-TM8), two re-entrant helix-turn-helix hairpins (HP1 and HP2), and three interfacial helices (IH1-IH3). The fold is novel, with a scaffold domain (TM1, TM2, IH1, EH, TM3, TM6) and a transport domain (IH2, HP1, TM4a/b, TM5 and IH3, HP2, TM7a/b, TM8) related by internal two-fold pseudo-symmetry.

### Nucleoside and Sodium Binding

Uridine binds in a cleft between HP1, HP2, TM4, and TM7. HP1 and TM4b interact with the [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) base, while HP2 and TM7 interact with the ribose. Key residues include Gln154, Thr155, Glu156 (HP1), Val188 (TM4b) for [URACIL](/xray-mp-wiki/reagents/ligands/uracil/), and Glu332 (HP2), Asn368, Ser371 (TM7) for ribose. A Na+ binding site is located between HP1 and the unwound region of TM4, coordinated by three backbone carbonyls, two side-chain hydroxyls, and a water molecule. Na+ binding is proposed to bring HP1 close to TM4 to complete the nucleoside-binding site.

### Transport Mechanism

The structure represents an inward-facing occluded conformation. A hypothetical alternating-access mechanism is proposed where rigid-body movement of the transport domain across TM6 (which serves as a hydrophobic barrier) permits transition between inward-facing and outward-facing conformations, while the scaffold domain is held in place.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/vccnt/">vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)</a> — Primary entity described in this paper
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> — Related ligand or cofactor
