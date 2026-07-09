---
title: "DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter"
created: 2026-06-05
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8995, doi/10.1038##nature17975, doi/10.1038##nsmb.2687]
verified: regex
uniprot_id: Q9KAX3
---

# DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KAX3">UniProt: Q9KAX3</a>

<span class="expr-badge">Bacillus halodurans</span>

## Overview

DinF-BH is a multidrug and toxic compound extrusion (MATE) family transporter from Bacillus halodurans that functions as an H+-coupled multidrug efflux pump. It belongs to the DinF subfamily of MATE transporters and exports a broad range of organic cations including [Ethidium](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, rhodamine 6G, and [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/). DinF-BH features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12). The protonation site D40 (equivalent to [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/) D41) has a physiologically relevant pKa of ~7, supporting a direct-competition mechanism wherein H+ and substrate compete for DinF-BH D40. The crystal structure of apo DinF-BH was determined at 3.2 A resolution, revealing an asymmetric arrangement of 12 transmembrane helices distinct from the pseudo-two-fold symmetry of NorM subfamily transporters.


## Publications

### doi/10.1038##ncomms8995

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c6n">5C6N</a></td>
      <td>3.0</td>
      <td>P 21 21 21</td>
      <td>DinF-BH D40N mutant, residues 3-448</td>
      <td>N40 (protonation-mimetic asparagine)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5c6o">5C6O</a></td>
      <td>3.0</td>
      <td>P 21 21 21</td>
      <td>DinF-BH wild type, residues 3-448</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/verapamil/">Verapamil</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI

- **Construct**: Full-length DinF-BH cloned into pET15b with C-terminal His6 tag; induced with 0.1 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/)


**Purification:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

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
      <td>Cell growth and induction</td>
      <td>E. coli culture in LB media</td>
      <td>--</td>
      <td>LB media + --</td>
      <td>OD600 = 0.5; induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> at 37 C for 3 h</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Microfluidizer, multiple passages</td>
      <td>--</td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Anatrace)</td>
      <td>Extracted with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Thrombin cleavage</td>
      <td>Thrombin protease incubation overnight</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cleaved C-terminal His6 tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion at 22 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DinF-BH D40N mutant at ~5 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM HEPES-NaOH pH 7.0, 100 mM NaCl, 30-35% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 2 weeks; full size in 1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Transfer to low pH solution: 100 mM Na <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> or <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> pH 4.0, 200 mM NaCl, 35-40% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>DinF-BH D40N crystals for low pH form soaked in <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> or <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> buffer at pH 4.0 for >12 h; heavy atom derivatization with 10 mM heavy metal compounds for 3 h at 22 C</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with <a href="/xray-mp-wiki/reagents/ligands/verapamil/">Verapamil</a>; hanging-drop vapor diffusion at 22 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DinF-BH at ~3 mg/ml incubated with 0.4 mM <a href="/xray-mp-wiki/reagents/ligands/verapamil/">Verapamil</a> for >24 h at 4 C</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
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
      <td>Phasing by molecular replacement and <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a>; verapamil-bound structure very similar to R6G-bound form (rmsd <0.5 A for 447 Ca positions)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c6n">5C6N</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ME</span><span class="topo-outside">QKQQSERLGTEAIPKLL</span><span class="topo-membrane">RSLSIPAMIGMFVMALYNVVNTIF</span><span class="topo-inside">ISYAVGIEGVAGV</span><span class="topo-membrane">TIAFPIMMIMMSMAGALGIGGA</span><span class="topo-outside">SVISRRLGERRGEEANQVFGNI</span><span class="topo-membrane">LTVILVLSVIGFISAFTLLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">PAL</span><span class="topo-inside">QLFGATSVTQGYA</span><span class="topo-membrane">TDYLFPILLGSIFFFFAFAANNIIRS</span><span class="topo-outside">EGN</span><span class="topo-membrane">ATFAMVTMIVPAVLNILLDVLFI</span><span class="topo-inside">FGLNMGV</span><span class="topo-membrane">LGASIATVIAQASVTGLVLRY</span><span class="topo-outside">FLTGKSTLSLHWSDLRMKGSVIKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">CLVGLPAFVQQSSASLMMIAIN</span><span class="topo-inside">SMLLRFGSDFYVGVF</span><span class="topo-membrane">GLVQRIMMFVMMPMMGIMQAMQ</span><span class="topo-outside">PIVGYNYGAKQYSRLRETVMLG</span><span class="topo-membrane">FKVATIFSIGIFALLMLFPEALL</span><span class="topo-inside">RVFTADREVIQAGV</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460   </span>
