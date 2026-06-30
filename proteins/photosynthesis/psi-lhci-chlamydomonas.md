---
title: "PSI-LHCI supercomplex from Chlamydomonas reinhardtii"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbabio.2023.148986]
verified: false
---

# PSI-LHCI supercomplex from Chlamydomonas reinhardtii

## Overview

The photosystem I–light-harvesting complex I (PSI-LHCI) supercomplex from the green alga Chlamydomonas reinhardtii. Three distinct structures were determined by X-ray crystallography and single particle [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/), revealing a resting state of PSI-8LHCI with reduced chlorophyll content, electron donors docked in waiting positions on the luminal side, and regulatory binding partners at the stromal electron acceptor site. Binding of oxidized ferredoxin triggers a conformational change that activates the complex for electron transfer.

## Publications

### doi/10.1016##j.bbabio.2023.148986

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a></td>
      <td>3.98 A</td>
      <td>C1 (single particle cryo-EM)</td>
      <td>PSI-8LHCI Form B (<a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> resting state structure)</td>
      <td>Chlorophyll a, carotenoids, iron-sulfur clusters (Fx, Fa, Fb), unidentified stromal binding partners (sigma1, sigma2, sigma3)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a></td>
      <td>4.94 A</td>
      <td>C1 (single particle cryo-EM)</td>
      <td>PSI-8LHCI with gallium-substituted ferredoxin (Fd_Ga) Form C (<a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> active state structure)</td>
      <td>Chlorophyll a, carotenoids, iron-sulfur clusters, gallium-ferredoxin (GaFd)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a></td>
      <td>3.0 A</td>
      <td>P21 (X-ray crystal structure)</td>
      <td>PSI-8LHCI Form A (X-ray crystal structure)</td>
      <td>Chlorophyll a, carotenoids, iron-sulfur clusters (Fx, Fa, Fb)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Chlamydomonas reinhardtii (green alga)
