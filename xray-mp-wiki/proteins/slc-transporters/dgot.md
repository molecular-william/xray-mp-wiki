---
title: "DgoT (E. coli D-galactonate Transporter)"
created: 2019-05-13
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pbio.3000260]
verified: regex
uniprot_id: J7QAK3
---

# DgoT (E. coli D-galactonate Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/J7QAK3">UniProt: J7QAK3</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

DgoT (D-galactonate transporter) is a proton-coupled D-galactonate/H+ symporter from
Escherichia coli that belongs to the solute carrier 17 (SLC17) family within the major
facilitator superfamily (MFS). The structure was determined in two conformations: an
inward-open apo state (PDB 6E9N) at 2.9 x 3.8 x 3.8 A resolution and an outward-facing,
substrate-bound occluded state (PDB 6E9O) at 3.5 A resolution. DgoT is composed of 12
transmembrane helices with an MFS fold and contains two intracellular helices (ICH1 and
ICH2). The structures reveal a putative H+ tunnel connecting the periplasm to a polar
pocket in the N-terminal lobe containing key protonatable residues Asp46 (TM1) and
Glu133 (TM4). Substrate recognition involves a salt bridge between Arg47 (TM1) and the
carboxyl group of D-galactonate, with nine hydrogen bonds from residues in both N- and
C-terminal domains conferring high specificity for D-galactonate over its epimer
gluconate. The transport mechanism couples H+ flux to substrate translocation via
reversible protonation of Asp46 and Glu133, with Glu133 protonation releasing Arg47 to
bind the anionic substrate.


## Publications

### doi/10.1371##journal.pbio.3000260

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6e9n">6E9N</a></td>
      <td>2.9 x 3.8 x 3.8 (anisotropic)</td>
      <td>P 1 21 1</td>
      <td>Wild-type DgoT (residues 27-443) from E. coli, C-terminal decahistidine tag with thrombin cleavage site</td>
      <td>beta-nonylglucoside (beta-NG), gluconate (nonspecific binding in cavity)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6e9o">6E9O</a></td>
      <td>3.5</td>
      <td>C 1 2 1</td>
      <td>E133Q mutant DgoT (residues 24-443) from E. coli, C-terminal decahistidine tag with thrombin cleavage site</td>
      <td>D-galactonate</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41(DE3)
- **Construct**: Full-length DgoT with C-terminal decahistidine tag and thrombin cleavage site (pQE60)
- **Induction**: 0.5-1 mM IPTG at OD600 0.6-0.8, 18C for 16 h
- **Media**: Terrific Broth (TB) supplemented with 2 mM MgSO4

**Purification:**

