---
title: "Chicken Kir2.2 Inward Rectifier K+ Channel"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, potassium-channel]
sources: [doi/10.1126##science.1180310, doi/10.1038##nature10370, doi/10.1085##jgp.201611616]
verified: false
---

# Chicken Kir2.2 Inward Rectifier K+ Channel

## Overview

Chicken Kir2.2 (cKir2.2) is a classical inward rectifier potassium channel whose gating is controlled by plasma membrane lipids. The first atomic structure of a eukaryotic Kir channel was determined by X-ray crystallography at 3.1 A resolution (Science 2009), revealing the TXGYGFR selectivity filter stabilized by disulfide bridges and salt bridges, multiple ion binding sites on the intracellular side of the filter that explain voltage-dependent block by multivalent cations, and distinctive turrets on the extracellular surface accounting for toxin insensitivity. Phosphatidylinositol-4,5-bisphosphate ([PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/)) is the primary agonist for Kir2 channels, through which this lipid can regulate a cell's resting membrane potential. Subsequent PIP2-bound structures revealed that [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binds at an interface between the transmembrane domain (TMD) and the cytoplasmic domain (CTD). On [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding, a flexible expansion linker contracts to a compact helical structure, the CTD translates 6 A and becomes tethered to the TMD, and the inner helix gate begins to open. Studies of the K62W mutant (PDB 5KUK, 5KUM) revealed a refined two-site lipid gating model with a primary [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) site and a second site for bulk anionic phospholipids (PL-).

## Publications

### doi/10.1126##science.1180310

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3jyc">3JYC</a></td>
      <td>3.10</td>
      <td>I4</td>
      <td>Chicken Kir2.2 wild-type, residues 46-370 (N- and C-termini truncated)</td>
      <td>Rb+, Sr2+, Eu3+ used for ion binding site mapping</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (Pichia)
- **Construct**: Chicken Kir2.2 with C-terminal GFP and 1D4 epitope tag; also with C-terminal GFP and 1D4 epitope for K62W mutant studies

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Kir2.2 at 9 mg/mL in 150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM n-decyl-beta-D-maltopyranoside (DM), 20 mM DTT, 3 mM TCEP. For ion soaks: 650 mM RbCl, 10-200 mM SrCl2, or 10 mM EuCl3 added.</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2-0.8 M KCl, 50 mM HEPES pH 6.5-7.5, 10-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>48 hours</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals in space group I4 with one subunit per asymmetric unit. Data collected at NSLS beamline X29. Structure solved by single-wavelength anomalous dispersion (SAD) using selenomethionine-substituted protein. Native data to 3.1 A, <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> data to 3.5 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3jyc">3JYC</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-inside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-inside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-inside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3jyc">3JYC</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-inside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-inside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-inside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3jyc">3JYC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-inside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-inside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-inside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3jyc">3JYC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-inside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-inside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-inside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##nature10370

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3spi">3SPI</a></td>
      <td>3.30</td>
      <td>I4</td>
      <td>Chicken Kir2.2 wild-type, with disordered N- and C-termini truncated; complexed with short-chain (dioctanoyl) <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
      <td>dioctanoyl <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3spc">3SPC</a></td>
      <td>3.00</td>
      <td>I4</td>
      <td>Chicken Kir2.2 I223L mutant with <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
      <td>dioctanoyl <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3spg">3SPG</a></td>
      <td>2.60</td>
      <td>I4</td>
      <td>Chicken Kir2.2 R186A mutant with <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
      <td>dioctanoyl <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3spj">3SPJ</a></td>
      <td>2.45</td>
      <td>I4</td>
      <td>Chicken Kir2.2 wild-type complexed with <a href="/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/">PPA</a> (dioctanoyl <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> pyrophosphatidic acid)</td>
      <td>dioctanoyl <a href="/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/">PPA</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (Pichia)
- **Construct**: Chicken Kir2.2 with C-terminal GFP and 1D4 epitope tag; also with C-terminal GFP and 1D4 epitope for K62W mutant studies

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
      <td>1. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>1D4 antibody <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>n-decyl-beta-D-maltopyranoside (DM) buffer</td>
      <td>Protein expressed in Pichia pastoris with C-terminal GFP and 1D4 epitope</td>
    </tr>
    <tr>
      <td>2. Protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> cleavage</td>
      <td>—</td>
      <td>DM-containing buffer</td>
      <td>Cleavage to remove GFP and affinity tags</td>
    </tr>
    <tr>
      <td>3. Size-exclusion chromatography</td>
      <td>Gel filtration (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>)</td>
      <td>—</td>
      <td>DM-containing buffer</td>
      <td>Purified protein concentrated to 9 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Kir2.2 at 8 mg/mL in 4 mM DM, 20 mM DTT, 3 mM TCEP, 150 mM KCl, 20 mM Tris-HCl pH 8.0, with 0.6-1 mM dioctanoyl <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> (or 5 mM <a href="/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/">PPA</a> for <a href="/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/">PPA</a> complex)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.3-0.6 M KCl, 50 mM HEPES pH 6.5-7.5, 10-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 or 3-8% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>48 hours</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diamond-shaped crystals, 150-350 um in longest dimension. Cryoprotected in reservoir solution with 25-30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Data collected at NSLS beamlines X29 and X25. Phases by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using apo-Kir2.2 (PDB 3JYC). Space group I4 with one subunit per asymmetric unit.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spi">3SPI</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AR</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spi">3SPI</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AR</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spi">3SPI</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AR</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spi">3SPI</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AR</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spc">3SPC</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDDKP</span><span class="topo-unknown">QRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>28</td>
      <td>41</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>64</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>337</td>
      <td>185</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spc">3SPC</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDDKP</span><span class="topo-unknown">QRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>28</td>
      <td>41</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>64</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>337</td>
      <td>185</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spc">3SPC</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDDKP</span><span class="topo-unknown">QRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>28</td>
      <td>41</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>64</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>337</td>
      <td>185</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spc">3SPC</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDDKP</span><span class="topo-unknown">QRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>28</td>
      <td>41</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>33</td>
      <td>64</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>337</td>
      <td>185</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spg">3SPG</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AA</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spg">3SPG</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AA</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spg">3SPG</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AA</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spg">3SPG</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-inside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">KPQRYIA</span><span class="topo-inside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-inside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-outside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-outside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-inside">AA</span><span class="topo-unknown">PKKRAQ</span><span class="topo-inside">TLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-inside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-inside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-inside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>36</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>185</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>158</td>
      <td>337</td>
      <td>193</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spj">3SPJ</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-outside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-outside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-outside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHLVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spj">3SPJ</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-outside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-outside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-outside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHLVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spj">3SPJ</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-outside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-outside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-outside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHLVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3spj">3SPJ</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRKCR</span><span class="topo-outside">NRFVKKNGQCNVEFTNMD</span><span class="topo-unknown">DKPQRYIAD</span><span class="topo-outside">MFTTCVDI</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIM</span><span class="topo-outside">AKMARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHLVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENKFLLSNS</span><span class="topo-unknown">LEVLFQ</span></span>
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
      <td>7</td>
      <td>36</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>43</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>61</td>
      <td>69</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>70</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>146</td>
      <td>156</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>337</td>
      <td>182</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>343</td>
      <td>373</td>
      <td>378</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1085##jgp.201611616

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kuk">5KUK</a></td>
      <td>2.00</td>
      <td>I 2 2 2</td>
      <td>Chicken Kir2.2 K62W mutant, C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> replaced with 1D4 sequence, <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> site</td>
      <td>decyl-maltoside (DM) detergent head group at second site</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kum">5KUM</a></td>
      <td>2.80</td>
      <td>I 2 2 2</td>
      <td>Chicken Kir2.2 K62W mutant with added <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
      <td><a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> (primary site), decyl-maltoside (DM) detergent head group (second site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (Pichia)
- **Construct**: Chicken Kir2.2 with C-terminal GFP and 1D4 epitope tag; also with C-terminal GFP and 1D4 epitope for K62W mutant studies

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
      <td>1. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>1D4 antibody <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>K62W mutant with C-terminal 1D4 tag</td>
    </tr>
    <tr>
      <td>2. Protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> cleavage</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3. Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td>150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM DM, 20 mM DTT, 3 mM TCEP</td>
      <td></td>
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
      <td>Protein sample</td>
      <td>Kir2.2 K62W mutant in 150 mM KCl, 20 mM Tris-HCl pH 8.0, 4 mM DM, 20 mM DTT, 3 mM TCEP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in detail</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 2.0 A (apo) and 2.8 A (with added <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a>). Space group I222. Data collected at APS beamline 24-ID-C/E.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kuk">5KUK</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kuk">5KUK</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kuk">5KUK</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kuk">5KUK</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kum">5KUM</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kum">5KUM</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kum">5KUM</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5kum">5KUM</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MARRK</span><span class="topo-outside">CRNRFVKKNGQCNVEFTNMDD</span><span class="topo-unknown">WPQRYIA</span><span class="topo-outside">D</span><span class="topo-unknown">MFTTCVD</span><span class="topo-outside">I</span><span class="topo-membrane">RWRYMLLLFSLAFLVSWL</span></span>
<span class="topo-line"><span class="topo-membrane">LFGLIFWLI</span><span class="topo-inside">ALIHGDLENPGGDDTFKPCVLQVNGF</span><span class="topo-unknown">VAAFLFSIETQTTIGYG</span><span class="topo-inside">FRCVTEEC</span></span>
<span class="topo-line"><span class="topo-membrane">PLAVFMVVVQSIVGCIIDSFMIGAIMAKM</span><span class="topo-outside">ARPKKRAQTLLFSHNAVVAMRDGKLCLMWRV</span></span>
<span class="topo-line"><span class="topo-outside">GNLRKSHIVEAHVRAQLIKPRITEEGEYIPLDQIDIDVGFDKGLDRIFLVSPITILHEIN</span></span>
<span class="topo-line"><span class="topo-outside">EDSPLFGISRQDLETDDFEIVVILEGMVEATAMTTQARSSYLASEILWGHRFEPVLFEEK</span></span>
<span class="topo-line"><span class="topo-outside">NQYKVDYSHFHKTYEVPSTPRCSAKDLVENK</span><span class="topo-unknown">FLLSNSLEVLFQ</span></span>
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
      <td>6</td>
      <td>26</td>
      <td>41</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>33</td>
      <td>62</td>
      <td>68</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>34</td>
      <td>34</td>
      <td>69</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>41</td>
      <td>70</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>42</td>
      <td>42</td>
      <td>77</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>78</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>95</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>131</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>148</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>149</td>
      <td>156</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>331</td>
      <td>185</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First atomic structure of a eukaryotic Kir channel

The 2009 Science paper (doi/10.1126/science.1180310) determined the first X-ray crystal structure of a eukaryotic inward-rectifier K+ channel, Kir2.2 from chicken, at 3.1 A resolution. The structure revealed the TXGYGFR selectivity filter sequence (versus the canonical TXGYGDX), which gives rise to distinct structural features including a disulfide bridge between C123 and C155 and an ionized hydrogen bond between R149 (in the filter) and E139. Multiple ion binding sites on the intracellular side of the selectivity filter (cavity, upper ring of charges, lower ring of charges) explain the mechanism of voltage-dependent block by intracellular multivalent cations (Mg2+, polyamines). The channel's extracellular surface features large structured turrets that constrict the pore entryway and explain the relative insensitivity of eukaryotic Kir channels to venom toxins.

### Ion binding sites for conduction and inward rectification

Crystals containing Rb+ (K+ analog), Sr2+ (Mg2+ mimic), and Eu3+ revealed distinct ion binding sites along the conduction pathway. Rb+ binds at multiple sites in the selectivity filter and at three positions intracellular to the filter (below the activation gate, at the upper ring of charges E225/E300, and at the lower ring of charges D256). Sr2+ binds in the cavity (weak, at D173), the upper ring (strong), and the lower ring (strong). Eu3+ binds only at the upper ring, which contains two concentric rings of acidic amino acids (E225 and E300). These sites are formed by planar rings of acidic amino acids too wide for direct ion coordination, suggesting ions at these positions interact through bridging water molecules. The strong electric field created by multiple negatively charged carboxyl groups favors multivalent cations, explaining the mechanism of inward rectification.

### PIP2 binding site at TMD-CTD interface

[PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binds at an interface between the transmembrane domain (TMD) and the cytoplasmic domain (CTD). The PIP2-binding site consists of a conserved non-specific phospholipid-binding region in the TMD and a specific phosphatidylinositol-binding region in the CTD. The acyl chains, [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) backbone and 1' phosphate of [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) interact with the TMD, while the inositol head group makes interactions with the CTD.

### Conformational change on PIP2 binding

On [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binding, a flexible expansion linker contracts to a compact helical structure, the CTD translates 6 A towards the TMD, and the inner helix gate begins to open (6.3 A at Ile177 in PIP2-bound vs 4.9 A in PPA-bound). The conformational changes include formation of two new helices: an N-terminal extension of the 'interfacial' helix and a 'tether' helix at the C terminus of the inner helix.

### PPA binds TMD but fails to activate

The small anionic lipid [PPA](/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/) (dioctanoyl [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) pyrophosphatidic acid) binds to the non-specific TMD region but not to the specific [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) region, and thus fails to engage the CTD or open the channel. The PPA-bound structure (PDB 3SPJ) shows a closed conformation similar to apo-Kir2.2 (PDB 3JYC) with the CTD unengaged and the inner helix gate tightly closed (4.9 A at Ile177).

### Conserved RWR sequence for 1' phosphate binding

The sequence arginine-tryptophan-arginine (R78-W79-R80) at the N terminus of the outer helix forms a binding site in which the 1' phosphate of [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) caps the helix and is cradled by main-chain amide nitrogen atoms and guanidinium groups. This sequence is conserved as RWR or KWR among many Kir channels.

### Two-site lipid gating model from K62W studies

Kir2 channels have two distinct lipid-binding sites: a primary [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) site at the TMD-CTD interface and a second site for bulk anionic phospholipids (PL-) at the N-terminal slide helix (K62 in cKir2.2). PL- binding at the second site pulls the CTD toward the membrane, inducing formation of the high-affinity primary [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) site. This explains the positive allostery between PL- binding and [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) sensitivity.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/dioctanoyl-ppa/">PPA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol/">Phosphatidylinositol</a> — Additive used in purification or crystallization buffers
