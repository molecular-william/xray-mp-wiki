---
title: "TmrAB Heterodimeric ABC Transporter from Thermus thermophilus"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1620009114]
verified: regex
uniprot_id: ['Q72J04', 'Q72J05']
---

# TmrAB Heterodimeric ABC Transporter from Thermus thermophilus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72J04">UniProt: Q72J04</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72J05">UniProt: Q72J05</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

TmrAB (TmrA/TmrB) from *Thermus thermophilus* is a heterodimeric ABC half-transporter that serves as a structural and functional homolog of the human transporter associated with antigen processing (TAP). It is a multidrug resistance protein that transports peptides, fluorophores, and potentially lipids. TmrAB shares 27-30% sequence identity with human TAP1/TAP2 and can restore antigen processing in human TAP-deficient cells. The 2.7-Å crystal structure reveals an asymmetric inward-facing conformation with a single catalytically active ATP-binding site, making it a model system for asymmetric ABC exporters.


## Publications

### doi/10.1073##pnas.1620009114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5mkk">5MKK</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length TmrA (TTC0976) and TmrB (TTC0977)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Full-length TmrA and TmrB co-expressed
- **Notes**: SeMet-labeled protein prepared using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) Expression Media. Detailed cloning described in Materials and Methods.

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
      <td>French press</td>
      <td>—</td>
      <td>20 mM Hepes pH 7.5, 300 mM NaCl</td>
      <td>Lysozyme and DNase I added. Cell debris removed by centrifugation at 10,000 x g.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>His-tag purification</td>
      <td>—</td>
      <td></td>
      <td>Details of purification described in Materials and Methods</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td></td>
      <td>Detailed in Materials and Methods</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified TmrAB in 20 mM Hepes pH 7.5, 140 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mkk">5MKK</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">TEDTYSKAF</span><span class="topo-outside">D</span><span class="topo-unknown">RALFARILRYV</span><span class="topo-membrane">WPYRLQVVLALLFLLVVTLAAA</span><span class="topo-inside">ATPLFFKWAIDLALVPTEPRPLAERFHLLLWISLGFL</span><span class="topo-membrane">AVRAVHFAATYGETYLIQWVG</span><span class="topo-outside">QRVLFDLRSDLFAKLMRLH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PGFYDRNPVGRLMTRVTSDVDAINQ</span><span class="topo-membrane">FITGGLVGVIADLFTLVGLLG</span><span class="topo-inside">FMLFLSPKLTLVV</span><span class="topo-membrane">LLVAPVLLAVTTWVRLGMR</span><span class="topo-outside">SAYREMRLRLARVNAALQENLSGVETIQLFVKEREREEKFDR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LNRDLFRAWVEI</span><span class="topo-membrane">IRWFALFFPVVGFLGDFAV</span><span class="topo-inside">ASLVYYGGGEVVRGAVSLGLLVAFVD</span><span class="topo-membrane">YTRQLFQPLQDLSDKFNLF</span><span class="topo-outside">QGAMASAERIFGVLDTEEELKDPEDPTPIRGFRGEVEFRDVWLA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">YTPKGVEPTEKDWVLKGVSFRVRPGEKVALVGATGAGKTSVVSLIARFYDPQRGCVFLDGVDVRRYRQEELRRHVGIVLQEPFLFSGTVLDNLRLFDPSVPPERVEEVARFLGAHEFILR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">LPKGYQTVLGERGAGLSTGEKQLLALVRALLASPDILLILDEATASVDSETEKRLQEALYKAMEGRTSLIIAHRLSTIRHVDRILVFRKGRLVEEGSHEELLAKGGYYAALYRLQFQEAK</span></span>
<span class="topo-ruler">       610 </span>
<span class="topo-line"><span class="topo-outside">LG</span><span class="topo-unknown">GGGENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>10</td>
      <td>10</td>
      <td>11</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>21</td>
      <td>12</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>43</td>
      <td>23</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>80</td>
      <td>45</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>82</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>145</td>
      <td>103</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>147</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>168</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>198</td>
      <td>181</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>252</td>
      <td>200</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>271</td>
      <td>254</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>297</td>
      <td>273</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>316</td>
      <td>299</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>602</td>
      <td>318</td>
      <td>603</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5mkk">5MKK</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">TGR</span><span class="topo-unknown">SAAPLLRRLWPYV</span><span class="topo-outside">GRYRW</span><span class="topo-membrane">RYLWAVLAGLVSIFFFVLTP</span><span class="topo-inside">YFLRLAVDAVQAGRGFGVYALAI</span><span class="topo-membrane">VASAALSGLLSYAMRRLAV</span><span class="topo-outside">VASRQVEYDLRRDLLHHLLTLDRDFYHKHRVGDLMNR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LNTDLSAVREMVGP</span><span class="topo-membrane">GILMGSRLSFLVLLAFLSMYA</span><span class="topo-inside">VNARLA</span><span class="topo-membrane">FYLTLILPGIFLAMRFLLRLID</span><span class="topo-outside">RRYREAQEVFDRISTLAQEAFSGIRVVKGYALERRMVAWFQDLNRLYVEKSL</span><span class="topo-membrane">ALARV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">EGPLHALLGFLMGFAFL</span><span class="topo-inside">TVLWAGGAMVVRGELSVGELVQF</span><span class="topo-membrane">NAYLAQLTWPILGLGWVM</span><span class="topo-outside">ALYQRGLTSLRRLFELLDEKPAIRDEDPLPLALEDLSGEVRFEGVGLKRDGRWLLRGLTLTI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">PEGMTLGITGRTGSGKSLLAALVPRLLDPSEGRVYVGGHEARRIPLAVLRKAVGVAPQEPFLFSETILENIAFGLDEVDRERVEWAARLAGIHEEILAFPKGYETVLGERGITLSGGQRQ</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       </span>
