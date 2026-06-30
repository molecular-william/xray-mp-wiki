---
title: "Human Neurokinin 1 Receptor (NK1R)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-07939-8, doi/10.1073##pnas.1812717115]
verified: false
---

# Human Neurokinin 1 Receptor (NK1R)

## Overview

The human neurokinin 1 receptor (NK1R, TACR1) is a class A G protein-coupled receptor that binds the neuropeptide Substance P (SP) as its preferred endogenous agonist. NK1R is expressed in the central and peripheral nervous system, smooth muscle, endothelial cells, and immune cells. It is implicated in nausea, analgesia, inflammation, pruritus, and depression, making it a key therapeutic target for chemotherapy-induced nausea and vomiting (CINV). The receptor was crystallized as a thermostabilized NK1R-PGS fusion construct (with Pyrococcus abyssi glycogen synthase replacing intracellular loop 3), and high-resolution structures were determined in complex with the antagonists CP-99,994 (3.27 A), [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) (2.40 A), [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) (2.20 A), and L760735 (3.4 A).


## Publications

### doi/10.1038##s41467-018-07939-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hll">6HLL</a></td>
      <td>3.27 A</td>
      <td>C2221</td>
      <td>Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
</td>
      <td>CP-99,994</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hlo">6HLO</a></td>
      <td>2.40 A</td>
      <td>P212121</td>
      <td>Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/aprepitant/">Aprepitant</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hlp">6HLP</a></td>
      <td>2.20 A</td>
      <td>P212121</td>
      <td>Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/netupitant/">Netupitant</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: Human NK1R with [PGS (Pyrococcus abyssi Glycogen Synthase) Fusion](/xray-mp-wiki/reagents/protein-tags/pgs-fusion/) replacing ICL3; N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His10 tag; 3C protease cleavage site for tag removal

- **Notes**: Receptor expressed in Sf9 insect cells using baculovirus system. Thermostabilized construct based on directed evolution studies (Schutz et al. 2016).


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
      <td>Membrane preparation</td>
      <td>Homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + None</td>
      <td>Sf9 cell pellet resuspended and membranes collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes solubilized for 1 h at 4 C with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Ni-NTA affinity</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>
 + 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His-tag</a>ged receptor bound to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin, eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Buffer exchange and tag cleavage</td>
      <td>Desalting (PD MiniTrap G-25)</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.03% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.006% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removed; <a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His-tag</a>ged 3C protease and PNGaseF added for 6 h at 4 C</td>
    </tr>
    <tr>
      <td>Reverse Ni-NTA</td>
      <td>Flow-through collection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>
 + 0.03% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.006% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Cleaved receptor collected as flow-through; uncleaved and 3C protease bind resin</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Vivaspin 2 concentrator (100 kDa MWCO)</td>
      <td>—</td>
      <td>as above + as above</td>
      <td>Concentrated to ~50-60 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~50-60 mg/ml NK1R-PGS in 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% (w/v) <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CP-99,994 complex crystals appeared in <1 h in broad conditions. <a href="/xray-mp-wiki/reagents/ligands/aprepitant/">Aprepitant</a> complex: 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 6.0, 31% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 50-70 mM MgCl2, 50 uM <a href="/xray-mp-wiki/reagents/ligands/aprepitant/">Aprepitant</a>. <a href="/xray-mp-wiki/reagents/ligands/netupitant/">Netupitant</a> complex: 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 6.0, 31% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 40-50 mM Mg(HCO3)2, 50 uM <a href="/xray-mp-wiki/reagents/ligands/netupitant/">Netupitant</a>. All crystals cryo-cooled in liquid nitrogen without additional cryoprotectant.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hll">6HLL</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDNVLPVDSDLSPNISTNTSEPNQFV</span><span class="topo-inside">QPA</span><span class="topo-membrane">WQIVLWAAAYTVIVVTSVVGNVVVM</span><span class="topo-outside">WIILAHKRMRTVTNYF</span><span class="topo-membrane">LVNAAFAEASMAAFNTVVNFTYAV</span><span class="topo-inside">HNEWY</span><span class="topo-membrane">YGLFYCKFHNFFPIAAIFASI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YSMTA</span><span class="topo-outside">VAFDRYMAIIHPLQPRLSLTATK</span><span class="topo-membrane">VVICVIWVLALLLAFPQGYYS</span><span class="topo-inside">TTETMPSRVVCKIEWPEHPNKI</span><span class="topo-membrane">YEKVYHICVTVLIYFLPLLVIGYLYT</span><span class="topo-outside">VVGITLRASGIDCSFWNESYLTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSEQVSAARKVVKMM</span><span class="topo-membrane">IVVVCTFAICWLPFHIFFLLPY</span><span class="topo-unknown">INPDLYLKKF</span><span class="topo-inside">IQ</span><span class="topo-membrane">QVYLAIMWLAM</span></span>
