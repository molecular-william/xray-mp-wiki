---
title: "E. coli DtpA Peptide Transporter"
created: 2026-05-29
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1021##jacs.8b11343]
verified: agent
uniprot_id: P77304
---

# E. coli DtpA Peptide Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P77304">UniProt: P77304</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

DtpA is a proton-dependent oligopeptide transporter (POT) from Escherichia coli and a member of the solute carrier 15 family (SLC15). It belongs to the major facilitator superfamily (MFS) of secondary active transporters. DtpA is notable for its high similarity to human PepT1 (SLC15A1) in ligand selectivity, transporting di- and tripeptides as well as peptidomimetic drugs including antiviral prodrugs such as [VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) and valacyclovir. Unlike most characterized bacterial POTs which prefer dipeptides, DtpA prefers tripeptides, a property attributed to a characteristic intra-helical loop in transmembrane helix 10 that enlarges its binding cavity.


## Publications

### doi/10.1021##jacs.8b11343

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gs7">6GS7</a></td>
      <td>3.30</td>
      <td>P212121</td>
      <td>Full-length DtpA from E. coli (Uniprot P77304), N- and C-terminal His6-tag, co-crystallized with conformation-selective <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">NANOBODY</a> N00</td>
      <td>None (ligand-free, <a href="/xray-mp-wiki/reagents/buffers/glycine">GLYCINE</a> buffer)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gs4">6GS4</a></td>
      <td>2.65</td>
      <td>P212121</td>
      <td>Full-length DtpA from E. coli (Uniprot P77304), N- and C-terminal His6-tag, co-crystallized with conformation-selective <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">NANOBODY</a> N00</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/valganciclovir">VALGANCICLOVIR</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length dtpA gene (Uniprot P77304) amplified from E. coli genome, cloned into pH27 vector with N- and C-terminal His6 tags
- **Notes**: Gene amplified from E. coli genome and cloned into pH27 vector. Expressed in E. coli cells. Purified using Ni-NTA affinity chromatography followed by size-exclusion chromatography.


**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length DtpA, N- and C-terminal [HIS6-TAG](/xray-mp-wiki/reagents/protein-tags/his6-tag), pH27 vector

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
      <td>Fermentation</td>
      <td>--</td>
      <td>Terrific broth (TB)</td>
      <td>DtpA expressed in E. coli</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>--</td>
      <td>Lysis buffer with protease inhibitor</td>
      <td>Membranes collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membrane fraction solubilized with n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">HIS6-TAG</a> affinity purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>HiLoad 16/600 Superdex 75 pg</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>DtpA-N00 complex formation evaluated by analytical gel filtration on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 5/150 GL</td>
    </tr>
    <tr>
      <td>Final sample</td>
      <td>Concentration</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Concentrated to 13 mg/ml using 5 kDa cut-off concentrator, flash-frozen and stored at -80C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Ligand-free DtpA-N00 in <a href="/xray-mp-wiki/reagents/buffers/glycine">GLYCINE</a> buffer. Crystals grew in 0.1 M glycine pH 9.0, 35% PEG 400, 0.15 M CaCl2. Data collected at beamline P14, PETRA III at 100 K wavelength 0.976 A. Solved by molecular replacement using ligand-free structure as search model.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>DtpA-N00 complex with <a href="/xray-mp-wiki/reagents/antibiotics/valganciclovir">VALGANCICLOVIR</a>. Drug added to DtpA solution in powder form (20 mM estimated concentration) and N00 added. Best diffracting crystals grew in 0.1 M glycine pH 9.0, 35% PEG 400, 0.15 M CaCl2, 0.02% Anapoe-C12E10. Data collected at beamline P13, PETRA III at 100 K wavelength 0.966 A. Solved by molecular replacement using ligand-free structure as search model.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gs7">6GS7</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSTANQKPTESVSLNA</span><span class="topo-inside">FKQPKAFY</span><span class="topo-membrane">LIFSIELWERFGYYGLQG</span><span class="topo-outside">IMAVYLVKQLGMSEADSITLF</span><span class="topo-membrane">SSFSALVYGLVAIGGWLG</span><span class="topo-inside">DKVLGT</span><span class="topo-membrane">KRVIMLGAIVLAIGYALVA</span><span class="topo-outside">WSGHDAGIVYM</span><span class="topo-membrane">GMA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AIAVGNGLFKANPS</span><span class="topo-inside">SLLSTCYEKNDPRLDGAFT</span><span class="topo-membrane">MYYMSVNIGSFFSMIAT</span><span class="topo-outside">PWLAAKYGWSVA</span><span class="topo-membrane">FALSVVGLLITIVNFAFC</span><span class="topo-inside">QRWVKQYGSKPDFEPINY</span><span class="topo-membrane">RNLLLTIIGVVALIAIATWLL</span><span class="topo-outside">H</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NQEV</span><span class="topo-membrane">ARMALGVVAFGIVVIFGKEAF</span><span class="topo-inside">AMKGAARRKM</span><span class="topo-membrane">IVAFILMLEAIIFFVLYSQMP</span><span class="topo-outside">TSLNFFAIRNVEHSILGLAVEPEQ</span><span class="topo-membrane">YQALNPFWIIIGSPILA</span><span class="topo-inside">AIYNKMGDTLPM</span><span class="topo-membrane">PTKFAIGMVMC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">SGAFLIL</span><span class="topo-outside">PLGAKFASDAGIVSVS</span><span class="topo-membrane">WLVASYGLQSIGELMISGLGLAMV</span><span class="topo-inside">AQLVPQRLMG</span><span class="topo-membrane">FIMGSWFLTTAGANLIGG</span><span class="topo-outside">YVAGMMAVPDNVTDPLMSLEVYGRVFLQ</span><span class="topo-membrane">IGVATAVIAVLMLLTAP</span></span>
