---
title: "Uric acid/xanthine H+ symporter UapA from Aspergillus nidulans"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms11336]
verified: regex
uniprot_id: Q07307
---

# Uric acid/xanthine H+ symporter UapA from Aspergillus nidulans

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q07307">UniProt: Q07307</a>

<span class="expr-badge">Aspergillus nidulans FGSC A4</span>

## Overview

UapA from Aspergillus nidulans is a high-affinity purine/H+ symporter specific for xanthine and uric acid, belonging to the nucleobase/ascorbate transporter (NAT) family. The crystal structure of a thermostabilized construct (UapA-G411VΔ1-11) in complex with xanthine was determined at 3.7 A resolution. UapA forms a homodimer in the crystals with dimer interactions formed exclusively through the gate domain. The structure reveals UapA in an inward-facing conformation with xanthine bound to residues in the core domain. Molecular dynamics simulations suggest that Arg481 from the opposing monomer approaches the central binding cavity, creating a specificity barrier and contributing to fine-tuning substrate selectivity. Dominant negative mutant analysis is consistent with dimerization playing a key role in transport. UapA is postulated to function by an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) shared with other structurally homologous transporters including anion exchangers and prestin.


## Publications

### doi/10.1038##ncomms11336

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i6c">5I6C</a></td>
      <td>3.7 A</td>
      <td>P2_1</td>
      <td>UapA-G411VΔ1-11 thermostabilized construct (G411V substitution, N-terminal 11 residues deleted) from A. nidulans, expressed in S. cerevisiae with C-terminal TEV-GFP-His8 tag; in complex with xanthine</td>
      <td>xanthine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae
- **Construct**: UapA-G411VΔ1-11 (G411V, Δ1-11) cloned into pDDGFP vector with C-terminal TEV cleavage site followed by GFP-His8 tag; expressed in S. cerevisiae FGY217 strain under galactose induction

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell disruption and membrane ultracentrifugation</td>
      <td>not specified</td>
      <td>not specified + not specified</td>
      <td>S. cerevisiae cells harvested after 22 h of galactose induction. Membranes prepared by ultracentrifugation.</td>
    </tr>
    <tr>
      <td>Solubilization and affinity purification</td>
      <td>Detergent solubilization and Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>not specified</td>
      <td>not specified + not specified</td>
      <td>Protein solubilized from membranes and purified via GFP-His8 tag.</td>
    </tr>
    <tr>
      <td>Tag cleavage and final purification</td>
      <td>TEV protease cleavage and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Superdex unspecified</td>
      <td>not specified + not specified</td>
      <td>GFP-His8 tag removed by TEV protease cleavage before SEC. Xanthine (or 8-bromoxanthine for derivative preparation) was included throughout purification.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified UapA-G411VΔ1-11 with xanthine bound, TEV-cleaved; initial screening with MemSys/MemStart screens</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1% MES pH 6.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 1% n-hexyl-beta-D-glucopyranoside</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>overnight</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals showed anisotropic diffraction; best crystals diffracted to 3.5 A in strongest direction. Space group P2_1 with two molecules per asymmetric unit. Initial phases by SIRAS using TaBr-soaked crystals (overnight soak with saturating TaBr). Data collected at Diamond Light Source. Phasing with SHELX and SHARP. Refinement with PHENIX including DEN refinement, Rosetta refinement, <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> averaging, and B-factor sharpening. Final R = 29.6%, Rfree = 32.7%. 8-bromoxanthine derivative used for anomalous phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i6c">5I6C</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDNSIHSTDGPDSVIPNSNPKKTVRQRVRLLARHLTTREGLIGDYDYGFLFRPELPFMKKDPRAP</span><span class="topo-outside">PFFGLNEKIPVLLAFILGL</span><span class="topo-membrane">QHALAMLAGVVTPPLIISSS</span><span class="topo-inside">LSLPSDL</span><span class="topo-membrane">QQYLVSTSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IVCGLLSMV</span><span class="topo-outside">QITRFHIYKTPYYIGSGVLSV</span><span class="topo-membrane">MGVSFSIISVASGAF</span><span class="topo-inside">NQMYSNGFCQLDEAGNRLPCPEA</span><span class="topo-membrane">YGALIGTSACCALVEIL</span><span class="topo-outside">LAFVPPKVIQKIFPPIV</span><span class="topo-membrane">TGPTVMLIGISLIGTGFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">DWA</span><span class="topo-inside">GGSACMDDGMLCPSATAPRPLPWGSPEF</span><span class="topo-membrane">IGLGFLVFVSIILCERF</span><span class="topo-outside">GAPIMKS</span><span class="topo-membrane">CSVVIGLLVGCIVAAA</span><span class="topo-inside">CGYFSHADIDAAPAASFIWVKTFP</span><span class="topo-membrane">LSVYGPMVLPIIAVFIICA</span><span class="topo-outside">CECIGD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VTATCDVSRLEVRGGTFESRIQGAVLAD</span><span class="topo-unknown">GINSVVAALATMTPMTTF</span><span class="topo-outside">AQNNVVIALTRCANRWAGYCC</span><span class="topo-membrane">CLILIVAGIFAKFAAAIVAIP</span><span class="topo-inside">N</span><span class="topo-membrane">SVMGGMKTFLFASVVISGQ</span><span class="topo-outside">AIVAKAPFTRRN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570    </span>
