---
title: "PglB (Campylobacter lari Oligosaccharyltransferase)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10151, doi/10.1038##nsmb.3491, doi/10.1038##s41598-018-34534-0]
verified: false
---

# PglB (Campylobacter lari Oligosaccharyltransferase)

## Overview

PglB is a single-subunit oligosaccharyltransferase (OST) from the Gram-negative pathogenic bacterium Campylobacter lari, a model system for studying N-linked protein glycosylation. OST catalyzes the transfer of glycans from lipid-linked oligosaccharides (LLOs) onto asparagine side chains within N-X-(S/T) sequons, the first step in protein N-glycosylation. The first X-ray structure of a bacterial OST was determined for PglB at 3.4 A resolution (Nature 2011), revealing a 13-transmembrane-helix architecture with a C-terminal periplasmic domain. A subsequent higher-resolution structure (NSMB 2017) trapped PglB in a ternary complex bound simultaneously to an acceptor peptide (DQNATF) and a nonhydrolyzable synthetic LLO analog ((omega ZZZ)-PPC-GlcNAc) at 2.7 A resolution, revealing the critical role of external loop EL5 in substrate recognition. This work defines the chemistry of a key intermediate in the OST reaction mechanism and provides opportunities for glycoengineering through rational design of PglB. A subsequent structure (Sci Rep 2018) captured PglB bound to a reactive LLO analog and an inhibitory Dab-containing peptide, revealing a conformation closer to the transition state with the substrates ~3.4 A apart and direct coordination of the LLO pyrophosphate by the catalytic Mn2+ ion, identifying D56 as a key residue in the hydrogen bonding network.


## Publications

### doi/10.1038##nature10151

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rce">3RCE</a></td>
      <td>3.4</td>
      <td>P212121</td>
      <td>Full-length PglB from C. lari with C-terminal His tag</td>
      <td>Acceptor peptide DQNATF</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold (DE3)