<span class="topo-ruler">       490       500        </span>
<span class="topo-line"><span class="topo-membrane">KL</span><span class="topo-inside">HRMTQ</span><span class="topo-unknown">DDAADKAAKAAVASTHHHHHH</span></span>
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
      <td>17</td>
      <td>24</td>
      <td>17</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>42</td>
      <td>25</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>81</td>
      <td>64</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>87</td>
      <td>82</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>117</td>
      <td>107</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>170</td>
      <td>154</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>171</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>218</td>
      <td>201</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>239</td>
      <td>219</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>240</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>265</td>
      <td>245</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>275</td>
      <td>266</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>296</td>
      <td>276</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>320</td>
      <td>297</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>337</td>
      <td>321</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>349</td>
      <td>338</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>367</td>
      <td>350</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>383</td>
      <td>368</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>407</td>
      <td>384</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>417</td>
      <td>408</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>435</td>
      <td>418</td>
      <td>435</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>436</td>
      <td>463</td>
      <td>436</td>
      <td>463</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>482</td>
      <td>464</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>487</td>
      <td>483</td>
      <td>487</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gs4">6GS4</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSTANQKPTESVSLNA</span><span class="topo-inside">FKQPKAFY</span><span class="topo-membrane">LIFSIELWERFGYYGLQG</span><span class="topo-outside">IMAVYLVKQLGMSEADSITLF</span><span class="topo-membrane">SSFSALVYGLVAIGGWLG</span><span class="topo-inside">DKVLGT</span><span class="topo-membrane">KRVIMLGAIVLAIGYALVA</span><span class="topo-outside">WSGHDAGIVYM</span><span class="topo-membrane">GMA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AIAVGNGLFKANPS</span><span class="topo-inside">SLLSTCYE</span><span class="topo-unknown">KN</span><span class="topo-inside">DPRLDGAFT</span><span class="topo-membrane">MYYMSVNIGSFFSMIAT</span><span class="topo-outside">PWLAAKYGWSVA</span><span class="topo-membrane">FALSVVGLLITIVNFAFC</span><span class="topo-inside">QRWVKQYGSKPDFEPINY</span><span class="topo-membrane">RNLLLTIIGVVALIAIATWLL</span><span class="topo-outside">H</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NQEV</span><span class="topo-membrane">ARMALGVVAFGIVVIFGKEAF</span><span class="topo-inside">AMKGAARRKM</span><span class="topo-membrane">IVAFILMLEAIIFFVLYSQMP</span><span class="topo-outside">TSLNFFAIRNVEHSILGLAVEPEQ</span><span class="topo-membrane">YQALNPFWIIIGSPILAAI</span><span class="topo-inside">YN</span><span class="topo-unknown">KM</span><span class="topo-inside">GDTLPM</span><span class="topo-membrane">PTKFAIGMVMC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">SGAFLIL</span><span class="topo-outside">PLGAKFASDAGIVSVS</span><span class="topo-membrane">WLVASYGLQSIGELMISGLGLAMVA</span><span class="topo-inside">QLVPQRL</span><span class="topo-membrane">MGFIMGSWFLTTAGANLIGG</span><span class="topo-outside">YVAGMMAVPDNVTDPLMSLEVYGRVFLQ</span><span class="topo-membrane">IGVATAVIAVLMLLTAP</span></span>