<span class="topo-line"><span class="topo-outside">RF</span><span class="topo-membrane">ILTASMALGYGATLV</span><span class="topo-inside">PTWFGNVFPQTENRDLEGF</span><span class="topo-membrane">ENAIELVLETGFAVTAFVAMLL</span><span class="topo-outside">NAIMPAE</span><span class="topo-unknown">VEEIGAVTPMPVSAHDNRDGEAEYQSKQA</span></span>
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
      <td>65</td>
      <td>1</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>104</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>111</td>
      <td>105</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>130</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>165</td>
      <td>151</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>188</td>
      <td>166</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>205</td>
      <td>189</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>222</td>
      <td>206</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>223</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>271</td>
      <td>244</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>288</td>
      <td>272</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>295</td>
      <td>289</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>311</td>
      <td>296</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>335</td>
      <td>312</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>354</td>
      <td>336</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>388</td>
      <td>355</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>406</td>
      <td>389</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>448</td>
      <td>428</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>449</td>
      <td>449</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>468</td>
      <td>450</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>482</td>
      <td>469</td>
      <td>482</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>497</td>
      <td>483</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>498</td>
      <td>516</td>
      <td>498</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>538</td>
      <td>517</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>539</td>
      <td>545</td>
      <td>539</td>
      <td>545</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>574</td>
      <td>546</td>
      <td>574</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i6c">5I6C</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDNSIHSTDGPDSVIPNSNPKKTVRQRVRLLARHLTTREGLIGDYDYGFLFRPELPFMKKDPRAP</span><span class="topo-outside">PFFGLNEKIPVLLAFILGL</span><span class="topo-membrane">QHALAMLAGVVTPPLIISSS</span><span class="topo-inside">LSLPSDL</span><span class="topo-membrane">QQYLVSTSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IVCGLLSMV</span><span class="topo-outside">QIT</span><span class="topo-unknown">RFHIYKTPYYIG</span><span class="topo-outside">SGVLSVM</span><span class="topo-membrane">GVSFSIISVASGAF</span><span class="topo-inside">NQMYSNGFCQLDEAGNRLPCPEA</span><span class="topo-membrane">YGALIGTSACCALVEIL</span><span class="topo-outside">LAFVPPKVIQKIFPPIV</span><span class="topo-membrane">TGPTVMLIGISLIGTGFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">DWA</span><span class="topo-inside">GGSACMDDGMLCPSATAPRPLPWGSPEF</span><span class="topo-membrane">IGLGFLVFVSIILCERF</span><span class="topo-outside">GAPIMKS</span><span class="topo-membrane">CSVVIGLLVGCIVAAAC</span><span class="topo-inside">GYFSHADIDAAPAASFIWVKTFP</span><span class="topo-membrane">LSVYGPMVLPIIAVFIICA</span><span class="topo-outside">CECIGD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VTATCDVSRLEVRGGTFESRIQGAVLAD</span><span class="topo-unknown">GINSVVAALATMTPMTTF</span><span class="topo-outside">AQNNVVIALTRCANRWAGYCC</span><span class="topo-membrane">CLILIVAGIFAKFAAAIVAIP</span><span class="topo-inside">N</span><span class="topo-membrane">SVMGGMKTFLFASVVISGQ</span><span class="topo-outside">AIVAKAPFTRRN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570    </span>