- **Construct**: Cysteineless PglB optimized for crystallization with multiple lattice-contact mutations. Grown in Terrific Broth with 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), induced with 0.1% arabinose at 37 C for 4 h at A600 of 3.0.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PglB at ~5 mg/ml in 10 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 100 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, cocrystallized with acceptor peptide DQNATF</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 0.2 M NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 3.4 A resolution, space group P212121. <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD phasing</a> using <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">selenomethionine</a> derivative. R_work = 23.8%, R_free = 27.1%.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rce">3RCE</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ELQQNFTDNNSIKYT</span><span class="topo-membrane">CILILIAFAFSVLC</span><span class="topo-inside">RLYWVAWASEFYEFFFNDQLMITTNDGYAF</span></span>
<span class="topo-line"><span class="topo-inside">AEGARDMIAGFHQPNDLSYFGS</span><span class="topo-unknown">SLSTLTYWLYS</span><span class="topo-inside">ILPFSFESIILYMSTF</span><span class="topo-membrane">FASLIVVPIIL</span></span>
<span class="topo-line"><span class="topo-membrane">IAR</span><span class="topo-outside">EYKLT</span><span class="topo-membrane">TYGFIAALLGSIA</span><span class="topo-inside">NSYYNRTMSGYYDTDML</span><span class="topo-membrane">VLVLPMLILLTFIRL</span><span class="topo-outside">TINKDIF</span></span>
<span class="topo-line"><span class="topo-membrane">TLLLSPIFIMIYLWW</span><span class="topo-inside">YPSS</span><span class="topo-membrane">YSLNFAMIGLFGLYTL</span><span class="topo-outside">VFHRKEKIF</span><span class="topo-membrane">YLAIALMIIALSMLA</span><span class="topo-inside">W</span></span>
<span class="topo-line"><span class="topo-membrane">QYKLALIVLLF</span><span class="topo-outside">AIFAFKEEKINFYMI</span><span class="topo-membrane">WALIFISISILHLSGG</span><span class="topo-unknown">LDPVLYQLKFYVFKASDV</span></span>
<span class="topo-line"><span class="topo-unknown">QNLKDA</span><span class="topo-inside">AFMYFNVNETIMEVNTID</span><span class="topo-unknown">PEVFMQRI</span><span class="topo-membrane">SSSVLVFILSFIGFILLCK</span><span class="topo-outside">DHK</span><span class="topo-membrane">SMLLAL</span></span>
<span class="topo-line"><span class="topo-membrane">PMLALGF</span><span class="topo-inside">MALRAGLRFTI</span><span class="topo-membrane">YAVPVMALGFGYFLYAF</span><span class="topo-outside">FNFLEKKQIKLSLRNKN</span><span class="topo-membrane">ILLILIAF</span></span>
<span class="topo-line"><span class="topo-membrane">FSISPAL</span><span class="topo-inside">MHIYYYKSSTVFTSYEASILNDLKNKAQREDYVVAWWDYGYPIRYYSDVKTLI</span></span>
<span class="topo-line"><span class="topo-inside">DGGKHLGKDNFFSSFVLSKEQIPAANMARLSVEYTEKSFKENYPDVLKAMVKDYNQTSAK</span></span>
<span class="topo-line"><span class="topo-inside">DFLESLNDKNFKFDTNKTRDVYIYMPYRMLRIMPVVAQFANTNPDNGEQEKSLFFSQANA</span></span>
<span class="topo-line"><span class="topo-inside">IAQD</span><span class="topo-unknown">KTT</span><span class="topo-inside">GSVMLDNGVEIINDFRALKVEGASIPLKAFVDIESITNGKFYYNEIDSKAQIY</span></span>
<span class="topo-line"><span class="topo-inside">LLFLREYKSFVILDESLYNSAYIQMFLLNQYDQDLFEQVTNDTRAKIYRLK</span><span class="topo-unknown">REFHHHHHH</span></span>
<span class="topo-line"><span class="topo-unknown">HHHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>16</td>
      <td>2</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>30</td>
      <td>17</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>82</td>
      <td>31</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>93</td>
      <td>83</td>
      <td>93</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>94</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>123</td>
      <td>110</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>128</td>
      <td>124</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>141</td>
      <td>129</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>158</td>
      <td>142</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>173</td>
      <td>159</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>180</td>
      <td>174</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>181</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>199</td>
      <td>196</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>200</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>224</td>
      <td>216</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>239</td>
      <td>225</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>240</td>
      <td>240</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>251</td>
      <td>241</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>266</td>
      <td>252</td>
      <td>266</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>267</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>306</td>
      <td>283</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>324</td>
      <td>307</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>332</td>
      <td>325</td>
      <td>332</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>351</td>
      <td>333</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>354</td>
      <td>352</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>367</td>
      <td>355</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>378</td>
      <td>368</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>395</td>
      <td>379</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>412</td>
      <td>396</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>427</td>
      <td>413</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>604</td>
      <td>428</td>
      <td>604</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>605</td>
      <td>607</td>
      <td>605</td>
      <td>607</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>608</td>
      <td>711</td>
      <td>608</td>
      <td>711</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>712</td>
      <td>724</td>
      <td>712</td>
      <td>724</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.3491

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ogl">5OGL</a></td>
      <td>2.7</td>
      <td>P212121</td>
      <td>Sequence-optimized PglB variant from C. lari with mutations K2E, C17A, C30A, A108T, C360L, N535Q, Q536K, K549P, D550N, F553I, N556P, A600P, A602D, T606K, T607Q, V610I, M611T, I619S, F622Y, A624S, V627I, A630N, F663Y, F670Y; cysteineless, removed glycosylation sites</td>
      <td>Acceptor peptide DQNATF and synthetic LLO analog (omega ZZZ)-PPC-GlcNAc</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold (DE3)