<span class="topo-line"><span class="topo-membrane">AMHILFCVTFLIGAQIVAGGLYQS</span><span class="topo-outside">LGKP</span><span class="topo-membrane">KQALILSLSRQIIFLIPLVLIL</span><span class="topo-inside">PHIFGLS</span><span class="topo-membrane">GVWWAFPIADVLSFILTVVLL</span><span class="topo-outside">YRDRNVFFLK</span><span class="topo-unknown">TKEERELDLVKTASS</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>3</td>
      <td>19</td>
      <td>3</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>43</td>
      <td>20</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>56</td>
      <td>44</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>100</td>
      <td>79</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>123</td>
      <td>101</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>136</td>
      <td>124</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>162</td>
      <td>137</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>165</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>188</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>189</td>
      <td>195</td>
      <td>189</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>216</td>
      <td>196</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>241</td>
      <td>217</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>263</td>
      <td>242</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>278</td>
      <td>264</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>300</td>
      <td>279</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>322</td>
      <td>301</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>345</td>
      <td>323</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>346</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>384</td>
      <td>360</td>
      <td>384</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>388</td>
      <td>385</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>389</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>417</td>
      <td>411</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>438</td>
      <td>418</td>
      <td>438</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>448</td>
      <td>439</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5c6o">5C6O</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ME</span><span class="topo-outside">QKQQSERLGTEAIPKLLRSLS</span><span class="topo-membrane">IPAMIGMFVMALYNVVDTIFI</span><span class="topo-inside">SYAVGIEGVAGV</span><span class="topo-membrane">TIAFPIMMIMMSMAGALGIGGA</span><span class="topo-outside">SVISRRLGERRGEEANQVFGN</span><span class="topo-membrane">ILTVILVLSVIGFISAFTLL</span><span class="topo-inside">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PALQLFGATSVTQGYATD</span><span class="topo-membrane">YLFPILLGSIFFFFAFAANNIIR</span><span class="topo-outside">SEGNA</span><span class="topo-membrane">TFAMVTMIVPAVLNILLDVLFIFGL</span><span class="topo-inside">NMGV</span><span class="topo-membrane">LGASIATVIAQASVTGLVLR</span><span class="topo-outside">YFLTGKSTLSLHWSDLRMKGSVIKE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">CLVGLPAFVQQSSASLMMIAIN</span><span class="topo-inside">SMLLRFGSDFYVGVF</span><span class="topo-membrane">GLVQRIMMFVMMPMMGIMQA</span><span class="topo-outside">MQPIVGYNYGAKQYSRLRETVMLG</span><span class="topo-membrane">FKVATIFSIGIFALLMLFPEALL</span><span class="topo-inside">RVFTADREVIQAGV</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460    </span>
<span class="topo-line"><span class="topo-membrane">AMHILFCVTFLIGAQIVAGGLYQ</span><span class="topo-outside">SLGKP</span><span class="topo-membrane">KQALILSLSRQIIFLIPLVLIL</span><span class="topo-inside">PHIFGLSG</span><span class="topo-membrane">VWWAFPIADVLSFILTVVLL</span><span class="topo-outside">YRDRNVFFLK</span><span class="topo-unknown">TKEERELDLVKTASST</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>3</td>
      <td>23</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>44</td>
      <td>24</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>56</td>
      <td>45</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>78</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>99</td>
      <td>79</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>119</td>
      <td>100</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>138</td>
      <td>120</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>161</td>
      <td>139</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>166</td>
      <td>162</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>191</td>
      <td>167</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>195</td>
      <td>192</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>215</td>
      <td>196</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>241</td>
      <td>216</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>263</td>
      <td>242</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>278</td>
      <td>264</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>298</td>
      <td>279</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>322</td>
      <td>299</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>345</td>
      <td>323</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>346</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>383</td>
      <td>360</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>388</td>
      <td>384</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>389</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>418</td>
      <td>411</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>438</td>
      <td>419</td>
      <td>438</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>448</td>
      <td>439</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature17975

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4d9a">4D9A</a></td>
      <td>3.0</td>
      <td>P 21 21 21</td>
      <td>DinF-BH wild type, residues 3-448</td>
      <td>Rhodamine 6G (R6G)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI

- **Construct**: Full-length DinF-BH cloned into pET15b with C-terminal His6 tag; induced with 0.1 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/)


**Purification:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

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
      <td>E. coli fermentation</td>
      <td>--</td>
      <td>LB medium + --</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell lysis and membrane preparation</td>
      <td>Microfluidizer</td>
      <td>--</td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes collected; solubilized with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion at 22 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DinF-BH wild type at ~10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.5, 100 mM NaCl, 20-30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 2 weeks; full size in 1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals diffracted to 3.0 A. Substrate soaking with 0.5 mM R6G for 48 h at 22 C.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##nsmb.2687

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lz6">4LZ6</a></td>
      <td>3.2</td>
      <td>P 21 21 21</td>
      <td>DinF-BH wild type, residues 3-448, C-terminal His6 tag</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lz9">4LZ9</a></td>
      <td>3.7</td>
      <td>P 21 21 21</td>
      <td>DinF-BH wild type, residues 3-448, C-terminal His6 tag</td>
      <td>Rhodamine 6G (R6G)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI

- **Construct**: Full-length DinF-BH cloned into pET15b with C-terminal His6 tag; induced with 0.1 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/)


**Purification:**

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

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
      <td>Cell growth and expression</td>
      <td>E. coli culture in LB medium</td>
      <td>--</td>
      <td>LB medium + --</td>
      <td>Induced with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> at OD600 ~0.5</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Microfluidizer, multiple passages</td>
      <td>--</td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes collected by ultracentrifugation; solubilized with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion at 22 C</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DinF-BH wild type at ~10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.5, 100 mM NaCl, 20-30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 2 weeks; full size in 1 month</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals diffracted to 3.2 A. Heavy atom derivatization with 5 mM compounds for 8 h at 22 C. Substrate soaking with 0.5 mM R6G or tetraphenylarsonium (TPP analog) for 48 h at 22 C. Structure solved by combination of molecular replacement and <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lz6">4LZ6</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">QKQQSERLGTEAIPKLLR</span><span class="topo-membrane">SLSIPAMIGMFVMALYNVVDT</span><span class="topo-inside">IFISYAVGIEGVAGV</span><span class="topo-membrane">TIAFPIMMIMMSMAGALGIGGA</span><span class="topo-outside">SVISRRLGERRGEEANQVF</span><span class="topo-membrane">GNILTVILVLSVIGFISAFTLL</span><span class="topo-inside">GPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQLFGATSVTQGYATDY</span><span class="topo-membrane">LFPILLGSIFFFFAFAANNIIRS</span><span class="topo-outside">EGN</span><span class="topo-membrane">ATFAMVTMIVPAVLNILLDVLF</span><span class="topo-inside">IFGLNMGVLG</span><span class="topo-membrane">ASIATVIAQASVTGLVLRYF</span><span class="topo-outside">LTGKSTLSLHWSDLRMKGSVIKEV</span><span class="topo-membrane">C</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">LVGLPAFVQQSSASLMMIAI</span><span class="topo-inside">NSMLLRFGSDFYVGVF</span><span class="topo-membrane">GLVQRIMMFVMMPMMGIMQAMQ</span><span class="topo-outside">PIVGYNYGAKQYSRLRETVMLG</span><span class="topo-membrane">FKVATIFSIGIFALLMLFPEAL</span><span class="topo-inside">LRVFTADREVIQAGVS</span><span class="topo-membrane">AM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440      </span>