- **Expression system**: E. coli C41(DE3)
- **Expression construct**: Full-length DgoT with C-terminal decahistidine tag (pQE60)
- **Tag info**: C-terminal decahistidine tag with thrombin cleavage site

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
      <td>Emulsiflex C3 homogenizer</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 300 mM NaCl</td>
      <td>5-6 cycles at 15,000-20,000 psi; debris removed at 10,000-18,000g for 20 min</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 300 mM NaCl</td>
      <td>185,500g for 1 h; membranes flash frozen in liquid N2 and stored at -80C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1.4% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltoside)</td>
      <td>2 h stirring at 4C; insoluble material removed at 185,500g for 20 min</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> cobalt affinity resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 10 CV wash buffer + 500 mM NaCl; elute with 150 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>Desalting column</td>
      <td>10-DG desalting column (Bio-Rad)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removed prior to tag cleavage</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin cleavage</td>
      <td>—</td>
      <td></td>
      <td>Overnight digestion at 4C with alpha-thrombin</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Centrifugal concentration</td>
      <td>—</td>
      <td></td>
      <td>Concentrated to 5 mg/ml using 100 kDa MWCO concentrator</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop vapor diffusion (HiLiDe method)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>WT DgoT at 5 mg/ml, repipidated into E. coli polar lipids (2.33:1 protein:lipid, 5:1 detergent:lipid)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>39% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400, 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> pH 5.35</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days (small rod-shaped crystals)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Well solution used as cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>HiLiDe-treated DgoT crystallized via hanging drop; Al's oil placed over well solution to slow vapor diffusion; protein pre-incubated with 10 mM sodium gluconate; space group P2_1; data collected at ALS Beamline 8.3.1 at wavelength 1.1159 A</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DgoT E133Q at 7-8 mg/ml (not lipidated)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>32% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 1000, 100 mM <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> pH 9.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 weeks to 9 months (150-200 um rectangular crystals)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Well solution used as cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein pre-incubated with 10 mM Na galactonate; space group C2; data collected at ALS Beamline 8.3.1 at wavelength 1.1158 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6e9n">6E9N</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVSGFAMPKIWRKLAMDIPVNAAKPG</span><span class="topo-inside">RRRYL</span><span class="topo-membrane">TLVMIFITVVICYVDRANLAVAS</span><span class="topo-outside">AHIQEEFGITKAEM</span><span class="topo-membrane">GYVFSAFAWLYTLCQIPGGWFL</span><span class="topo-inside">DRVGS</span><span class="topo-membrane">RVTYFIAIFGWSVATLFQGFA</span><span class="topo-outside">TGLM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SLIGLRAITGIFEAPAFPTN</span><span class="topo-inside">NRMVTSWFPEHERASA</span><span class="topo-membrane">VGFYTSGQFVGLAFLTPLLIWI</span><span class="topo-outside">QEMLSWH</span><span class="topo-membrane">WVFIVTGGIGIIWSLIWFKVY</span><span class="topo-inside">QPPRLTKGISKAELDYIRDGGGLVDGDA</span><span class="topo-unknown">PVKKEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">RQ</span><span class="topo-inside">PLTAKDWKLVFHR</span><span class="topo-membrane">KLIGVYLGQFAVASTLWFFLTWFP</span><span class="topo-outside">NYLTQEKGITALKAG</span><span class="topo-membrane">FMTTVPFLAAFVGVLLSGWV</span><span class="topo-inside">ADLLVRKGFSLGFAR</span><span class="topo-membrane">KTPIICGLLISTCIMGAN</span><span class="topo-outside">YTNDPM</span><span class="topo-membrane">MIMCLMA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-membrane">LAFFGNGFASITW</span><span class="topo-inside">SLVSSLAPMRLIGLTG</span><span class="topo-membrane">GVFNFAGGLGGITVPLVVGYL</span><span class="topo-outside">AQGYGFAP</span><span class="topo-membrane">ALVYISAVALIGALSYILLVG</span><span class="topo-inside">DVKR</span><span class="topo-unknown">VGSLVPRGSGSHHHHHH</span></span>
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
      <td>26</td>
      <td>1</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>31</td>
      <td>27</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>54</td>
      <td>32</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>68</td>
      <td>55</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>90</td>
      <td>69</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>95</td>
      <td>91</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>116</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>120</td>
      <td>117</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>140</td>
      <td>121</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>156</td>
      <td>141</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>178</td>
      <td>157</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>179</td>
      <td>185</td>
      <td>179</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>206</td>
      <td>186</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>234</td>
      <td>207</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>242</td>
      <td>235</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>243</td>
      <td>255</td>
      <td>243</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>279</td>
      <td>256</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>294</td>
      <td>280</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>314</td>
      <td>295</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>329</td>
      <td>315</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>347</td>
      <td>330</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>353</td>
      <td>348</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>373</td>
      <td>354</td>
      <td>373</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>389</td>
      <td>374</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>410</td>
      <td>390</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>418</td>
      <td>411</td>
      <td>418</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>439</td>
      <td>419</td>
      <td>439</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>440</td>
      <td>443</td>
      <td>440</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>460</td>
      <td>444</td>
      <td>460</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6e9o">6E9O</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVSGFAMPKIWRKLAMDIPVNAA</span><span class="topo-outside">KPGRRRYL</span><span class="topo-membrane">TLVMIFITVVICYVDRANL</span><span class="topo-inside">AVASAHIQEEFGITKAEMGYV</span><span class="topo-membrane">FSAFAWLYTLCQIPGGWFL</span><span class="topo-outside">DRVGSR</span><span class="topo-membrane">VTYFIAIFGWSVATLFQGF</span><span class="topo-inside">ATGLM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-membrane">LIGLRAITGIFQAPAFPTNN</span><span class="topo-outside">RMVTSWFPEHER</span><span class="topo-membrane">ASAVGFYTSGQFVGLAFLTPLL</span><span class="topo-inside">IWIQEMLSWHW</span><span class="topo-membrane">VFIVTGGIGIIWSLIWFKV</span><span class="topo-outside">YQPPRLTKGISKAELDYIRDGGGLV</span><span class="topo-unknown">DGDAPVKKEA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">RQ</span><span class="topo-outside">PLTAKDWKLV</span><span class="topo-membrane">FHRKLIGVYLGQFAVASTLWFFLT</span><span class="topo-inside">WFPNYLTQEKGIT</span><span class="topo-unknown">ALKAG</span><span class="topo-inside">FMTT</span><span class="topo-membrane">VPFLAAFVGVLLSGWVAD</span><span class="topo-outside">LLVRKGFSLGF</span><span class="topo-membrane">ARKTPIICGLLISTCIMG</span><span class="topo-inside">ANYTNDPMMIMC</span><span class="topo-membrane">LMA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-membrane">LAFFGNGFASITWSLV</span><span class="topo-outside">SSLAPMRLIG</span><span class="topo-membrane">LTGGVFNFAGGLGGITVPLV</span><span class="topo-inside">VGYLAQGYGFAPAL</span><span class="topo-membrane">VYISAVALIGALSYILLV</span><span class="topo-outside">GDVK</span><span class="topo-unknown">RVGSLVPRGSGSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>24</td>
      <td>31</td>
      <td>24</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>32</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>71</td>
      <td>51</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>90</td>
      <td>72</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>96</td>
      <td>91</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>115</td>
      <td>97</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>141</td>
      <td>122</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>153</td>
      <td>142</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>154</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>186</td>
      <td>176</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>205</td>
      <td>187</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>230</td>
      <td>206</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>252</td>
      <td>243</td>
      <td>252</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>276</td>
      <td>253</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>289</td>
      <td>277</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>298</td>
      <td>295</td>
      <td>298</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>299</td>
      <td>316</td>
      <td>299</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>327</td>
      <td>317</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>345</td>
      <td>328</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>357</td>
      <td>346</td>
      <td>357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>376</td>
      <td>358</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>386</td>
      <td>377</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>406</td>
      <td>387</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>420</td>
      <td>407</td>
      <td>420</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>438</td>
      <td>421</td>
      <td>438</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>442</td>
      <td>439</td>
      <td>442</td>
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