<span class="topo-line"><span class="topo-outside">RF</span><span class="topo-membrane">ILTASMALGYGATLVPTW</span><span class="topo-inside">FGNVFPQTENRDLEGF</span><span class="topo-membrane">ENAIELVLETGFAVTAFVAMLL</span><span class="topo-outside">NAIMPAE</span><span class="topo-unknown">VEEIGAVTPMPVSAHDNRDGEAEYQSKQA</span></span>
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
      <td>1</td>
      <td>65</td>
      <td>1</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>84</td>
      <td>66</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>104</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>111</td>
      <td>105</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>112</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>132</td>
      <td>130</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>144</td>
      <td>133</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>145</td>
      <td>151</td>
      <td>145</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>165</td>
      <td>152</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>188</td>
      <td>166</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>205</td>
      <td>189</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>222</td>
      <td>206</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>223</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>271</td>
      <td>244</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>288</td>
      <td>272</td>
      <td>288</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>289</td>
      <td>295</td>
      <td>289</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>312</td>
      <td>296</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>335</td>
      <td>313</td>
      <td>335</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>354</td>
      <td>336</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>388</td>
      <td>355</td>
      <td>388</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>406</td>
      <td>389</td>
      <td>406</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>407</td>
      <td>427</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>448</td>
      <td>428</td>
      <td>448</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>449</td>
      <td>449</td>
      <td>449</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>468</td>
      <td>450</td>
      <td>468</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>482</td>
      <td>469</td>
      <td>482</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>483</td>
      <td>500</td>
      <td>483</td>
      <td>500</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>501</td>
      <td>516</td>
      <td>501</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>538</td>
      <td>517</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>539</td>
      <td>545</td>
      <td>539</td>
      <td>545</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>546</td>
      <td>574</td>
      <td>546</td>
      <td>574</td>
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

### UapA structure reveals homodimer formation

UapA contains 14 transmembrane domains (TMs) organized into a 7+7 TM fold divided into a core domain (TMs 1-4 and 8-11) and a gate domain (TMs 5-7 and 12-14), similar to [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/). Unlike [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) which was observed as a monomer, UapA forms a dimer in the crystals with interactions exclusively through the gate domain. The extracellular loop between TMs 3 and 4 contains a disulphide bond (Cys174-Cys185) highly conserved in fungi; mutation of either residue causes marked reduction in expression and membrane sorting.

### Substrate binding site

Xanthine binds to residues in the core domain. The binding site involves Glu356, Gln408, Ala407, Phe155, Val153, and Phe406. Key contacts include the amide N of Phe155 with N9 of xanthine, Glu356 with N7-H, Gln408 with N1-H and C2=O, and the amide N of Ala407 with C6=O. Phe155 and Phe406 provide aromatic packing around the xanthine.

### Arg481 from opposing monomer contributes to specificity

Molecular dynamics simulations suggest that Arg481 from the opposite monomer approaches the central binding cavity, creating a specificity barrier on the pathway to the cytoplasm. Arg481 is the most commonly mutated residue in genetic selection experiments that alter substrate specificity. The simulations show xanthine forms transient H-bond and pi-pi stacking interactions with Arg481 before moving to the cytosol.

### Dominant negative mutations support functional dimerization

Co-expression of wild-type UapA with transport-deficient mutants (G411V, Q408P, N409D, Q408E) results in dominant negative effects, reducing xanthine uptake compared to wild-type alone. This suggests that one subunit influences the transport function of the other, consistent with dimerization playing a direct role in transport rather than just trafficking.

### Postulated elevator transport mechanism

Based on structural homology with [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/), anion exchanger 1 (AE1), and SLC26 transporters, UapA is proposed to function by an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/). The core domain containing the substrate-binding site moves relative to the fixed gate domain, effectively carrying xanthine across the membrane. The G411V mutation (which sterically hinders core domain sliding) retains binding but abolishes transport, consistent with this mechanism.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/uraA/">Uracil:Proton Symporter UraA from Escherichia coli</a> — Homologous NAT/NCS2 family transporter with the same 7+7 TM fold
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — UapA proposed to function via elevator mechanism based on structural homology
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Elevator mechanism is a specific variant of alternating access
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — Related alternating-access mechanism; gate domain motions contribute to transport
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/peg300/">PEG300</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