- **Construct**: PSI-8LHCI supercomplex purified directly from thylakoid membranes

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
      <td>Thylakoid membrane isolation</td>
      <td>Cell disruption and membrane isolation</td>
      <td>--</td>
      <td>Slightly acidic buffer, pH 6.5, low ionic strength + --</td>
      <td>PSI-LHCI supercomplexes purified from thylakoid membranes of C. reinhardtii. Mild, column-free isolation procedure.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>pH 6.5 buffer + n-dodecyl-beta-D-maltopyranoside (beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilization by beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> from thylakoid membranes. Mild detergent used for preserving supercomplex integrity.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient ultracentrifugation</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient ultracentrifugation</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> gradient</td>
      <td>pH 6.5 buffer + beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purification by <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient ultracentrifugation yielded PSI-8LHCI supercomplexes suitable for crystallography and <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a>.</td>
    </tr>
    <tr>
      <td>Detergent exchange for <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a></td>
      <td>Detergent exchange</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient</td>
      <td>pH 6.5 buffer + <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a> (<a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a>)</td>
      <td>For <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> sample preparation, beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> exchanged to <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a> (<a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">GDN</a>) by second <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient ultracentrifugation.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PSI-8LHCI supercomplex at 3 mg/mL in pH 6.5 buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 7.0), 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Li2SO4</a>, 4.5-7.0% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Initial crystals appeared after 3 days; grew to 0.3 mm over 3-4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals soaked in crystallization buffer with 0.05% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, then gradually increased <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000 and Li2SO4 to 8% and 100 mM respectively, followed by <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 (17.5% v/v) and triethylene glycol (TEG, 17.5% v/v)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>One PSI-LHCI molecule per asymmetric unit. Crystals diffracted to 3.2 A resolution. Space group P21, a=94.6 A, b=98.1 A, c=210.1 A, gamma=94.6 deg. Data collected at SPring-8 BL44XU at 100 K.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTISTPEREAK</span><span class="topo-inside">KVKIAVDRNPVETSFEKWAKPGHFSRTLSKGPNTTTWIWNLHADAHDFDSHTSDLEEISRKVFSA</span><span class="topo-membrane">HFGQLGIIFIWLSG</span><span class="topo-outside">MYFHGARFSNYEAWLSDPTHIKPSAQVVWP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IVGQEILNGDVGGGFQGIQITSGFFQLWRASGITSELQLYTT</span><span class="topo-membrane">AIGGLVMAAAMFFA</span><span class="topo-inside">GWFHYHKAAPKLEWFQNVESM</span><span class="topo-membrane">LNHHLGGLLGLGSLAW</span><span class="topo-outside">AGHQIHVSLPVNKLLDAGVDPKEIPLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">HDLLLNRAIMADLYPSFAKGIAPFFTLNWSEYSDFLTFKGGLNPVTGGLWLSDTAHHHV</span><span class="topo-membrane">AIAVLFLVAGHM</span><span class="topo-inside">YRTNWGIGHSMKEILEAHRGPFTGEGHVGLYEILTTSWHAQL</span><span class="topo-membrane">AINLALF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">GSLSIIV</span><span class="topo-outside">AHHMYAMPPYPYLATDYGTQLSLFT</span><span class="topo-membrane">HHTWIGGFCIVGAGA</span><span class="topo-inside">HAAIFMVRDYDPTNNYNNLLDRVIRHRDAII</span><span class="topo-membrane">SHLNWVCIFLGFHSF</span><span class="topo-outside">GLYIHNDTMSALGRPQDMFSDTAIQLQ</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">PVFAQWIQNTHFLAPQLTAPNALAATSLTWGGDLVAVGGKVAMMPISLGTSDFMVH</span><span class="topo-membrane">HIHAFTIHVTVLILL</span><span class="topo-inside">KGVLFARSSRLIPDKANLGFRFPCDGPGRGGTCQVSAWD</span><span class="topo-membrane">HVFLGLFWMY</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">NSLS</span><span class="topo-outside">IVIFHFSWKMQSDVWGTVT</span><span class="topo-unknown">AS</span><span class="topo-outside">GVSHITGGNFAQSANTINGWLRDFLWAQSSQVIQSYGSALSAYGLIFLGAH</span><span class="topo-membrane">FVWAFSLMFLFS</span><span class="topo-inside">GRGYWQELIESIVWAHNKLKVAPAIQPRALSI</span></span>
<span class="topo-ruler">       730       740       750 </span>
<span class="topo-line"><span class="topo-inside">TQ</span><span class="topo-membrane">GRAVGVAHYLLGGIA</span><span class="topo-outside">TTWSFFLARIISVG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>76</td>
      <td>12</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>90</td>
      <td>77</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>162</td>
      <td>91</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>163</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>177</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>213</td>
      <td>198</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>299</td>
      <td>214</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>311</td>
      <td>300</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>353</td>
      <td>312</td>
      <td>353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>367</td>
      <td>354</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>392</td>
      <td>368</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>407</td>
      <td>393</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>438</td>
      <td>408</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>453</td>
      <td>439</td>
      <td>453</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>536</td>
      <td>454</td>
      <td>536</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>537</td>
      <td>551</td>
      <td>537</td>
      <td>551</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>552</td>
      <td>590</td>
      <td>552</td>
      <td>590</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>604</td>
      <td>591</td>
      <td>604</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>605</td>
      <td>623</td>
      <td>605</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>624</td>
      <td>625</td>
      <td>624</td>
      <td>625</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>626</td>
      <td>676</td>
      <td>626</td>
      <td>676</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>677</td>
      <td>688</td>
      <td>677</td>
      <td>688</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>689</td>
      <td>722</td>
      <td>689</td>
      <td>722</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>723</td>
      <td>737</td>
      <td>723</td>
      <td>737</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>738</td>
      <td>751</td>
      <td>738</td>
      <td>751</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-inside">TKLFPKFSQGLAQDPTTRRIWYGLAMAHDFESHDGMTEENLYQK</span><span class="topo-membrane">IFASHFGQLSIIFL</span><span class="topo-outside">WTSGNLFHVAWQGNFEQWVTDPVHIRPIAHAIWDPHFGQPAVEAFTRGGASGPVNISTSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VYQWWYTIGMRTNQDLYVGSVFLA</span><span class="topo-membrane">LVSAIFLFAGWLH</span><span class="topo-inside">LQPNFQPSLSWFKD</span><span class="topo-membrane">AESRLNHHLSGLFGVS</span><span class="topo-outside">SLAWTGHLVHVAIPESRGQHVGWDNFLSVLPHPQGLTPFFTGNWAAYAQSPDT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASHVFGTAQGSGQAILTFLGGFHPQTQSLWLTDMAHHHLAIAV</span><span class="topo-membrane">IFIVAGHMYRT</span><span class="topo-inside">NFGIGHRMQAILEAHTPPSGSLGAGHKGLFDTVNNSLHF</span><span class="topo-membrane">QLGLALASVGTITS</span><span class="topo-outside">LVAQHMYSLPPYA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">FQAIDFTTQAALYTHHQ</span><span class="topo-membrane">YIAGFIMCGAFAHG</span><span class="topo-inside">AIFFIRDYDPEQNKGNVLARMLDHKEA</span><span class="topo-membrane">LISHLSWVSLFLGFHTLG</span><span class="topo-outside">LYVHNDVMQAFGTPEKQILIEPVFAQWIQAAHGKALYGFDFLLS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">SKTSAAFANGQSLWLPGWLDAINNNQNSLFLTIGPGDFLVHH</span><span class="topo-membrane">AIALGLHTTTLILVK</span><span class="topo-inside">GALDARGSKLMPDKKDFGYSFPCDGPGRGGTCDISAYD</span><span class="topo-membrane">AFYLAVFWMLNTI</span><span class="topo-outside">GWVTFYWHWKHL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">TLWQGNVAQFDESSTYLMGWLRDYLWLNSSQLINGYNPFGMNSLSVWAWTFLFGH</span><span class="topo-membrane">LIYATGFMFLISW</span><span class="topo-inside">RGYWQELIETLVWAHEKTPLANLVYWKDKPVALSIV</span><span class="topo-membrane">QARLVGLAHFSVGY</span><span class="topo-outside">IF</span></span>
<span class="topo-ruler">       730     </span>
<span class="topo-line"><span class="topo-outside">TYAAFLIASTSGRF</span><span class="topo-unknown">G</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>46</td>
      <td>3</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>60</td>
      <td>47</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>144</td>
      <td>61</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>157</td>
      <td>145</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>171</td>
      <td>158</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>187</td>
      <td>172</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>283</td>
      <td>188</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>294</td>
      <td>284</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>333</td>
      <td>295</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>347</td>
      <td>334</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>377</td>
      <td>348</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>391</td>
      <td>378</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>418</td>
      <td>392</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>436</td>
      <td>419</td>
      <td>436</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>522</td>
      <td>437</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>523</td>
      <td>537</td>
      <td>523</td>
      <td>537</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>538</td>
      <td>575</td>
      <td>538</td>
      <td>575</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>576</td>
      <td>588</td>
      <td>576</td>
      <td>588</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>589</td>
      <td>655</td>
      <td>589</td>
      <td>655</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>656</td>
      <td>668</td>
      <td>656</td>
      <td>668</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>669</td>
      <td>704</td>
      <td>669</td>
      <td>704</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>718</td>
      <td>705</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>719</td>
      <td>734</td>
      <td>719</td>
      <td>734</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>735</td>
      <td>735</td>
      <td>735</td>
      <td>735</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALTMRNPAVKASSRVAPSSRRALRVACQAQKNETASKVGTALAASALAAAVSLSAPSAAMA</span><span class="topo-outside">DIAGLTPCSESKAYAKLEKKELKTLEKRLKQYEADSAPAVALKATMERTKARFANYAK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">AGLLCGNDGLPHLIADPGLALKYGHAGEVFIP</span><span class="topo-membrane">TFGFLYVAGYIGYV</span><span class="topo-inside">GRQYLIAVKGEAKPTDKEIIIDVPLATKLAWQGAGWPLAAVQELQRGTLLEKEENITVSPR</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>62</td>
      <td>1</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>152</td>
      <td>63</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>166</td>
      <td>153</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>227</td>
      <td>167</td>
      <td>227</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain J (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-inside">MKDFTTYLSTA</span><span class="topo-membrane">PVIATIWFTFTAGLL</span><span class="topo-outside">IEINRYFPDPLVF</span><span class="topo-unknown">SF</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>39</td>
      <td>27</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 1 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRTLSARTAAPRGFSGRRVAAVSNGSRVTM</span><span class="topo-inside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFT</span><span class="topo-membrane">ESEVIHGRWAMLGVAG</span><span class="topo-outside">SLAVELLGYGNWYDAPLWAVNGGKATWFGIEVP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-outside">FDLNALL</span><span class="topo-membrane">AFEFVAMAAAEGQRG</span><span class="topo-inside">DAGGVVYPGGAFDPLGFAKDSSKSGELKL</span><span class="topo-membrane">KEIKNGRLAMVAFLG</span><span class="topo-outside">FVAQHAATGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>30</td>
      <td>5</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>71</td>
      <td>35</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>76</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>127</td>
      <td>92</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>142</td>
      <td>132</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>171</td>
      <td>147</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>186</td>
      <td>176</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>224</td>
      <td>191</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 3 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMLTKSAQAAFSGKVARPAKANRARLVCRAEEKSIAKVDRSKDQLYVGASQSSLAYLDGS</span><span class="topo-inside">LPGDFGFDPLGLLDPVNSGGFIEPKWLQYSEVI</span><span class="topo-membrane">HARWAMLGAAGCIAPEVL</span><span class="topo-outside">GAAGLIPDA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TNIKWFESGVIPPAGSYNGYWADP</span><span class="topo-membrane">YTIFFVEIVAMQFAE</span><span class="topo-inside">LRRLQDFRYPGSMGQQYFLGLEAIFKGSGDAAYPGGPFFNLFNLGKTEAAMKELKLKEIKN</span><span class="topo-membrane">GRLAMLAMLGYGAQA</span><span class="topo-outside">VMTGK</span></span>
<span class="topo-ruler">       250       260       270       280       290        </span>
<span class="topo-line"><span class="topo-outside">GPFQNLVEHLADPVNNNILTNF</span><span class="topo-unknown">AGRVSGSSQPWRPHGWWRRRYRSVAALALIRNRSVC</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>93</td>
      <td>61</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>144</td>
      <td>112</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>159</td>
      <td>145</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>220</td>
      <td>160</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>235</td>
      <td>221</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>262</td>
      <td>236</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>298</td>
      <td>263</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 7 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALSMIAQRRAGAFSARQAPRAVRAQAA</span><span class="topo-inside">VRPVWFPGNPPPAHLDGSLAGDYGFDPLFLGQEPQTLKWYVQ</span><span class="topo-membrane">AELVHGRFAMLGAAGIIL</span><span class="topo-outside">TSIGAKVGLGFPEWYDAGKVVVEKNNIDFPTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MVIQFYLMGWAETK</span><span class="topo-inside">RWYDFKNPGSQADGSFLGFTEEFKGLENGYPGGRFFDPMGLSRGDAAKYQEYKQKEV</span><span class="topo-membrane">KNGRLAMIACLGFAA</span><span class="topo-outside">QYAATGKGPLDNLADHLADPNHVNFATNGVSIPI</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">A</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>70</td>
      <td>29</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>88</td>
      <td>71</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>120</td>
      <td>89</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>134</td>
      <td>121</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>191</td>
      <td>135</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>206</td>
      <td>192</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>240</td>
      <td>207</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 8 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALTMKRSGVAARSASSRKSVVTCVA</span><span class="topo-inside">RQSWLPGSQIPAHLDTPAAQALAGNFGFDPLGLGKDPVALRWYQ</span><span class="topo-membrane">QAELIHCRTAMAGVAG</span><span class="topo-outside">ILIPGLLTKAGALNVPEWYDAGKVAIENSFAPWG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SLLA</span><span class="topo-membrane">VQLFLCGFVEAKRW</span><span class="topo-inside">QDIRKPGSQGEPGSFLGFEASLKGTSELGYPGGPFDPLGLSKEADKWADWKL</span><span class="topo-membrane">KEVKNGRLAMLAFLG</span><span class="topo-outside">FVAQKYATGAGPVDNLAAHLKDPWHVNYATNGVSL</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-outside">PFL</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>70</td>
      <td>27</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>71</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>124</td>
      <td>87</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>138</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>190</td>
      <td>139</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>205</td>
      <td>191</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>243</td>
      <td>206</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain Z (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALSMRTLSARTAAPRGFSGRRVAAVSNGSRVTM</span><span class="topo-inside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFTE</span><span class="topo-membrane">SEVIHGRWAMLGVAGSLA</span><span class="topo-outside">VELLGYGNWYDAPLWAVN</span><span class="topo-unknown">GG</span><span class="topo-outside">KATWFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220        </span>
<span class="topo-line"><span class="topo-outside">IEVPFDLNALL</span><span class="topo-membrane">AFEFVAMAAAEGQR</span><span class="topo-inside">GDAGGVVYPGGAFDPLGFAKDSSKSGELKLK</span><span class="topo-membrane">EIKNGRLAMVAFLGFVA</span><span class="topo-outside">QHAATGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>76</td>
      <td>35</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>94</td>
      <td>77</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>112</td>
      <td>95</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>114</td>
      <td>113</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>115</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>145</td>
      <td>132</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>176</td>
      <td>146</td>
      <td>176</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>193</td>
      <td>177</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>228</td>
      <td>194</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 4 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAFVLAKSSAFGVAAKPVSRRSSVAVKASAVPENVKEAREWIDAWKSKSGGAKRDAA</span><span class="topo-inside">LPSWMPGADLPGYLNGTLPGDFGFDPLYLGQDPVKLKWYAQ</span><span class="topo-membrane">AELMNARFAMLAVAGILV</span><span class="topo-outside">PELL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SNIG</span><span class="topo-unknown">FSW</span><span class="topo-outside">PGAGVAWYDAGKFEYFAPASSL</span><span class="topo-membrane">FGVQMLLFAWVEI</span><span class="topo-inside">RRYQDFVKPGSANQDPIFTNNKLPDGNEPGYPGGIFDPFGWSKGDIKSLKL</span><span class="topo-membrane">KEIKNGRLAMLAFAGF</span><span class="topo-outside">IGQAYTTGTTP</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-outside">LKNLSTHLADPWSTTVWQNDLAR</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>57</td>
      <td>1</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>98</td>
      <td>58</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>117</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>127</td>
      <td>125</td>
      <td>127</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>162</td>
      <td>150</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>213</td>
      <td>163</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>229</td>
      <td>214</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>263</td>
      <td>230</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>264</td>
      <td>264</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 5 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAALMQKSALSRPACSTRSSRRAVVVRAAAD</span><span class="topo-inside">RKLWAPGVVAPEYLKGDLAGDYGWDPLGLGADPTALKWYRQSELQHA</span><span class="topo-membrane">RWAMLGVAGVLVQEIV</span><span class="topo-outside">KPDVYFYEAGLPQNLPEPFTNINMG</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAWEFILMHWVE</span><span class="topo-inside">VRRWQDYKNFGSVNEDPIFKGNKVPNPEMGYPGGIFDPFGFS</span><span class="topo-unknown">KG</span><span class="topo-inside">NLKELQTKEIKNGR</span><span class="topo-membrane">LAMIAYMAFILQAQ</span><span class="topo-outside">ATGKGPLAALSAHLSNPFGNNILKNIGTCTVPHSV</span></span>
<span class="topo-ruler">       250       </span>
<span class="topo-line"><span class="topo-outside">DVQGLTIPLTCLWPGS</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>31</td>
      <td>1</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>78</td>
      <td>32</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>79</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>119</td>
      <td>95</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>175</td>
      <td>134</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>177</td>
      <td>176</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>191</td>
      <td>178</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>205</td>
      <td>192</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>256</td>
      <td>206</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>257</td>
      <td>257</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wyi">7WYI</a> — Chain 6 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMLVAKNAVAARPSARSARRSVVAKASS</span><span class="topo-inside">RPLWLPGSTPPAHLKGDLPGDFGFDPLGLGANAESLKWFKESEL</span><span class="topo-membrane">VHSRWAMAAVAGILVQ</span><span class="topo-outside">EIVRPDVFWYNAGKEVESPLGPLG</span><span class="topo-membrane">LLAVEFFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MHWVEV</span><span class="topo-inside">RRWQDLRKPGSVDQDPIFSQYKLPPHEVGYPGGVFAPFIPGDLAELKVKEIK</span><span class="topo-membrane">NGRLAMLAFVGFVMA</span><span class="topo-outside">AQVTGKGPIAALQEHLADPWGTTIFSKAAVVPGQAVAPPCKIPASVS</span></span>
<span class="topo-ruler">       250       </span>
<span class="topo-line"><span class="topo-outside">YKGIEIPTPCFLQGLWP</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>72</td>
      <td>29</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>73</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>89</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>113</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>178</td>
      <td>127</td>
      <td>178</td>
      <td>Inside</td>
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
      <td>257</td>
      <td>194</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTISTPEREAK</span><span class="topo-inside">KVKIAVDRNPVETSFEKWAKPGHFSRTLSKGPNTTTWIWNLHADAHDFDSHTSDLEEISRKVFSA</span><span class="topo-membrane">HFGQLGIIFIWLSG</span><span class="topo-outside">MYFHGARFSNYEAWLSDPTHIKPSAQVVWP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">IVGQEILNGDVGGGFQGIQITSGFFQLWRASGITSELQLYTT</span><span class="topo-membrane">AIGGLVMAAAMFFA</span><span class="topo-inside">GWFHYHKAAPKLEWFQNVESM</span><span class="topo-membrane">LNHHLGGLLGLGSLA</span><span class="topo-outside">WAGHQIHVSLPVNKLLDAGVDPKEIPLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">HDLLLNRAIMADLYPSFAKGIAPFFTLNWSEYSDFLTFKGGLNPVTGGLWLSDTAHHHV</span><span class="topo-membrane">AIAVLFLVAGHM</span><span class="topo-inside">YRTNWGIGHSMKEILEAHRGPFTGEGHVGLYEILTTSWHAQ</span><span class="topo-membrane">LAINLALF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">GSLSIIV</span><span class="topo-outside">AHHMYAMPPYPYLATDYGTQLSLFT</span><span class="topo-membrane">HHTWIGGFCIVGAGA</span><span class="topo-inside">HAAIFMVRDYDPTNNYNNLLDRVIRHRDAI</span><span class="topo-membrane">ISHLNWVCIFLGFH</span><span class="topo-outside">SFGLYIHNDTMSALGRPQDMFSDTAIQLQ</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">PVFAQWIQNTHFLAPQLTAPNALAATSLTWGGDLVAVGGKVAMMPISLGTSDFMVHH</span><span class="topo-membrane">IHAFTIHVTVLILL</span><span class="topo-inside">KGVLFARSSRLIPDKANLGFRFPCDGPGRGGTCQVSAWD</span><span class="topo-membrane">HVFLGLFWMY</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">NSLS</span><span class="topo-outside">IVIFHFSWKMQSDVWGTVT</span><span class="topo-unknown">AS</span><span class="topo-outside">GVSHITGGNFAQSANTINGWLRDFLWAQSSQVIQSYGSALSAYGLIFLGAH</span><span class="topo-membrane">FVWAFSLMFLFS</span><span class="topo-inside">GRGYWQELIESIVWAHNKLKVAPAIQPRALSI</span></span>
<span class="topo-ruler">       730       740       750 </span>
<span class="topo-line"><span class="topo-inside">TQ</span><span class="topo-membrane">GRAVGVAHYLLGGI</span><span class="topo-outside">ATTWSFFLARIISVG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>76</td>
      <td>12</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>90</td>
      <td>77</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>162</td>
      <td>91</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>176</td>
      <td>163</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>177</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>212</td>
      <td>198</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>299</td>
      <td>213</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>311</td>
      <td>300</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>352</td>
      <td>312</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>367</td>
      <td>353</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>392</td>
      <td>368</td>
      <td>392</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>407</td>
      <td>393</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>437</td>
      <td>408</td>
      <td>437</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>438</td>
      <td>451</td>
      <td>438</td>
      <td>451</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>537</td>
      <td>452</td>
      <td>537</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>538</td>
      <td>551</td>
      <td>538</td>
      <td>551</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>552</td>
      <td>590</td>
      <td>552</td>
      <td>590</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>604</td>
      <td>591</td>
      <td>604</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>605</td>
      <td>623</td>
      <td>605</td>
      <td>623</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>624</td>
      <td>625</td>
      <td>624</td>
      <td>625</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>626</td>
      <td>676</td>
      <td>626</td>
      <td>676</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>677</td>
      <td>688</td>
      <td>677</td>
      <td>688</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>689</td>
      <td>722</td>
      <td>689</td>
      <td>722</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>723</td>
      <td>736</td>
      <td>723</td>
      <td>736</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>737</td>
      <td>751</td>
      <td>737</td>
      <td>751</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-inside">TKLFPKFSQGLAQDPTTRRIWYGLAMAHDFESHDGMTEENLYQK</span><span class="topo-membrane">IFASHFGQLSIIFL</span><span class="topo-outside">WTSGNLFHVAWQGNFEQWVTDPVHIRPIAHAIWDPHFGQPAVEAFTRGGASGPVNISTSG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VYQWWYTIGMRTNQDLYVGSVFLA</span><span class="topo-membrane">LVSAIFLFAGWLHL</span><span class="topo-inside">QPNFQPSLSWFKD</span><span class="topo-membrane">AESRLNHHLSGLFGV</span><span class="topo-outside">SSLAWTGHLVHVAIPESRGQHVGWDNFLSVLPHPQGLTPFFTGNWAAYAQSPDT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ASHVFGTAQGSGQAILTFLGGFHPQTQSLWLTDMAHHHLAIAV</span><span class="topo-membrane">IFIVAGHMYRT</span><span class="topo-inside">NFGIGHRMQAILEAHTPPSGSLGAGHKGLFDTVNNSL</span><span class="topo-membrane">HFQLGLALASVGTIT</span><span class="topo-outside">SLVAQHMYSLPPYA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">FQAIDFTTQAALYTHHQ</span><span class="topo-membrane">YIAGFIMCGAFAHG</span><span class="topo-inside">AIFFIRDYDPEQNKGNVLARMLDHKEA</span><span class="topo-membrane">LISHLSWVSLFLGFHTLG</span><span class="topo-outside">LYVHNDVMQAFGTPEKQILIEPVFAQWIQAAHGKALYGFDFLLS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">SKTSAAFANGQSLWLPGWLDAINNNQNSLFLTIGPGDFLVHHA</span><span class="topo-membrane">IALGLHTTTLILVK</span><span class="topo-inside">GALDARGSKLMPDKKDFGYSFPCDGPGRGGTCDISAY</span><span class="topo-membrane">DAFYLAVFWMLNTI</span><span class="topo-outside">GWVTFYWHWKHL</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">TLWQGNVAQFDESSTYLMGWLRDYLWLNSSQLINGYNPFGMNSLSVWAWTFLFGH</span><span class="topo-membrane">LIYATGFMFLISW</span><span class="topo-inside">RGYWQELIETLVWAHEKTPLANLVYWKDKPVALSIV</span><span class="topo-membrane">QARLVGLAHFSVGY</span><span class="topo-outside">IF</span></span>
<span class="topo-ruler">       730     </span>
<span class="topo-line"><span class="topo-outside">TYAAFLIASTSGRF</span><span class="topo-unknown">G</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>46</td>
      <td>3</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>60</td>
      <td>47</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>144</td>
      <td>61</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>158</td>
      <td>145</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>171</td>
      <td>159</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>186</td>
      <td>172</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>283</td>
      <td>187</td>
      <td>283</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>294</td>
      <td>284</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>331</td>
      <td>295</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>346</td>
      <td>332</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>377</td>
      <td>347</td>
      <td>377</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>391</td>
      <td>378</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>392</td>
      <td>418</td>
      <td>392</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>436</td>
      <td>419</td>
      <td>436</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>523</td>
      <td>437</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>524</td>
      <td>537</td>
      <td>524</td>
      <td>537</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>538</td>
      <td>574</td>
      <td>538</td>
      <td>574</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>575</td>
      <td>588</td>
      <td>575</td>
      <td>588</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>589</td>
      <td>655</td>
      <td>589</td>
      <td>655</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>656</td>
      <td>668</td>
      <td>656</td>
      <td>668</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>669</td>
      <td>704</td>
      <td>669</td>
      <td>704</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>718</td>
      <td>705</td>
      <td>718</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>719</td>
      <td>734</td>
      <td>719</td>
      <td>734</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>735</td>
      <td>735</td>
      <td>735</td>
      <td>735</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALTMRNPAVKASSRVAPSSRRALRVACQAQKNETASKVGTALAASALAAAVSLSAPSAAMA</span><span class="topo-outside">DIAGLTPCSESKAYAKLEKKELKTLEKRLKQYEADSAPAVALKATMERTKARFANYAK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">AGLLCGNDGLPHLIADPGLALKYGHAGEVFIP</span><span class="topo-membrane">TFGFLYVAGYIGYVG</span><span class="topo-inside">RQYLIAVKGEAKPTDKEIIIDVPLATKL</span><span class="topo-unknown">AWQGAGWPLAAV</span><span class="topo-inside">QELQRGTLLEKEENITVSPR</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>62</td>
      <td>1</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>152</td>
      <td>63</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>167</td>
      <td>153</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>195</td>
      <td>168</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>207</td>
      <td>196</td>
      <td>207</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>208</td>
      <td>227</td>
      <td>208</td>
      <td>227</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain J (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-inside">MKDFTTYLSTA</span><span class="topo-membrane">PVIATIWFTFTAGLL</span><span class="topo-outside">IEINRYFPDPLVF</span><span class="topo-unknown">SF</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>26</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>39</td>
      <td>27</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 1 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRTLSARTAAPRGFSGRRVAAVSNGSRVTM</span><span class="topo-inside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFT</span><span class="topo-membrane">ESEVIHGRWAMLGVA</span><span class="topo-outside">GSLAVELLGYGNWYDAPLWAVNGGKATWFGIEVP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220    </span>
<span class="topo-line"><span class="topo-outside">FDLNALLA</span><span class="topo-membrane">FEFVAMAAAEGQRGD</span><span class="topo-inside">AGGVVYPGGAFDPLGFAKDSSKSGELKL</span><span class="topo-membrane">KEIKNGRLAMVAFLG</span><span class="topo-outside">FVAQHAATGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>30</td>
      <td>5</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>71</td>
      <td>35</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>86</td>
      <td>76</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>128</td>
      <td>91</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>143</td>
      <td>133</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>171</td>
      <td>148</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>186</td>
      <td>176</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>224</td>
      <td>191</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 3 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMLTKSAQAAFSGKVARPAKANRARLVCRAEEKSIAKVDRSKDQLYVGASQSSLAYLDGS</span><span class="topo-inside">LPGDFGFDPLGLLDPVNSGGFIEPKWLQYSEVI</span><span class="topo-membrane">HARWAMLGAAGCIAPEVL</span><span class="topo-outside">GAAGLIPDA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TNIKWFESGVIPPAGSYNGYWADP</span><span class="topo-membrane">YTIFFVEIVAMQFAE</span><span class="topo-inside">LRRLQDFRYPGSMGQQYFLGLEAIFKGSGDAAYPGGPFFNLFNLGKTEAAMKELKLKEIKN</span><span class="topo-membrane">GRLAMLAMLGYGAQA</span><span class="topo-outside">VMTGK</span></span>
<span class="topo-ruler">       250       260       270       280       290        </span>
<span class="topo-line"><span class="topo-outside">GPFQNLVEHLADPVNNNILTNF</span><span class="topo-unknown">AGRVSGSSQPWRPHGWWRRRYRSVAALALIRNRSVC</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>60</td>
      <td>1</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>93</td>
      <td>61</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>111</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>144</td>
      <td>112</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>159</td>
      <td>145</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>220</td>
      <td>160</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>235</td>
      <td>221</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>262</td>
      <td>236</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>298</td>
      <td>263</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 7 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALSMIAQRRAGAFSARQAPRAVRAQAA</span><span class="topo-inside">VRPVWFPGNPPPAHLDGSLAGDYGFDPLFLGQEPQTLKWYVQ</span><span class="topo-membrane">AELVHGRFAMLGAAGIIL</span><span class="topo-outside">TSIGAKVGLGFPEWYDAGKVVVEKNNIDFPTL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MVIQFYLMGWAETK</span><span class="topo-inside">RWYDFKNPGSQADGSFLGFTEEFKGLENGYPGGRFFDPMGLSRGDAAKYQEYKQKEV</span><span class="topo-membrane">KNGRLAMIACLGFAA</span><span class="topo-outside">QYAATGKGPLDNLADHLADPNHVNFATNGVSIPI</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">A</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>70</td>
      <td>29</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>88</td>
      <td>71</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>120</td>
      <td>89</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>134</td>
      <td>121</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>191</td>
      <td>135</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>206</td>
      <td>192</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>240</td>
      <td>207</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 8 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALTMKRSGVAARSASSRKSVVTCVA</span><span class="topo-inside">RQSWLPGSQIPAHLDTPAAQALAGNFGFDPLGLGKDPVALRWYQ</span><span class="topo-membrane">QAELIHCRTAMAGVAG</span><span class="topo-outside">ILIPGLLTKAGALNVPEWYDAGKVAIENSFAPWG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SLLA</span><span class="topo-membrane">VQLFLCGFVEAKRW</span><span class="topo-inside">QDIRKPGSQGEPGSFLGFEASLKGTSELGYPGGPFDPLGLSKEADKWADWKL</span><span class="topo-membrane">KEVKNGRLAMLAFLG</span><span class="topo-outside">FVAQKYATGAGPVDNLAAHLKDPWHVNYATNGVSL</span></span>
<span class="topo-ruler">   </span>
<span class="topo-line"><span class="topo-outside">PFL</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>70</td>
      <td>27</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>86</td>
      <td>71</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>124</td>
      <td>87</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>138</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>190</td>
      <td>139</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>205</td>
      <td>191</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>243</td>
      <td>206</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain Z (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MALSMRTLSARTAAPRGFSGRRVAAVSNGSRVTM</span><span class="topo-inside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFTE</span><span class="topo-membrane">SEVIHGRWAMLGVAGSL</span><span class="topo-outside">AVELLGYGNWYDAPLWAVN</span><span class="topo-unknown">GG</span><span class="topo-outside">KATWFG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220        </span>
<span class="topo-line"><span class="topo-outside">IEVPFDLNALL</span><span class="topo-membrane">AFEFVAMAAAEGQRG</span><span class="topo-inside">DAGGVVYPGGAFDPLGFAKDSSKSGELKL</span><span class="topo-membrane">KEIKNGRLAMVAFLGF</span><span class="topo-outside">VAQHAATGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>34</td>
      <td>1</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>76</td>
      <td>35</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>114</td>
      <td>113</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>131</td>
      <td>115</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>146</td>
      <td>132</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>175</td>
      <td>147</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>191</td>
      <td>176</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>228</td>
      <td>192</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 4 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAFVLAKSSAFGVAAKPVSRRSSVAVKASAVPENVKEAREWIDAWKSKSGGAKRDAA</span><span class="topo-inside">LPSWMPGADLPGYLNGTLPGDFGFDPLYLGQDPVKLKWYAQ</span><span class="topo-membrane">AELMNARFAMLAVAGILV</span><span class="topo-outside">PELL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SNIG</span><span class="topo-unknown">FSW</span><span class="topo-outside">PGAGVAWYDAGKFEYFAPASSL</span><span class="topo-membrane">FGVQMLLFAWVEI</span><span class="topo-inside">RRYQDFVKPGSANQDPIFTNNKLPDGNEPGYPGGIFDPFGWSKGDIKSLKL</span><span class="topo-membrane">KEIKNGRLAMLAFAGF</span><span class="topo-outside">IGQAYTTGTTP</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-outside">LKNLSTHLADPWSTTVWQNDLAR</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>57</td>
      <td>1</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>58</td>
      <td>98</td>
      <td>58</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>124</td>
      <td>117</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>127</td>
      <td>125</td>
      <td>127</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>162</td>
      <td>150</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>213</td>
      <td>163</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>229</td>
      <td>214</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>263</td>
      <td>230</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>264</td>
      <td>264</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 5 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAALMQKSALSRPACSTRSSRRAVVVRAAAD</span><span class="topo-inside">RKLWAPGVVAPEYLKGDLAGDYGWDPLGLGADPTALKWYRQSELQ</span><span class="topo-membrane">HARWAMLGVAGVLVQEIV</span><span class="topo-outside">KPDVYFYEAGLPQNLPEPFTNINM</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LLAWEFILMHWVE</span><span class="topo-inside">VRRWQDYKNFGSVNEDPIFKGNKVPNPEMGYPGGIFDPFGFS</span><span class="topo-unknown">KG</span><span class="topo-inside">NLKELQTKEIKNGR</span><span class="topo-membrane">LAMIAYMAFILQAQ</span><span class="topo-outside">ATGKGPLAALSAHLSNPFGNNILKNIGTCTVPHSV</span></span>
<span class="topo-ruler">       250       </span>
<span class="topo-line"><span class="topo-outside">DVQGLTIPLTCLWPGS</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>31</td>
      <td>1</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>76</td>
      <td>32</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>94</td>
      <td>77</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>118</td>
      <td>95</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>133</td>
      <td>119</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>175</td>
      <td>134</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>177</td>
      <td>176</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>191</td>
      <td>178</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>205</td>
      <td>192</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>256</td>
      <td>206</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>257</td>
      <td>257</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wzn">7WZN</a> — Chain 6 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MMLVAKNAVAARPSARSARRSVVAKASS</span><span class="topo-inside">RPLWLPGSTPPAHLKGDLPGDFGFDPLGLGANAESLKWFKESEL</span><span class="topo-membrane">VHSRWAMAAVAGILVQ</span><span class="topo-outside">EIVRPDVFWYNAGKEVESPLGPLG</span><span class="topo-membrane">LLAVEFFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MHWVEV</span><span class="topo-inside">RRWQDLRKPGSVDQDPIFSQYKLPPHEVGYPGGVFAPFIPGDLAELKVKEIK</span><span class="topo-membrane">NGRLAMLAFVGFVMA</span><span class="topo-outside">AQVTGKGPIAALQEHLADPWGTTIFSKAAVVPGQAVAPPCKIPASVS</span></span>
<span class="topo-ruler">       250       </span>
<span class="topo-line"><span class="topo-outside">YKGIEIPTPCFLQG</span><span class="topo-unknown">LWP</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>72</td>
      <td>29</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>73</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>89</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>126</td>
      <td>113</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>178</td>
      <td>127</td>
      <td>178</td>
      <td>Inside</td>
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
      <td>254</td>
      <td>194</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>257</td>
      <td>255</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTISTPEREAK</span><span class="topo-outside">KVKIAVDRNPVETSFEKWAKPGHFSRTLSKGPNTTTWIWNLHADAHDFDSHTSDLEEISRKVFSAH</span><span class="topo-membrane">FGQLGIIFIWLSGMYFHG</span><span class="topo-inside">ARFSNYEAWLSDPTHIKPSAQVVWP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IVGQEILNGDVGGGFQGIQITSGFFQLWRASGITSELQ</span><span class="topo-membrane">LYTTAIGGLVMAAAMF</span><span class="topo-outside">FAGWFHYHKAAPKLEWFQNVESMLN</span><span class="topo-membrane">HHLGGLLGLGSLAWAGHQ</span><span class="topo-inside">IHVSLPVNKLLDAGVDPKEIPLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">HDLLLNRAIMADLYPSFAKGIAPFFTLNWSEYSDFLTFKGGLNPVTGGLWLSDT</span><span class="topo-membrane">AHHHVAIAVLFLVAGHM</span><span class="topo-outside">YRTNWGIGHSMKEILEAHRGPFTGEGHVGLYEILTTSWHAQLAI</span><span class="topo-membrane">NLALF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">GSLSIIVAHHM</span><span class="topo-inside">YAMPPYPYLATDYGTQLS</span><span class="topo-membrane">LFTHHTWIGGFCIVGAG</span><span class="topo-outside">AHAAIFMVRDYDPTNNYNNLLDRVIRHRDAIISH</span><span class="topo-membrane">LNWVCIFLGFHSFGLYIH</span><span class="topo-inside">NDTMSALGRPQDMFSDTAIQLQ</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">PVFAQWIQNTHFLAPQLTAPNALAATSLTWGGDLVAVGGKVAMMPISLGTSDF</span><span class="topo-membrane">MVHHIHAFTIHVTVLIL</span><span class="topo-outside">LKGVLFARSSRLIPDKANLGFRFPCDGPGRGGTCQVSAWDHV</span><span class="topo-membrane">FLGLFWMY</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">NSLSIVIFHF</span><span class="topo-inside">SWKMQSDVWGTVT</span><span class="topo-unknown">AS</span><span class="topo-inside">GVSHITGGNFAQSANTINGWLRDFLWAQSSQVIQSYGSALSAYGL</span><span class="topo-membrane">IFLGAHFVWAFSLMFLFS</span><span class="topo-outside">GRGYWQELIESIVWAHNKLKVAPAIQPRALSI</span></span>
<span class="topo-ruler">       730       740       750 </span>
<span class="topo-line"><span class="topo-outside">TQGRA</span><span class="topo-membrane">VGVAHYLLGGIATTWS</span><span class="topo-inside">FFLARIISVG</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>77</td>
      <td>12</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>158</td>
      <td>96</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>174</td>
      <td>159</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>199</td>
      <td>175</td>
      <td>199</td>
      <td>Outside</td>
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
      <td>294</td>
      <td>218</td>
      <td>294</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>311</td>
      <td>295</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>355</td>
      <td>312</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>389</td>
      <td>372</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>406</td>
      <td>390</td>
      <td>406</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>407</td>
      <td>440</td>
      <td>407</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>458</td>
      <td>441</td>
      <td>458</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>533</td>
      <td>459</td>
      <td>533</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>534</td>
      <td>550</td>
      <td>534</td>
      <td>550</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>551</td>
      <td>592</td>
      <td>551</td>
      <td>592</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>593</td>
      <td>610</td>
      <td>593</td>
      <td>610</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>611</td>
      <td>623</td>
      <td>611</td>
      <td>623</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>624</td>
      <td>625</td>
      <td>624</td>
      <td>625</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>626</td>
      <td>670</td>
      <td>626</td>
      <td>670</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>671</td>
      <td>688</td>
      <td>671</td>
      <td>688</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>689</td>
      <td>725</td>
      <td>689</td>
      <td>725</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>726</td>
      <td>741</td>
      <td>726</td>
      <td>741</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>742</td>
      <td>751</td>
      <td>742</td>
      <td>751</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MATHHHHHHHHHHHHHHHHHHH</span><span class="topo-outside">HKLFPKFSQGLAQDPTTRRIWYGLAMAHDFESHDGMTEENLYQKIFA</span><span class="topo-membrane">SHFGQLSIIFLWTSGN</span><span class="topo-inside">LFHVAWQGNFEQWVTDPVHIRPIAHAIWDPHFGQP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVEAFTRGGASGPVNISTSGVYQWWYTIGMRTNQDLYVG</span><span class="topo-membrane">SVFLALVSAIFLFAGWL</span><span class="topo-outside">HLQPNFQPSLSWFKDAESR</span><span class="topo-membrane">LNHHLSGLFGVSSLAWTG</span><span class="topo-inside">HLVHVAIPESRGQHVGWDNFLSVLPHP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QGLTPFFTGNWAAYAQSPDTASHVFGTAQGSGQAILTFLGGFHPQTQSLWLTDMAHH</span><span class="topo-membrane">HLAIAVIFIVAGHMY</span><span class="topo-outside">RTNFGIGHRMQAILEAHTPPSGSLGAGHKGLFDTVNNSLHFQL</span><span class="topo-membrane">GLALA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">SVGTITSLVAQH</span><span class="topo-inside">MYSLPPYAFQAIDFTTQAAL</span><span class="topo-membrane">YTHHQYIAGFIMCGAF</span><span class="topo-outside">AHGAIFFIRDYDPEQNKGNVLARMLDHKEALISH</span><span class="topo-membrane">LSWVSLFLGFHTLGLYVHNDV</span><span class="topo-inside">MQAFGTPEKQILIEPVF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">AQWIQAAHGKALYGFDFLLSSKTSAAFANGQSLWLPGWLDAINNNQNSLFLTIGPGDF</span><span class="topo-membrane">LVHHAIALGLHTTTLIL</span><span class="topo-outside">VKGALDARGSKLMPDKKDFGYSFPCDGPGRGGTCDISAYDAF</span><span class="topo-membrane">YLA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">VFWMLNTIGWVTFY</span><span class="topo-inside">WHWKHLTLWQGNVAQFDESSTYLMGWLRDYLWLNSSQLINGYNPFGMNSLSVWAWT</span><span class="topo-membrane">FLFGHLIYATGFMFLIS</span><span class="topo-outside">WRGYWQELIETLVWAHEKTPLANLVYWKDKPVA</span></span>
<span class="topo-ruler">       730       740       750     </span>
<span class="topo-line"><span class="topo-outside">LSIVQAR</span><span class="topo-membrane">LVGLAHFSVGYIFTYA</span><span class="topo-inside">AFLIASTSGRF</span><span class="topo-unknown">G</span></span>
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
      <td>-19</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>69</td>
      <td>3</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>85</td>
      <td>50</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>159</td>
      <td>66</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>140</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>195</td>
      <td>157</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>213</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>297</td>
      <td>194</td>
      <td>277</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>312</td>
      <td>278</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>355</td>
      <td>293</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>372</td>
      <td>336</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>392</td>
      <td>353</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>393</td>
      <td>408</td>
      <td>373</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>442</td>
      <td>389</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>463</td>
      <td>423</td>
      <td>443</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>464</td>
      <td>538</td>
      <td>444</td>
      <td>518</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>539</td>
      <td>555</td>
      <td>519</td>
      <td>535</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>597</td>
      <td>536</td>
      <td>577</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>614</td>
      <td>578</td>
      <td>594</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>670</td>
      <td>595</td>
      <td>650</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>671</td>
      <td>687</td>
      <td>651</td>
      <td>667</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>688</td>
      <td>727</td>
      <td>668</td>
      <td>707</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>728</td>
      <td>743</td>
      <td>708</td>
      <td>723</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>744</td>
      <td>754</td>
      <td>724</td>
      <td>734</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>755</td>
      <td>755</td>
      <td>735</td>
      <td>735</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80 </span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AHIVKIYDTCIGCTQCVRACPLDVLEMVPWDGCKASQMASAPRTEDCVGCKRCETACPTDFLSVRVYLGSESTRSMGLSY</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>81</td>
      <td>2</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">EAEAAPAAAKKAAEKPA</span><span class="topo-outside">WTVPTLNPDTPSPIFGGSTGGLLRKAQTEEFYVITWEAKKEQIFEMPTGGAAIMRQGPNLLKFGKKEQCLALTTQLRNKFKLTPCFYRVFPDGKVQYLHPADG</span></span>
<span class="topo-ruler">       130       140       150       160 </span>
<span class="topo-line"><span class="topo-outside">VYPEKVNAGRVGANQNMRRIGQNVNPIKVKFSGRMMSPAEI</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>17</td>
      <td>36</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>161</td>
      <td>53</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70   </span>
<span class="topo-line"><span class="topo-unknown">EEVKAAPKKEV</span><span class="topo-outside">GPKRGSLVKILRPESYWFNQVGKVVSVDQSGVRYPVVVRFENQNYAGVTTNNYALDEVVAA</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>25</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>72</td>
      <td>36</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>97</td>
      <td>97</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">DIAGLTPCSESKAYAKLEKKELKTLEKRLKQYEADSAPAVALKATMERTKARFANYAKAGLLCGNDGLPHLIADPGLALKYGHA</span><span class="topo-membrane">GEVFIPTFGFLYVAGYIG</span><span class="topo-outside">YVGRQYLIAVKGEAKPTD</span></span>
<span class="topo-ruler">       130       140       150       160     </span>
<span class="topo-line"><span class="topo-outside">KEIIIDVPLATKLAWQGAGWPLAAVQELQRGTLLEKEENITVSPR</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>84</td>
      <td>63</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>102</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>165</td>
      <td>165</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">LDP</span><span class="topo-membrane">QIVISGSTAAFLAIGRFVF</span><span class="topo-outside">LGYQRREAN</span><span class="topo-unknown">FDSTVGPKTTGATYFDDLQKNST</span><span class="topo-outside">IFATNDPAGFNI</span><span class="topo-membrane">IDVAGWGALGHAVGFAVL</span><span class="topo-inside">AINSLQG</span><span class="topo-unknown">AN</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>31</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>35</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>32</td>
      <td>54</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>55</td>
      <td>63</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>56</td>
      <td>67</td>
      <td>86</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>85</td>
      <td>98</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>92</td>
      <td>116</td>
      <td>122</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>94</td>
      <td>123</td>
      <td>124</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain I (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100      </span>
<span class="topo-line"><span class="topo-unknown">MALRAVSAKSAVRPTVARASVKPVAALKPAQKMALAGAASVALLAASSSSAEASQVIATVASAAQGY</span><span class="topo-inside">PFVPPSWAPSV</span><span class="topo-membrane">FVPLTGLVLPAIAMATLF</span><span class="topo-outside">VYIEKEAP</span><span class="topo-unknown">SS</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>67</td>
      <td>1</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>78</td>
      <td>68</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>79</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>104</td>
      <td>97</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>106</td>
      <td>105</td>
      <td>106</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain J (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40 </span>
<span class="topo-line"><span class="topo-outside">MKDFTTYLSTAPV</span><span class="topo-membrane">IATIWFTFTAGLLIEINRYF</span><span class="topo-inside">PDPLVF</span><span class="topo-unknown">SF</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>33</td>
      <td>14</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>34</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>40</td>
      <td>41</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain K (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80       </span>
<span class="topo-line"><span class="topo-unknown">DG</span><span class="topo-inside">F</span><span class="topo-membrane">IGSSTNLIMVASTTATLA</span><span class="topo-outside">A</span><span class="topo-unknown">ARFGLAPTVKKNTTAGLKLVDSKNSAGVISNDPAGF</span><span class="topo-outside">TIVDVL</span><span class="topo-membrane">AMGAAGHGLGVGIVLGLK</span><span class="topo-inside">G</span><span class="topo-unknown">IGAL</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>2</td>
      <td>27</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>29</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>21</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>22</td>
      <td>48</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>58</td>
      <td>49</td>
      <td>84</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>64</td>
      <td>85</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>82</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>83</td>
      <td>109</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>110</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain L (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">QVISPVNGDPFV</span><span class="topo-outside">GMLETPVTSAPIVATYLSNLPAYRTGVAPV</span><span class="topo-membrane">LRGVEIGLAHGFLLAGPFI</span><span class="topo-inside">KLGPLRNVPETAEIAG</span><span class="topo-membrane">SLSAAGLVLILALCLSI</span><span class="topo-outside">YGSAQFQ</span><span class="topo-unknown">STPSIGVKTLSGRSVARD</span><span class="topo-outside">P</span></span>
<span class="topo-ruler">       130       140       150      </span>
<span class="topo-line"><span class="topo-outside">LFSADGWSEF</span><span class="topo-membrane">AAGFLVGGEAGVAWAYVC</span><span class="topo-unknown">TQILPYYS</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>12</td>
      <td>41</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>42</td>
      <td>53</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>61</td>
      <td>83</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>77</td>
      <td>102</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>94</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>101</td>
      <td>135</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>119</td>
      <td>142</td>
      <td>159</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>130</td>
      <td>160</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>156</td>
      <td>189</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 1 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFTES</span><span class="topo-membrane">EVIHGRWAMLGVAGSLAVELL</span><span class="topo-inside">GYGNWYDAPLWAVNGGKATWFGIEVPFDL</span><span class="topo-membrane">NALLAFEFVAMAAAEG</span><span class="topo-outside">QRGDAGGVVYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190    </span>
<span class="topo-line"><span class="topo-outside">GGAFDPLGFAKDSSKSGELKLKE</span><span class="topo-membrane">IKNGRLAMVAFLGFVAQHAA</span><span class="topo-inside">TGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>43</td>
      <td>35</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>93</td>
      <td>99</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>109</td>
      <td>128</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>143</td>
      <td>144</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>178</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>194</td>
      <td>198</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 3 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">EEKSIAKVDRSKDQLYVGASQSSLAYLDGS</span><span class="topo-outside">LPGDFGFDPLGLLDPVNSGGFIEPKWLQYSEVIHARW</span><span class="topo-membrane">AMLGAAGCIAPEVLGAA</span><span class="topo-inside">GLIPDATNIKWFESGVIPPAGSYNG</span><span class="topo-membrane">YWADPYTIFFV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">EIVAMQFA</span><span class="topo-outside">ELRRLQDFRYPGSMGQQYFLGLEAIFKGSGDAAYPGGPFFNLFNLGKTEAAMKELKLKEIKNGRL</span><span class="topo-membrane">AMLAMLGYGAQAVMTG</span><span class="topo-inside">KGPFQNLVEHLADPVNNNILTNFA</span><span class="topo-unknown">GRVSGSS</span></span>
<span class="topo-ruler">       250       260        </span>
<span class="topo-line"><span class="topo-unknown">QPWRPHGWWRRRYRSVAALALIRNRSVC</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>30</td>
      <td>31</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>67</td>
      <td>61</td>
      <td>97</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>84</td>
      <td>98</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>109</td>
      <td>115</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>128</td>
      <td>140</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>193</td>
      <td>159</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>209</td>
      <td>224</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>233</td>
      <td>240</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>268</td>
      <td>264</td>
      <td>298</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 7 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AA</span><span class="topo-outside">VRPVWFPGNPPPAHLDGSLAGDYGFDPLFLGQEPQTLKWYVQA</span><span class="topo-membrane">ELVHGRFAMLGAAGIILTSIG</span><span class="topo-inside">AKVGLGFPEWYDAGKVVVEKNNIDF</span><span class="topo-membrane">PTLMVIQFYLMGWAET</span><span class="topo-outside">KRWYDFKNPGSQA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210     </span>
<span class="topo-line"><span class="topo-outside">DGSFLGFTEEFKGLENGYPGGRFFDPMGLSRGDAAKYQEYKQKEVK</span><span class="topo-membrane">NGRLAMIACLGFAAQYAA</span><span class="topo-inside">TGKGPLDNLADHLADPNHVNFATNGVSIPI</span><span class="topo-unknown">A</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>2</td>
      <td>27</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>45</td>
      <td>29</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>66</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>91</td>
      <td>93</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>107</td>
      <td>118</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>166</td>
      <td>134</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>193</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>214</td>
      <td>211</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>215</td>
      <td>241</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 8 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">RQSWLPGSQIPAHLDTPAAQALAGNFGFDPLGLGKDPVALRWYQQA</span><span class="topo-membrane">ELIHCRTAMAGVAGILIPGLL</span><span class="topo-inside">TKAGALNVPEWYDAGKVAIENSFAPW</span><span class="topo-membrane">GSLLAVQLFLCGFVEAK</span><span class="topo-outside">RWQDIRKPGS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       </span>
<span class="topo-line"><span class="topo-outside">QGEPGSFLGFEASLKGTSELGYPGGPFDPLGLSKEADKWADWKLK</span><span class="topo-membrane">EVKNGRLAMLAFLGFVAQKY</span><span class="topo-inside">ATGAGPVDNLAAHLKDPWHVNYATNGVSLPFL</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>46</td>
      <td>27</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>67</td>
      <td>73</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>93</td>
      <td>94</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>120</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>165</td>
      <td>137</td>
      <td>191</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>192</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>217</td>
      <td>212</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain Z (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">KAGNWLPGSDAPAWLPDDLPGNYGFDPLSLGKEPASLKRFTES</span><span class="topo-membrane">EVIHGRWAMLGVAGSLAV</span><span class="topo-inside">ELLGYGNWYDAPLWAVN</span><span class="topo-unknown">GG</span><span class="topo-inside">KATWFGIEVPFDLN</span><span class="topo-membrane">ALLAFEFVAMAAAEGQR</span><span class="topo-outside">GDAGGVVYP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190    </span>
<span class="topo-line"><span class="topo-outside">GGAFDPLGFAKDSSKSGELKLK</span><span class="topo-membrane">EIKNGRLAMVAFLGFVAQHA</span><span class="topo-inside">ATGKGPIAALGEHLANPWGANFATNGISVPFF</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>43</td>
      <td>35</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>61</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>78</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>80</td>
      <td>113</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>115</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>129</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>142</td>
      <td>146</td>
      <td>176</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>162</td>
      <td>177</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>194</td>
      <td>197</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 4 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SAVPENVKEAREWIDAWKSKSGGAKRDAA</span><span class="topo-outside">LPSWMPGADLPGYLNGTLPGDFGFDPLYLGQDPVKLKWYAQ</span><span class="topo-membrane">AELMNARFAMLAVAGILVP</span><span class="topo-inside">ELLSNIG</span><span class="topo-unknown">FSW</span><span class="topo-inside">PGAGVAWYDAGKFEYFAPAS</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230      </span>
<span class="topo-line"><span class="topo-membrane">LFGVQMLLFAWVEIRRY</span><span class="topo-outside">QDFVKPGSANQDPIFTNNKLPDGNEPGYPGGIFDPFGWSKGDIKSLKLK</span><span class="topo-membrane">EIKNGRLAMLAFAGFIGQ</span><span class="topo-inside">AYTTGTTPLKNLSTHLADPWSTTVWQNDLAR</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>29</td>
      <td>57</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>70</td>
      <td>58</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>89</td>
      <td>99</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>118</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>99</td>
      <td>125</td>
      <td>127</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>100</td>
      <td>119</td>
      <td>128</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>137</td>
      <td>148</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>186</td>
      <td>166</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>204</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>235</td>
      <td>233</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>236</td>
      <td>264</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 5 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AAD</span><span class="topo-outside">RKLWAPGVVAPEYLKGDLAGDYGWDPLGLGADPTALKWYRQSELQH</span><span class="topo-membrane">ARWAMLGVAGVLVQEIVKPDV</span><span class="topo-inside">YFYEAGLPQNLPEPFTNI</span><span class="topo-membrane">NMGGLLAWEFILMHWVE</span><span class="topo-outside">VRRWQDYKNFGSVNE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-outside">DPIFKGNKVPNPEMGYPGGIFDPFGFS</span><span class="topo-unknown">KG</span><span class="topo-outside">NLKELQTKEIKNGRL</span><span class="topo-membrane">AMIAYMAFILQAQATG</span><span class="topo-inside">KGPLAALSAHLSNPFGNNILKNIGTCTVPHSVDVQGLTIPLTCLWPGS</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>29</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>49</td>
      <td>32</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>70</td>
      <td>78</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>88</td>
      <td>99</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>105</td>
      <td>117</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>147</td>
      <td>134</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>149</td>
      <td>176</td>
      <td>177</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>150</td>
      <td>164</td>
      <td>178</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>180</td>
      <td>193</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>228</td>
      <td>209</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>257</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 6 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ASS</span><span class="topo-outside">RPLWLPGSTPPAHLKGDLPGDFGFDPLGLGANAESLKWFKES</span><span class="topo-membrane">ELVHSRWAMAAVAGILVQEIV</span><span class="topo-inside">RPDVFWYNAGKEVESPLGPL</span><span class="topo-membrane">GLLAVEFFLMHWVEVRRW</span><span class="topo-outside">QDLRKPGSVDQDPIFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230  </span>
<span class="topo-line"><span class="topo-outside">QYKLPPHEVGYPGGVFAPFIPGDLAELKVKEIK</span><span class="topo-membrane">NGRLAMLAFVGFVMAAQV</span><span class="topo-inside">TGKGPIAALQEHLADPWGTTIFSKAAVVPGQAVAPPCKIPASVSYKGIEIPTPCFLQGLWP</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>26</td>
      <td>28</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>45</td>
      <td>29</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>66</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>86</td>
      <td>92</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>153</td>
      <td>130</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>171</td>
      <td>179</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>232</td>
      <td>197</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 2 (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">STRPM</span><span class="topo-outside">WYPGATAP</span><span class="topo-unknown">AHLDGSML</span><span class="topo-outside">GDYGFDPLR</span><span class="topo-unknown">LGVNKDN</span><span class="topo-outside">LKWFREA</span><span class="topo-membrane">ELTNGRWAMAAVVGILF</span><span class="topo-inside">TD</span><span class="topo-unknown">AVGLPKFWTAGAEKYALDNQTLALI</span><span class="topo-inside">E</span><span class="topo-membrane">VAVFAVLEGKRY</span><span class="topo-outside">EI</span><span class="topo-unknown">YKKTGETGFLSFAPFDP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220 </span>
<span class="topo-line"><span class="topo-unknown">MGMKSEEM</span><span class="topo-outside">KLK</span><span class="topo-membrane">ELKNGRLAMLAFLGFCSQ</span><span class="topo-inside">AAVYGKGPIETLQLHLAD</span><span class="topo-unknown">PGHNNIYTSS</span><span class="topo-inside">V</span><span class="topo-membrane">GPETAVTVAVLCVLPMI</span><span class="topo-outside">IEAT</span><span class="topo-unknown">KTLNPGKESVPYFPWNEPWNKV</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>5</td>
      <td>26</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>31</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>21</td>
      <td>39</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>30</td>
      <td>47</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>37</td>
      <td>56</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>44</td>
      <td>63</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>61</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>63</td>
      <td>87</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>88</td>
      <td>89</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>89</td>
      <td>114</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>101</td>
      <td>115</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>103</td>
      <td>127</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>128</td>
      <td>129</td>
      <td>153</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>129</td>
      <td>131</td>
      <td>154</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>149</td>
      <td>157</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>167</td>
      <td>175</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>177</td>
      <td>193</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>178</td>
      <td>178</td>
      <td>203</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>195</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>199</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>225</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jo5">6JO5</a> — Chain 9 (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ASARP</span><span class="topo-outside">TWLPGLNPPA</span><span class="topo-unknown">HLKGALA</span><span class="topo-outside">GDNGFDPLGLGQDEGRLKWYAEA</span><span class="topo-membrane">EKTNGRWAMMAVAGILGQ</span><span class="topo-inside">ELL</span><span class="topo-unknown">GVT</span><span class="topo-inside">PAWWEAGAKEYDIPAQA</span><span class="topo-membrane">LTPIEFIVMGFLEIKR</span><span class="topo-outside">YQGF</span><span class="topo-unknown">KQTGTSGFINSFPF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180         </span>
<span class="topo-line"><span class="topo-unknown">DPAGM</span><span class="topo-outside">NSPSMATK</span><span class="topo-membrane">EVKNGRLAMVAFIGFCVQ</span><span class="topo-inside">ALATRTQPIEGLTAHLADPFGKNITYYLTHLPETL</span><span class="topo-unknown">GSA</span></span>
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
      <td>5</td>
      <td>25</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>15</td>
      <td>30</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>40</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>45</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>70</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>88</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>69</td>
      <td>91</td>
      <td>93</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>86</td>
      <td>94</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>111</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>106</td>
      <td>127</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>125</td>
      <td>131</td>
      <td>149</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>126</td>
      <td>133</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>151</td>
      <td>158</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>186</td>
      <td>176</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>211</td>
      <td>213</td>
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

### Resting state of PSI-LHCI

The PSI-LHCI supercomplex exists in a resting state with reduced chlorophyll content (six bridging chlorophylls absent from the luminal LHCI belt), electron donors (plastocyanin) docked in waiting positions on the luminal side, and regulatory binding partners (sigma1, sigma2, sigma3) positioned at the stromal electron acceptor site. This resting state avoids undesirable electron injection from plastocyanin or cytochrome c6 while allowing rapid productive binding for electron donation when needed.

### Ferredoxin-induced activation

Binding of oxidized ferredoxin to the PsaC electron acceptor site triggers dissociation of stromal regulatory binding partners (sigma1, sigma2, sigma3) and causes luminal electron donors to leave their waiting positions. This activates the PSI-LHCI complex for productive electron transfer. The edge-to-edge distance between the FB cluster and the Fe2S2 cluster of ferredoxin is approximately 9 Angstroms, close enough for efficient electron tunneling.

### Chlorophyll loss from LHCI belt

The Form A X-ray structure reveals absence of six chlorophylls from the luminal side of the LHCI belts. These bridging chlorophylls are normally found in previous [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures and their absence may significantly influence excitation energy transfer between light harvesting complexes and the PSI core.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Primary detergent used for solubilization of thylakoid membranes and purification of PSI-8LHCI supercomplex
- <a href="/xray-mp-wiki/reagents/detergents/glyco-diosgenin/">Glyco-diosgenin (GDN)</a> — Used for detergent exchange for cryo-EM sample preparation
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Crystallization buffer component (50 mM Tris-HCl, pH 7.0)
- <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Lithium Sulfate</a> — Crystallization precipitant component (50-100 mM Li2SO4)
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Crystallization precipitant (4.5-7.0% PEG 6000) and cryoprotectant component (PEG 400)
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/">Membrane Protein Structural Biology Concepts</a> — PSI-LHCI is a large multisubunit membrane protein complex embedded in the thylakoid membrane
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Related ligand or cofactor