<span class="topo-ruler">       490       500       510       520</span>
<span class="topo-line"><span class="topo-membrane">SSTMYNPIIY</span><span class="topo-outside">CCLN</span><span class="topo-unknown">DRFRLGFKHA</span><span class="topo-outside">F</span><span class="topo-unknown">RCCPFISAGDYEGLE</span></span>
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
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>54</td>
      <td>30</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>94</td>
      <td>71</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>99</td>
      <td>95</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>125</td>
      <td>100</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>148</td>
      <td>126</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>169</td>
      <td>149</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>191</td>
      <td>170</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>217</td>
      <td>192</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>435</td>
      <td>218</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>457</td>
      <td>251</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>468</td>
      <td>469</td>
      <td>283</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>490</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>494</td>
      <td>306</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>495</td>
      <td>504</td>
      <td>310</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>505</td>
      <td>505</td>
      <td>320</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hlo">6HLO</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDNVLPVDSDLSPNISTNTSEPNQFVQ</span><span class="topo-inside">PAW</span><span class="topo-membrane">QIVLWAAAYTVIVVTSVVGNVV</span><span class="topo-outside">VMWIILAHKRMRTVTNYFLVN</span><span class="topo-membrane">AAFAEASMAAFNTVVNFTYA</span><span class="topo-inside">VHNEWYY</span><span class="topo-membrane">GLFYCKFHNFFPIAAIFASI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YSMT</span><span class="topo-outside">AVAFDRYMAIIHPLQPRLSLTATKVVI</span><span class="topo-membrane">CVIWVLALLLAFPQGYYST</span><span class="topo-inside">TETMPSRVVCKIEWPEHPNKI</span><span class="topo-membrane">YEKVYHICVTVLIYFLPLLVIG</span><span class="topo-outside">YLYTVVGITLRASGIDCSFWNESYLTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSEQVSAARKVVKMMIV</span><span class="topo-membrane">VVCTFAICWLPFHIFFLLPYIN</span><span class="topo-inside">PDLY</span><span class="topo-unknown">LKK</span><span class="topo-inside">FIQQ</span><span class="topo-membrane">VYLAIMWLAM</span></span>