- **Construct**: Cysteineless PglB optimized for crystallization with multiple lattice-contact mutations. Grown in Terrific Broth with 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), induced with 0.1% arabinose at 37 C for 4 h at A600 of 3.0.

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
      <td>Cell resuspension and lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">Microfluidizer</a> disruption at 15,000 psi</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 250 mM NaCl + --</td>
      <td>Cells disrupted at 15,000 psi chamber pressure; membranes pelleted by centrifugation at 100,000g for 30 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 250 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + 1% N-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, Anatrace)</td>
      <td>Membranes solubilized for 1.5 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity purification</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Superflow</a> column (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 250 mM NaCl, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Purified on <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> column</td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>Desalting</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.5, 100 mM NaCl, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Desalted for crystallization experiments</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultrafiltration/">Ultrafiltration</a></td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.5, 100 mM NaCl, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Concentrated to 6 mg/ml using Amicon Ultra-15 concentrator (100 kDa MWCO)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Superdex 200</a> 10/300 column (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.5, 100 mM NaCl, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Concentrated to 12 mg/ml after <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in this paper</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PglB at 12 mg/ml in 10 mM <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.5, 100 mM NaCl, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 0.016% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, cocrystallized with peptide DQNATF and LLO analog (omega ZZZ)-PPC-GlcNAc</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 2.7-A resolution, space group P212121. SAD or <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> not specified.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ogl">5OGL</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ELQQNFTDNNSIKY</span><span class="topo-membrane">TAILILIAFAFSVLARL</span><span class="topo-inside">YWVAWASEFYEFFFNDQLMITTNDGYAF</span></span>
<span class="topo-line"><span class="topo-inside">AEGARDMIAGFHQPNDLSYFGS</span><span class="topo-unknown">SLSTLTYWLYSI</span><span class="topo-inside">LPFSFESIILYMST</span><span class="topo-membrane">FFASLIVVPIIL</span></span>
<span class="topo-line"><span class="topo-membrane">IAREY</span><span class="topo-outside">KL</span><span class="topo-membrane">TTYGFIAALLGSIANSYY</span><span class="topo-inside">NRTMSGYYDTDM</span><span class="topo-membrane">LVLVLPMLILLTFIRLT</span><span class="topo-outside">INKD</span><span class="topo-membrane">IF</span></span>
<span class="topo-line"><span class="topo-membrane">TLLLSPVFIMIYLWW</span><span class="topo-inside">YPSS</span><span class="topo-membrane">YSLNFAMIGLFGLYTLVF</span><span class="topo-outside">HRKEK</span><span class="topo-membrane">IFYLTIALMIIALSML</span><span class="topo-inside">A</span><span class="topo-membrane">W</span></span>
<span class="topo-line"><span class="topo-membrane">QYKLALIVLLFAIF</span><span class="topo-outside">AFKEEKINF</span><span class="topo-membrane">YMIWALIFISILILHLS</span><span class="topo-inside">GGLDPVLYQLKFYVFKASDV</span></span>
<span class="topo-line"><span class="topo-inside">QNLKDAAFMYFNVNETIMEVNTIDPEVF</span><span class="topo-membrane">MQRISSSVLVFILSFIGFILLLK</span><span class="topo-outside">DH</span><span class="topo-membrane">KSMLLAL</span></span>
<span class="topo-line"><span class="topo-membrane">PMLALGFM</span><span class="topo-inside">ALRAGLRFT</span><span class="topo-membrane">IYAVPVMALGFGYFLYAF</span><span class="topo-outside">FNFLEKKQIKLSLRNKN</span><span class="topo-membrane">ILLILIAF</span></span>
<span class="topo-line"><span class="topo-membrane">FSISPALM</span><span class="topo-inside">HIYYYKSSTVFTSYEASILNDLKNKAQREDYVVAWWDYGYPIRYYSDVKTLI</span></span>
<span class="topo-line"><span class="topo-inside">DGGKHLGKDNFFSSFVLSKEQIPAANMARLSVEYTEKSFKENYPDVLKAMVKDYQKTSAK</span></span>
<span class="topo-line"><span class="topo-inside">DFLESLNDPNFKIDTPKTRDVYIYMPYRMLRIMPVVAQFANTNPDNGEQEKSLFFSQANP</span></span>
<span class="topo-line"><span class="topo-inside">LDQD</span><span class="topo-unknown">KKQ</span><span class="topo-inside">GSITLDNGVEISNDYRSLKIEGNSIPLKAFVDIESITNGKFYYNEIDSKAQIY</span></span>
<span class="topo-line"><span class="topo-inside">LLYLREYKSYVILDESLYNSSYIQMFLLNQYDQDLFEQITNDTRAKIYRLK</span><span class="topo-unknown">RE</span></span>
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
      <td>2</td>
      <td>15</td>
      <td>2</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>82</td>
      <td>33</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>94</td>
      <td>83</td>
      <td>94</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>95</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>125</td>
      <td>109</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>127</td>
      <td>126</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>145</td>
      <td>128</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>157</td>
      <td>146</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>178</td>
      <td>175</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>179</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>199</td>
      <td>196</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>200</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>222</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>238</td>
      <td>223</td>
      <td>238</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>239</td>
      <td>239</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>254</td>
      <td>240</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>263</td>
      <td>255</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>328</td>
      <td>281</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>351</td>
      <td>329</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>353</td>
      <td>352</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>368</td>
      <td>354</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>377</td>
      <td>369</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>395</td>
      <td>378</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>412</td>
      <td>396</td>
      <td>412</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>428</td>
      <td>413</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>604</td>
      <td>429</td>
      <td>604</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>608</td>
      <td>711</td>
      <td>608</td>
      <td>711</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41598-018-34534-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gxc">6GXC</a></td>
      <td>3.4</td>
      <td>P212121</td>
      <td>Cysteineless PglB variant from C. lari (sequence optimized, same construct as 5OGL)</td>
      <td>Reactive LLO analog (nerylneryl-PP-GlcNAc) and inhibitory Dab-containing peptide Ac-DQ(Dab)ATF(p-NO2)-NH2</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold (DE3)
- **Construct**: Cysteineless PglB optimized for crystallization with multiple lattice-contact mutations. Grown in Terrific Broth with 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), induced with 0.1% arabinose at 37 C for 4 h at A600 of 3.0.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (<a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging drop</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PglB at 12 mg/ml with 0.75 mM Ac-DQ(Dab)ATF(p-NO2)-NH2, 1.5 mM nerylneryl-PP-GlcNAc, 2 mM MnCl2</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine Buffer</a> pH 9.4, 50-200 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-acetate">Magnesium Acetate</a>, 27-31% <a href="/xray-mp-wiki/reagents/additives/peg-400">PEG400</a></td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>2:1 protein-to-reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10-14 days to appear, 3-4 weeks to full size</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise addition of <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>400 to 30% final, flash frozen in liquid N2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 3.4-A resolution, space group P212121. Data collected at SLS X06SA beamline at 1.000 A. R_work = 0.249, R_free = 0.283. PDB ID not available in raw text.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gxc">6GXC</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ELQQNFTDNNSIK</span><span class="topo-membrane">YTAILILIAFAFSVLARL</span><span class="topo-inside">YWVAWASEFYEFFFNDQLMITTNDGYAF</span></span>
<span class="topo-line"><span class="topo-inside">AEGARDMIAGFHQPNDLSYFGS</span><span class="topo-unknown">SLSTLTYWLYSI</span><span class="topo-inside">LPFSFESIILYMST</span><span class="topo-membrane">FFASLIVVPIIL</span></span>
<span class="topo-line"><span class="topo-membrane">IARE</span><span class="topo-outside">YKLT</span><span class="topo-membrane">TYGFIAALLGSIANSYY</span><span class="topo-inside">NRTMSGYYDTDM</span><span class="topo-membrane">LVLVLPMLILLTFIRLT</span><span class="topo-outside">INKD</span><span class="topo-membrane">IF</span></span>
<span class="topo-line"><span class="topo-membrane">TLLLSPVFIMIYL</span><span class="topo-inside">WWYPSS</span><span class="topo-membrane">YSLNFAMIGLFGLYTLV</span><span class="topo-outside">FHRKEK</span><span class="topo-membrane">IFYLTIALMIIALS</span><span class="topo-inside">ML</span><span class="topo-membrane">AW</span></span>
<span class="topo-line"><span class="topo-membrane">QYKLALIVLLFAIFA</span><span class="topo-outside">FKEEKI</span><span class="topo-membrane">NFYMIWALIFISILILH</span><span class="topo-inside">LSGGL</span><span class="topo-unknown">DPVLYQLKFY</span><span class="topo-inside">VFKASDV</span></span>
<span class="topo-line"><span class="topo-inside">QNLKDAAFMYFNVNETIMEVNTIDP</span><span class="topo-membrane">EVFMQRISSSVLVFILSFIGFILLL</span><span class="topo-outside">KDHK</span><span class="topo-membrane">SMLLAL</span></span>
<span class="topo-line"><span class="topo-membrane">PMLALGFMAL</span><span class="topo-inside">RAGLRF</span><span class="topo-membrane">TIYAVPVMALGFGYFL</span><span class="topo-outside">YAFFNFLEKKQIKLSLRNKNIL</span><span class="topo-membrane">LILIAF</span></span>
<span class="topo-line"><span class="topo-membrane">FSISPALMHI</span><span class="topo-inside">YYYKSSTVFTSYEASILNDLKNKAQREDYVVAWWDYGYPIRYYSDVKTLI</span></span>
<span class="topo-line"><span class="topo-inside">DGGKHLGKDNFFSSFVLSKEQIPAANMARLSVEYTEKSFKENYPDVLKAMVKDYQKTSAK</span></span>
<span class="topo-line"><span class="topo-inside">DFLESLNDPNFKIDTPKTRDVYIYMPYRMLRIMPVVAQFANTNPDNGEQEKSLFFSQANP</span></span>
<span class="topo-line"><span class="topo-inside">LDQ</span><span class="topo-unknown">DKKQ</span><span class="topo-inside">GSITLDNGVEISNDYRSLKIEGNSIPLKAFVDIESITNGKFYYNEIDSKAQIY</span></span>
<span class="topo-line"><span class="topo-inside">LLYLREYKSYVILDESLYNSSYIQMFLLNQYDQDLFEQITNDTRAKIYRLK</span><span class="topo-unknown">REFHHHHHH</span></span>
<span class="topo-line"><span class="topo-unknown">HHHH</span></span>
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
      <td>2</td>
      <td>14</td>
      <td>2</td>
      <td>14</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>15</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>82</td>
      <td>33</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>94</td>
      <td>83</td>
      <td>94</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>95</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>124</td>
      <td>109</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>145</td>
      <td>129</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>157</td>
      <td>146</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>174</td>
      <td>158</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>178</td>
      <td>175</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>193</td>
      <td>179</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>199</td>
      <td>194</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>200</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>222</td>
      <td>217</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>236</td>
      <td>223</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>237</td>
      <td>238</td>
      <td>237</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>255</td>
      <td>239</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>261</td>
      <td>256</td>
      <td>261</td>
      <td>Outside</td>
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
      <td>283</td>
      <td>279</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>293</td>
      <td>284</td>
      <td>293</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>294</td>
      <td>325</td>
      <td>294</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>350</td>
      <td>326</td>
      <td>350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>354</td>
      <td>351</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>376</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>392</td>
      <td>377</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>414</td>
      <td>393</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>430</td>
      <td>415</td>
      <td>430</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>431</td>
      <td>603</td>
      <td>431</td>
      <td>603</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>608</td>
      <td>711</td>
      <td>608</td>
      <td>711</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First structure of a bacterial oligosaccharyltransferase

The 3.4 A X-ray structure of PglB from C. lari represents the first three-dimensional structure of a bacterial OST. PglB has 13 transmembrane helices and a C-terminal periplasmic globular domain. The structure reveals the architecture of the sequon-binding pocket and the catalytic site containing a bound Mn2+ ion coordinated by D56 and E319, with the catalytic mechanism involving direct SN2 attack of the asparagine side chain on the lipid-linked oligosaccharide.

### Dual function of external loop EL5 in substrate recognition (NSMB 2017)

The ternary complex structure reveals that EL5 has a dual function: the N-terminal half (N-EL5) forms an alpha-helix at the membrane boundary and binds the LLO substrate, while the C-terminal half (C-EL5) pins the acceptor peptide against the periplasmic domain. N-EL5 was previously disordered in the peptide-only structure but adopts a defined conformation upon LLO binding, suggesting that LLO binding induces ordering of this loop.

### LLO-binding site and pyrophosphate interactions (NSMB 2017)

The polypropenyl tail of LLO reaches approximately halfway across the membrane, embedded in a hydrophobic groove of the transmembrane domain. The pyrophosphate moiety forms a salt bridge with conserved residue R375 and hydrogen bonds with Y293 from N-EL5. The shortest distance between pyrophosphate oxygens and the catalytic Mn2+ ion is approximately 5 A, with no direct contact.

### Ternary complex intermediate and conformational change requirement (NSMB 2017)

The distance between the carboxamide nitrogen of the acceptor asparagine and the C1 atom of the reducing-end GlcNAc is approximately 6 A in the ternary complex structure, too long for the glycan transfer reaction. This requires a conformational change during which the LLO must shift toward the peptide. The DGGK loop imposes steric constraints during this transfer reaction.

### Transition-state-like ternary complex with reactive LLO (Sci Rep 2018)

The X-ray structure of PglB bound to a reactive LLO analog (nerylneryl-PP-GlcNAc) and an inhibitory Dab-containing peptide captured a conformation closer to the transition state of the glycosylation reaction. The distance between C-1 of GlcNAc and the -NH2 group of Dab is ~3.4 A, compared to ~6 A in the previous structure with non-hydrolyzable LLO. The pyrophosphate group of LLO directly coordinates the catalytic Mn2+ ion at a distance of ~4 A, providing direct evidence that the metal stabilizes the pyrophosphate leaving group. Residue D56 mediates a hydrogen bonding network between the reducing-end GlcNAc, the acceptor peptide, and Mn2+.

### Role of Mn2+ in activating the glycosidic oxygen (Sci Rep 2018)

The Mn2+ ion coordinates the glycosidic oxygen of LLO rather than the negatively charged phosphate oxygens, suggesting the metal may directly activate the glycosidic oxygen during the reaction by generating a reactive electrophile. This mechanism could compensate for the poor nucleophilicity of the carboxamide group of the acceptor asparagine, potentially allowing glycan transfer without amide activation.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Primary buffer (25 mM pH 8.0) for PglB resuspension and purification
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (N-Dodecyl-beta-D-maltoside)</a> — Primary solubilization detergent (1% during extraction, 0.016% during purification)
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — Used at 10 mM pH 6.5 for desalting and SEC buffers
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — 250 mM NaCl in resuspension buffer, 100 mM in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — 10% glycerol in solubilization buffer, 3% in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — MgCl2 mentioned in transport assay buffers
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Used for His-tag affinity purification of PglB
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Superdex 200 SEC used for final purification before crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