### Two conformations capture alternating access mechanism

The two crystal structures of DgoT (inward-open apo and outward-facing substrate-bound
occluded) capture snapshots of the alternating access transport cycle. In the
inward-open conformation, the cytoplasmic side is open with a wide aqueous cavity,
while the periplasmic side is sealed. In the outward-facing occluded state (E133Q
mutant with D-galactonate bound), the substrate is occluded within the central
binding site, with TM7 bending inward over the substrate to form a periplasmic gate.

### Proton translocation pathway via N-terminal polar pocket

The inward-facing structure reveals a putative water-filled H+ tunnel connecting the
periplasmic surface (near Glu180 in TM5) to a membrane-embedded polar pocket in the
N-terminal lobe containing Asp46 (TM1) and Glu133 (TM4). The tunnel has an entrance
diameter of 3.6 A, a constriction of 2.4 A (near Phe278, Pro279, and Thr297), and
an exit at Asp46 of 5.0 A. Polar residues including Glu59, Gln179, Glu180 at the
entrance and Thr172, Thr297 in the interior potentially facilitate H+ movement.
Asp46 (predicted pKa ~6.0) is likely protonated in the inward-open structure.

### Substrate recognition by both N- and C-terminal domains

Unlike sugar transporters that segregate H+ and substrate translocation to different
lobes, DgoT uses both N-terminal (Tyr44, Arg47 from TM1; Tyr79 from TM2; Gln164 from
TM5) and C-terminal domains (Gln264 from TM7; Ser370 from TM10; Asn393 from TM11) for
substrate recognition. Arg47 forms a salt bridge with the D-galactonate carboxyl group
(3.6 A), while four residues (Asn393, Gln264, Ser370, Gln164) provide eight hydrogen
bonds with the five substrate -OH groups, conferring high specificity for D-galactonate
over the epimer gluconate.