<span class="topo-ruler">       490       500       510       520</span>
<span class="topo-line"><span class="topo-membrane">SSTMYNPII</span><span class="topo-outside">YCCLN</span><span class="topo-unknown">DRFRLGFKHA</span><span class="topo-outside">FRCC</span><span class="topo-unknown">PFISAGDYEGLE</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>28</td>
      <td>30</td>
      <td>28</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>52</td>
      <td>31</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>73</td>
      <td>53</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>93</td>
      <td>74</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>100</td>
      <td>94</td>
      <td>100</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>124</td>
      <td>101</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>151</td>
      <td>125</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>170</td>
      <td>152</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>191</td>
      <td>171</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>213</td>
      <td>192</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>437</td>
      <td>214</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>438</td>
      <td>459</td>
      <td>253</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>460</td>
      <td>463</td>
      <td>275</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>470</td>
      <td>282</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>489</td>
      <td>286</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>494</td>
      <td>305</td>
      <td>309</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>495</td>
      <td>504</td>
      <td>310</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>505</td>
      <td>508</td>
      <td>320</td>
      <td>324</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hlp">6HLP</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDNVLPVDSDLSPNISTNTSEPNQFV</span><span class="topo-inside">QPA</span><span class="topo-membrane">WQIVLWAAAYTVIVVTSVVGNVVVM</span><span class="topo-outside">WIILAHKRMRTVTNYF</span><span class="topo-membrane">LVNAAFAEASMAAFNTVVNFTYAV</span><span class="topo-inside">HNEW</span><span class="topo-membrane">YYGLFYCKFHNFFPIAAIFASI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">YSMTA</span><span class="topo-outside">VAFDRYMAIIHPLQPRLSLTATKVV</span><span class="topo-membrane">ICVIWVLALLLAFPQGYYSTT</span><span class="topo-inside">ETMPSRVVCKIEWPEHPNK</span><span class="topo-membrane">IYEKVYHICVTVLIYFLPLLVIGY</span><span class="topo-outside">LYTVVGITLRASGIDCSFWNESYLTG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSEQVSAARKVVKMM</span><span class="topo-membrane">IVVVCTFAICWLPFHIFFLLPYINP</span><span class="topo-inside">DL</span><span class="topo-unknown">Y</span><span class="topo-inside">LKKF</span><span class="topo-membrane">IQQVYLAIMWLAM</span></span>
<span class="topo-ruler">       490       500       510       520</span>
<span class="topo-line"><span class="topo-membrane">SSTMYNPIIY</span><span class="topo-outside">CCLNDRFRLGFKHAFRC</span><span class="topo-unknown">C</span><span class="topo-outside">PFIS</span><span class="topo-unknown">AGDYEGLE</span></span>
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
      <td>1</td>
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>27</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>54</td>
      <td>30</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>94</td>
      <td>71</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>98</td>
      <td>95</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>125</td>
      <td>99</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>150</td>
      <td>126</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>171</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>172</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>214</td>
      <td>191</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>226</td>
      <td>215</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>422</td>
      <td>1218</td>
      <td>1413</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>435</td>
      <td>238</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>460</td>
      <td>251</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>461</td>
      <td>462</td>
      <td>276</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>463</td>
      <td>463</td>
      <td>278</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>464</td>
      <td>467</td>
      <td>279</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>490</td>
      <td>283</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>506</td>
      <td>306</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>507</td>
      <td>323</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>508</td>
      <td>324</td>
      <td>324</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>509</td>
      <td>512</td>
      <td>324</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>520</td>
      <td>328</td>
      <td>335</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1812717115

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6e59">6E59</a></td>
      <td>3.4 A</td>
      <td>not specified</td>
      <td>Human NK1R-PGS fusion: Pyrococcus abyssi glycogen synthase (PGS) replacing ICL3; expressed in Sf9 insect cells via baculovirus
</td>
      <td>L760735</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: Human NK1R with [PGS (Pyrococcus abyssi Glycogen Synthase) Fusion](/xray-mp-wiki/reagents/protein-tags/pgs-fusion/) replacing ICL3; N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His10 tag; 3C protease cleavage site for tag removal

- **Notes**: Receptor expressed in Sf9 insect cells using baculovirus system. Thermostabilized construct based on directed evolution studies (Schutz et al. 2016).