<span class="topo-line"><span class="topo-membrane">HILFCVTFLIGAQIVAGGLYQ</span><span class="topo-outside">SLGKP</span><span class="topo-membrane">KQALILSLSRQIIFLIPLVLIL</span><span class="topo-inside">PHIFGLS</span><span class="topo-membrane">GVWWAFPIADVLSFILTVVLL</span><span class="topo-outside">YRDRNVFFLK</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>3</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>54</td>
      <td>42</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>76</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>95</td>
      <td>79</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>117</td>
      <td>98</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>137</td>
      <td>120</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>160</td>
      <td>140</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>163</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>185</td>
      <td>166</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>195</td>
      <td>188</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>215</td>
      <td>198</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>239</td>
      <td>218</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>260</td>
      <td>242</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>276</td>
      <td>263</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>298</td>
      <td>279</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>320</td>
      <td>301</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>342</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>343</td>
      <td>358</td>
      <td>345</td>
      <td>360</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>381</td>
      <td>361</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>386</td>
      <td>384</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>408</td>
      <td>389</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>411</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>436</td>
      <td>418</td>
      <td>438</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>446</td>
      <td>439</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lz9">4LZ9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">QKQQSERLGTEAIPKLLRSLSI</span><span class="topo-membrane">PAMIGMFVMALYNVV</span><span class="topo-inside">DTIFISYAVGIEGVAGVTIA</span><span class="topo-membrane">FPIMMIMMSMAGALG</span><span class="topo-outside">IGGASVISRRLGERRGEEANQVFGNILT</span><span class="topo-membrane">VILVLSVIGFISAFT</span><span class="topo-inside">LLGPA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LQLFGATSVTQGYATDYLF</span><span class="topo-membrane">PILLGSIFFFFAFAAN</span><span class="topo-outside">NIIRSEGNATF</span><span class="topo-membrane">AMVTMIVPAVLNILL</span><span class="topo-inside">DVLFIFGLNMGVLGAS</span><span class="topo-membrane">IATVIAQASVTGLV</span><span class="topo-outside">LRYFLTGKSTLSLHWSDLRMKGSVIKEVC</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LVG</span><span class="topo-membrane">LPAFVQQSSASLMM</span><span class="topo-inside">IAINSMLLRFGSDFYVGVFGLV</span><span class="topo-membrane">QRIMMFVMMPMMG</span><span class="topo-outside">IMQAMQPIVGYNYGAKQYSRLRETVMLGFKV</span><span class="topo-membrane">ATIFSIGIFALLMLFP</span><span class="topo-inside">EALLRVFTADREVIQAGVSAM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440      </span>
<span class="topo-line"><span class="topo-membrane">HILFCVTFLIGAQI</span><span class="topo-outside">VAGGLYQSLGKPKQA</span><span class="topo-membrane">LILSLSRQIIFLIPLVLI</span><span class="topo-inside">LPHIFGLSGV</span><span class="topo-membrane">WWAFPIADVLSFIL</span><span class="topo-outside">TVVLLYRDRNVFFLK</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>3</td>
      <td>24</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>25</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>57</td>
      <td>40</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>72</td>
      <td>60</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>100</td>
      <td>75</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>115</td>
      <td>103</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>139</td>
      <td>118</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>155</td>
      <td>142</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>166</td>
      <td>158</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>181</td>
      <td>169</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>197</td>
      <td>184</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>211</td>
      <td>200</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>243</td>
      <td>214</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>257</td>
      <td>246</td>
      <td>259</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>279</td>
      <td>260</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>292</td>
      <td>282</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>323</td>
      <td>295</td>
      <td>325</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>339</td>
      <td>326</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>360</td>
      <td>342</td>
      <td>362</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>374</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>375</td>
      <td>389</td>
      <td>377</td>
      <td>391</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>407</td>
      <td>392</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>417</td>
      <td>410</td>
      <td>419</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>431</td>
      <td>420</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>446</td>
      <td>434</td>
      <td>448</td>
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

### Direct-competition-based antiport mechanism

DinF-BH uses a direct-competition mechanism wherein H+ and substrate compete for the protonation site D40. The calculated and experimentally determined pKa for DinF-BH D40 converged to ~7, making it a physiologically relevant protonation site. Protonation of D40 triggers substrate release without requiring substantial conformational changes such as TM1 bending, distinguishing it from the indirect coupling mechanism proposed for [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/).