<span class="topo-ruler">       490       500        </span>
<span class="topo-line"><span class="topo-membrane">KL</span><span class="topo-inside">HRMTQD</span><span class="topo-unknown">DAADKAAKAAVASTHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>17</td>
      <td>24</td>
      <td>17</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>42</td>
      <td>25</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>81</td>
      <td>64</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>87</td>
      <td>82</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>117</td>
      <td>107</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>142</td>
      <td>135</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>153</td>
      <td>145</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>170</td>
      <td>154</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>171</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>183</td>
      <td>200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>218</td>
      <td>201</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>239</td>
      <td>219</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>240</td>
      <td>244</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>265</td>
      <td>245</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>275</td>
      <td>266</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>296</td>
      <td>276</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>320</td>
      <td>297</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>339</td>
      <td>321</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>341</td>
      <td>340</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>349</td>
      <td>344</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>350</td>
      <td>367</td>
      <td>350</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>383</td>
      <td>368</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>408</td>
      <td>384</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>415</td>
      <td>409</td>
      <td>415</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>416</td>
      <td>435</td>
      <td>416</td>
      <td>435</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>436</td>
      <td>463</td>
      <td>436</td>
      <td>463</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>482</td>
      <td>464</td>
      <td>482</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>488</td>
      <td>483</td>
      <td>488</td>
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

### Tripeptide preference over dipeptides

DtpA preferentially binds and transports tripeptides over dipeptides, in contrast to most other POTs with known structures which show dipeptide preference. Tripeptide binding increased thermal stability by a median of 7.1 C compared to 2.4 C for dipeptides. The highest binding affinity by MST was for tripeptide LLA (Kd = 58 +/- 10 uM). This preference relates to the presence of an intra-helical loop in TM10, also found in PepTSo2.

### Valganciclovir binding mode

[VALGANCICLOVIR](/xray-mp-wiki/reagents/antibiotics/valganciclovir) binds in the ligand-binding site with its guanine base mimicking the N-terminal residue of a canonical peptide substrate, and its valine residue inserting into a pocket equivalent to the P2 peptide side chain binding pocket of PepTSo2. This binding mode was also modeled to apply to human PepT1 based on homology modeling. The binding cavity in DtpA is the largest among POTs with known structures, accommodating the guanine base of valganciclovir.

### TM10 intra-helical loop enlarges binding cavity

DtpA has a characteristic intra-helical loop in TM10 that shifts TM11 by 6.8 A (F424 Calpha in TM11) relative to POTs without this feature. This creates a significantly enlarged binding cavity, which appears to be an adaptation for binding and transport of larger substrates like tripeptides and drug prodrugs.

### Functional validation by mutagenesis

Five residues in the binding site (Y38, Y71, K130, N160, I399) were mutated to alanine. Binding affinities for di/tripeptides and drugs were strongly reduced and AK-AMCA uptake was abolished, confirming the location of the ligand-binding site by functional assays. Two additional mutants Y156A and F289L also abrogated uptake.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/ybgH/">E. coli YbgH Peptide Transporter</a> — Another E. coli POT family member (DtpD) with reported crystal structure
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-so/">PepT_So Oligopeptide Transporter</a> — POT family member with intra-helical loop in TM10, similar substrate preference
- <a href="/xray-mp-wiki/proteins/mfs-transporters/pept-st/">PepT_St Proton-Dependent Oligopeptide Transporter</a> — POT family member with reported crystal structure
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/pot-family/">POT Family</a> — DtpA is a member of the POT (proton-dependent oligopeptide transporter) family
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily</a> — POT family is a subfamily of MFS transporters
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for DtpA solubilization, purification, and crystallization
- <a href="/xray-mp-wiki/reagents/antibiotics/valganciclovir/">Valganciclovir</a> — Antiviral prodrug that binds to DtpA and is transported by it
- <a href="/xray-mp-wiki/reagents/antibodies/nb-at110i1/">Nb.AT110i1 Synthetic Nanobody</a> — Conformation-selective nanobody technology used for DtpA crystallization (N00)
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">NANOBODY</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/antibiotics/valganciclovir">VALGANCICLOVIR</a> — Reagent used in this study
