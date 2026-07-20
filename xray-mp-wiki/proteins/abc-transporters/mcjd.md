---
title: "McjD - Antibacterial Peptide ABC Exporter from Escherichia coli"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1320506111, doi/10.15252##embj.201797278, doi/10.1107##S2052252520012312]
verified: agent
uniprot_id: ['P04191', 'Q9X2W0']
---

# McjD - Antibacterial Peptide ABC Exporter from Escherichia coli

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P04191">UniProt: P04191</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9X2W0">UniProt: Q9X2W0</a>

<span class="expr-badge">Oryctolagus cuniculus</span>

## Overview

McjD is an ATP-binding cassette (ABC) exporter from Escherichia coli that
confers self-immunity to the producing strain by exporting the antimicrobial
lasso peptide microcin J25 (MccJ25). It is, to the authors' knowledge, the
first crystal structure of an antibacterial peptide ABC transporter. McjD
adopts a homodimeric architecture similar to multidrug ABC exporters such as
[Sav1866](/xray-mp-wiki/proteins/abc-transporters/sav1866/) and
[MsbA](/xray-mp-wiki/proteins/abc-transporters/msba/), but crystallizes in a novel
nucleotide-bound outward-occluded conformation that represents an intermediate
state between the outward-open and inward-open states of ABC exporters.
Each monomer comprises an N-terminal transmembrane domain (TMD) with six
transmembrane helices and a C-terminal nucleotide-binding domain (NBD).
The structure was determined at 2.7-A resolution in complex with the ATP
analog AMP-PNP and Mg2+. Subsequent work captured the McjD-ADP-VO4
(nucleotide-bound, 2.7 A) and McjD-apo (nucleotide-free, 2.5 A) states,
revealing NBD disengagement in the absence of nucleotides. EPR spectroscopy
and MD simulations showed the NBDs separate by up to 16 A in the apo state,
while substrate binding (MccJ25) enhances conformational sampling of the
inward-open conformation. Vanadium SAD (V-SAD) phasing using the anomalous
signal from the vanadate ion in McjD-ADP-VO4 crystals successfully provided
experimental phases at 3.4 A resolution, enabling structure solution despite
severe anisotropy.


## Publications

### doi/10.1073##pnas.1320506111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4pl0">4PL0</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length McjD with C-terminal GFP-His6 tag (cleaved)</td>
      <td>AMP-PNP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: McjD with C-terminal GFP-His6 tag and TEV protease cleavage site