**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Human NK1R-PGS fusion with N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) and His10 tag
- **Tag info**: N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) + His10 tag

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
      <td>Membrane preparation</td>
      <td>Homogenization and ultracentrifugation</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Sf9 cell pellet homogenized</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 500 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% Na Cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>, 5 uM L760735 + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% Na Cholate, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilization for 1 h at 4 C, ultracentrifugation at 100,000 x g</td>
    </tr>
    <tr>
      <td>Ni-NTA batch binding</td>
      <td>Batch binding with <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% Na Cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 uM L760735</td>
      <td>20 GE <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> added before binding, batch mode for 4 h at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA elution</td>
      <td>Column elution</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% Na Cholate, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 uM L760735</td>
      <td>Eluted with 5 volumes of elution buffer</td>
    </tr>
    <tr>
      <td>M1 anti-FLAG affinity</td>
      <td>M1 <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> with detergent exchange</td>
      <td>M1 anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> agarose</td>
      <td>200 ug/mL <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + Detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/Na Cholate/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> to 0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> on M1 beads</td>
      <td>2 mM CaCl2 added before loading; eluted with <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide + <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td></td>
      <td>Single monomeric peak collected, purity checked by SDS/PAGE</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>30-50 mg/ml NK1R-PGS</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% (w/w) <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (2:3 protein:lipid mass ratio)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals observed in 1 day, full size in 1 week. Cryoprotected in crystallization mother liquid. Data from 36 merged crystals. Diffraction data collected at APS 23ID-D beamline (12 keV, Pilatus3 6M detector). Resolution limit 3.4 A. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with Phaser.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Antagonist binding modes reveal induced-fit mechanism

The three structures reveal distinct binding poses for the progenitor
antagonist CP-99,994 and the clinically approved antagonists [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/)
and [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/). CP-99,994 binds with its core (piperidine ring) between
F268(6.55) and Q165(4.60), with two arms targeting distinct lipophilic
subpockets. [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/), with an additional arm 3 (triazolinone) substituent,
creates an extended binding pocket ([EBP](/xray-mp-wiki/proteins/enzymes/human-ebp/)) at the interface of helices IV,
V and ECL2, inducing an induced-fit conformational change. [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/),
with its distinct chemical scaffold (substituted pyridine core), binds in
a more upright position with its arm 3 targeting a hydrophobic groove
between F268(6.55), P271(6.58) and Y272(6.59) at the extracellular tip
of helix VI.

### Histidine lock — interhelical H-bond network for insurmountable antagonism

Both [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) and [Netupitant](/xray-mp-wiki/reagents/ligands/netupitant/) induce a distinct receptor conformation
characterized by a reorientation of H197(5.39) and Y272(6.59), forming
an extended interhelical hydrogen bond network that cross-links the
extracellular ends of helices V and VI. The network involves residues
Y272(6.59), H197(5.39), T201(5.43) and H265(6.52). This "histidine lock"
reduces conformational flexibility and provides a structural rationale
for the insurmountable antagonism observed for these clinically approved
antagonists. CP-99,994 does not induce this network.

### E78(2.50) replaces sodium ion for lack of basal activity

NK1R has a glutamate (E78) at position 2.50 instead of the more common
aspartate found in most class A GPCRs. This larger glutamate side chain
forms a direct bidentate interaction with the amide group of N301(7.49)
and hydrogen bonds to S119(3.39), replacing the structural role of the
allosteric sodium ion observed in other inactive class A GPCRs. This
tighter helical bundle cross-linking provides a structural basis for
the observed lack of basal signaling in NK1R.

### L760735 antagonist binding and MD simulation analysis

The 3.4 A crystal structure of hNK1R bound to L760735 (a close [Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/)
analog with amine-substituted triazole instead of 3-oxo-substituted triazole)
reveals a three-layered antagonist architecture spanning 14 A in a narrow
orthosteric pocket. The fluorophenyl and 3,5-trifluoromethyl-benzylether
moieties form an intramolecular pi-pi stacking interaction. Glide docking
and MD simulations in explicit lipid bilayers show that L760735 and
[Aprepitant](/xray-mp-wiki/reagents/ligands/aprepitant/) prefer to bind in their neutral forms, with the neutral form
adopting a conformation more consistent with the crystal structure.
W261(6.48) at the pocket base contributes to ligand stability. The
antagonist does not make strong contacts with TM2 and TM7, allowing
binding without orthosteric pocket contraction.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/aprepitant/">Aprepitant</a> — L760735 is a close analog of the clinically approved drug aprepitant
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent exchanged on M1 anti-FLAG beads during purification
- <a href="/xray-mp-wiki/concepts/tachykinin-receptor-family/">Tachykinin Receptor Family</a> — NK1R is the founding member of the tachykinin receptor family
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/human-ebp/">EBP</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
