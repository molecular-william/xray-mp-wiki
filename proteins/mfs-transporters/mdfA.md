---
title: "MdfA Multidrug Efflux Transporter"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2018.02.026, doi/10.1038##cr.2015.94, doi/10.1038##s41467-018-06306-x]
verified: false
---

# MdfA Multidrug Efflux Transporter

## Overview

MdfA is a secondary multidrug efflux transporter from Escherichia coli belonging to the Major Facilitator Superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)). It functions as a drug/proton antiporter that exports a broad spectrum of chemically dissimilar toxic compounds, including neutral, zwitterionic, and monovalent cationic drugs. MdfA is fueled by the proton electrochemical potential. Crystal structures of the MdfA(Q131R) mutant have been determined with bound ligands [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/) (PDB 4ZP0, 2.0 A), [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (PDB 4ZOW, 2.4 A), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (PDB 4ZP2, 2.2 A), revealing the substrate-binding mode of an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporter. A double mutant MdfA(Q131R/L339E) was crystallized at 2.2 A resolution (PDB 6EUQ). Studies revealed that membrane-embedded MdfA assumes a relatively stable inward-closed conformation that is further stabilized by substrates and [deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/).


## Publications

### doi/10.1016##j.jmb.2018.02.026

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6euq">6EUQ</a></td>
      <td>2.2 A</td>
      <td>P21</td>
      <td>MdfA(Q131R/L339E) double mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/deoxycholate/">deoxycholate</a> (DXC)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli UTL2 mdfA::Kan
- **Construct**: MdfA-6His or various mutants overexpressed from multi-copy plasmids (pUC18/Para/mdfA-6His or pT7-5/mdfA-6His) under arabinose-inducible promoter

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
      <td>Cell growth and membrane preparation</td>
      <td>E. coli cells grown at 37 C, diluted and induced with 0.2% arabinose for 18 h at 16 C. Cells disrupted by pressure cell homogenizer at 15 kPsi. Membranes collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 167,000g for 1 h.</td>
      <td>--</td>
      <td>50 mM KPi pH 7.3, 2 mM MgSO4, 10 ug/mL <a href="/xray-mp-wiki/reagents/additives/dnase/">DNase</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a> + --</td>
      <td>Membranes resuspended in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.5 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> and stored at -80 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membranes solubilized with 1.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (10% stock), insoluble material removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 167,000g for 30 min</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.5 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 1.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized at 4 C for 2 hr</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> using <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> beads, washed with solubilization buffer, eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> beads (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.2, 0.5 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Agitated for 2 hr at 4 C, eluted in 30 column volumes of wash buffer</td>
    </tr>
    <tr>
      <td>Dialysis and concentration</td>
      <td>Dialyzed overnight against dialysis buffer at 4 C, protein concentration determined by A280 (1 mg/mL = 2.1 A280)</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.2, 0.12 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified MdfA used for binding assays, crystallization, and MD simulations</td>
    </tr>
  </tbody>
</table>

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
      <td>MdfA(Q131R/L339E) purification for crystallization</td>
      <td>Membranes solubilized with 0.5% DM (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>), <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a>, <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> on <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/30 column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> beads (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 0.5 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.2% DM, 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + 0.2% DM (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Concentrated to 10 mg/mL before <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/30 column pre-equilibrated with <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/30 (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>, 1.2 mM sodium <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">deoxycholate</a> (omitted in some experiments), 0.2-0.4% n-nonyl-beta-D-glucopyranoside (Anatrace), 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (Anatrace) + 0.2-0.4% NG (n-nonyl-beta-D-glucopyranoside), 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Peak fractions pooled and concentrated to 15 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6euq">6EUQ</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNKLASGARLGRQ</span><span class="topo-inside">ALLFPLC</span><span class="topo-membrane">LVLYEFSTYIGNDMIQPG</span><span class="topo-outside">MLAVVEQYQAGIDWVP</span><span class="topo-membrane">TSMTAYLAGGMFLQW</span><span class="topo-inside">LLGPLSDRIGRRPVML</span><span class="topo-membrane">AGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-inside">GAVGYAAIRESFEEAVCIKITAL</span><span class="topo-membrane">MANVALIAPLLGPLVGAAW</span><span class="topo-outside">I</span><span class="topo-unknown">H</span><span class="topo-outside">VLPW</span><span class="topo-membrane">EGMFVLFAALAAISFF</span><span class="topo-inside">GLQRAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVL</span><span class="topo-inside">KNGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">QS</span><span class="topo-outside">PIIIITGEQLSSYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLL</span><span class="topo-inside">ARLTSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVAA</span><span class="topo-outside">AATVISSHAYLWM</span><span class="topo-membrane">TAGLSIYAFGIGLANA</span><span class="topo-inside">GLVRLTEFASDMSKGTVSAA</span><span class="topo-membrane">MGMLQMLI</span></span>
<span class="topo-ruler">       370       380       390       400       410         </span>
<span class="topo-line"><span class="topo-membrane">FTVGIEISK</span><span class="topo-outside">HAWLNGGNGLF</span><span class="topo-membrane">NLFNLVNGILWLSLMVI</span><span class="topo-inside">FLK</span><span class="topo-unknown">DKQMGNSHEGASTHHHHHH</span></span>
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
      <td>15</td>
      <td>21</td>
      <td>15</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>39</td>
      <td>22</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>55</td>
      <td>40</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>70</td>
      <td>56</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>71</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>106</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>122</td>
      <td>107</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>145</td>
      <td>123</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>164</td>
      <td>146</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>165</td>
      <td>165</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>166</td>
      <td>166</td>
      <td>166</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>170</td>
      <td>167</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>186</td>
      <td>171</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>204</td>
      <td>187</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>216</td>
      <td>205</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>217</td>
      <td>222</td>
      <td>217</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>242</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>258</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>287</td>
      <td>276</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>303</td>
      <td>288</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>316</td>
      <td>304</td>
      <td>316</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>352</td>
      <td>333</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>369</td>
      <td>353</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>380</td>
      <td>370</td>
      <td>380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>397</td>
      <td>381</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>400</td>
      <td>398</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##cr.2015.94

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zp0">4ZP0</a></td>
      <td>2.0 A</td>
      <td>P212121</td>
      <td>MdfA(Q131R) mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag</td>
      <td><a href="/xray-mp-wiki/reagents/additives/deoxycholate/">deoxycholate</a> (DXC)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zow">4ZOW</a></td>
      <td>2.4 A</td>
      <td>P212121</td>
      <td>MdfA(Q131R) mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">chloramphenicol</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zp2">4ZP2</a></td>
      <td>2.2 A</td>
      <td>P212121</td>
      <td>MdfA(Q131R) mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli UTL2 mdfA::Kan
- **Construct**: MdfA-6His or various mutants overexpressed from multi-copy plasmids (pUC18/Para/mdfA-6His or pT7-5/mdfA-6His) under arabinose-inducible promoter

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
      <td>Expression and membrane preparation</td>
      <td>Full-length MdfA gene cloned from E. coli BL21(DE3) genome. Overexpressed in E. coli C43 (DE3) with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6</a> tag, induced with 0.5 mM <a href="/xray-mp-wiki/methods/expression-systems/iptg-induction/">IPTG</a> at OD600 0.8, grown at 16 C for 18 h. Cells homogenized at 10,000-15,000 p.s.i., membrane fraction collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 100,000g for 1 h.</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a> + --</td>
      <td>Incidental Q131R mutation introduced during cloning; considered WT</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane fraction solubilized with 0.5% DM for 2 h at 4 C, clarified by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 100,000g for 30 min</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>, 0.5% DM + 0.5% DM (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Solubilized at 4 C for 2 hr</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity resin, washed with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, eluted with 350 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>, 0.2% DM, 350 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + 0.2% DM</td>
      <td>Concentrated to 10-15 mg/mL</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/30 column pre-equilibrated with <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> 10/30 (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>, 1.2 mM sodium <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">deoxycholate</a>, 0.2% n-nonyl-beta-D-glucopyranoside, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> + 0.2% NG (n-nonyl-beta-D-glucopyranoside), 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Peak fractions pooled and concentrated to 15 mg/mL before crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>15 mg/mL MdfA(Q131R) in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-mercaptoethanol</a>, 1.2 mM sodium <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">deoxycholate</a>, 0.2% NG, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">sodium acetate</a> pH 5.8, 20-24% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a>, 10 mM praseodymium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer</a>, 50 mM magnesium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>16 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>About 3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 20 x 20 x 50 um in about 3 days. Se-Met derivative crystals grown under same conditions. Cm-containing crystals obtained by <a href="/xray-mp-wiki/methods/crystallography/soaking/">soaking</a> original crystals in reservoir solution supplemented with 5.0 mM <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">chloramphenicol</a>. <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>-bound structure obtained when crystallization pH was adjusted from 5.8 to 8.5. PDB 4ZOW (Cm complex, 2.4 A), 4ZP0 (Dxc complex, 2.0 A), 4ZP2 (<a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> complex, 2.2 A). Phases obtained by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a>.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zp0">4ZP0</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ARLGRQALLFP</span><span class="topo-membrane">LCLVLYEFSTYIGNDMIQPGM</span><span class="topo-outside">LAVVEQYQAGIDWV</span><span class="topo-membrane">PTSMTAYLAGGMFLQWLLG</span><span class="topo-inside">PLSDRIGRRP</span><span class="topo-membrane">VMLAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLCFIGAVG</span><span class="topo-inside">YA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIRESFEEAVCIKITA</span><span class="topo-membrane">LMANVALIAPLLGPLVGAAWI</span><span class="topo-outside">HVLPW</span><span class="topo-membrane">EGMFVLFAALAAISFFGLQR</span><span class="topo-inside">AMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVL</span><span class="topo-inside">KNGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWIAQSP</span><span class="topo-outside">IIIIT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GEQLSSY</span><span class="topo-membrane">EYGLLQVPIFGALIAGNLLL</span><span class="topo-inside">ARLTSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVAAAATV</span><span class="topo-outside">ISSHAY</span><span class="topo-membrane">LWMTAGLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVS</span><span class="topo-membrane">AAMGMLQMLIFTVGIEIS</span></span>
<span class="topo-ruler">       370       380       390  </span>
<span class="topo-line"><span class="topo-membrane">KHAW</span><span class="topo-outside">LNGGN</span><span class="topo-membrane">GLFNLFNLVNGILWLSLMVIF</span><span class="topo-inside">LK</span></span>
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
      <td>1</td>
      <td>11</td>
      <td>9</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>32</td>
      <td>20</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>41</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>65</td>
      <td>55</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>75</td>
      <td>74</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>94</td>
      <td>84</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>98</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>118</td>
      <td>107</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>136</td>
      <td>127</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>145</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>162</td>
      <td>166</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>171</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>191</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>208</td>
      <td>205</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>209</td>
      <td>214</td>
      <td>217</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>235</td>
      <td>223</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>247</td>
      <td>244</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>267</td>
      <td>256</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>279</td>
      <td>276</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>299</td>
      <td>288</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>305</td>
      <td>308</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>327</td>
      <td>314</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>342</td>
      <td>336</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>364</td>
      <td>351</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>369</td>
      <td>373</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>390</td>
      <td>378</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>392</td>
      <td>399</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zow">4ZOW</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">RLGRQALLFPL</span><span class="topo-membrane">CLVLYEFSTYIGNDMIQPGM</span><span class="topo-outside">LAVVEQYQAGIDWV</span><span class="topo-membrane">PTSMTAYLAGGMFLQWLL</span><span class="topo-inside">GPLSDRIGRRP</span><span class="topo-membrane">VMLAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLCFIGAVG</span><span class="topo-inside">YAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRESFEEAVCIKITA</span><span class="topo-membrane">LMANVALIAPLLGPLVGAAW</span><span class="topo-outside">IHVLPW</span><span class="topo-membrane">EGMFVLFAALAAISFFGLQ</span><span class="topo-inside">RAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLV</span><span class="topo-inside">LKNGRF</span><span class="topo-membrane">VAGALALGFVSLPLLAWIAQS</span><span class="topo-outside">PIIIITG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">EQLSSYEY</span><span class="topo-membrane">GLLQVPIFGALIAGNLLLA</span><span class="topo-inside">RLTSRRTVRSL</span><span class="topo-membrane">IIMGGWPIMIGLLVAAAA</span><span class="topo-outside">TVISSHAYL</span><span class="topo-membrane">WMTAGLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVS</span><span class="topo-membrane">AAMGMLQMLIFTVGIEISK</span></span>
<span class="topo-ruler">       370       380       390 </span>
<span class="topo-line"><span class="topo-outside">HAWLNGGNGL</span><span class="topo-membrane">FNLFNLVNGILWLSLMVIF</span><span class="topo-inside">LK</span></span>
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
      <td>1</td>
      <td>11</td>
      <td>10</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>21</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>41</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>55</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>73</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>93</td>
      <td>84</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>98</td>
      <td>103</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>117</td>
      <td>108</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>135</td>
      <td>127</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>145</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>161</td>
      <td>165</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>180</td>
      <td>171</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>190</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>206</td>
      <td>205</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>207</td>
      <td>212</td>
      <td>216</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>233</td>
      <td>222</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>248</td>
      <td>243</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>267</td>
      <td>258</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>268</td>
      <td>278</td>
      <td>277</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>296</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>305</td>
      <td>306</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>326</td>
      <td>315</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>341</td>
      <td>336</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>360</td>
      <td>351</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>370</td>
      <td>370</td>
      <td>379</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>389</td>
      <td>380</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>391</td>
      <td>399</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zp2">4ZP2</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ARLGRQALLFP</span><span class="topo-membrane">LCLVLYEFSTYIGNDMIQPGM</span><span class="topo-outside">LAVVEQYQAGIDWV</span><span class="topo-membrane">PTSMTAYLAGGMFLQWLL</span><span class="topo-inside">GPLSDRIGRRP</span><span class="topo-membrane">VMLAGVVWFIVTCLAILLA</span><span class="topo-outside">QNIE</span><span class="topo-membrane">QFTLLRFLQGISLCFIGAVG</span><span class="topo-inside">YA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AIRESFEEAVCIKIT</span><span class="topo-membrane">ALMANVALIAPLLGPLVGAAW</span><span class="topo-outside">IHVLPW</span><span class="topo-membrane">EGMFVLFAALAAISFFGLQ</span><span class="topo-inside">RAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLV</span><span class="topo-inside">LKNGRFV</span><span class="topo-membrane">AGALALGFVSLPLLAWIAQS</span><span class="topo-outside">PIIIIT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GEQLSSYEYG</span><span class="topo-membrane">LLQVPIFGALIAGNLLLAR</span><span class="topo-inside">LTSRRTVRS</span><span class="topo-membrane">LIIMGGWPIMIGLLVAAAA</span><span class="topo-outside">TVISSHAYL</span><span class="topo-membrane">WMTAGLSIYAFGIGLANAGLV</span><span class="topo-inside">RLTLFASDMSKGTVS</span><span class="topo-membrane">AAMGMLQMLIFTVGIEIS</span></span>
<span class="topo-ruler">       370       380       390  </span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-outside">HAWLNGGNGL</span><span class="topo-membrane">FNLFNLVNGILWLSLMVIF</span><span class="topo-inside">LK</span></span>
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
      <td>1</td>
      <td>11</td>
      <td>9</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>32</td>
      <td>20</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>41</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>64</td>
      <td>55</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>75</td>
      <td>73</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>94</td>
      <td>84</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>98</td>
      <td>103</td>
      <td>106</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>118</td>
      <td>107</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>135</td>
      <td>127</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>156</td>
      <td>144</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>162</td>
      <td>165</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>171</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>196</td>
      <td>190</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>205</td>
      <td>215</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>208</td>
      <td>214</td>
      <td>216</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>250</td>
      <td>243</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>269</td>
      <td>259</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>278</td>
      <td>278</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>287</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>306</td>
      <td>306</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>307</td>
      <td>327</td>
      <td>315</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>342</td>
      <td>336</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>361</td>
      <td>351</td>
      <td>369</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>362</td>
      <td>371</td>
      <td>370</td>
      <td>379</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>390</td>
      <td>380</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>392</td>
      <td>399</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-018-06306-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gv1">6GV1</a></td>
      <td>3.4 A</td>
      <td>P6_1_22</td>
      <td>MdfA WT in complex with Fab YN1074 (stabilizing antibody fragment), <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag</td>
      <td>none (outward open, substrate-free state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli UTL2 mdfA::Kan
- **Construct**: MdfA-6His or various mutants overexpressed from multi-copy plasmids (pUC18/Para/mdfA-6His or pT7-5/mdfA-6His) under arabinose-inducible promoter

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gv1">6GV1</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNKLASGARLGR</span><span class="topo-outside">QALLFP</span><span class="topo-membrane">LCLVLYEFSTYIGNDMI</span><span class="topo-inside">QPGM</span><span class="topo-unknown">LAVVEQ</span><span class="topo-inside">YQAGIDWVPTS</span><span class="topo-membrane">MTAYLAGGMFLQWLLG</span><span class="topo-outside">PLSDRIGRRPV</span><span class="topo-membrane">MLAGVVWFIVTCLAILLA</span><span class="topo-inside">QNIEQ</span><span class="topo-membrane">FTLLRFLQGISLC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FIGAVGY</span><span class="topo-outside">AAIQESFEEAVCI</span><span class="topo-membrane">KITALMANVALIAPLLGPLVG</span><span class="topo-unknown">AAWIHV</span><span class="topo-inside">LPW</span><span class="topo-membrane">EGMFVLFAALAAISFFG</span><span class="topo-outside">LQRAMPETATRIGEKLS</span><span class="topo-unknown">LKELGRDYKLVLK</span><span class="topo-outside">NG</span><span class="topo-membrane">RFVAGALALGFVSLPLLAWIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QSPIIIITGEQLSSYEYGLLQ</span><span class="topo-membrane">VPIFGALIAGNLLLARL</span><span class="topo-outside">TSRRTVRS</span><span class="topo-membrane">LIIMGGWPIMIGLLVAAA</span><span class="topo-inside">ATVISSHAYLWMT</span><span class="topo-membrane">AGLSIYAFGIGLANAGLVR</span><span class="topo-outside">LTLFASDMSKGT</span><span class="topo-membrane">VSAAMGMLQMLI</span></span>
<span class="topo-ruler">       370       380       390       400       410</span>
<span class="topo-line"><span class="topo-membrane">FTVGIEIS</span><span class="topo-inside">KHAWLNGGNGLFN</span><span class="topo-membrane">LFNLVNGILWLSLMVIF</span><span class="topo-outside">LK</span><span class="topo-unknown">DKQMGNSHEG</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>19</td>
      <td>14</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>36</td>
      <td>20</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>40</td>
      <td>37</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>46</td>
      <td>41</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>57</td>
      <td>47</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>73</td>
      <td>58</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>102</td>
      <td>85</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>107</td>
      <td>103</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>127</td>
      <td>108</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>140</td>
      <td>128</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>167</td>
      <td>162</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>170</td>
      <td>168</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>187</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>204</td>
      <td>188</td>
      <td>204</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>217</td>
      <td>205</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>219</td>
      <td>218</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>240</td>
      <td>220</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>261</td>
      <td>241</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>278</td>
      <td>262</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>286</td>
      <td>279</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>304</td>
      <td>287</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>317</td>
      <td>305</td>
      <td>317</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>336</td>
      <td>318</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>348</td>
      <td>337</td>
      <td>348</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>368</td>
      <td>349</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>381</td>
      <td>369</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>398</td>
      <td>382</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>400</td>
      <td>399</td>
      <td>400</td>
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

### Substrate-binding mode in MFS antiporters

The crystal structures of MdfA in complex with three distinct ligands ([chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/),
[deoxycholate](/xray-mp-wiki/reagents/additives/deoxycholate/), and [LDAO](/xray-mp-wiki/reagents/detergents/ldao/)) reveal the substrate-binding mode of an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporter. The
substrate-binding site sits proximal to the conserved acidic residue D34. Twelve amino
acid residues form the binding cavity, with over two-thirds being hydrophobic. Key
residues Y30, N33, and D34 from motif-D form [hydrogen bonds](/xray-mp-wiki/concepts/hydrogen-bonding/) with [chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/).
D34 directly interacts with the substrate while E26 is not directly involved in binding.
The binding of hydrophobic substrates reduces the dielectric constant inside the cavity,
enhancing the electrostatic field and affecting protonation status.

### Protonation and substrate binding competition

In antiporters, substrate binding and protonation compete with each other. MdfA has
two proton-titratable residues in the central cavity: E26 and D34. D34 is directly
involved in substrate binding while E26 is over 8 A away. Substrate binding induces
deprotonation of D34, triggering the Cin-to-Cout [conformational change](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/). Motif-B
(R112xxQG) generates a positive electrostatic field that promotes deprotonation of
D34 in the Cin state. A proton-wire mechanism involving conserved Y30 may facilitate
proton transfer between E26 and D34.

### Conformational changes upon substrate binding

[smFRET](/xray-mp-wiki/methods/biophysical/smfret/) imaging revealed that Cm binding induces closure of the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) side of
MdfA, shifting the conformation to the Cin state. Mutations in motif-C (P154A,
P158A) destabilize the Cin state and favor the Cout conformation. Motif-C specifically
evolved to stabilize the hydrophobic inter-domain interaction of [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporters in
the Cin state. The proline residues in motif-C introduce kinks in the TM helix and
participate in water-mediated interactions at the inter-domain interface.

### Outward open conformation and TM5 switching mechanism

The crystal structure of MdfA in the outward open (Oo) conformation (PDB 6GV1, 3.4 A, P6_1_22), trapped by Fab YN1074, reveals the transporter with the N- and C-lobes closely apposed at the intracellular face, sealing off the cytoplasmic entrance via a hydrophobic plug centered around Phe340(TM10). Comparison with the inward-facing (If) state shows the two lobes rotate as rigid bodies by 33.5 degrees about an axis parallel to the membrane. TM5 undergoes a dramatic conformational change: a 15-degree kink and ca. 45-degree clockwise twist, driven by the antiporter motif C (AlaProXaaXaaGlyPro) that is absent in symporters and uniporters. Critical residue Met146(TM5) disengages from the N-terminal domain and engages the C-terminal domain in the Oo state, while Tyr127(TM4) shifts to form a hydrogen bond with Glu26(TM1). MD simulations suggest that protonation of Asp34(TM1) triggers transition from Oo to an occluded state, while Glu26 protonation is not rate-limiting for chloramphenicol transport. These findings establish MdfA as a model system for understanding conformational switching in MFS MDR antiporters.

### Conserved motifs in MFS antiporters

Four motifs (A-D) are conserved in [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) antiporters. Motif-A stabilizes the Cout
state. Motif-B (R112xxQG in TM4) contains an essential basic residue that generates
a positive electrostatic field promoting D34 deprotonation. Motif-C (the antiporter
motif in TM5) stabilizes the Cin state through inter-domain hydrophobic interactions.
Motif-D contains the two titratable acidic residues E26 and D34 essential for
transport activity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — MdfA belongs to the MFS, the largest family of bacterial drug transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — MdfA functions via alternating access between inward-facing and outward-facing states
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism in MFS Transporters</a> — MFS-specific transport mechanism used by MdfA
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/substrate-protonation-coupling/">Substrate-Protonation Coupling in MFS Symporters</a> — MdfA substrate binding induces deprotonation of D34, driving transport
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for MdfA solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Used for MdfA(Q131R) purification for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Used as crystallization additive and bound ligand in MdfA-LDAO structure (PDB 4ZP2)
- <a href="/xray-mp-wiki/reagents/additives/deoxycholate/">Deoxycholate (DXC)</a> — Bound ligand in MdfA-Dxc structure (PDB 4ZP0) and used in SEC buffer
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Entity mentioned in text