### H+/substrate coupling mechanism via Asp46-Glu133-Arg47 triad

A mechanism for coupling H+ flux to substrate translocation is proposed. In the
outward-facing conformation, Glu133 is protonated, allowing Arg47 to provide the
positive charge to bind the anionic substrate carboxyl. Substrate binding stabilizes
the protonated state of Glu133. After reorientation to the cytoplasmic side, substrate
and H+ are released. Glu133 deprotonation enables formation of a charge pair with Arg47,
facilitating reorientation of the empty carrier. Both Asp46 (D46N) and Glu133 (E133Q)
mutations eliminate active transport, supporting their essential roles.

### Electrogenic transport with H+/substrate stoichiometry >1

DgoT catalyzes electrogenic transport with H+/D-galactonate stoichiometry greater
than 1. The H+ ionophore nigericin (dissipates DeltapH) and the K+ ionophore
[Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin/) (dissipates Deltapsi) both eliminate galactonate uptake, demonstrating
electrogenic H+ cotransport. Thermodynamic calculations suggest that the H+
stoichiometry of >1 enables DgoT to generate approximately 50:1 substrate gradients
under physiological conditions (external pH ~5.5, internal pH ~7.5, Deltapsi = -60 mV).

### VGLUTs and sialin divergence from bacterial SLC17 transporters

The DgoT structures suggest a common mechanism for divergent ionic coupling in the
SLC17 family. The VGLUTs (vesicular glutamate transporters) lack the TM1 acidic
residue equivalent to Asp46 but retain Glu133, which may serve as an allosteric
H+ activation site rather than a coupled transport residue. Sialin retains both
Asp46 and Glu133 for coupled H+ symport. The H183R mutation in sialin corresponds
to Asn141 in DgoT, which forms hydrogen bonds positioning Trp373 for substrate
interaction, explaining the loss of transport in infantile sialic acid storage disease
(ISSD).


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — DgoT belongs to the MFS fold with 12 TM helices arranged in 2 six-helix bundles
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Two structures capture inward-open and outward-facing states of the transport cycle
- <a href="/xray-mp-wiki/proteins/mfs-transporters/xyle/">XylE (E. coli Sugar Transporter)</a> — Related MFS transporter; structural comparison for periplasmic gating via TM7 bending
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for DgoT solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/og/">beta-Octylglucoside (OG) / beta-Nonylglucoside (beta-NG)</a> — Beta-NG identified in aqueous cavity of WT DgoT structure
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for cobalt affinity elution at 150 mM
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Used for induction of DgoT expression at 0.5-1 mM
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer used in purification (20 mM Tris pH 7.4)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Used at 10% in purification buffers for protein stability
- <a href="/xray-mp-wiki/reagents/protein-tags/thrombin-protease/">Thrombin Protease</a> — Used to cleave decahistidine tag from DgoT