### Verapamil-binding site and poly-specific drug recognition

The verapamil-binding chamber in DinF-BH is hydrophobic and methionine-rich, featuring interactions with side chains of N37 (TM1), Q252 (TM7), M33, Y36 (TM1), F60, M63, M64, M67 (TM2), F150, F154 (TM4), M286 and M293 (TM8). The extended conformation of [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) across the membrane bilayer allows contacts with both N and C domains. The methionine-rich chamber design enables 'poly-specific' binding of chemically and structurally diverse drugs.

### Mutational analysis of the verapamil-binding site

Mutations of M33, N37, D40 and M286 abolished cellular resistance to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), confirming their critical roles in [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) transport. Mutations of Y36, F60, M63, M64, F150 and Q252 rendered DinF-BH-mediated drug efflux resistant to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) treatment, suggesting these residues play regulatory roles in transport function by affecting protein conformational changes.

### Mechanistic differences between MATE subfamilies

DinF-BH (DinF subfamily) differs mechanistically from NorM-NG (NorM subfamily) in how cation binding triggers substrate release. DinF-BH uses direct competition at D40, while NorM-NG shifts transmembrane helices upon Na+ binding. Eukaryotic MATE transporters including hMATE1 are mechanically more similar to NorM-NG than to DinF-BH, despite sequence similarity between DinF-BH and [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/).

### Asymmetric architecture of DinF-BH

Unlike the pseudo-two-fold symmetric NorM transporters, DinF-BH exhibits an asymmetric arrangement of its 12 transmembrane helices. Structural superimposition of the N domain (TM1-TM6) and C domain (TM7-TM12) yielded an r.m.s. deviation of 3.30 A for 138 common C-alpha positions, substantially larger than the 2.39 A observed for NorM-NG. The main difference localizes to extracellular halves of TM7 and TM8 (residues 253-288), which are more kinked than their TM1-TM2 counterparts, induced by P247 and P291.

### D40 as dual-function residue for substrate binding and protonation

D40 in DinF-BH serves a dual role in both substrate binding and protonation. Located within a membrane-embedded chamber shielded by TM7 and TM8, D40 has a calculated pKa of 7.4, making it suitable as a protonation site at physiological pH. The D40N mutation abrogated drug resistance and H+ release upon substrate binding, with R6G binding affinity reduced from Kd 3.1 uM (wild type) to 107.2 uM (D40N). This direct competition between H+ and substrate for D40 is the basis of the antiport mechanism.

### Proposed transport mechanism involving 20 degree rotation

Based on the extracellular-facing structure, an intracellular-facing model was generated by rotating the cytoplasmic halves of TM7 and TM8, as well as TM9-TM12, by 20 degrees relative to the rest of the protein. This rotation collapses the solvent-exposed crevice in the C domain and exposes the drug-binding site toward the cytoplasm. Proline (P247, P291) and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G245, G294) residues in TM7 and TM8 accommodate this motion by straightening the kinks. Mutations of L22, V241, V244, F249 and Q297 along the intracellular transport path impaired transport function.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/nor-mng/">NorM-NG (Neisseria gonorrhoeae NorM)</a> — Co-reported in same paper; mechanistic comparison between DinF and NorM subfamilies
- <a href="/xray-mp-wiki/proteins/norm-vc/">NorM-VC (Vibrio cholerae NorM)</a> — Earlier MATE family structure; NorM subfamily member
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mate-transporter-family/">MATE Transporter Family</a> — DinF-BH is a DinF subfamily member of the MATE family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — MATE transporters operate via alternating access mechanism
- <a href="/xray-mp-wiki/reagents/ligands/ethidium/">Ethidium</a> — Referenced in context related to Ethidium
- <a href="/xray-mp-wiki/reagents/ligands/verapamil/">Verapamil</a> — Referenced in context related to Verapamil
- <a href="/xray-mp-wiki/proteins/abc-transporters/pfmate/">Pfmate</a> — Referenced in context related to Pfmate
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in context related to Iptg
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in context related to DDM
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in context related to Tris Hcl