<span class="topo-line"><span class="topo-outside">RVALARALAKRPKILILDDALSAVDAETEARILQGLKTVLGKQTTLLISHRTAALRHADWIIVLDGGRIVEEGTHESLLQAGGLYAEMDRLQKEVEA</span></span>
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
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>16</td>
      <td>5</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>21</td>
      <td>18</td>
      <td>22</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>41</td>
      <td>23</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>42</td>
      <td>64</td>
      <td>43</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>83</td>
      <td>66</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>134</td>
      <td>85</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>155</td>
      <td>136</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>157</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>183</td>
      <td>163</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>235</td>
      <td>185</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>257</td>
      <td>237</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>280</td>
      <td>259</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>298</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>577</td>
      <td>300</td>
      <td>578</td>
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

### Functional TAP Homolog

TmrAB shares 27-30% sequence identity with human TAP1/TAP2 and can restore MHC-I surface expression in TAP1-deficient human fibroblast cells. It transports peptides (optimal length ~7-9 aa) with broad specificity, concentrating substrates up to 4,000-fold in liposomes.

### Asymmetric Inward-Facing Conformation

The 2.7-Å crystal structure reveals a unique asymmetric inward-facing state. TmrAB has only one catalytically active ATP-binding site (in TmrA). The C-terminal zipper helices rearrange during NBD closure and are essential for efficient transport.

### Periplasmic Gate Dynamics

PELDOR/DEER spectroscopy shows the periplasmic gate opens ~20 Å in detergent and ~35 Å in lipid bilayers upon vanadate trapping (mimicking the ATP hydrolysis transition state). Only the ATP hydrolysis transition state drives outward-facing conformation, unlike homodimeric ABC transporters.

### Broad Substrate Specificity

TmrAB transports peptides (7-35 aa), fluorophores (fluorescein), and may function as a lipid flippase. Activity is modulated by lipid composition, with 30% [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) essential for activity. The binding cavity is chemically heterogeneous: TmrA contributes charged residues, TmrB contributes hydrophobic residues.

### Lateral Lipid Entry Gate

TM4 and TM6 of TmrB form a laterally open V-shaped gate at the inner membrane leaflet for membrane-embedded substrate access. Five arginines (R177, R181, R185, R186, R188) line the rim, providing a positively charged groove for phospholipid headgroups. MD simulations confirm [POPE](/xray-mp-wiki/reagents/lipids/pope/) and [POPG](/xray-mp-wiki/reagents/lipids/popg/) binding at this site.

### Zipper Helix Mechanism

The C-terminal helices of TmrA and TmrB form a zipper-like structure that plays a crucial role in guiding conformational changes during substrate transport. Deletion of the zipper helix (Δzipper) significantly reduces transport activity without affecting K_m, indicating a role in turnover rather than substrate binding.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — TmrAB is a heterodimeric ABC exporter and member of the ABC transporter superfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-allosteric-regulation/">ABC Transporter Allosteric Regulation</a> — TmrAB exhibits asymmetric ATP hydrolysis with one degenerate nucleotide-binding site
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/conformational-asymmetry-abc-transporters/">Conformational Asymmetry in ABC Transporters</a> — TmrAB structure reveals asymmetric inward-facing state with C-terminal zipper helices
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Buffer HEPES</a> — Used in purification and reconstitution buffers for TmrAB
- <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE (1-Palmitoyl-2-Oleoyl-Phosphatidylethanolamine)</a> — Used in MD simulations and lipid modulation studies of TmrAB
- <a href="/xray-mp-wiki/reagents/lipids/popg/">POPG (1-Palmitoyl-2-Oleoyl-Phosphatidylglycerol)</a> — Used in MD simulations; 30% PG essential for TmrAB activity
- <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC (1-Palmitoyl-2-Oleoyl-Phosphatidylcholine)</a> — Used in liposome reconstitution for TmrAB transport assays
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Used as a minor component (5 mol%) in liposome reconstitution
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