- **Notes**: Drug-hypersensitive E. coli strain lacking AcrAB-TolC used for functional studies; non-GFP-tagged for cellular assays

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: McjD-GFP-His6

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
      <td>Affinity chromatography</td>
      <td>Ni Sepharose <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>—</td>
      <td>0.03% n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>GFP-tag removed by <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease before crystallization</td>
    </tr>
    <tr>
      <td>Exchange into crystallization detergent</td>
      <td>Detergent exchange</td>
      <td>—</td>
      <td></td>
      <td>Exchanged into nonyl-glucopyranoside for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: McjD in nonyl-glucopyranoside with 10 mM AMP-PNP and 2.5 mM MgCl2

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in main text</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>McjD in nonyl-glucopyranoside with 10 mM AMP-PNP, 2.5 mM MgCl2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence of nonyl-glucopyranoside; structure solved by molecular replacement using MsbA and Sav1866 as search models</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4pl0">4PL0</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MERKQKNS</span><span class="topo-inside">L</span><span class="topo-unknown">FNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSS</span><span class="topo-inside">LRINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKDW</span><span class="topo-membrane">FSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>1</td>
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>15</td>
      <td>10</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>92</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>138</td>
      <td>93</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>167</td>
      <td>164</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>189</td>
      <td>168</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>580</td>
      <td>580</td>
      <td>580</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4pl0">4PL0</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MER</span><span class="topo-inside">K</span><span class="topo-unknown">QKNSLFNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSS</span><span class="topo-inside">LRINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKD</span><span class="topo-membrane">WFSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>92</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>138</td>
      <td>93</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>166</td>
      <td>164</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>167</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>580</td>
      <td>580</td>
      <td>580</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.15252##embj.201797278

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length McjD</td>
      <td>ADP-VO4</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a></td>
      <td>2.5</td>
      <td>—</td>
      <td>Full-length McjD</td>
      <td>none (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: McjD with C-terminal GFP-His6 tag and TEV protease cleavage site
- **Notes**: Drug-hypersensitive E. coli strain lacking AcrAB-TolC used for functional studies; non-GFP-tagged for cellular assays

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>McjD with ADP-VO4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>McjD-ADP-VO4 and McjD-apo crystals grown by vapor diffusion; data collected at Diamond Light Source beamlines</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MERKQKNS</span><span class="topo-inside">L</span><span class="topo-unknown">FNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSSL</span><span class="topo-inside">RINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKD</span><span class="topo-membrane">WFSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>15</td>
      <td>10</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>138</td>
      <td>94</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>166</td>
      <td>164</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>167</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MER</span><span class="topo-inside">K</span><span class="topo-unknown">QKNSLFNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSS</span><span class="topo-inside">LRINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKD</span><span class="topo-membrane">WFSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>92</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>138</td>
      <td>93</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>166</td>
      <td>164</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>167</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MERKQKNS</span><span class="topo-inside">L</span><span class="topo-unknown">FNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSSL</span><span class="topo-inside">RINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKD</span><span class="topo-membrane">WFSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>15</td>
      <td>10</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>70</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>138</td>
      <td>94</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>166</td>
      <td>164</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>167</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ofr">5OFR</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MER</span><span class="topo-inside">K</span><span class="topo-unknown">QKNSLFNYIYS</span><span class="topo-inside">LMDVRGK</span><span class="topo-membrane">FLFFSMLFITSLSSIIISISPLIL</span><span class="topo-outside">AKITDLLSGSLSNFSYEYLVLLA</span><span class="topo-membrane">CLYMFCVISNKASVFLFMILQSS</span><span class="topo-inside">LRINMQKKMSLKYLRELYNENITNLSKN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">NAGYTTQSLNQASNDIYI</span><span class="topo-membrane">LVRNVSQNILSPVIQLISTIVVVLS</span><span class="topo-outside">TKD</span><span class="topo-membrane">WFSAGVFFLYILVFVIFNTRLTG</span><span class="topo-inside">SLASLRKHSMDITLNSYSLLSDTVDNMIAAKKNNALRLISERYEDALTQEN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NAQKKYW</span><span class="topo-membrane">LLSSKVLLLNSLLAVILFGSVFIY</span><span class="topo-outside">NILGVLNGVVSIGHFI</span><span class="topo-membrane">MITSYIILLSTPVENIGALLSEIR</span><span class="topo-inside">QSMSSLAGFIQRHAENKATSPSIPFLNMERKLNLSIRELSFSYSDDKKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LNSVSLDLFTGKMYSLTGPSGSGKSTLVKIISGYYKNYFGDIYLNDISLRNISDEDLNDAIYYLTQDDYIFMDTLRFNLRLANYDASENEIFKVLKLANLSVVNNEPVSLDTHLINRGNN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580</span>
<span class="topo-line"><span class="topo-inside">YSGGQKQRISLARLFLRKPAIIIIDEATSALDYINESEILSSIRTHFPDALIINISHRINLLECSDCVYVLNEGNIVASGHFRDLMVSNEYISGLASVT</span><span class="topo-unknown">E</span></span>
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
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>22</td>
      <td>16</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>23</td>
      <td>46</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>69</td>
      <td>47</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>92</td>
      <td>70</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>138</td>
      <td>93</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>163</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>166</td>
      <td>164</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>167</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>247</td>
      <td>190</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>271</td>
      <td>248</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>287</td>
      <td>272</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>311</td>
      <td>288</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>579</td>
      <td>312</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1107##S2052252520012312

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6yso">6YSO</a></td>
      <td>3.4 (V-SAD), 2.7 (phase extension)</td>
      <td>—</td>
      <td>Full-length McjD with ADP-VO4</td>
      <td>ADP-VO4</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: McjD with C-terminal GFP-His6 tag and TEV protease cleavage site
- **Notes**: Drug-hypersensitive E. coli strain lacking AcrAB-TolC used for functional studies; non-GFP-tagged for cellular assays

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: McjD

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
      <td>Purification</td>
      <td>As described previously (Bountra et al., 2017; Choudhury et al., 2014)</td>
      <td>—</td>
      <td>20 mM Tris pH 7.8, 150 mM NaCl, 0.03% dodecyl maltopyranoside</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: McjD at 15 mg/ml in 20 mM Tris pH 7.8, 150 mM NaCl, 0.03% DDM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>15 mg/ml McjD incubated with 2 mM ATP, 2 mM sodium orthovanadate, 5 mM MgCl2 for 1 h at room temperature</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% PEG 4000, 100 mM ammonium sulfate, 100 mM HEPES pH 7.5, 22% glycerol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Directly flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>McjD-ADP-VO4 complex crystals; space group C2; data collected on beamline I23 at Diamond Light Source using PILATUS 12M detector</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yso">6YSO</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEEGKS</span><span class="topo-unknown">LWELVIEQ</span><span class="topo-membrane">FEDLLVRILLLAACISFVLA</span><span class="topo-inside">WFEEGEETITAF</span><span class="topo-membrane">VEPFVILLILIANAIV</span><span class="topo-outside">GVWQERNAENAIEALK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSILTGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ATEQDKTPLQQKLDEF</span><span class="topo-membrane">GEQLSKVISLICVAVWLIN</span><span class="topo-inside">IGH</span><span class="topo-unknown">FNDPVHGGS</span><span class="topo-inside">WIRGAIYY</span><span class="topo-membrane">FKIAVALAVAAIPEGLPAV</span><span class="topo-outside">ITTCLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALCNDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">KEFTLEFSRDRKSMSVYCSPAKSSRAAVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGPVKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDDLPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQF</span><span class="topo-membrane">IRYLISSNVGEVVCIFLTAAL</span><span class="topo-inside">GLPEA</span><span class="topo-membrane">LIPVQLLWVNLVTDGLPATA</span><span class="topo-outside">LGFNPPDLDIMDRPPRSPKEPLISGWLF</span><span class="topo-membrane">FRYMAI</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVGAA</span><span class="topo-inside">AWWFMYAEDGPGVTYHQLTHFMQC</span><span class="topo-unknown">TED</span><span class="topo-inside">HPHFEGLDCEIFEAPEPM</span><span class="topo-membrane">TMALSVLVTIEMCNALNS</span><span class="topo-outside">LSENQSLMRMPPWVNI</span><span class="topo-membrane">WLLGSICLSMSLHFLILYV</span><span class="topo-unknown">DPLPMI</span><span class="topo-inside">FKLK</span></span>
<span class="topo-ruler">       970       980       990    </span>
<span class="topo-line"><span class="topo-inside">ALDLTQ</span><span class="topo-membrane">WLMVLKISLPVIGLDEILKFI</span><span class="topo-outside">ARNYLEG</span></span>
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
      <td>48</td>
      <td>1</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>88</td>
      <td>77</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>104</td>
      <td>89</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>256</td>
      <td>105</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>275</td>
      <td>257</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>278</td>
      <td>276</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>295</td>
      <td>288</td>
      <td>295</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>314</td>
      <td>296</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>760</td>
      <td>315</td>
      <td>760</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>761</td>
      <td>781</td>
      <td>761</td>
      <td>781</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>782</td>
      <td>786</td>
      <td>782</td>
      <td>786</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>806</td>
      <td>787</td>
      <td>806</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>807</td>
      <td>834</td>
      <td>807</td>
      <td>834</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>835</td>
      <td>852</td>
      <td>835</td>
      <td>852</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>853</td>
      <td>876</td>
      <td>853</td>
      <td>876</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>880</td>
      <td>897</td>
      <td>880</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>915</td>
      <td>898</td>
      <td>915</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>916</td>
      <td>931</td>
      <td>916</td>
      <td>931</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>932</td>
      <td>950</td>
      <td>932</td>
      <td>950</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>956</td>
      <td>951</td>
      <td>956</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>957</td>
      <td>966</td>
      <td>957</td>
      <td>966</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>967</td>
      <td>987</td>
      <td>967</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>994</td>
      <td>988</td>
      <td>994</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6yso">6YSO</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEEGKS</span><span class="topo-unknown">LWELVIEQ</span><span class="topo-outside">F</span><span class="topo-membrane">EDLLVRILLLAACISF</span><span class="topo-inside">VLAWFEEGEETITAFV</span><span class="topo-membrane">EPFVILLILIANAIVGV</span><span class="topo-outside">WQERNAENAIEALK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSILTGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ATEQDKTPLQQKL</span><span class="topo-membrane">DEFGEQLSKVISLICVAVWL</span><span class="topo-inside">INIGHFN</span><span class="topo-unknown">DPVH</span><span class="topo-inside">GGSWIRGAIYYF</span><span class="topo-membrane">KIAVALAVAAIPEGLPAVITT</span><span class="topo-outside">CLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALCNDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">KEFTLEFSRDRKSMSVYCSPAKSSRAAVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGPVKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDDLPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQF</span><span class="topo-membrane">IRYLISSNVGEVVCIFLTAA</span><span class="topo-inside">LGLPEA</span><span class="topo-membrane">LIPVQLLWVNLVTDGLPATAL</span><span class="topo-outside">GFNPPDLDIMDRPPRSPKEPLISGW</span><span class="topo-membrane">LFFRYMAI</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVGA</span><span class="topo-inside">AAWWFMYAEDGPGVTYHQLTHFM</span><span class="topo-unknown">Q</span><span class="topo-inside">CT</span><span class="topo-unknown">E</span><span class="topo-inside">DHPHFEGLDCEIFEAPEPMTM</span><span class="topo-membrane">ALSVLVTIEMCNALNSL</span><span class="topo-outside">SENQSLMRMPPWVN</span><span class="topo-membrane">IWLLGSICLSMSLHFLIL</span><span class="topo-inside">YVDPLPMIFKLK</span></span>
<span class="topo-ruler">       970       980       990    </span>
<span class="topo-line"><span class="topo-inside">ALDLTQW</span><span class="topo-membrane">LMVLKISLPVIGLDEILKFI</span><span class="topo-outside">ARNY</span><span class="topo-unknown">LEG</span></span>
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
      <td>48</td>
      <td>1</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>57</td>
      <td>Outside</td>
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
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>106</td>
      <td>90</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>253</td>
      <td>107</td>
      <td>253</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>273</td>
      <td>254</td>
      <td>273</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>274</td>
      <td>280</td>
      <td>274</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>296</td>
      <td>285</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>760</td>
      <td>318</td>
      <td>760</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>761</td>
      <td>780</td>
      <td>761</td>
      <td>780</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>781</td>
      <td>786</td>
      <td>781</td>
      <td>786</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>807</td>
      <td>787</td>
      <td>807</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>808</td>
      <td>832</td>
      <td>808</td>
      <td>832</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>833</td>
      <td>851</td>
      <td>833</td>
      <td>851</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>852</td>
      <td>874</td>
      <td>852</td>
      <td>874</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>876</td>
      <td>877</td>
      <td>876</td>
      <td>877</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>879</td>
      <td>899</td>
      <td>879</td>
      <td>899</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>900</td>
      <td>916</td>
      <td>900</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>930</td>
      <td>917</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>948</td>
      <td>931</td>
      <td>948</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>949</td>
      <td>967</td>
      <td>949</td>
      <td>967</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>968</td>
      <td>987</td>
      <td>968</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>991</td>
      <td>988</td>
      <td>991</td>
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

### Novel outward-occluded conformation

McjD represents a new conformation for ABC exporters, termed nucleotide-bound
outward occluded. Unlike the outward-open Sav1866 and MsbA structures, both
the cytoplasmic and periplasmic sides of the McjD dimer are occluded. The
occluded state is formed by rotation of TMs 1 and 2 toward the equivalent
TMs of the opposite monomer, without the intertwining of TM helices seen in
Sav1866. Salt bridges (Lys80-Glu301, Arg141-Glu309, Arg195-Asp135) stabilize
the occluded packing.

### Substrate-binding cavity

McjD defines a clear internal cavity of approximately 1,784 A3 that can
accommodate one MccJ25 molecule. Mutagenesis identified Phe86, Asn134, and
Asn302 as important for MccJ25 recognition. The cavity is wider and more
charged at the cytoplasmic side and more narrow and hydrophobic at the
periplasmic face, consistent with binding the lariat ring and loop regions
of MccJ25 respectively.

### MccJ25 binding and ATPase stimulation

McjD binds MccJ25 with a KD of 104 +- 52 uM as measured by microscale
thermophoresis. The ATPase activity of McjD (Km 169.3 uM, Vmax 44.4 nmol
min-1 mg-1) is stimulated by MccJ25 in both detergent solution and
proteoliposomes. McjD also transports the multidrug substrate Hoechst 33342,
underscoring structural similarities with multidrug ABC exporters.

### Nucleotide-dependent NBD dynamics

Comparison of McjD-ADP-VO4 (nucleotide-bound) and McjD-apo (nucleotide-free)
structures reveals that the NBDs disengage in the absence of nucleotides.
In the ADP-VO4-bound state, the NBDs form a firmly closed dimer, while in
the apo state they separate by up to 16 A (measured at residue C547).
EPR spectroscopy and MD simulations confirm these large-scale NBD motions.
The TMDs show only minor rearrangements between the two states, indicating
that nucleotide binding primarily affects NBD dimerization.

### Substrate-induced conformational sampling

Cysteine cross-linking and PEGylation studies demonstrate that the presence
of substrate MccJ25 enhances conformational sampling of the inward-open
conformation. The L53C construct shows increased cross-linking efficiency
in the presence of MccJ25, suggesting substrate binding promotes transition
to the inward-open state. The A122C and S509C constructs show similar
substrate-enhanced accessibility, consistent with an induced-fit mechanism
where MccJ25 binding stabilizes the inward-facing conformation.

### McjD structure solved by vanadium SAD phasing

McjD-ADP-VO4 was used as a test case for vanadium-based experimental phasing
(V-SAD). Data collected at lambda = 2.2604 A on beamline I23 at Diamond Light
Source exploited the vanadium K-edge anomalous signal (f'' ~4 e-). Despite
severe anisotropy and low resolution (3.4 A), the two vanadium sites (one per
monomer) were located by SHELXD with strong anomalous peaks (19.5 and 13.7
sigma). After anisotropy correction with STARANISO, initial electron-density
maps from the CRANK2 pipeline clearly showed transmembrane and nucleotide-binding
domains. Phase extension using a higher-resolution (2.7 A) dataset at
lambda = 0.9791 A enabled complete model building. This demonstrated that V-SAD
can succeed at low resolution and with a low scatterer-to-residue ratio (1:580).


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/sav1866/">Sav1866 Multidrug ABC Exporter</a> — Structural comparison; McjD shares similar overall architecture but adopts distinct occluded conformation
- <a href="/xray-mp-wiki/proteins/abc-transporters/msba/">MsbA Lipid Flippase</a> — Structural comparison; used as search model for molecular replacement
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — McjD is a member of the ABC exporter family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — McjD's outward-occluded state represents an intermediate in the alternating access cycle
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-outward-occluded-mechanism/">ABC Transporter Outward-Occluded Mechanism</a> — McjD defines the outward-occluded conformation in ABC exporters
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/vanadate-inhibition/">Vanadate Inhibition</a> — Vanadate binding used for V-SAD phasing of McjD structure
